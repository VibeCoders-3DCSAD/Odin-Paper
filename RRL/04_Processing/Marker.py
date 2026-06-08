#!/usr/bin/env python3
"""
PDF to Markdown Converter

Usage: python Marker.py [target_directory]

Scans the target directory (current directory by default) for PDF files,
converts each to Markdown (via the markitdown package), and creates an empty summary file.
"""

import argparse
import logging
import sys
from pathlib import Path

try:
    from markitdown import MarkItDown
except ImportError:
    raise ImportError(
        "The 'markitdown' package is required. Install it with: pip install markitdown"
    )


def find_pdfs(directory: Path) -> list[Path]:
    """Return a list of PDF file paths in the given directory."""
    return list(directory.glob("*.pdf"))


def convert_pdf_to_markdown(pdf_path: Path, output_md_path: Path) -> None:
    """
    Convert a PDF file to Markdown using MarkItDown and write to output_md_path.
    """
    md_converter = MarkItDown()
    result = md_converter.convert(str(pdf_path))
    output_md_path.write_text(result.text_content, encoding="utf-8")


def create_empty_summary(summary_path: Path) -> None:
    """Create an empty summary file."""
    summary_path.touch()


def main():
    parser = argparse.ArgumentParser(
        description="Convert PDF files in a directory to Markdown and create empty summary files."
    )
    parser.add_argument(
        "target_dir",
        nargs="?",
        default=".",
        help="Directory containing PDF files (default: current directory)",
    )
    parser.add_argument(
        "--suffix",
        default="_marked.md",
        help="Suffix for the converted Markdown file (default: '_marked.md')",
    )
    parser.add_argument(
        "--summary-suffix",
        default="_summarized.md",
        help="Suffix for the empty summary file (default: '_summarized.md')",
    )
    parser.add_argument(
        "--no-summary",
        action="store_true",
        help="Do not create empty summary files",
    )
    parser.add_argument(
        "--verbose", "-v", action="store_true", help="Enable verbose logging"
    )

    args = parser.parse_args()

    # Configure logging
    log_level = logging.DEBUG if args.verbose else logging.INFO
    logging.basicConfig(level=log_level, format="%(levelname)s: %(message)s")

    target_dir = Path(args.target_dir).resolve()
    if not target_dir.is_dir():
        logging.error(f"'{target_dir}' is not a valid directory.")
        sys.exit(1)

    pdf_files = find_pdfs(target_dir)
    if not pdf_files:
        logging.info(f"No PDF files found in '{target_dir}'.")
        return

    logging.info(f"Found {len(pdf_files)} PDF file(s) in '{target_dir}'.")
    success_count = 0

    for idx, pdf_path in enumerate(pdf_files, start=1):
        stem = pdf_path.stem
        marked_path = target_dir / f"{stem}{args.suffix}"
        summary_path = target_dir / f"{stem}{args.summary_suffix}"

        logging.info(f"[{idx}/{len(pdf_files)}] Converting: {pdf_path.name}")
        try:
            convert_pdf_to_markdown(pdf_path, marked_path)
            logging.debug(f"  -> Created {marked_path.name}")
        except Exception as e:
            logging.error(f"  Failed to convert {pdf_path.name}: {e}")
            continue  # Skip summary creation if conversion fails

        if not args.no_summary:
            create_empty_summary(summary_path)
            logging.debug(f"  -> Created empty summary {summary_path.name}")

        success_count += 1

    logging.info(f"Successfully processed {success_count} of {len(pdf_files)} PDF(s).")


if __name__ == "__main__":
    main()