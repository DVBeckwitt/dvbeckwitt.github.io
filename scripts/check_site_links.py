#!/usr/bin/env python3
"""Validate a generated Jekyll site for broken internal links and missing assets.

Run after `bundle exec jekyll build`:

    python scripts/check_site_links.py _site

The checker is intentionally dependency-free so it can run in GitHub Actions
without adding another package install step.
"""

from __future__ import annotations

import argparse
import posixpath
import re
import sys
from dataclasses import dataclass
from html.parser import HTMLParser
from pathlib import Path
from typing import Iterable
from urllib.parse import unquote, urljoin, urlsplit


IGNORED_SCHEMES = {
    "blob",
    "data",
    "ftp",
    "irc",
    "javascript",
    "mailto",
    "sms",
    "tel",
    "webcal",
}

LINK_ATTRS: dict[str, tuple[str, ...]] = {
    "a": ("href",),
    "area": ("href",),
    "audio": ("src",),
    "embed": ("src",),
    "form": ("action",),
    "iframe": ("src",),
    "img": ("src", "longdesc"),
    "input": ("src",),
    "link": ("href",),
    "object": ("data",),
    "script": ("src",),
    "source": ("src", "srcset"),
    "track": ("src",),
    "video": ("src", "poster"),
}

IMAGE_REFERENCES = {
    ("img", "src"),
    ("input", "src"),
    ("source", "src"),
    ("source", "srcset"),
    ("video", "poster"),
    ("meta", "content"),
}

META_IMAGE_NAMES = {
    "og:image",
    "og:image:url",
    "twitter:image",
    "twitter:image:src",
}

CSS_URL_RE = re.compile(r"url\(\s*(['\"]?)(?P<url>.*?)(?:\1)\s*\)", re.IGNORECASE)


@dataclass(frozen=True)
class Reference:
    source_file: Path
    source_url: str
    line: int
    tag: str
    attr: str
    value: str
    kind: str


class SiteHTMLParser(HTMLParser):
    """Collect link-like references and anchors from a built HTML document."""

    def __init__(self, source_file: Path, source_url: str) -> None:
        super().__init__(convert_charrefs=True)
        self.source_file = source_file
        self.source_url = source_url
        self.references: list[Reference] = []
        self.anchors: set[str] = set()

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attrs_dict = {name.lower(): value for name, value in attrs if value is not None}
        line = self.getpos()[0]

        element_id = attrs_dict.get("id")
        if element_id:
            self.anchors.add(element_id)

        # Legacy named anchors are still valid fragment targets.
        if tag == "a":
            name = attrs_dict.get("name")
            if name:
                self.anchors.add(name)

        for attr in LINK_ATTRS.get(tag, ()):
            value = attrs_dict.get(attr)
            if value:
                kind = "image" if (tag, attr) in IMAGE_REFERENCES else "link"
                self.references.append(
                    Reference(self.source_file, self.source_url, line, tag, attr, value, kind)
                )

        if tag == "meta":
            meta_name = (attrs_dict.get("property") or attrs_dict.get("name") or "").lower()
            content = attrs_dict.get("content")
            if meta_name in META_IMAGE_NAMES and content:
                self.references.append(
                    Reference(self.source_file, self.source_url, line, tag, "content", content, "image")
                )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Check a generated Jekyll _site directory for broken internal links."
    )
    parser.add_argument(
        "site_dir",
        nargs="?",
        default="_site",
        help="Generated site directory to inspect. Defaults to _site.",
    )
    parser.add_argument(
        "--config",
        default="_config.yml",
        help="Jekyll config file used to infer url/baseurl for absolute internal URLs.",
    )
    return parser.parse_args()


def read_simple_config(config_path: Path) -> tuple[str | None, str]:
    """Read top-level `url:` and `baseurl:` values without requiring PyYAML."""

    site_url: str | None = None
    base_url = ""

    if not config_path.exists():
        return site_url, base_url

    for raw_line in config_path.read_text(encoding="utf-8", errors="replace").splitlines():
        line = raw_line.split("#", 1)[0].strip()
        if not line or ":" not in line:
            continue

        key, value = line.split(":", 1)
        key = key.strip()
        value = value.strip().strip("'\"")

        if key == "url" and value:
            site_url = value.rstrip("/")
        elif key == "baseurl":
            base_url = value.rstrip("/")

    return site_url, base_url


def file_url(site_dir: Path, html_file: Path) -> str:
    rel = html_file.relative_to(site_dir).as_posix()

    if rel == "index.html":
        return "/"

    if rel.endswith("/index.html"):
        return "/" + rel.removesuffix("index.html")

    return "/" + rel


def split_srcset(value: str) -> Iterable[str]:
    for candidate in value.split(","):
        candidate = candidate.strip()
        if not candidate:
            continue
        yield candidate.split()[0]


def iter_reference_values(ref: Reference) -> Iterable[str]:
    if ref.attr == "srcset":
        yield from split_srcset(ref.value)
    else:
        yield ref.value


