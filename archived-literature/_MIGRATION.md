# RRL Migration Notice (Final)

**All RRL processing has moved to Odin-Literature.**

> **Odin-Literature** — https://github.com/VibeCoders-3DCSAD/Odin-Literature

This repository (`Odin-Paper`) is now a **knowledge base** for thesis documentation. The `literature/` folder is deprecated. See `literature/DEPRECATED.md`.

## What moved where

| Path | Status | Where it is now |
|------|--------|-----------------|
| `literature/conversions/` (518 `_marked.md` + 518 `_summarized.json`) | **Moved** | `Odin-Literature/literature/conversions/` |
| `literature/summaries/` (23 JSON) | **Deleted** | Redundant — all stems in Odin-Literature |
| `literature/archive/` | **Deleted** | Superseded |
| `literature/compilations/` | **Deprecated** | Do not use; old taxonomy |
| `literature/papers/` (518 source PDFs, Git LFS) | **Kept, pending migration** | Will be verified against new topical outline and migrated to Odin-Literature manually |
| `literature/scripts/` | **Deleted** | All useful scripts superseded by Odin-Literature/scripts/ |
| `literature/skills/` | **Partially deleted** | 4 active skills remain; 2 superseded skills (scorer, culler) deleted |

## Standards that moved

| Standard | Odin-Literature location |
|----------|------------------------|
| Summary JSON schema | `docs/standards/summary-format.md` |
| RRL naming conventions | `docs/standards/rrl-naming-conventions.md` |
| RRL workflow | `docs/standards/rrl-workflow.md` |

## For new work

All new RRL work happens in Odin-Literature. Refer to:
- `Odin-Literature/AGENTS.md` — agent navigation guide
- `Odin-Literature/docs/standards/rrl-workflow.md` — full processing workflow
