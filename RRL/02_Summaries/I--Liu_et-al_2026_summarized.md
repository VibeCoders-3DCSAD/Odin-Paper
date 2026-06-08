# Proteus: Shapeshifting Desktop Visualizations for Mobile via Multi-level Intelligent Adaptation

## Metadata

```yaml
---
paper_id: "f6d4c8a2-9b3e-4d7a-8c1f-5e2b0a9d7c3e"
designation: algorithm-specific
title: "Proteus: Shapeshifting Desktop Visualizations for Mobile via Multi-level Intelligent Adaptation"
authors: "Liu, C.; Cheng, S.; Liang, F.; Jiang, Z.; Huang, L.; Athapaththu, K.; Wang, Y."
year: 2026
venue: "Proceedings of ACM Designing Interactive Systems Conference (DIS '26)"
odin_topics: ["B.1", "J.1"]
shorthand_tags: ["/mobile-first-def", "/eval-frameworks"]
member_checklist:
  - name: "Gabion, Stefanie S."
    status: "[ ]"
  - name: "Guevarra, Joaquin Luis T."
    status: "[x]"
  - name: "San Jose, Alexa Joanne Paula G."
    status: "[ ]"
  - name: "Togle, Charles Nathaniel B."
    status: "[ ]"
---
```

## TL;DR

A multi-level design space and LLM-driven multi-agent system transform desktop visualizations into mobile-optimized versions, achieving 91.8% render success and significantly higher readability and interaction quality than baseline.

## Problem and Motivation

Desktop visualizations scaled directly to mobile screens become illegible due to viewport shrinkage, overlapping text, and lost interaction affordances. Poor mobile readability undermines data comprehension, yet most visualizations are still authored only for desktop. Prior responsive techniques treat adaptation as a flat layout puzzle without semantic understanding of chart structure and cross-level constraints.

## Approach

- **Design space:** Three levels — Global Topology (axis transposition, grid reflow), Reference Frame (tick decimation, viewport constriction, tooltip injection), Visual Elements (semantic abbreviation, mark rescaling, filter enabling).
- **Multi-agent system (Proteus):** Five agents — Semantic Parser (deconstructs chart from HTML/SVG), Data Extractor (recovers dataset), Design Planner (selects adaptation actions from design space), Frontend Engineer (generates TypeScript/Recharts code), Visual Critic (evaluates and iterates).
- **Dataset:** 67 desktop visualizations from Vega, Vega-Lite, Altair, and D3 galleries.
- **Baseline:** Same multi-agent architecture without the multi-level design space knowledge.
- **User study:** 12 participants, within-subjects, rated outputs on five dimensions (0 = render failure, 1–7 Likert for quality).

## Findings

1. Proteus achieved **91.8% render success** (D0) vs. baseline's 87.8%.
2. Data fidelity (D1): Proteus rated higher (𝑝 < 0.05, Wilcoxon signed-rank).
3. Perceptual readability (D2): Proteus rated higher (𝑝 < 0.05).
4. Interaction reasonableness (D3): Proteus rated higher (𝑝 < 0.001).
5. Visual aesthetics (D4): Proteus rated higher (𝑝 < 0.001).

- Baseline often produced correct trends but incorrect encoded values (e.g., shifted scales).
- Proteus successfully externalized annotations, added range sliders, and transformed hover interactions into touch-friendly controls.

## Key Figures and Tables

- Figure 3: Five case studies (bar chart, line chart, map, multi-view dashboards) → Proteus preserves data and adds scrollable panels or sliders for mobile.
- Figure 4: User study boxplots → Proteus beats baseline on all dimensions; significance indicated.
- Figure 5: Side-by-side comparison → Baseline misrepresents data distribution; Proteus adds readable layout and interactive filters.

## Key Equations

None.

## Definitions