def css_references(site_dir: Path, css_file: Path) -> Iterable[Reference]:
    source_url = "/" + css_file.relative_to(site_dir).as_posix()

    for line_number, line in enumerate(
        css_file.read_text(encoding="utf-8", errors="replace").splitlines(), start=1
    ):
        for match in CSS_URL_RE.finditer(line):
            value = match.group("url").strip()
            if value:
                yield Reference(css_file, source_url, line_number, "css", "url", value, "asset")


def is_external_url(url: str, site_url: str | None) -> bool:
    parts = urlsplit(url)

    if not parts.scheme and not parts.netloc:
        return False

    if parts.scheme in IGNORED_SCHEMES:
        return True

    if parts.scheme in {"http", "https"}:
        if site_url:
            site_parts = urlsplit(site_url)
            return parts.netloc.lower() != site_parts.netloc.lower()
        return True

    # Protocol-relative URLs are external unless they match the configured host.
    if parts.netloc:
        if site_url:
            site_parts = urlsplit(site_url)
            return parts.netloc.lower() != site_parts.netloc.lower()
        return True

    return True


def normalize_internal_path(raw_url: str, source_url: str, site_url: str | None, base_url: str) -> tuple[str, str | None] | None:
    url = raw_url.strip()

    if not url:
        return None

    parts = urlsplit(url)

    if parts.scheme in IGNORED_SCHEMES:
        return None

    if is_external_url(url, site_url):
        return None

    if parts.scheme in {"http", "https"} or parts.netloc:
        path = parts.path or "/"
    elif not parts.path:
        path = source_url
    elif parts.path.startswith("/"):
        path = parts.path
    else:
        path = urljoin(source_url, parts.path)

    path = unquote(path)

    if base_url and (path == base_url or path.startswith(base_url + "/")):
        path = path[len(base_url) :] or "/"

    path = "/" + posixpath.normpath(path).lstrip("/")
    if raw_url.strip().split("#", 1)[0].split("?", 1)[0].endswith("/") and not path.endswith("/"):
        path += "/"

    fragment = unquote(parts.fragment) if parts.fragment else None
    return path, fragment


def candidate_files(site_dir: Path, url_path: str) -> Iterable[Path]:
    rel = url_path.lstrip("/")

    if url_path == "/":
        yield site_dir / "index.html"
        return

    if url_path.endswith("/"):
        yield site_dir / rel / "index.html"
        return

    yield site_dir / rel

    # Extensionless pretty URLs may resolve to a directory index.
    yield site_dir / rel / "index.html"

    # Jekyll can also emit explicit .html files for non-pretty URLs.
    if not Path(rel).suffix:
        yield site_dir / f"{rel}.html"


def resolve_target(site_dir: Path, url_path: str) -> Path | None:
    site_root = site_dir.resolve()

    for candidate in candidate_files(site_dir, url_path):
        resolved = candidate.resolve()
        if not str(resolved).startswith(str(site_root)):
            continue
        if candidate.is_file():
            return candidate

    return None


def collect_site(site_dir: Path) -> tuple[list[Reference], dict[Path, set[str]]]:
    references: list[Reference] = []
    anchors_by_file: dict[Path, set[str]] = {}

    for html_file in sorted(site_dir.rglob("*.html")):
        parser = SiteHTMLParser(html_file, file_url(site_dir, html_file))
        parser.feed(html_file.read_text(encoding="utf-8", errors="replace"))
        references.extend(parser.references)
        anchors_by_file[html_file] = parser.anchors

    for css_file in sorted(site_dir.rglob("*.css")):
        references.extend(css_references(site_dir, css_file))

    return references, anchors_by_file


def reference_location(site_dir: Path, ref: Reference) -> str:
    return f"{ref.source_file.relative_to(site_dir).as_posix()}:{ref.line}"


def main() -> int:
    args = parse_args()
    site_dir = Path(args.site_dir).resolve()
    config_path = Path(args.config).resolve()

    if not site_dir.is_dir():
        print(f"error: generated site directory does not exist: {site_dir}", file=sys.stderr)
        return 2

    site_url, base_url = read_simple_config(config_path)
    references, anchors_by_file = collect_site(site_dir)

    errors: list[str] = []

    if not (site_dir / "index.html").is_file():
        errors.append("missing root index.html")

    for ref in references:
        for value in iter_reference_values(ref):
            normalized = normalize_internal_path(value, ref.source_url, site_url, base_url)
            if normalized is None:
                continue

            path, fragment = normalized
            target_file = resolve_target(site_dir, path)
            location = reference_location(site_dir, ref)

            if target_file is None:
                errors.append(
                    f"{location}: missing {ref.kind} target {value!r} "
                    f"from <{ref.tag} {ref.attr}>"
                )
                continue

            if fragment and fragment.startswith(":~:text="):
                continue

            if fragment and target_file.suffix == ".html":
                anchors = anchors_by_file.get(target_file, set())
                if fragment not in anchors:
                    errors.append(
                        f"{location}: missing fragment #{fragment} in "
                        f"{target_file.relative_to(site_dir).as_posix()} for {value!r}"
                    )

    if errors:
        print("Generated site validation failed:")
        for error in errors:
            print(f"  - {error}")
        return 1

    print(f"Generated site validation passed: checked {len(references)} references.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
