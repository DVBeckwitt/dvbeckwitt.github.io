#!/usr/bin/env python3
"""Create and read simple AI-legible DOCX application documents.

The writer intentionally supports a conservative Markdown subset: headings,
paragraphs, hyphen bullets, numbered lines, links, and simple pipe-table rows.
It avoids columns, text boxes, images, comments, tracked changes, and custom
binary dependencies so generated application files stay easy for humans, ATS
systems, and AI tools to parse.
"""

from __future__ import annotations

import argparse
import re
import zipfile
from collections.abc import Iterable
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from xml.etree import ElementTree
from xml.sax.saxutils import escape

ROOT = Path(__file__).resolve().parents[1]
MARKDOWN_LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
MARKDOWN_CODE_SPAN_RE = re.compile(r"`([^`]+)`")
MARKDOWN_BOLD_RE = re.compile(r"(\*\*|__)(?=\S)(.+?\S)\1")
MARKDOWN_ITALIC_RE = re.compile(r"(?<!\*)\*(?!\*)(?=\S)(.+?\S)(?<!\*)\*(?!\*)")
PIPE_TABLE_DELIMITER_RE = re.compile(r"^\s*\|?(?:\s*:?-{3,}:?\s*\|)+\s*:?-{3,}:?\s*\|?\s*$")
WORD_NAMESPACE = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"


@dataclass(frozen=True)
class DocxBlock:
    style: str
    text: str


def clean_inline_markdown(text: str) -> str:
    text = MARKDOWN_LINK_RE.sub(r"\1 (\2)", text)
    text = MARKDOWN_CODE_SPAN_RE.sub(r"\1", text)
    text = MARKDOWN_BOLD_RE.sub(r"\2", text)
    text = MARKDOWN_ITALIC_RE.sub(r"\1", text)
    return text.strip()


def pipe_row_to_text(line: str) -> str:
    cells = [clean_inline_markdown(cell.strip()) for cell in line.strip().strip("|").split("|")]
    return " | ".join(cell for cell in cells if cell)


def markdown_to_blocks(markdown: str) -> list[DocxBlock]:
    blocks: list[DocxBlock] = []
    for raw_line in markdown.splitlines():
        line = raw_line.rstrip()
        stripped = line.strip()
        if not stripped:
            continue
        if PIPE_TABLE_DELIMITER_RE.match(stripped):
            continue
        if stripped.startswith("#"):
            marker, _, heading = stripped.partition(" ")
            level = min(max(len(marker), 1), 3)
            blocks.append(DocxBlock(f"Heading{level}", clean_inline_markdown(heading)))
            continue
        if stripped.startswith("- "):
            blocks.append(DocxBlock("ListParagraph", "- " + clean_inline_markdown(stripped[2:])))
            continue
        if stripped.startswith("* "):
            blocks.append(DocxBlock("ListParagraph", "- " + clean_inline_markdown(stripped[2:])))
            continue
        if re.match(r"^\d+\.\s+", stripped):
            blocks.append(DocxBlock("ListParagraph", clean_inline_markdown(stripped)))
            continue
        if "|" in stripped and stripped.count("|") >= 2:
            blocks.append(DocxBlock("Normal", pipe_row_to_text(stripped)))
            continue
        blocks.append(DocxBlock("Normal", clean_inline_markdown(stripped)))
    return blocks


def paragraph_xml(block: DocxBlock) -> str:
    style_xml = ""
    if block.style != "Normal":
        style_xml = f'<w:pPr><w:pStyle w:val="{escape(block.style)}"/></w:pPr>'
    text = escape(block.text)
    return f"<w:p>{style_xml}<w:r><w:t>{text}</w:t></w:r></w:p>"


def document_xml(blocks: Iterable[DocxBlock]) -> str:
    paragraphs = "".join(paragraph_xml(block) for block in blocks)
    return f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">
  <w:body>
    {paragraphs}
    <w:sectPr>
      <w:pgSz w:w="12240" w:h="15840"/>
      <w:pgMar
        w:top="720"
        w:right="720"
        w:bottom="720"
        w:left="720"
        w:header="360"
        w:footer="360"
        w:gutter="0"/>
    </w:sectPr>
  </w:body>
</w:document>
"""


def content_types_xml() -> str:
    return """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
  <Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>
  <Default Extension="xml" ContentType="application/xml"/>
  <Override
    PartName="/word/document.xml"
    ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>
  <Override
    PartName="/word/styles.xml"
    ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.styles+xml"/>
  <Override
    PartName="/docProps/core.xml"
    ContentType="application/vnd.openxmlformats-package.core-properties+xml"/>
  <Override
    PartName="/docProps/app.xml"
    ContentType="application/vnd.openxmlformats-officedocument.extended-properties+xml"/>
</Types>
"""


def package_rels_xml() -> str:
    return """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship
    Id="rId1"
    Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument"
    Target="word/document.xml"/>
  <Relationship
    Id="rId2"
    Type="http://schemas.openxmlformats.org/package/2006/relationships/metadata/core-properties"
    Target="docProps/core.xml"/>
  <Relationship
    Id="rId3"
    Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/extended-properties"
    Target="docProps/app.xml"/>
</Relationships>
"""


def document_rels_xml() -> str:
    return """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship
    Id="rId1"
    Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/styles"
    Target="styles.xml"/>
