"""Fetch all files from the Drive thesis folder to google-drive/."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from auth import get_credentials
from client import list_files_in_folder, download_file, export_google_file, EXPORT_MIME_TYPES
from config import THESIS_FOLDER_ID

GOOGLE_DRIVE_DIR = Path(__file__).parent.parent.parent / "google-drive"


def fetch_folder(creds, folder_id: str, out_dir: Path) -> None:
    """Recursively fetch all files from a Drive folder."""
    items = list_files_in_folder(creds, folder_id, page_size=50)

    for item in items:
        name = item["name"]

        if item["mimeType"] == "application/vnd.google-apps.folder":
            sub_dir = out_dir / name.lower().replace(" ", "-")
            sub_dir.mkdir(parents=True, exist_ok=True)
            fetch_folder(creds, item["id"], sub_dir)
        elif item["mimeType"].startswith("application/vnd.google-apps."):
            # Google Workspace file - export as native format
            if item["mimeType"] in EXPORT_MIME_TYPES:
                ext_map = {
                    "application/vnd.google-apps.spreadsheet": ".csv",
                    "application/vnd.google-apps.document": ".docx",
                    "application/vnd.google-apps.form": ".pdf",
                }
                ext = ext_map[item["mimeType"]]
                out_path = out_dir / (name + ext)
                print(f"  {out_dir.name}/{name}{ext} (exported)")
                try:
                    export_google_file(creds, item["id"], str(out_path), item["mimeType"])
                except Exception as e:
                    print(f"  WARNING: Failed to export {name}: {e}")
                    # Remove empty file if created
                    if out_path.exists() and out_path.stat().st_size == 0:
                        out_path.unlink()
        else:
            # Direct download (PDFs, images, .docx, etc.)
            out_path = out_dir / name
            print(f"  {out_dir.name}/{name}")
            download_file(creds, item["id"], str(out_path))


def main():
    creds = get_credentials()
    GOOGLE_DRIVE_DIR.mkdir(parents=True, exist_ok=True)
    print("Fetching all files from Drive thesis folder...\n")

    fetch_folder(creds, THESIS_FOLDER_ID, GOOGLE_DRIVE_DIR)

    print("\nDone.")


if __name__ == "__main__":
    main()
