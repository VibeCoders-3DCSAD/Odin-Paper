```yaml
paper_id: d2b5c3f1-6a7e-4b8c-9d0f-1e2a3b4c5d6e
designation: international
title: "Proteus: Shapeshifting Desktop Visualizations for Mobile via Multi-level Intelligent Adaptation"
authors: "Liu, C.; Cheng, S.; Liang, F.; Jiang, Z.; Huang, L.; Athapaththu, K.; Wang, Y."
year: 2026
venue: "ACM Designing Interactive Systems Conference (DIS'26)"
odin_topics:
  - 9.A
  - 9.B
  - 12.A
  - 12.B
shorthand_tags:
  - /mobile-first-design
  - /mobile-ux
  - /system-evaluation
  - /algorithm-evaluation
tldr: "Proteus is an LLM-driven multi-agent framework that transforms desktop visualizations into mobile-optimized versions using a novel multi-level design space, outperforming a strong baseline in user studies."
problem_and_motivation: "Desktop visualizations are ill-suited for mobile screens due to different viewport sizes and interaction paradigms. Direct scaling causes illegible text, information loss, and interaction failures. Existing responsive visualization techniques treat adaptation as a flat layout puzzle lacking semantic understanding and hierarchical constraint propagation."
approach:
  - "The authors propose a multi-level design space with three layers: Global Topology, Reference Frame, and Visual Elements."
  - "They develop Proteus, a five-agent LLM system (Semantic Parser, Data Extractor, Design Planner, Frontend Engineer, Visual Critic) that iteratively adapts visualizations."
  - "The system accepts HTML/SVG source code and renders mobile-optimized components using TypeScript and Recharts."
  - "Evaluation uses a benchmark of 67 desktop visualizations from D3, Vega-Lite, and Altair galleries."
  - "A within-subjects user study with 12 participants compares Proteus against a multi-agent baseline lacking the design space knowledge."
findings:
  - "num: Proteus achieved 91.8% render success rate on 67 visualizations versus 87.8% for the baseline."
  - "num: Wilcoxon signed-rank tests showed significant improvements for data fidelity and readability (p < 0.05) and for interaction reasonableness and aesthetics (p < 0.001)."
  - "The multi-level design space enables hierarchical constraint propagation from global topology down to individual visual marks."
  - "The visual critic agent autonomously evaluates and guides iterative refinement, essential for zero-intervention robustness."
key_figures_tables:
  - "Figure 1: Multi-level design space with three layers → Organizes adaptation from global topology to visual elements."
  - "Figure 2: Multi-agent framework of Proteus → Shows iterative workflow from parsing to code generation."
  - "Figure 3: Five case studies → Demonstrates effective adaptation of single-view and multi-view visualizations."
  - "Figure 4: User study results → Proteus outperforms baseline across all five evaluation dimensions."
  - "Figure 5: Qualitative comparison → Proteus preserves data distribution and provides more readable layouts."
key_equations:
  - equation: "None."
    explanation: ""
definitions:
  - term: "LLM"
    definition: "Large Language Model"
  - term: "SVG"
    definition: "Scalable Vector Graphics"
  - term: "DOM"
    definition: "Document Object Model"
  - term: "D3"
    definition: "Data-Driven Documents"
  - term: "Proteus"
    definition: "Proposed LLM-driven multi-agent framework for mobile visualization adaptation"
critical_citations:
  - "[Hoffswell et al., 2020] — Established responsive visualization design space."
  - "[Kim et al., 2022] — Cicero declarative grammar for responsive visualizations."
  - "[Wu et al., 2020] — MobileVisFixer for automated SVG adaptation via reinforcement learning."
relevance:
  topics:
    - code: "9.A"
      name: "Mobile-First Design Principles and Rationale"
      justification: "Paper defines mobile design requirements and a multi-level design space for adapting visualizations to small screens."
    - code: "9.B"
      name: "Mobile UX Design for Personal Finance"
      justification: "Addresses touch interaction, scrolling, tooltips, and readability for mobile consumption of data visualizations."
    - code: "12.A"
      name: "Evaluation Frameworks for Personal Finance Systems"
      justification: "Conducts user study with metrics for execution completeness, data fidelity, readability, interaction, and aesthetics."
    - code: "12.B"
      name: "Evaluation of Algorithmic Modules"
      justification: "Compares Proteus against a strong LLM baseline using statistical testing (Wilcoxon signed-rank) on quantitative outcomes."
  contribution: "Proteus provides a multi-level design space that can inform Odin's mobile-first design for visualizing financial data. The multi-agent LLM approach can automate adaptation of expense categorization charts and spending forecasts from desktop to mobile. The evaluation methodology with user studies on readability and interaction offers a template for testing Odin's mobile UI modules. The critic agent ensures data fidelity, which is crucial for financial accuracy. The iterative refinement loop can be adapted for Odin's feedback-driven user engagement features."
  directly_justifies:
    - "Mobile adaptation requires semantic re-authoring rather than simple geometric resizing."
    - "A multi-level design space with hierarchical constraint propagation improves readability and interaction on small screens."
    - "LLM-based multi-agent systems can automate visualization adaptation with high fidelity and minimal human intervention."
    - "Zero-intervention robustness is achievable via an autonomous critic agent that evaluates intermediate designs."
  limits:
    - "Evaluation focuses on standard gallery visualizations, not long-tail bespoke or artistic designs."
    - "Does not assess whether adapted visualizations support the same analytic tasks as the originals."
    - "Current implementation requires vector-based input (SVG/HTML); raster images need additional reverse engineering. [unacknowledged]"
    - "Financial data visualizations were not tested explicitly. [unacknowledged]"
  mapping_rationale: "The paper is international, focusing on general data visualization adaptation. It strongly aligns with mobile-first design (9.A and 9.B) because it systematically addresses screen constraints, touch interaction, and readability. The evaluation methodology (12.A and 12.B) is directly applicable to assessing Odin's algorithmic modules and user interfaces. Topics related to behavioral profiling, spending forecasting, budget recommendation, anomaly detection, savings, and debt are not covered, as the paper does not deal with personal financial data or user financial behaviors."
limitations:
  - "High latency for complex SVG/HTML inputs due to large token counts."
  - "Preserving subtle aesthetic qualities of bespoke visualizations remains difficult."
  - "No task-oriented evaluation of analytic equivalence between desktop and mobile versions. [unacknowledged]"
  - "Only tested on web visualizations, not on domain-specific financial charts. [unacknowledged]"
remember_this:
  - "Proteus achieves 91.8% render success on 67 diverse visualizations."
  - "Multi-level design space outperforms flat geometry-centric heuristics."
  - "LLM agents with a critic loop enable zero-intervention mobile adaptation."
  - "Data fidelity and text readability are critical for mobile visualization success."
```