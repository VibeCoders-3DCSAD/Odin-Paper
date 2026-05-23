# Skill: Thematic Review Table Generator from Research Chronicle

## Purpose
This skill directs an AI agent to transform a research chronicle (a markdown file containing summarized research papers) into a **thematic review of related literature (RRL) table** focused on a user‑specified theme. The output is clean markdown suitable for a thesis or report.

## Inputs Required from User
1. **Chronicle file content** – A markdown document where each source entry contains structured sections (e.g., `## Source:`, `### TL;DR`, `### Findings`, `### Relevance to Odin`, `### Limitations`, etc.).
2. **Focus theme** – A short phrase describing the topic to extract (e.g., “anomaly detection”, “spending forecasting”, “behavioral profiling”, “data privacy”, “mobile-first design”).

## Output Specifications
The agent will produce **pure markdown** containing:

1. A heading:  
   `# Thematic Review of Related Literature (RRL) – [Focus Theme] (Odin Project)`

2. A markdown table with the following columns:
   - `No.`
   - `Theme`
   - `Key Authors/Studies`
   - `Page/Paragraph Citation` → **always left blank**
   - `Main Findings`
   - `Common Insights`
   - `Research Gaps`
   - `Relevance to Odin`

3. One row per theme – each theme groups **one or more studies** from the chronicle that address that specific sub‑topic within the focus theme.

4. **Final synthesis** (after the table) – One single paragraph summarizing:
   - Most promising approaches for Odin given the focus theme
   - Key trade‑offs (accuracy, interpretability, cold‑start, mobile constraints)
   - Critical research gaps that Odin can fill
   - Recommended evaluation metrics (where applicable)

## Procedure for the Agent

### Step 1 – Identify relevant sources
Scan the chronicle for all source entries. For each source, examine:
- The `## Relevance to Odin` section (especially bullet lists of topics)
- The `### Findings` and `### TL;DR`
- The `### Directly justifies` block (if present)
- The `### Limits of relevance` and `### Limitations`

Keep a source if **any** of its topics or content directly relates to the user’s focus theme.

### Step 2 – Extract candidate themes from relevant sources
From the kept sources, list all specific subtopics that fall under the focus theme.  
Group sources that discuss the same or very similar subtopics. Ensure themes are neither too broad (e.g., “Machine learning”) nor too narrow (e.g., “Isolation Forest hyperparameter tuning on Tuesdays”).

### Step 3 – For each theme, fill the table columns
- **Key Authors/Studies**: List author names + year (e.g., “Bhavana et al. (2025); Shuryhin & Zinovatna (2024)”). Use the citation style from the chronicle.
- **Page/Paragraph Citation**: Always leave blank or `—`. Do not attempt to extract page numbers.
- **Main Findings**: Synthesize 1–2 sentences from the `### Findings` or `### Directly justifies` sections of the grouped sources. Use direct quotes when powerful.
- **Common Insights**: What do multiple papers agree on? If only one paper, state what that paper uniquely contributes.
- **Research Gaps**: Extract from `### Limits of relevance` and `### Limitations` sections of the grouped sources. Synthesize gaps specific to the focus theme.
- **Relevance to Odin**: Extract from `### Relevance to Odin` or `### Contribution to Odin` sections. If not directly stated, write a short sentence on how the theme applies to Odin’s design (manual input, mobile‑first, Filipino context).

### Step 4 – Write the final synthesis
Based on all themes, produce a synthesis that:
- Summarises which algorithms or methods are most suitable for Odin given the focus theme.
- Discusses major trade‑offs (e.g., accuracy vs. false positives, cold‑start vs. data‑hungry models, explainability vs. complexity).
- Identifies the most critical research gaps that Odin’s thesis can address (e.g., no evaluation on manual‑entry data, no local spending patterns, no user trust measurement).
- Recommends specific evaluation metrics for Odin’s module (e.g., precision, recall, F1, false positive rate, user satisfaction, cold‑start performance over time).

### Step 5 – Output pure markdown
Do not add any conversational text before or after the markdown. The entire response must be the markdown content starting with `# Thematic Review...`.

## Notes for the Agent
- If the chronicle contains no source relevant to the focus theme, output a single row: “No relevant studies found” and a brief synthesis explaining why.
- Do not invent data. Only extract from the provided chronicle.
- Keep the tone academic and concise.
- Ensure the markdown table is properly aligned and readable.
- The final synthesis must be part of the markdown output (not a separate message).

---