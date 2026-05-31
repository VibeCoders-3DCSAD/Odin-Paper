#!/usr/bin/env python3
from __future__ import annotations

import argparse
import sys
import tempfile
from email.parser import BytesParser
from email.policy import default
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

from pdf_to_md import convert_pdf_to_markdown


ROOT = Path(__file__).resolve().parent


def parse_form_data(content_type: str, body: bytes) -> dict[str, tuple[str | None, bytes]]:
    raw_message = (
        f"Content-Type: {content_type}\r\nMIME-Version: 1.0\r\n\r\n".encode("utf-8") + body
    )
    message = BytesParser(policy=default).parsebytes(raw_message)
    if not message.is_multipart():
        raise ValueError("Expected multipart form data.")

    fields: dict[str, tuple[str | None, bytes]] = {}
    for part in message.iter_parts():
        if part.get_content_disposition() != "form-data":
            continue
        name = part.get_param("name", header="content-disposition")
        if not name:
            continue
        fields[name] = (
            part.get_filename(),
            part.get_payload(decode=True) or b"",
        )
    return fields


class PdfToMarkdownHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(ROOT), **kwargs)

    def do_POST(self) -> None:
        if self.path != "/api/pdf-to-md":
            self.send_error(404, "Not found.")
            return

        content_type = self.headers.get("Content-Type", "")
        if "multipart/form-data" not in content_type:
            self.send_error(415, "Use multipart/form-data.")
            return

        try:
            content_length = int(self.headers.get("Content-Length", "0"))
        except ValueError:
            self.send_error(400, "Invalid Content-Length header.")
            return

        if content_length <= 0:
            self.send_error(400, "Request body is empty.")
            return

        body = self.rfile.read(content_length)
        try:
            fields = parse_form_data(content_type, body)
        except ValueError as exc:
            self.send_error(400, str(exc))
            return

        filename, data = fields.get("pdf", (None, b""))
        if not data:
            self.send_error(400, "Upload a PDF file in the `pdf` field.")
            return

        suffix = Path(filename or "upload.pdf").suffix or ".pdf"
        temp_path: Path | None = None
        try:
            with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as handle:
                handle.write(data)
                temp_path = Path(handle.name)

            markdown = convert_pdf_to_markdown(temp_path)
        except SystemExit as exc:
            self.send_error(500, str(exc))
            return
        finally:
            if temp_path:
                temp_path.unlink(missing_ok=True)

        payload = markdown.encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.send_header("Content-Length", str(len(payload)))
        self.end_headers()
        self.wfile.write(payload)


def build_argument_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Serve the PDF-to-Markdown browser UI and upload API."
    )
    parser.add_argument("--host", default="127.0.0.1", help="Host to bind. Default: 127.0.0.1")
    parser.add_argument("--port", default=8000, type=int, help="Port to bind. Default: 8000")
    return parser


def main() -> int:
    args = build_argument_parser().parse_args()
    server = ThreadingHTTPServer((args.host, args.port), PdfToMarkdownHandler)
    address = f"http://{args.host}:{args.port}"
    print(f"Serving {ROOT} at {address}", file=sys.stderr)

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
