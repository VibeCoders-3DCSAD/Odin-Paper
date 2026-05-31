#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import re
import statistics
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path


LIGATURES = str.maketrans(
    {
        "ﬀ": "ff",
        "ﬁ": "fi",
        "ﬂ": "fl",
        "ﬃ": "ffi",
        "ﬄ": "ffl",
        "ﬅ": "ft",
        "ﬆ": "st",
    }
)

HEADER_FOOTER_PATTERNS = (
    re.compile(r"^https?://", re.IGNORECASE),
    re.compile(r"^\d+\s+of\s+\d+$", re.IGNORECASE),
    re.compile(r"^\d{1,2}/\d{1,2}/\d{2,4},\s+\d{1,2}:\d{2}"),
)

BULLET_CHARS = "•●◦▪▫‣"


@dataclass(frozen=True)
class Word:
    text: str
    left: float
    top: float
    width: float
    height: float

    @property
    def right(self) -> float:
        return self.left + self.width

    @property
    def char_width(self) -> float:
        visible = max(len(self.text.strip()), 1)
        return self.width / visible


@dataclass
class Line:
    page: int
    paragraph: int
    block: int
    number: int
    left: float
    top: float
    height: float
    words: list[Word]
    page_height: float

    @property
    def right(self) -> float:
        return max(word.right for word in self.words)

    @property
    def text(self) -> str:
        return build_text(self.words)

    @property
    def cells(self) -> list[str]:
        return build_cells(self.words, self.height)


def normalize_text(value: str) -> str:
    return value.translate(LIGATURES).replace("\u00a0", " ")


def build_text(words: list[Word]) -> str:
    if not words:
        return ""
    text = " ".join(normalize_text(word.text).strip() for word in words if word.text.strip())
    text = re.sub(r"\s+([,.;:!?%])", r"\1", text)
    text = re.sub(r"([(\[{])\s+", r"\1", text)
    text = re.sub(r"\s+([)\]}])", r"\1", text)
    return re.sub(r"\s{2,}", " ", text).strip()


def build_cells(words: list[Word], line_height: float) -> list[str]:
    if not words:
        return []

    segments: list[list[Word]] = [[words[0]]]
    previous = words[0]
    for word in words[1:]:
        gap = word.left - previous.right
        threshold = max(previous.char_width * 2.4, word.char_width * 2.4, line_height * 1.15)
        if gap > threshold:
            segments.append([word])
        else:
            segments[-1].append(word)
        previous = word
    return [build_text(segment) for segment in segments if build_text(segment)]


def is_centered(line: Line, page_width: float = 612.0) -> bool:
    left_margin = line.left
    right_margin = max(page_width - line.right, 0.0)
    return abs(left_margin - right_margin) <= max(line.height * 2.2, 18.0)


def is_probable_table_row(line: Line) -> bool:
    cells = line.cells
    if len(cells) < 2:
        return False
    text = line.text
    if len(text) > 140:
        return False
    if text.startswith(tuple(f"{n}." for n in range(1, 10))):
        return False
    if text.startswith(tuple(BULLET_CHARS)):
        return False
    return True


def extract_lines(pdf_path: Path) -> list[Line]:
    command = ["pdftotext", "-tsv", "-enc", "UTF-8", str(pdf_path), "-"]
    try:
        result = subprocess.run(command, check=True, capture_output=True, text=True)
    except FileNotFoundError as exc:
        raise SystemExit("`pdftotext` is required but was not found in PATH.") from exc
    except subprocess.CalledProcessError as exc:
        stderr = exc.stderr.strip() or "pdftotext failed to read the PDF."
        raise SystemExit(stderr) from exc

    rows = csv.DictReader(result.stdout.splitlines(), delimiter="\t")
    page_heights: dict[int, float] = {}
    grouped: dict[tuple[int, int, int, int], list[Word]] = {}
    line_meta: dict[tuple[int, int, int, int], tuple[float, float, float]] = {}

    for row in rows:
        level = int(row["level"])
        page = int(row["page_num"])
        if level == 1 and row["text"] == "###PAGE###":
            page_heights[page] = float(row["height"])
            continue
        if level != 5:
            continue
        key = (
            page,
            int(row["par_num"]),
            int(row["block_num"]),
            int(row["line_num"]),
        )
        word = Word(
            text=row["text"],
            left=float(row["left"]),
            top=float(row["top"]),
            width=float(row["width"]),
            height=float(row["height"]),
        )
        grouped.setdefault(key, []).append(word)
        line_meta.setdefault(
            key,
            (
                float(row["left"]),
                float(row["top"]),
                float(row["height"]),
            ),
        )

    lines: list[Line] = []
    for key in sorted(grouped):
        page, paragraph, block, line_number = key
        words = sorted(grouped[key], key=lambda item: (item.left, item.top))
        left, top, height = line_meta[key]
        page_height = page_heights.get(page, 792.0)
        text = build_text(words)
        if not text:
            continue
        lines.append(
            Line(
                page=page,
                paragraph=paragraph,
                block=block,
                number=line_number,
                left=left,
                top=top,
                height=height,
                words=words,
                page_height=page_height,
            )
        )

    return remove_headers_and_footers(lines)


