# A machine learning ensemble approach to predicting factors affecting the intention and usage behavior towards online groceries applications in the Philippines

## Metadata

```yaml
---
paper_id: "10.1016/j.heliyon.2023.e20644"
designation: algorithm-specific
title: "A machine learning ensemble approach to predicting factors affecting the intention and usage behavior towards online groceries applications in the Philippines"
authors: "Gumasing, M. J. J.; Ong, A. K. S.; Sy, M. A. P. C.; Prasetyo, Y. T.; Persada, S. F."
year: 2023
venue: "Heliyon"
odin_topics: ["5.C", "12.B"]
shorthand_tags: ["/classifier-candidates", "/classifier-eval-metrics", "/eval-ml-design"]
member_checklist:
  - name: "Gabion, Stefanie S."
    status: "[ ]"
  - name: "Guevarra, Joaquin Luis T."
    status: "[X]"
  - name: "San Jose, Alexa Joanne Paula G."
    status: "[ ]"
  - name: "Togle, Charles Nathaniel B."
    status: "[ ]"
---
```

## TL;DR

Random Forest and Artificial Neural Network ensembles predicted online grocery usage behavior with 96% accuracy, identifying perceived benefits and vulnerability as top factors.

## Problem and Motivation

Despite the rapid growth of e-commerce in the Philippines, no study has holistically measured online grocery acceptance using both technology acceptance and health motivation theories. Understanding these factors is critical for grocers and policymakers during COVID-19, as consumer behavior shifted toward contactless transactions. Prior work relied on statistical methods (SEM) that cannot capture nonlinear relationships or mediator effects as effectively as machine learning.

## Approach

- Survey of 373 Filipino online grocery users (61% female, majority 31–40 years old) using a 67-item questionnaire.
- Integrated UTAUT2 (performance expectancy, effort expectancy, social influence, hedonic motivation, facilitating conditions) and Protection Motivation Theory (perceived benefits, vulnerability, severity, susceptibility, response efficacy).
- Data preprocessing: correlation threshold 0.20, min-max normalization.
- Random Forest Classifier optimized over 6,400 runs; best depth=6, gini criterion, 90:10 train-test split, achieving 96% accuracy with 0.00 SD.
- Artificial Neural Network with Tanh hidden and Softmax output activation, Adam optimizer, 150 epochs, 90 hidden nodes, achieving 96.63% testing accuracy.

## Findings

1. ANN ranked perceived benefit as most important factor (importance score 0.270), followed by perceived vulnerability (0.265), behavioral intention (0.258), performance expectancy (0.248), and perceived severity (0.244).
2. Random Forest decision tree showed that perceived benefit and perceived vulnerability lead to **very high usage behavior**; perceived benefit, behavioral intention, and perceived severity lead to high usage behavior.
3. All 12 hypotheses were accepted (p < 0.05); facilitating conditions had the lowest importance (0.158) but still significant.
- Cronbach's alpha for all constructs >0.8, VIF <5 (no multicollinearity).
- Taylor diagram confirmed consistency between ANN and RF results (correlation >0.9, RMSE <20%).

## Key Figures and Tables

- Figure 2: Conceptual framework → integrated UTAUT2 and PMT constructs with 12 hypotheses.
- Figure 4: Decision tree → perceived benefit as root node; very high usage when vulnerability and performance expectancy are high.
- Figure 5: Optimum ANN architecture → input layer 11 nodes, hidden layer 90 nodes, output layer 2 nodes.
- Table 6: Importance scores and Cronbach's alpha → perceived benefit highest (27%), facilitating conditions lowest (15.8%).

## Key Equations

None.

## Definitions

| Term / Acronym | Plain-English Definition |
| -------------- | ------------------------ |
| UTAUT2 | Unified Theory of Acceptance and Use of Technology 2 – a framework for understanding technology adoption. |
| PMT | Protection Motivation Theory – a health behavior model focusing on threat and coping appraisal. |
| Random Forest Classifier | An ensemble of decision trees that votes on the most common classification. |
| Artificial Neural Network | A computational model inspired by biological neurons, used for pattern recognition. |
| Perceived benefit | Belief that using online groceries reduces COVID-19 infection risk. |
| Perceived vulnerability | Belief about one's personal risk of contracting COVID-19. |
| Response efficacy | Belief that recommended actions (using online groceries) effectively prevent infection. |
| Behavioral intention | A person's plan or willingness to use online groceries. |

## Critical Citations

- [Venkatesh et al., 2012] — UTAUT2 framework extended to consumer technology acceptance.
- [Janz & Becker, 1984] — Health Belief Model underpinning PMT's threat appraisal constructs.
- [Davis, 1989] — Original TAM defining perceived usefulness and ease of use.

## Relevance to Odin

**Topics:**

5.C — Financial Behavioral Profile Classification Algorithm

12.B — Evaluation of Algorithmic Modules

**Contribution to Odin:**

This paper demonstrates that Random Forest and Artificial Neural Network ensembles achieve high accuracy (96–97%) in classifying behavioral intention and usage patterns from survey data. For Odin's financial behavioral profiling module, this justifies using ensemble machine learning (specifically RF or ANN) over traditional statistical methods like SEM, as ML captures nonlinear relationships better. The paper's Filipino respondent base (though for groceries) provides a precedent for ML-based classification of technology acceptance in the local context, which can be transferred to personal finance apps. The evaluation metrics (accuracy, standard deviation, Taylor diagram) offer a template for Odin's module-level algorithm validation.

**Directly justifies:**

- "Random Forest Classifier achieved 96% accuracy with 0.00 standard deviation in predicting usage behavior, demonstrating stable classification performance for consumer technology adoption."
- "Artificial Neural Network achieved 96.63% testing accuracy in ranking factor importance for behavioral intention, outperforming traditional SEM in capturing nonlinear relationships."
- "Perceived benefit, perceived vulnerability, and behavioral intention are the top three predictors of usage behavior, suggesting that health-related threat appraisal drives technology adoption during a pandemic."
- "Ensemble of RF and ANN provides a reliable framework for predicting human behavior, with Taylor diagram confirming consistency (correlation >0.9)."

**Limits of relevance:**

- Paper focuses on online grocery shopping, not personal financial management; behavioral drivers may differ.
- Study conducted during COVID-19 pandemic; findings about threat perception may not generalize to normal conditions.
- Data collected via convenience sampling from urban areas; rural Filipino young professionals underrepresented.
- No longitudinal validation; classification model tested on single survey, not on actual transaction behavior over time.

## Limitations

- Respondents mainly from highly urbanized cities, limiting generalizability to rural Filipinos. (acknowledged)
- Socio-economic factors not analyzed via clustering; future work needed for customer segmentation. (acknowledged)
- No validation of ML predictions against actual behavioral outcomes (self-reported usage only). [unacknowledged]
- Cold-start scenario not considered; model requires survey data, not transaction histories. [unacknowledged]
- The 373 sample size may not capture full diversity of Filipino young professionals. [unacknowledged]

## Remember This

- 🔑 **96.63% accuracy** — ANN and RF ensemble reliably predicts usage behavior.
- 📌 Perceived benefit is top factor (27% importance) — health benefits drive adoption.
- ⚠️ Filipino urban sample only — rural and income diversity not captured.
- 💡 Ensemble ML beats SEM for nonlinear behavioral prediction — applicable to Odin's profiling.
