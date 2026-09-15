# DEPRECATED — old-topic compilation copies

These JSON files are copies of the `_summarized.json` summaries, organized under
the **old** topic taxonomy (1.A–14.C, folders `1.X`–`13.X`).

## Status: DEPRECATED

- The old topic outline has been superseded by the new thesis topical outline (on Google Drive: `google-drive/topical-outline/`), and re-mapping the RRL taxonomy to it is pending.
- The source `_summarized.json` files themselves now live in **Odin-Literature**
  (`Odin-Literature/literature/conversions/`). Every file here is a copy.
- The old per-paper → topic mapping is preserved in each file's `topic_tags` field.

## What to use instead

- **Relevance/quality of a paper** — the automated scorer in
  `Odin-Literature/scripts/score.py` (module queries in
  `Odin-Literature/config/modules.yaml`, outputs in `Odin-Literature/scores/`).
- **Topic organization** — once the new taxonomy is finalized, the scorer's
  module config becomes the organization; this folder will then be removed.

These files are kept only so members still working under the old outline can
browse the topic groupings. Do not add new files here.
