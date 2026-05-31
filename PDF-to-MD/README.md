# PDF to Markdown

Standalone local tool for converting PDF files into Markdown.

## What it includes

- `pdf_to_md.py`: command-line PDF to Markdown converter
- `pdf_to_md_server.py`: local web server for the browser UI
- `index.html`, `pdf-to-md.js`, `markdown-preview.js`, `styles.css`: browser interface

## Requirements

- Python 3.10+
- `pdftotext` available in `PATH`

Check it with:

```bash
pdftotext -v
```

If `pdftotext` is missing, install Poppler utilities for your OS.

## Optional virtual environment

This project uses only the Python standard library, so a virtual environment is not required.
If you still want one:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

## CLI usage

Convert a PDF and print Markdown to stdout:

```bash
python3 pdf_to_md.py input.pdf
```

Write Markdown to a file:

```bash
python3 pdf_to_md.py input.pdf -o output.md
```

## Browser usage

Start the local server:

```bash
python3 pdf_to_md_server.py
```

Then open:

```text
http://127.0.0.1:8000
```

Upload a PDF, click `Convert PDF`, review the Markdown preview, then click `Download MD`.

## Notes

- The conversion is heuristic. Clean PDFs work best.
- Complex layouts, multi-column documents, and dense tables may need manual Markdown cleanup.
- The web UI calls the local `/api/pdf-to-md` endpoint exposed by `pdf_to_md_server.py`.