def remove_headers_and_footers(lines: list[Line]) -> list[Line]:
    if not lines:
        return []

    counts: dict[str, int] = {}
    for line in lines:
        counts[line.text] = counts.get(line.text, 0) + 1

    filtered: list[Line] = []
    for line in lines:
        text = line.text
        if any(pattern.search(text) for pattern in HEADER_FOOTER_PATTERNS):
            continue
        repeated = counts[text] > 1
        near_top = line.top < 36
        near_bottom = line.top > line.page_height - 28
        if repeated and (near_top or near_bottom):
            continue
        filtered.append(line)
    return filtered


def median_body_height(lines: list[Line]) -> float:
    heights = [
        line.height
        for line in lines
        if re.search(r"[A-Za-z0-9]", line.text)
        and not re.match(rf"^[{re.escape(BULLET_CHARS)}]\s*$", line.text)
    ]
    return statistics.median(heights) if heights else 14.0


def body_left_margin(lines: list[Line]) -> float:
    candidates = [
        line.left
        for line in lines
        if len(line.text) > 40
        and not is_heading(line, 14.0)
        and not is_list_item(line)
        and not is_probable_table_row(line)
    ]
    return statistics.median(candidates) if candidates else 66.0


def is_heading(line: Line, body_height: float) -> bool:
    text = line.text
    if len(text) > 120:
        return False
    ratio = line.height / max(body_height, 1.0)
    if ratio >= 1.45:
        return True
    if ratio >= 1.22 and is_centered(line):
        return True
    if text.isupper() and 3 <= len(text) <= 60:
        return True
    return False


def collect_heading(lines: list[Line], start: int, body_height: float) -> tuple[str, int]:
    current = lines[start]
    parts = [current.text]
    index = start + 1

    while index < len(lines):
        line = lines[index]
        if line.page != current.page:
            break
        if not is_heading(line, body_height):
            break
        if abs(line.height - current.height) > body_height * 0.2:
            break
        if line.top - lines[index - 1].top > current.height * 1.6:
            break
        if line.block != current.block and line.paragraph != current.paragraph:
            break
        parts.append(line.text)
        index += 1

    return " ".join(parts), index


def heading_prefix(line: Line, body_height: float, index: int) -> str:
    ratio = line.height / max(body_height, 1.0)
    centered = is_centered(line)
    if index == 0 and centered:
        return "#"
    if ratio >= 1.75:
        return "#"
    if ratio >= 1.45 or centered:
        return "##"
    return "###"


def is_list_item(line: Line) -> bool:
    text = line.text
    if re.match(rf"^[{re.escape(BULLET_CHARS)}]\s+", text):
        return True
    if re.match(r"^\d+[.)]\s+", text):
        return True
    if re.match(r"^[-*+]\s+", text):
        return True
    return False


def list_prefix(text: str) -> tuple[str, str]:
    bullet_match = re.match(rf"^([{re.escape(BULLET_CHARS)}]|[-*+])\s+(.*)$", text)
    if bullet_match:
        return "- ", bullet_match.group(2).strip()
    ordered_match = re.match(r"^(\d+)[.)]\s+(.*)$", text)
    if ordered_match:
        return f"{ordered_match.group(1)}. ", ordered_match.group(2).strip()
    return "", text.strip()


def indent_level(line: Line, base_left: float, body_height: float) -> int:
    raw = max(line.left - base_left, 0.0)
    return int(round(raw / max(body_height * 1.25, 12.0)))


