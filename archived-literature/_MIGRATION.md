# RRL Migration Notice (Final)

**All RRL processing has moved to BUDI-Literature.**

> **BUDI-Literature** — https://github.com/VibeCoders-3DCSAD/Odin-Literature

This repository (`BUDI-Base`) is now a **knowledge base** for thesis documentation. The `archived-literature/` folder is deprecated. See `archived-literature/DEPRECATED.md`.

## What moved where

| Path | Status | Where it is now |
|------|--------|-----------------|
| `literature/conversions/` (`_marked.md` + `_summarized.json` pairs) | **Moved** | `BUDI-Literature/literature/conversions/` |
| `literature/summaries/` (23 JSON) | **Deleted** | Redundant — all stems in BUDI-Literature |
| `literature/archive/` | **Deleted** | Superseded |
| `literature/compilations/` | **Deleted** | Old taxonomy; superseded by the flat corpus in BUDI-Literature |
| `literature/papers/` (source PDFs, Git LFS) | **Kept, pending migration** | Will be verified against new topical outline and migrated to BUDI-Literature manually |
| `literature/scripts/` | **Deleted** | All useful scripts superseded by BUDI-Literature/scripts/ |
| `literature/skills/` | **Deleted** | Summarizing skills superseded by the BUDI-Literature two-phase workflow; scoring skills by `BUDI-Literature/scripts/score.py` |

## Standards that moved

| Standard | BUDI-Literature location |
|----------|------------------------|
| Summary JSON schema | `docs/standards/summary-format.md` |
| RRL naming conventions | `docs/standards/rrl-naming-conventions.md` |
| RRL workflow | `docs/standards/rrl-workflow.md` |

## For new work

All new RRL work happens in BUDI-Literature. Refer to:
- `BUDI-Literature/AGENTS.md` — agent navigation guide
- `BUDI-Literature/docs/standards/rrl-workflow.md` — full processing workflow
