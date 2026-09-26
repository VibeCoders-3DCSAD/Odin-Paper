"""Fetch all files from the Drive thesis folder to google-drive/.

Also writes google-drive/INVENTORY.md: every item's Drive ID, MIME type,
modified time, and local mirror path. AGENTS.md carries the human-maintained
tree, and it kept going stale because nothing recorded the IDs as they were
fetched. Regenerate the inventory and copy the new rows across after any fetch
that adds or moves a file.
"""

import sys
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from auth import get_credentials
from client import list_files_in_folder, download_file, export_google_file, EXPORT_MIME_TYPES
from config import THESIS_FOLDER_ID

GOOGLE_DRIVE_DIR = Path(__file__).parent.parent.parent / "google-drive"
INVENTORY = GOOGLE_DRIVE_DIR / "INVENTORY.md"

# Collected during the walk: (depth, name, drive_id, mime, modified, local_path)
_rows: list[tuple] = []


def _stamp(item) -> str:
    raw = item.get("modifiedTime")
    if not raw:
        return ""
    return datetime.fromisoformat(raw.replace("Z", "+00:00")).astimezone().strftime("%Y-%m-%d")


def fetch_folder(creds, folder_id: str, out_dir: Path) -> None:
    """Recursively fetch all files from a Drive folder."""
    items = list_files_in_folder(creds, folder_id, page_size=50)

    for item in items:
        name = item["name"]

        if item["mimeType"] == "application/vnd.google-apps.folder":
            sub_dir = out_dir / name.lower().replace(" ", "-")
            sub_dir.mkdir(parents=True, exist_ok=True)
            _rows.append((len(out_dir.relative_to(GOOGLE_DRIVE_DIR).parts),
                          name, item["id"], "Folder", _stamp(item),
                          str(sub_dir.relative_to(GOOGLE_DRIVE_DIR)) + "/"))
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
                _rows.append((len(out_dir.relative_to(GOOGLE_DRIVE_DIR).parts), name, item["id"],
                              item["mimeType"].rsplit(".", 1)[-1].title(), _stamp(item),
                              str(out_path.relative_to(GOOGLE_DRIVE_DIR))))
        else:
            # Direct download (PDFs, images, .docx, etc.)
            out_path = out_dir / name
            print(f"  {out_dir.name}/{name}")
            download_file(creds, item["id"], str(out_path))
            _rows.append((len(out_dir.relative_to(GOOGLE_DRIVE_DIR).parts), name, item["id"],
                          Path(name).suffix.lstrip(".").upper() or "Binary", _stamp(item),
                          str(out_path.relative_to(GOOGLE_DRIVE_DIR))))


def write_inventory() -> None:
    """Emit the ID table that AGENTS.md has to mirror by hand."""
    now = datetime.now(timezone.utc).astimezone().strftime("%Y-%m-%d %H:%M %Z")
    lines = [
        "# Google Drive Inventory (generated)",
        "",
        f"Generated {now} by `scripts/gdrive/fetch_drive.py`. Do not edit by hand.",
        "",
        "AGENTS.md carries the curated Drive tree and ID table. After a fetch that adds, moves,",
        "or renames anything, diff this file against that table and copy the changed rows across.",
        "",
        f"{len(_rows)} items.",
        "",
        "| Item | Drive ID | Type | Modified | Local mirror |",
        "|---|---|---|---|---|",
    ]
    for _, name, did, mime, mod, local in sorted(_rows, key=lambda r: (r[5].lower(), r[1].lower())):
        lines.append(f"| {name} | `{did}` | {mime} | {mod} | `{local}` |")
    INVENTORY.write_text("\n".join(lines) + "\n")
    print(f"\nWrote {INVENTORY} ({len(_rows)} items).")
    print("Reminder: sync new/changed rows into the AGENTS.md Drive table.")


def main():
    creds = get_credentials()
    GOOGLE_DRIVE_DIR.mkdir(parents=True, exist_ok=True)
    print("Fetching all files from Drive thesis folder...\n")

    fetch_folder(creds, THESIS_FOLDER_ID, GOOGLE_DRIVE_DIR)
    write_inventory()

    print("\nDone.")


if __name__ == "__main__":
    main()
