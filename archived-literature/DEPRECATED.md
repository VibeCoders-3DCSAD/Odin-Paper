# Odin-Paper — literature/ (DEPRECATED)

**This entire directory is deprecated.** All RRL processing has moved to **Odin-Literature** (https://github.com/VibeCoders-3DCSAD/Odin-Literature).

## What lives where now

| What | Where it is now |
|------|-----------------|
| Curated corpus (conversions, summaries, scores) | `Odin-Literature/literature/conversions/` |
| Scoring pipeline (embed, score, manifest) | `Odin-Literature/scripts/` |
| Module configuration | `Odin-Literature/config/modules.yaml` |
| PDF fetch/convert/dedupe/count scripts | `Odin-Literature/scripts/` |
| Summary JSON schema | `Odin-Literature/docs/standards/summary-format.md` |
| Naming conventions | `Odin-Literature/docs/standards/rrl-naming-conventions.md` |
| Workflow documentation | `Odin-Literature/docs/standards/rrl-workflow.md` |

## What remains here (until manual migration)

- `papers/` — source PDFs (Git LFS). These will be migrated to Odin-Literature when relevance is verified against the new topical outline.
- `skills/` — 4 AI prompt skills still referenced for summarizing new papers (paper-summarizer, paper-verifier, cross-topic-synthesis, synthesis-compiler). The 2 superseded skills (scorer, culler) have been deleted.

## What was deprecated and removed

- `scripts/` — deleted. All scripts were superseded by their equivalents in Odin-Literature/scripts/.
- `skills/paper-scorer-skill.md` — deleted, replaced by `Odin-Literature/scripts/score.py`.
- `skills/paper-culler-skill.md` — deleted, replaced by automated scoring in `Odin-Literature/scores/`.

## Migration timeline

PDFs in `literature/papers/` will be verified against the new topical outline and migrated to Odin-Literature manually. Until then, the Odin-Literature pipeline operates on the already-migrated markdown conversions (518 papers in `literature/conversions/batch-1..6/`).
