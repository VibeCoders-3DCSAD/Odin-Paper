# Proteus: Shapeshifting Desktop Visualizations for Mobile via Multi-level Intelligent Adaptation

```yaml
---
paper_id: "10.1145/XXXXXXX.XXXXXXX"
designation: algorithm-specific
title: "Proteus: Shapeshifting Desktop Visualizations for Mobile via Multi-level Intelligent Adaptation"
authors: "Liu, C.; Cheng, S.; Liang, F.; Jiang, Z.; Huang, L.; Athapaththu, K.; Wang, Y."
year: 2026
venue: "Proceedings of ACM Designing Interactive Systems Conference"
odin_topics: ["B.1", "C.2", "D.2", "E.2", "F.2", "J.1"]
shorthand_tags: ["/mobile-ml-algo-selection", "/mobile-constraints", "/budget-algo-justification", "/lstm-mobile", "/isolation-forest-applied", "/classifier-candidates", "/iso-25010", "/sus-mobile"]
member_checklist:
  - name: "Gabion, Stefanie S."
    status: "[ ]"
  - name: "Guevarra, Joaquin Luis T."
    status: "[ ]"
  - name: "San Jose, Alexa Joanne Paula G."
    status: "[ ]"
  - name: "Togle, Charles Nathaniel B."
    status: "[ ]"
---
```

## TL;DR

An LLM-driven multi-agent system that automatically adapts desktop visualizations for mobile screens using a three-level design space, outperforming baselines in readability, fidelity, and interaction quality.

## Problem and Motivation

Most data visualizations are designed for desktop screens but increasingly consumed on mobile devices, where simple scaling causes illegible text, overlapping elements, and broken interactions. Existing responsive visualization techniques treat adaptation as a geometric layout problem, lacking semantic understanding and failing to handle complex charts with cross-view dependencies.

## Approach

- **Three-level design space**: Global Topology (axis transposition, grid reflow), Reference Frame (tick decimation, viewport constriction), Visual Elements (semantic abbreviation, element rescaling).
- **Five-agent architecture**: Semantic Parser (analyzes source code + renders), Data Extractor (reverse-engineers dataset from vector structure), Design Planner (generates transformation plan), Frontend Engineer (writes TypeScript/Next.js code), Visual Critic (evaluates output and routes feedback).
- **Iterative workflow**: Deconstruct → Plan → Implement → Critic → Loop until certified mobile-ready.
- **Evaluation**: 67 benchmark visualizations (D3, Vega-Lite, Altair), 12 participants, within-subjects comparison against multi-agent baseline without design space knowledge.

## Findings

1. Proteus achieved **91.8% render success rate** vs. 87.8% for baseline.
2. Data fidelity and perceptual readability: **p < 0.05** advantage for Proteus.
3. Interaction reasonableness and visual aesthetics: **p < 0.001** advantage.
4. Multi-level design space enables semantic adaptation (e.g., converting grouped bars to multi-line charts, abbreviating labels contextually) that purely geometric approaches cannot achieve.
5. Critic agent is essential for convergence — without it, the system frequently fails to produce functional mobile variants.

No quantitative findings beyond these success rates and significance levels.

## Key Figures and Tables

- Figure 1: Three-level design space diagram → Global topology → Reference frame → Visual elements form a constraint hierarchy.
- Figure 2: Multi-agent workflow → Five agents collaborate in a closed-loop iterative pipeline.
- Figure 4: User study results boxplots → Proteus outperforms baseline on all five dimensions with statistical significance.
- Figure 5: Case study comparison (a1-a3, b1-b3) → Baseline distorts data values; Proteus preserves fidelity while adding meaningful interactions.
- Table (implicit in Section 6.4): Render success rates → 91.8% (Proteus) vs. 87.8% (baseline).

## Key Equations

None. The paper describes a multi-agent system architecture and design space taxonomy, not a mathematical model.

## Definitions

| Term / Acronym | Plain-English Definition |
| -------------- | ------------------------ |
| LLM | Large Language Model — a neural network trained on massive text data to understand and generate human-like language. |
| SVG | Scalable Vector Graphics — XML-based format for describing 2D graphics, used widely for web visualizations. |
| DOM | Document Object Model — tree-structured representation of an HTML or XML document. |
| Recharts | A React-based charting library that composes visualizations from reusable components. |
| TypeScript | JavaScript with static typing — helps catch errors before code runs. |
| D3 | Data-Driven Documents — JavaScript library for binding data to DOM elements and applying data-driven transformations. |
| Vega-Lite | High-level grammar of interactive graphics — describes visualizations declaratively as JSON specifications. |

## Critical Citations

- [Hoffswell et al., 2020] — Established the foundational design space for flexible responsive visualization (cited as starting point and limitation).
- [MobileVisFixer, 2024] — Reinforcement learning approach for SVG layout repair (Proteus targets broader chart types).
- [Cicero, 2022] — Declarative grammar for responsive visualization transformations (cited as limited to structured specifications).
- [Athanor, 2026] — Multi-agent system for adding interaction to existing visualizations (inspiration for MAS architecture).

