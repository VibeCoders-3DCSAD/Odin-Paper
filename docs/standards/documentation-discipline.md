# Documentation Discipline

Standards for maintaining thesis documents in this repository.

## Purpose

This document governs how Odin thesis documentation is structured, tracked, and kept current. The shared formatting rules (metadata block, heading hierarchy, cross-reference style, placeholder format) live in `documentation-format.md` and apply across all Odin repositories.

## Rules

1. Every document must have a clear purpose stated in its first heading or opening line.
2. Follow the heading hierarchy and formatting rules in `documentation-format.md`.
3. Version-sensitive documents (System Specification, PRD, Model Design) must include the JSON `## Metadata` block (`document-type`, `version`, `date`, `authors`). See `documentation-format.md`.
4. When moving a file, update all documents that reference its old path. Check `INDEX.md`, `AGENTS.md`, and any cross-referencing documents.
5. Mark outdated documents clearly with `(OLD)` or `(OUTDATED)` in the filename and a notice at the top of the file body. Do not delete them outright — they may contain historical context.
6. Keep `INDEX.md` as the authoritative navigation index. When adding, moving, or removing files, update `INDEX.md` in the same commit.
7. AI-generated content (summaries, compilations, analyses) must be distinguishable from human-authored content. Use clear file naming (`_summarized.json`, `_Compilation.md`) and avoid mixing generated and hand-written prose in the same file.
8. Binary assets (PDFs, XLSX, CSV, ZIP) should be tracked via Git LFS. Do not commit large binaries directly to git history.
9. The authoritative versions of the thesis documents live in the Google Drive folder. Repo copies are working mirrors — never assume they are current; verify against the Drive source before citing.
10. Do not leave documents as empty stubs or bare HTML comments. Unwritten documents must use the placeholder format in `documentation-format.md`.

## Cross-References

When one document references another, use relative paths:

```markdown
See [System Specification](docs/requirements-engineering/technical-specification.md) for details.
```

Verify the path exists before committing. Broken cross-references degrade agent navigation.
