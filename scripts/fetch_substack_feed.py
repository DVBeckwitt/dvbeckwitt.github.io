#!/usr/bin/env python3
"""Fetch recent Substack RSS entries into Jekyll's _data directory.

This script uses only the Python standard library so the site build does not
need another dependency.
"""

from __future__ import annotations

import argparse
import email.utils
import html
import json
import re
import sys
import urllib.request
import xml.etree.ElementTree as ET
from dataclasses import dataclass
from datetime import timezone
from html.parser import HTMLParser
from pathlib import Path
from typing import Iterable

DEFAULT_FEED_URL = "https://scatterguy.substack.com/feed"
DEFAULT_OUTPUT = Path("_data/substack_posts.json")
DEFAULT_MAX_POSTS = 8

NAMESPACES = {
    "atom": "http://www.w3.org/2005/Atom",
    "content": "http://purl.org/rss/1.0/modules/content/",
    "dc": "http://purl.org/dc/elements/1.1/",
}


class HTMLStripper(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.parts: list[str] = []

    def handle_data(self, data: str) -> None:
        self.parts.append(data)

    def get_text(self) -> str:
        return " ".join(self.parts)


@dataclass
class FeedPost:
    title: str
    url: str
    published: str
    summary: str


def strip_html(value: str) -> str:
    stripper = HTMLStripper()
    stripper.feed(value or "")
    text = html.unescape(stripper.get_text())
    return re.sub(r"\s+", " ", text).strip()


def truncate(value: str, max_chars: int = 260) -> str:
    value = value.strip()
    if len(value) <= max_chars:
        return value
    clipped = value[: max_chars + 1].rsplit(" ", 1)[0].rstrip()
    return f"{clipped}..."


def parse_date(value: str) -> str:
    if not value:
        return ""
    try:
        parsed = email.utils.parsedate_to_datetime(value)
        if parsed.tzinfo is None:
            parsed = parsed.replace(tzinfo=timezone.utc)
        return parsed.astimezone(timezone.utc).isoformat()
    except Exception:
        return value


def find_text(element: ET.Element, paths: Iterable[str]) -> str:
    for path in paths:
        found = element.find(path, NAMESPACES)
        if found is not None and found.text:
            return found.text.strip()
    return ""


def parse_rss(root: ET.Element) -> list[FeedPost]:
    posts: list[FeedPost] = []
    for item in root.findall("./channel/item"):
        title = find_text(item, ["title"])
        url = find_text(item, ["link"])
        published = parse_date(find_text(item, ["pubDate", "dc:date"]))
        raw_summary = find_text(item, ["description", "content:encoded"])
        summary = truncate(strip_html(raw_summary))
        if title and url:
            posts.append(FeedPost(title=title, url=url, published=published, summary=summary))
    return posts


def parse_atom(root: ET.Element) -> list[FeedPost]:
    posts: list[FeedPost] = []
    for entry in root.findall("./atom:entry", NAMESPACES) or root.findall("./entry"):
        title = find_text(entry, ["atom:title", "title"])
        url = ""
        for link in entry.findall("atom:link", NAMESPACES) + entry.findall("link"):
            href = link.attrib.get("href")
            rel = link.attrib.get("rel", "alternate")
            if href and rel == "alternate":
                url = href
                break
        published = parse_date(find_text(entry, ["atom:published", "atom:updated", "published", "updated"]))
        raw_summary = find_text(entry, ["atom:summary", "atom:content", "summary", "content"])
        summary = truncate(strip_html(raw_summary))
        if title and url:
            posts.append(FeedPost(title=title, url=url, published=published, summary=summary))
    return posts


def fetch_feed(feed_url: str, timeout: int) -> str:
    request = urllib.request.Request(
        feed_url,
        headers={
            "User-Agent": "dvbeckwitt.github.io RSS importer",
        },
    )
    with urllib.request.urlopen(request, timeout=timeout) as response:
        return response.read().decode("utf-8", errors="replace")


def posts_to_json(posts: list[FeedPost], max_posts: int) -> str:
    payload = [
        {
            "title": post.title,
            "url": post.url,
            "published": post.published,
            "summary": post.summary,
        }
        for post in posts[:max_posts]
    ]
    return json.dumps(payload, ensure_ascii=False, indent=2) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--feed-url", default=DEFAULT_FEED_URL)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--max-posts", type=int, default=DEFAULT_MAX_POSTS)
    parser.add_argument("--timeout", type=int, default=20)
    args = parser.parse_args()

    args.output.parent.mkdir(parents=True, exist_ok=True)

    try:
        feed_xml = fetch_feed(args.feed_url, args.timeout)
        root = ET.fromstring(feed_xml)
        posts = parse_rss(root)
        if not posts:
            posts = parse_atom(root)
        args.output.write_text(posts_to_json(posts, args.max_posts), encoding="utf-8")
        print(f"Wrote {min(len(posts), args.max_posts)} Substack post(s) to {args.output}")
    except Exception as exc:
        # Do not fail the website build because an external feed is temporarily unavailable.
        args.output.write_text("[]\n", encoding="utf-8")
        print(f"Warning: could not import Substack feed: {exc}", file=sys.stderr)
        print(f"Wrote empty fallback data file to {args.output}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