def collect_wrapped_text(lines: list[Line], start: int, base_left: float, body_height: float) -> tuple[str, int]:
    current = lines[start]
    text = current.text
    parts = [text]
    index = start + 1

    while index < len(lines):
        line = lines[index]
        previous = lines[index - 1]
        if line.page != current.page:
            break
        if is_heading(line, body_height) or is_list_item(line) or is_probable_table_row(line):
            break
        if line.block != current.block and line.paragraph != current.paragraph:
            break
        if abs(line.height - current.height) > body_height * 0.18:
            break
        if line.left + body_height * 0.4 < previous.left:
            break
        parts.append(line.text)
        index += 1

    merged = " ".join(part.strip() for part in parts)
    merged = re.sub(r"\s+", " ", merged).strip()
    return merged, index


def collect_list_item(lines: list[Line], start: int, base_left: float, body_height: float) -> tuple[str, int]:
    line = lines[start]
    prefix, initial = list_prefix(line.text)
    parts = [initial]
    index = start + 1

    while index < len(lines):
        next_line = lines[index]
        if next_line.page != line.page:
            break
        if is_heading(next_line, body_height) or is_list_item(next_line) or is_probable_table_row(next_line):
            break
        continuation_indent = next_line.left - line.left
        if continuation_indent < body_height * 0.6 and next_line.block != line.block:
            break
        parts.append(next_line.text)
        index += 1

    content = " ".join(part.strip() for part in parts)
    content = re.sub(r"\s+", " ", content).strip()
    level = indent_level(line, base_left, body_height)
    return f"{'  ' * level}{prefix}{content}", index


def collect_table(lines: list[Line], start: int) -> tuple[list[str], int] | None:
    first = lines[start]
    if not is_probable_table_row(first):
        return None

    rows = [first.cells]
    index = start + 1
    column_count = len(rows[0])

    while index < len(lines):
        line = lines[index]
        cells = line.cells
        if line.page != first.page or not is_probable_table_row(line):
            break
        if len(cells) != column_count:
            break
        rows.append(cells)
        index += 1

    if len(rows) < 2:
        return None
    if column_count < 3 and len(rows) < 3:
        return None

    markdown_rows = []
    header = rows[0]
    markdown_rows.append("| " + " | ".join(cell.strip() for cell in header) + " |")
    markdown_rows.append("| " + " | ".join("---" for _ in header) + " |")
    for row in rows[1:]:
        markdown_rows.append("| " + " | ".join(cell.strip() for cell in row) + " |")
    return markdown_rows, index


def is_blockquote(line: Line, base_left: float, body_height: float) -> bool:
    return False


def convert_lines_to_markdown(lines: list[Line]) -> str:
    if not lines:
        return ""

    body_height = median_body_height(lines)
    base_left = body_left_margin(lines)
    output: list[str] = []
    index = 0

    while index < len(lines):
        line = lines[index]
        text = line.text.strip()
        if not text:
            index += 1
            continue

        table = collect_table(lines, index)
        if table:
            rows, next_index = table
            output.extend(rows)
            output.append("")
            index = next_index
            continue

        if is_heading(line, body_height):
            heading_text, next_index = collect_heading(lines, index, body_height)
            output.append(f"{heading_prefix(line, body_height, index)} {heading_text}")
            output.append("")
            index = next_index
            continue

        if is_list_item(line):
            item, next_index = collect_list_item(lines, index, base_left, body_height)
            output.append(item)
            index = next_index
            if index >= len(lines) or not is_list_item(lines[index]):
                output.append("")
            continue

        paragraph, next_index = collect_wrapped_text(lines, index, base_left, body_height)
        if is_blockquote(line, base_left, body_height):
            output.append(f"> {paragraph}")
        else:
            output.append(paragraph)
        output.append("")
        index = next_index

    markdown = "\n".join(output)
    markdown = re.sub(r"\n{3,}", "\n\n", markdown).strip()
    return markdown + "\n"


def convert_pdf_to_markdown(pdf_path: Path) -> str:
    return convert_lines_to_markdown(extract_lines(pdf_path))


def build_argument_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Convert a PDF into Markdown using pdftotext and local layout heuristics."
    )
    parser.add_argument("pdf", type=Path, help="Path to the source PDF file.")
    parser.add_argument(
        "-o",
        "--output",
        type=Path,
        help="Write the Markdown output to this file instead of stdout.",
    )
    return parser


def main() -> int:
    parser = build_argument_parser()
    args = parser.parse_args()

    pdf_path: Path = args.pdf.expanduser().resolve()
    if not pdf_path.is_file():
        parser.error(f"PDF file not found: {pdf_path}")

    markdown = convert_pdf_to_markdown(pdf_path)

    if args.output:
        output_path = args.output.expanduser().resolve()
        output_path.write_text(markdown, encoding="utf-8")
    else:
        sys.stdout.write(markdown)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