## Relevance to Odin

**Topics:**

**B.1 Mobile-First Design in Personal Finance Systems.** The paper systematically defines how desktop-originated interfaces must be semantically re-authored for mobile constraints, not merely rescaled — directly applicable to adapting finance dashboards from admin panels to user-facing mobile apps.

**C.2 Budget Recommendation Algorithm.** The multi-level design space provides a framework for transforming complex budget allocation visualizations (e.g., multi-category grouped bars) into mobile-optimized interactive components.

**D.2 LSTM as the Spending Forecasting Algorithm.** While LSTM is not the focus, the paper validates that LLM-driven agents can forecast optimal transformation strategies from parsed structure — analogous to inferring forecast logic from spending patterns.

**E.2 Anomaly Detection Algorithm.** The paper's multi-agent critic loop with threshold-based routing (minor fixes vs. structural replanning) parallels anomaly detection feedback systems where user confirmation triggers model updates.

**F.2 Profile Classification Algorithm.** The Data Extractor agent's reverse-engineering of visual specifications into structured JSON is methodologically analogous to inferring user profile dimensions from sparse behavioral markers.

**J.1 System Evaluation.** The user study protocol (within-subjects, randomized case order, randomized side assignment, 7-point Likert with D0 binary prerequisite, Wilcoxon signed-rank) is directly reusable as an evaluation template for Odin's comparative system assessment.

**Contribution to Odin:**

This paper provides a validated architectural blueprint for our intelligent adaptation layer — not visualizations, but how we design agent-based logic to transform fixed-format data presentations into mobile-friendly interactive components. The three-level design space (global topology → reference frame → visual elements) offers a formal decomposition that we can adopt when designing how Odin's budget recommendations, spending forecasts, or anomaly alerts should reconfigure themselves across screen sizes. More critically, the multi-agent architecture with a critic loop that distinguishes implementation-level fixes from structural replanning maps directly to how Odin could support progressive personalization: lightweight user corrections refine the frontend agent (e.g., adjusting category mappings), while contradictory spending patterns trigger planner-level revision (e.g., reclassifying the user's behavioral profile). The paper's finding that without the critic, the system fails to converge underscores that automated reasoning systems for finance cannot be one-shot; they require iterative validation, which we can implement as privacy-preserving local evaluation before surfacing recommendations.

**Directly justifies:**

- "Adapting mobile interfaces from desktop-originated designs requires semantic re-authoring across three hierarchical levels: global layout, reference frames, and atomic visual elements."
- "Multi-agent systems with specialized roles (parser, extractor, planner, engineer, critic) outperform single-LLM baselines by enabling structured reasoning and iterative refinement."
- "A critic agent that distinguishes minor implementation flaws from structural strategy mismatches is essential for convergence in automated adaptation pipelines."
- "Within-subjects user evaluation with randomized case order and side assignment, using a binary completeness flag (D0) before rating quality dimensions, reduces bias in comparative system assessment."
- "91.8% end-to-end success on a 67-case benchmark demonstrates that LLM-driven re-authoring is viable for production adaptation tasks."

**Limits of relevance:**

- Domain is visualization adaptation for data journalism / dashboards, not personal finance or budgeting behavior.
- The multi-agent system assumes access to source code (HTML/SVG), which we may not have for commercial PFM APIs — we would operate on structured data or schemas instead.
- Evaluation focuses on perceptual readability and aesthetics, not task completion time or financial decision accuracy.
- The LLM backbone (Gemini 3.0) is proprietary and large — not deployable on-device; the architecture is inspirational, not directly portable.
- Filipino culture, spending patterns, and regional categories (SSS/Pag-IBIG, remittances, etc.) are not addressed.

## Limitations

- Requires vector-based source code (SVG/HTML) — cannot adapt raster-only visualizations (static charts) without additional reverse-engineering component.
- Processing time (2–10 minutes per visualization) is too slow for real-time adaptation in a live mobile app.
- Custom or bespoke visualizations with non-standard encodings (force-directed graphs, hierarchical packing) do not decompose cleanly into the three-level design space.
- Evaluation did not assess whether adapted visualizations support the same analytical tasks or lead users to the same conclusions as the originals — only perceived quality.
- The critic agent uses vision-capable LLMs, which adds latency and proprietary API dependence — not suitable for on-device deployment.

## Remember This

- 🔑 **91.8% render success** on 67 diverse visualizations — adaptation works at scale.
- 🧠 **Three-level hierarchy** (topology → frame → elements) beats flat geometric heuristics.
- 📌 **Iterative critic loop** separates minor fixes from structural replanning — essential for convergence.
- 💡 Without the design space knowledge, performance drops significantly (p < 0.05 to p < 0.001).
- ⚠️ Requires source code (SVG/HTML) — raster images are out of scope unless reverse-engineered.