| Term / Acronym | Plain-English Definition |
| -------------- | ------------------------ |
| LLM | Large Language Model — an AI trained on text that can reason about charts and generate code. |
| Multi-agent system | Multiple specialized AI agents (parser, planner, coder, critic) that collaborate on a task. |
| Global Topology | The high-level arrangement of chart components (layout, grid, coordinate system). |
| Reference Frame | Axes, legends, and scales that help interpret data values. |
| Visual Elements | Individual marks (bars, points) and text labels. |
| Tick decimation | Reducing the number of axis tick labels to avoid overlap, relying on user interpolation. |
| Semantic abbreviation | Shortening category names intelligently (e.g., “United States” → “USA”) instead of blind truncation. |

## Critical Citations

- [Hoffswell et al., 2020] — Established responsive visualization techniques; baseline for flat adaptation taxonomies.
- [Wu et al., 2020] — MobileVisFixer; reinforcement learning for layout repair on single charts.
- [Kim et al., 2022] — Cicero; declarative grammar for responsive transformations; compared as grammar-based approach.

## Relevance to Odin

**Topics:**

B.1 — Mobile-First Design in Personal Finance Systems

J.1 — System Evaluation

**Contribution to Odin:**

This paper provides a validated framework for adapting any desktop visualization to mobile screens while preserving data fidelity and usability — directly applicable to Odin’s need to display budget charts, spending forecasts, and anomaly alerts on small mobile viewports. The multi-level design space (topology → reference frame → elements) offers a structured checklist for Odin’s mobile UX design, ensuring that decisions like axis transposition or tooltip injection are made systematically rather than ad hoc. The user study methodology (5 dimensions, within-subjects, Wilcoxon signed-rank) and the 91.8% render success benchmark provide a rigorous evaluation template for Odin’s own ISO 25010 and SUS assessments.

**Directly justifies:**

- “Desktop-to-mobile visualization adaptation requires coordinated decisions across global layout, reference frames, and visual elements — a flat list of heuristics is insufficient.”
- “LLM-driven multi-agent systems can achieve 91.8% render success on diverse real-world charts, outperforming baselines without structured design knowledge (p < 0.05 for fidelity and readability).”
- “Externalizing dense annotations into scrollable panels (e.g., ‘Key insights’) and converting hover interactions into dedicated sliders preserves information while respecting touch constraints.”
- “User evaluations of mobile adaptations should include separate ratings for data fidelity, perceptual readability, interaction reasonableness, and visual aesthetics — all improved significantly by hierarchical planning.”

**Limits of relevance:**

- Domain is general visualization, not personal finance — but Odin’s charts (budget, spending, forecasts) share the same mobile legibility constraints.
- Study participants were visualization-experienced, not Filipino young professionals — usability findings may generalize but need local validation.
- The system requires vector source code (SVG/HTML); Odin’s own generated charts are code-based, so the method is directly applicable.
- No evaluation of cold-start or partial data scenarios; Odin’s early-user phase may require additional adaptation rules.

## Limitations

- Evaluation focused on benchmark visualizations, not live financial data with dynamic updates or real user spending patterns. [unacknowledged]
- User study participants were not representative of Filipino young professionals; cultural and income-specific usability factors not tested.
- The framework assumes access to original chart source code; it does not handle raster-only images (legacy visualizations).
- Latency increases with chart complexity (more DOM nodes → more LLM tokens), which may affect real-time adaptation in Odin’s mobile app. [unacknowledged]
- No longitudinal or task-completion time measurement; the study measured subjective quality, not efficiency of analysis.

## Remember This

- 🔑 **91.8% render success** — Proteus reliably generates working mobile charts; baseline fails on 12% of cases.
- 📌 Three-level design space (topology → frame → elements) — hierarchical planning beats flat heuristics for mobile adaptation.
- 💡 Externalize dense info into scrollable panels — don’t shrink; move annotations and controls below the chart.
- ✅ Significant gains in interaction (p < 0.001) and readability (p < 0.05) — proven by 12-user within-subjects study.
- ⚠️ No Filipino user testing yet — use the method but validate with local participants.