</Relationships>
"""


def styles_xml() -> str:
    return """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:styles xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">
  <w:style w:type="paragraph" w:default="1" w:styleId="Normal">
    <w:name w:val="Normal"/>
    <w:qFormat/>
    <w:pPr><w:spacing w:after="120"/></w:pPr>
    <w:rPr><w:rFonts w:ascii="Calibri" w:hAnsi="Calibri"/><w:sz w:val="22"/></w:rPr>
  </w:style>
  <w:style w:type="paragraph" w:styleId="Heading1">
    <w:name w:val="heading 1"/>
    <w:basedOn w:val="Normal"/>
    <w:next w:val="Normal"/>
    <w:qFormat/>
    <w:pPr><w:spacing w:before="240" w:after="120"/></w:pPr>
    <w:rPr><w:b/><w:sz w:val="32"/></w:rPr>
  </w:style>
  <w:style w:type="paragraph" w:styleId="Heading2">
    <w:name w:val="heading 2"/>
    <w:basedOn w:val="Normal"/>
    <w:next w:val="Normal"/>
    <w:qFormat/>
    <w:pPr><w:spacing w:before="200" w:after="80"/></w:pPr>
    <w:rPr><w:b/><w:sz w:val="26"/></w:rPr>
  </w:style>
  <w:style w:type="paragraph" w:styleId="Heading3">
    <w:name w:val="heading 3"/>
    <w:basedOn w:val="Normal"/>
    <w:next w:val="Normal"/>
    <w:qFormat/>
    <w:pPr><w:spacing w:before="160" w:after="80"/></w:pPr>
    <w:rPr><w:b/><w:sz w:val="23"/></w:rPr>
  </w:style>
  <w:style w:type="paragraph" w:styleId="ListParagraph">
    <w:name w:val="List Paragraph"/>
    <w:basedOn w:val="Normal"/>
    <w:qFormat/>
    <w:pPr><w:ind w:left="360" w:hanging="180"/></w:pPr>
  </w:style>
</w:styles>
"""


def core_props_xml() -> str:
    timestamp = datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")
    return f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<cp:coreProperties
  xmlns:cp="http://schemas.openxmlformats.org/package/2006/metadata/core-properties"
  xmlns:dc="http://purl.org/dc/elements/1.1/"
  xmlns:dcterms="http://purl.org/dc/terms/"
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dc:creator>Beckwitt_CV repository</dc:creator>
  <cp:lastModifiedBy>Beckwitt_CV repository</cp:lastModifiedBy>
  <dcterms:created xsi:type="dcterms:W3CDTF">{timestamp}</dcterms:created>
  <dcterms:modified xsi:type="dcterms:W3CDTF">{timestamp}</dcterms:modified>
</cp:coreProperties>
"""


def app_props_xml() -> str:
    return """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Properties xmlns="http://schemas.openxmlformats.org/officeDocument/2006/extended-properties" xmlns:vt="http://schemas.openxmlformats.org/officeDocument/2006/docPropsVTypes">
  <Application>Beckwitt_CV repository</Application>
</Properties>
"""


def write_docx_from_markdown(markdown: str, output_path: Path) -> Path:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    blocks = markdown_to_blocks(markdown)
    with zipfile.ZipFile(output_path, "w", compression=zipfile.ZIP_DEFLATED) as docx:
        docx.writestr("[Content_Types].xml", content_types_xml())
        docx.writestr("_rels/.rels", package_rels_xml())
        docx.writestr("word/_rels/document.xml.rels", document_rels_xml())
        docx.writestr("word/document.xml", document_xml(blocks))
        docx.writestr("word/styles.xml", styles_xml())
        docx.writestr("docProps/core.xml", core_props_xml())
        docx.writestr("docProps/app.xml", app_props_xml())
    return output_path


def docx_part_text(docx: zipfile.ZipFile, part_name: str) -> list[str]:
    if part_name not in docx.namelist():
        return []
    root = ElementTree.fromstring(docx.read(part_name))
    lines: list[str] = []
    for paragraph in root.iter(f"{WORD_NAMESPACE}p"):
        pieces: list[str] = []
        for element in paragraph.iter():
            if element.tag == f"{WORD_NAMESPACE}t" and element.text:
                pieces.append(element.text)
            elif element.tag == f"{WORD_NAMESPACE}tab":
                pieces.append("\t")
            elif element.tag == f"{WORD_NAMESPACE}br":
                pieces.append("\n")
        line = "".join(pieces).strip()
        if line:
            lines.append(line)
    return lines


def extract_docx_text(path: Path) -> str:
    with zipfile.ZipFile(path) as docx:
        part_names = ["word/document.xml"]
        part_names.extend(
            sorted(
                name
                for name in docx.namelist()
                if re.fullmatch(r"word/(?:header|footer)\d+\.xml", name)
            )
        )
        lines: list[str] = []
        for part_name in part_names:
            lines.extend(docx_part_text(docx, part_name))
    return "\n".join(lines).strip() + "\n"


def default_output_path(input_path: Path) -> Path:
    return input_path.with_suffix(".docx")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path, help="Markdown or plain-text source file.")
    parser.add_argument(
        "output",
        type=Path,
        nargs="?",
        help="DOCX output path. Defaults to the input path with a .docx suffix.",
    )
    parser.add_argument(
        "--extract-text",
        action="store_true",
        help="Print extracted DOCX text instead of creating a DOCX file.",
    )
    return parser.parse_args()


def display_path(path: Path) -> str:
    try:
        return path.resolve().relative_to(ROOT).as_posix()
    except ValueError:
        return str(path)


def main() -> int:
    args = parse_args()
    if args.extract_text:
        print(extract_docx_text(args.input), end="")
        return 0

    markdown = args.input.read_text(encoding="utf-8")
    output = args.output or default_output_path(args.input)
    write_docx_from_markdown(markdown, output)
    print(f"Wrote {display_path(output)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
