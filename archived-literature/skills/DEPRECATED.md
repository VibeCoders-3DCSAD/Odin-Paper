# Skill Status

| Skill | Status |
|-------|--------|
| `paper-summarizer-skill.md` | **Active** — still used to fill `_summarized.json` for new papers (before files move to Odin-Literature) |
| `synthesis-compiler-skill.md` | Active — per-topic synthesis (old-taxonomy, see `compilations/DEPRECATED.md`) |
| `cross-topic-synthesis-skill.md` | Active — cross-topic synthesis |
| `paper-verifier-skill.md` | Active — verifies summary completeness |
| ~~`paper-scorer-skill.md`~~ | **Deleted** — replaced by `Odin-Literature/scripts/score.py` (offline BERT + TF-IDF + BM25 relevance, rule-based quality) |
| ~~`paper-culler-skill.md`~~ | **Deleted** — the automated scorer produces tier flags (crucial/supporting/cull) and near-duplicate clusters with keep/cull decisions in `Odin-Literature/scores/redundancy.json`. The culler's recency→quality tie-breaker is implemented there. |