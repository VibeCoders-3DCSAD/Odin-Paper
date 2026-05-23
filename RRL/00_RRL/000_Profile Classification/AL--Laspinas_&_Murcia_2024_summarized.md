# Machine Learning Approaches in Classifying Income Levels

## Metadata

```yaml
---
paper_id: "10.5281/zenodo.10049652"
designation: algorithm-specific
title: "Machine Learning Approaches in Classifying Income Levels"
authors: "Laspiñas, E. L.; Murcia, J. V. B."
year: 2024
venue: "TWIST"
odin_topics: ["5.A", "5.C", "12.B"]
shorthand_tags: ["/profiling-role", "/profile-dimensions", "/classifier-candidates", "/classifier-eval-metrics", "/eval-ml-design"]
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

RandomForest and Random Tree achieved ~98% accuracy in predicting adult income levels, outperforming Logistic, J48, k‑NN, and NaiveBayes on a US census dataset.

## Problem and Motivation

Conventional econometric models rely on linear assumptions and limited factors, failing to capture the complex, non‑linear dynamics of income distribution. Accurate income classification is essential for socioeconomic planning and policy interventions to address rising inequality. No prior study had systematically compared multiple ML classifiers on adult income prediction with hyperparameter tuning.

## Approach

- Dataset: 16,281 adult records from US Census (Adult Income Prediction dataset); 13 attributes (age, occupation, education, marital status, capital gains/losses, etc.); binary target: income >$50K or ≤$50K.
- Classifiers: Logistic, J48 (decision tree), RandomForest, Random Tree, IBk (k‑NN), NaiveBayes.
- Hyperparameter tuning: J48 confidence factors (0.25, 0.50, 0.75); k‑NN with k=3,5,7,9.
- Feature selection: InfoGainAttributeEval + Ranker; ‘Relationship’ had highest information gain (0.16575).
- Evaluation: 10‑fold cross‑validation; metrics = TP rate, FP rate, precision, recall, F‑measure, kappa.

## Findings

1. RandomForest and Random Tree achieved **98.35% and 98.37% accuracy** respectively – the highest among all classifiers.
2. RandomForest F‑measure = 0.983; Random Tree F‑measure = 0.984, indicating excellent precision‑recall balance.
3. J48 accuracy increased with confidence factor: 87.21% (C=0.25) → 90.85% (C=0.75).
4. k‑NN accuracy decreased as k increased: 89.11% (k=3) → 85.74% (k=9), contradicting the assumption that larger k always improves performance.
- Logistic regression (85.82%) and NaiveBayes (82.24%) performed adequately but lagged behind ensemble methods.

## Key Figures and Tables

- Table 2: Classification accuracy for all classifiers → Random Tree highest (98.37%), NaiveBayes lowest (82.24%).
- Table 3: Performance metrics (TP, FP, precision, recall, F‑measure, kappa) → RandomForest and Random Tree dominate all metrics; kappa = 0.954 for both.

## Key Equations

None.

## Definitions

| Term / Acronym | Plain-English Definition |
| -------------- | ------------------------ |
| ML | Machine learning – algorithms that learn patterns from data without explicit programming. |
| Classifier | A model that assigns input data to a predefined category (e.g., high or low income). |
| TP rate | True positive rate = proportion of actual positives correctly identified. |
| FP rate | False positive rate = proportion of negatives incorrectly classified as positives. |
| Precision | Of all positive predictions, how many were actually correct. |
| Recall | Of all actual positives, how many were correctly found (same as TP rate). |
| F‑measure | Harmonic mean of precision and recall; balances both metrics into one score. |
| kappa (κ) | Agreement between predicted and actual classes, adjusted for chance agreement. |
| Cross‑validation | Technique to estimate model performance by splitting data into training/test folds repeatedly. |
| Ensemble method | Combines multiple models (e.g., RandomForest) to improve accuracy and reduce overfitting. |
| Hyperparameter | Settings configured before training (e.g., confidence factor, k value) that control learning. |
| J48 | Weka’s implementation of C4.5 decision tree algorithm. |
| IBk | Weka’s implementation of k‑nearest neighbors (k‑NN). |

## Critical Citations

- [Liaw & Wiener, 2002] – Introduced RandomForest, the basis for the paper’s top‑performing classifier.
- [Kohavi, 1995] – Established 10‑fold cross‑validation as the evaluation standard used here.
- [Peng, Lee & Ingersoll, 2002] – Foundational reference for logistic regression in binary classification.

## Relevance to Odin

**Topics:**

5.A — Financial Behavioral Profiles in Personal Finance

5.C — Financial Behavioral Profile Classification Algorithm

12.B — Evaluation of Algorithmic Modules

**Contribution to Odin:**

This paper directly informs Odin’s financial behavioral profiling module by benchmarking six supervised classifiers on income‑level prediction – a core dimension of user financial profiles (e.g., income stability and obligation weight). The finding that RandomForest and Random Tree achieve near‑98% accuracy on a large demographic dataset provides strong justification for considering ensemble methods when Odin’s classification module is implemented. Although the dataset is US‑based and the target is binary (>$50K), the methodological framework (tuning, cross‑validation, multi‑metric evaluation) is directly transferable to evaluating Odin’s profile classification algorithms.

**Directly justifies:**

- “RandomForest achieved 98.35% accuracy on binary income classification using demographic and employment features, outperforming Logistic, J48, k‑NN, and NaiveBayes.”
- “Ensemble methods (RandomForest, Random Tree) consistently deliver higher F‑measure (>0.98) and kappa (>0.95) than single classifiers on income prediction tasks.”
- “Hyperparameter tuning (J48 confidence factor, k‑NN’s k) significantly changes classifier performance – J48 accuracy rose from 87.2% to 90.8% as confidence increased.”
- “k‑NN accuracy decreases as neighborhood size grows beyond k=3 on the income dataset, contradicting the general assumption that larger k improves performance.”

**Limits of relevance:**

- Dataset is US Census data, not Filipino; income thresholds ($50K) and demographic distributions differ substantially.
- Target variable is binary (above/below $50K), whereas Odin may require multi‑class income typology or continuous estimation.
- No evaluation on sequential spending data or cold‑start conditions – Odin’s profiling must handle sparse early transactions.
- The paper does not address computational constraints on mobile devices, where ensemble methods may be heavier than simpler classifiers.

## Limitations

- Dataset is US‑based; findings may not generalize to Filipino income structures or cultural‑economic contexts. [unacknowledged]
- No comparison of ensemble methods against deep learning (e.g., LSTM) or recent boosting algorithms (XGBoost, LightGBM).
- Evaluation uses only 10‑fold CV on a single dataset; no external validation or out‑of‑sample testing on a separate holdout.
- Class imbalance not discussed – the dataset’s original proportion of >$50K earners is not reported, which affects precision/recall interpretation. [unacknowledged]
- Hyperparameter search limited to confidence factor and k; no optimization of tree depth, number of trees, or other critical parameters.

## Remember This

- 🔑 **98.37% accuracy** – Random Tree matches RandomForest with lower complexity.
- 📌 Ensemble methods (RandomForest/Random Tree) dominate single classifiers – strong starting point for Odin’s profiling module.
- 💡 J48 accuracy rises with confidence (87%→91%); k‑NN falls as k grows (89%→86%) – tuning matters.
- ⚠️ US dataset, not Filipino – income thresholds and demographics do not directly transfer.
