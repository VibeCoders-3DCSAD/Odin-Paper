"""Google Drive API wrapper functions."""

from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials

# MIME type mapping for Google Workspace file exports
EXPORT_MIME_TYPES = {
    "application/vnd.google-apps.spreadsheet": "text/csv",
    "application/vnd.google-apps.document": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
    "application/vnd.google-apps.form": "application/pdf",
}


def _service(creds: Credentials):
    return build("drive", "v3", credentials=creds)


def list_files(creds: Credentials, page_size: int = 10) -> list[dict]:
    """List top-level files visible to the account."""
    service = _service(creds)
    results = (
        service.files()
        .list(pageSize=page_size, fields="files(id, name, mimeType, modifiedTime)")
        .execute()
    )
    return results.get("files", [])


def list_files_in_folder(
    creds: Credentials, folder_id: str, page_size: int = 10
) -> list[dict]:
    """List files inside a specific folder."""
    service = _service(creds)
    q = f"'{folder_id}' in parents and trashed=false"
    results = (
        service.files()
        .list(
            q=q,
            pageSize=page_size,
            fields="files(id, name, mimeType, modifiedTime)",
        )
        .execute()
    )
    return results.get("files", [])


def download_file(creds: Credentials, file_id: str, output_path: str) -> None:
    """Download a file by its ID to the given output path."""
    service = _service(creds)
    request = service.files().get_media(fileId=file_id)

    with open(output_path, "wb") as f:
        from googleapiclient.http import MediaIoBaseDownload

        downloader = MediaIoBaseDownload(f, request)
        done = False
        while not done:
            _, done = downloader.next_chunk()


def export_google_file(creds: Credentials, file_id: str, output_path: str, mime_type: str) -> None:
    """Export a Google Workspace file and save to output_path."""
    service = _service(creds)
    export_mime = EXPORT_MIME_TYPES.get(mime_type)
    if not export_mime:
        raise ValueError(f"Unsupported Google Workspace type: {mime_type}")
    
    request = service.files().export_media(fileId=file_id, mimeType=export_mime)
    with open(output_path, "wb") as f:
        from googleapiclient.http import MediaIoBaseDownload
        downloader = MediaIoBaseDownload(f, request)
        done = False
        while not done:
            _, done = downloader.next_chunk()


def get_file_metadata(creds: Credentials, file_id: str) -> dict:
    """Return metadata for a single file."""
    service = _service(creds)
    return (
        service.files()
        .get(
            fileId=file_id,
            fields="id, name, mimeType, size, createdTime, modifiedTime, owners",
        )
        .execute()
    )


def search_files(creds: Credentials, query: str, page_size: int = 10) -> list[dict]:
    """Search files using Drive query syntax (e.g. name contains 'report')."""
    service = _service(creds)
    q = f"name contains '{query}' and trashed=false"
    results = (
        service.files()
        .list(
            q=q,
            pageSize=page_size,
            fields="files(id, name, mimeType, modifiedTime)",
        )
        .execute()
    )
    return results.get("files", [])
