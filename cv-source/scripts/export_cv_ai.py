#!/usr/bin/env python3
"""Generate AI-readable CV exports from data/cv_master.json.

Outputs are intentionally plain: Markdown, JSON, and text. They avoid columns,
graphics, private phone numbers, addresses, and references by default.
"""

from __future__ import annotations

import argparse
import json
import re
from datetime import date
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "data" / "cv_master.json"
EXPORTS = ROOT / "exports"
EXPORT_DATE_RE = re.compile(r"\d{4}-\d{2}-\d{2}")


def bullet(items: list[str]) -> str:
    return "".join(f"- {item}\n" for item in items)


def claim_block(claims: list[str], indent: str = "") -> str:
    return "".join(f"{indent}- {claim}\n" for claim in claims)


def generate_markdown(cv: dict[str, Any], export_date: str | None = None) -> str:
    export_date = export_date or date.today().isoformat()
    lines: list[str] = []
    lines.append("# David Beckwitt - AI-readable CV\n")
    lines.append(f"Export date: {export_date}\n\n")
    lines.append(
        "This export is plain text, table-free, column-free, and intended for AI parsing. "
        "It omits private phone numbers, addresses, and professional references by default.\n\n"
    )

    ident = cv["identity"]
    lines.append("## Identity\n\n")
    lines.append(f"Name: {ident['name']}\n\n")
    lines.append(f"Degree status: {cv['metadata']['degree_status_required_phrase']}\n\n")
    lines.append(f"Positioning: {ident['current_positioning']}\n\n")
    lines.append(f"Short positioning: {ident['short_positioning']}\n\n")
    lines.append(f"Email: {ident['email']}\n\n")
    lines.append(f"GitHub: {ident['github']}\n\n")
    lines.append(f"LinkedIn: {ident['linkedin']}\n\n")
    lines.append(f"ResearchGate: {ident['researchgate']}\n\n")

    lines.append("## Education\n\n")
    for edu in cv["education"]:
        degree = edu["degree"]
        inst = edu["institution"]
        loc = edu.get("location", "")
        status = edu.get("status") or edu.get("date", "")
        lines.append(f"### {degree}, {inst}\n\n")
        if loc:
            lines.append(f"Location: {loc}\n\n")
        if status:
            lines.append(f"Date/status: {status}\n\n")
        if "dissertation" in edu:
            lines.append(f"Dissertation: {edu['dissertation']}\n\n")
        if "advisor" in edu:
            lines.append(f"Advisor: {edu['advisor']}\n\n")
        if "minors" in edu:
            lines.append("Minors:\n")
            lines.append(bullet(edu["minors"]))
            lines.append("\n")

    lines.append("## Experience\n\n")
    for role in cv["experience"]:
        lines.append(f"### {role['title']}, {role['organization']}\n\n")
        if role.get("location"):
            lines.append(f"Location: {role['location']}\n\n")
        lines.append(f"Dates: {role['dates']}\n\n")
        if role.get("focus"):
            lines.append(f"Focus: {role['focus']}\n\n")
        lines.append("Supported claims:\n")
        lines.append(claim_block(role["supported_claims"]))
        lines.append("\n")

    lines.append("## Applied research tools\n\n")
    for project in cv["projects"]:
        lines.append(f"### {project['name']}\n\n")
        lines.append(f"Dates: {project['dates']}\n\n")
        lines.append(f"Type: {project['type']}\n\n")
        lines.append(f"URL: {project['url']}\n\n")
        lines.append("Supported claims:\n")
        lines.append(claim_block(project["supported_claims"]))
        lines.append("\n")

    lines.append("## Skills\n\n")
    for group, values in cv["skills"].items():
        title = group.replace("_", " ").title()
        lines.append(f"### {title}\n\n")
        lines.append(bullet(values))
        lines.append("\n")

    lines.append("## Publications\n\n")
    for pub in cv["publications"]:
        lines.append(f"- {pub['citation']}\n")
        if pub.get("doi"):
            lines.append(f"  - DOI: {pub['doi']}\n")
    lines.append("\n")

    lines.append("## Selected presentations\n\n")
    lines.append(bullet(cv["presentations"]))
    lines.append("\n")

    lines.append("## Teaching\n\n")
    for role in cv["teaching"]["roles"]:
        org = role.get("organization") or ", ".join(role.get("organizations", []))
        lines.append(f"### {role['title']}, {org}\n\n")
        lines.append(f"Dates: {role['dates']}\n\n")
        lines.append("Supported claims:\n")
        lines.append(claim_block(role["supported_claims"]))
        lines.append("\n")
    lines.append("### Teaching methods from teaching philosophy\n\n")
    lines.append(bullet(cv["teaching"]["methods_from_teaching_philosophy"]))
    lines.append("\n")

    lines.append("## Service and outreach\n\n")
    lines.append(bullet(cv["service_and_outreach"]))
    lines.append("\n")

    lines.append("## Awards\n\n")
    lines.append(bullet(cv["awards"]))
    lines.append("\n")

    lines.append("## Claims requiring confirmation before use\n\n")
    lines.append(bullet(cv["claims_requiring_confirmation_before_use"]))
    return "".join(lines)


def markdown_to_plain_text(markdown: str) -> str:
    text = markdown.replace("#", "")
    text = text.replace("**", "")
    lines = [line.rstrip() for line in text.splitlines()]
    return "\n".join(lines).strip() + "\n"


def write_exports(output_dir: Path = EXPORTS, export_date: str | None = None) -> list[Path]:
    export_date = export_date or date.today().isoformat()
    output_dir.mkdir(parents=True, exist_ok=True)
    cv = json.loads(SOURCE.read_text(encoding="utf-8"))
    cv_export = json.loads(json.dumps(cv))
    cv_export.setdefault("metadata", {})["export_date"] = export_date
    json_path = output_dir / "Beckwitt_CV_AI.json"
    markdown_path = output_dir / "Beckwitt_CV_AI.md"
    text_path = output_dir / "Beckwitt_CV_AI.txt"
    json_path.write_text(
        json.dumps(cv_export, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    markdown = generate_markdown(cv, export_date=export_date)
    markdown_path.write_text(markdown, encoding="utf-8")
    text_path.write_text(markdown_to_plain_text(markdown), encoding="utf-8")
    return [markdown_path, json_path, text_path]


def parse_export_date(value: str) -> str:
    if EXPORT_DATE_RE.fullmatch(value) is None:
        raise argparse.ArgumentTypeError("export date must use YYYY-MM-DD")
    try:
        parsed = date.fromisoformat(value)
    except ValueError as exc:
        raise argparse.ArgumentTypeError("export date must be a valid date") from exc
    if parsed.isoformat() != value:
        raise argparse.ArgumentTypeError("export date must round-trip as YYYY-MM-DD")
    return value


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=EXPORTS,
        help="Directory for generated exports. Defaults to exports/.",
    )
    parser.add_argument(
        "--export-date",
        type=parse_export_date,
        default=None,
        help="Override export date in YYYY-MM-DD form. Defaults to today.",
    )
    return parser.parse_args()


def display_path(path: Path) -> str:
    try:
        return path.resolve().relative_to(ROOT).as_posix()
    except ValueError:
        return str(path)


def main() -> None:
    args = parse_args()
    for path in write_exports(output_dir=args.output_dir, export_date=args.export_date):
        print(f"Wrote {display_path(path)}")


if __name__ == "__main__":
    main()
