# BUDI-Base — literature/ (DEPRECATED)

**This entire directory is deprecated.** All RRL processing has moved to **BUDI-Literature** (https://github.com/VibeCoders-3DCSAD/Odin-Literature).

## What lives where now

| What | Where it is now |
|------|-----------------|
| Curated corpus (conversions, summaries, scores) | `BUDI-Literature/literature/conversions/` |
| Scoring pipeline (embed, score, manifest) | `BUDI-Literature/scripts/` |
| Module configuration | `BUDI-Literature/config/modules.yaml` |
| PDF fetch/convert/dedupe/count scripts | `BUDI-Literature/scripts/` |
| Summary JSON schema | `BUDI-Literature/docs/standards/summary-format.md` |
| Naming conventions | `BUDI-Literature/docs/standards/rrl-naming-conventions.md` |
| Workflow documentation | `BUDI-Literature/docs/standards/rrl-workflow.md` |

## What remains here (until manual migration)

- `papers/` — source PDFs (Git LFS), batch-1 through batch-6. These will be migrated to BUDI-Literature when relevance is verified against the new topical outline.

## What was deprecated and removed

- `compilations/` — deleted. Old taxonomy, superseded by the flat corpus in BUDI-Literature.
- `scripts/` — deleted. All scripts were superseded by their equivalents in BUDI-Literature/scripts/.
- `skills/` — deleted in full. The summarizing skills (paper-summarizer, paper-verifier, cross-topic-synthesis, synthesis-compiler) are superseded by the BUDI-Literature two-phase workflow; the scoring skills (scorer, culler) by `BUDI-Literature/scripts/score.py` and automated scoring in `BUDI-Literature/scores/`.

## Migration timeline

PDFs in `archived-literature/papers/` will be verified against the new topical outline and migrated to BUDI-Literature manually. Until then, the BUDI-Literature pipeline operates on the markdown conversions already migrated out of this directory.
