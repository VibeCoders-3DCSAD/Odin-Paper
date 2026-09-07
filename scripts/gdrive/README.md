# Google Drive API CLI

Local-only CLI for reading files from Google Drive via OAuth 2.0 refresh token authentication.

## Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Copy `.env.example` to `.env` and fill in your credentials:
   ```bash
   cp .env.example .env
   ```

## Usage

All commands are run from this directory:

```bash
python cli.py --list                      # List top-level files
python cli.py --folder FOLDER_ID          # List files in a folder
python cli.py --search "query"            # Search files by name
python cli.py --info FILE_ID              # Get file metadata
python cli.py --download FILE_ID -o out   # Download a file
```

Add `--limit N` to control result count (default: 10).

## File Export

The `fetch_drive.py` script automatically exports Google Workspace files to their native formats:

| Google Workspace Type | Export Format | Extension |
|----------------------|---------------|-----------|
| Google Sheets | CSV | `.csv` |
| Google Docs | DOCX | `.docx` |
| Google Forms | PDF | `.pdf` |

Direct downloads (PDFs, images, .docx files) are saved as-is.

## Files

| File | Purpose |
|------|---------|
| `config.py` | Shared constants (THESIS_FOLDER_ID) |
| `auth.py` | OAuth 2.0 credential management, token caching |
| `client.py` | Google Drive API wrapper functions |
| `cli.py` | CLI entry point (argparse) |
| `fetch_drive.py` | Fetch all Drive files to google-drive/ |
| `.env` | Live credentials (gitignored, never commit) |
| `.env.example` | Credential template |
