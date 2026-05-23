# Predicting student retention: A comparative study of machine learning approach utilizing sociodemographic and academic factors

## Metadata

```yaml
---
paper_id: "10.1016/j.sasc.2025.200352"
designation: local
title: "Predicting student retention: A comparative study of machine learning approach utilizing sociodemographic and academic factors"
authors: "Deleña, R. D.; Dia, N. J.; Sacayan, R. R.; Sieras, J. C.; Khalid, S. A.; Macatotong, A. H. T.; Gulam, S. B."
year: 2025
venue: "Systems and Soft Computing"
odin_topics: ["5.C", "8.B", "12.B"]
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

XGBoost achieved **90.66% cross-validated accuracy** predicting student dropout from sociodemographic and academic data, outperforming nine other ML algorithms on a Philippine university dataset.

## Problem and Motivation

Student dropout rates in higher education remain persistently high, especially in developing regions with limited intervention resources, yet traditional retention approaches rely on subjective assessments. High attrition wastes institutional resources and undermines graduation targets, making early identification of at-risk students critical for targeted support. Prior studies lacked systematic benchmarking of multiple machine learning algorithms on local, long-term institutional data from underrepresented Southeast Asian contexts.

## Approach

- Dataset: 482 student records (2012–2022) from Mindanao State University – Main Campus, 146 variables (sociodemographic + academic), balanced dropout/retention (50.2%/49.8%).
- Preprocessing: Power BI cleaning, CRISP-DM methodology, Spearman correlation removed multicollinearity (79 features retained).
- Algorithms: Ten models evaluated — XGBoost, Gradient Boosting (GB), Artificial Neural Network (ANN), Decision Tree (DT), Random Forest (RF), Multilayer Perceptron (MLP), Logistic Regression (LR), K-Nearest Neighbor (KNN), SVM, Naïve Bayes (NB).
- Evaluation: Train-test split (70/30) plus 5-fold cross-validation; metrics: Accuracy, Precision, Recall, F1, MSE, Log Loss.
- Implementation: Python 3.10, Jupyter Notebook, scikit-learn, xgboost library.

## Findings

1. XGBoost achieved the **highest cross-validated accuracy (90.66%)** and F1 Score (90.72), with low error (MSE = 9.34, Log Loss = 0.26).
2. GB and ANN followed closely: GB at 89.42% accuracy, ANN at 88.39% accuracy, both with strong precision-recall balance.
3. Naïve Bayes had the highest recall (97.21%) but excessive false positives (31), limiting practical use.
- Decision Tree overfit: dropped from 90.34% (train-test) to 84.44% (cross-validation) accuracy.
- Ensemble models (XGBoost, GB) showed stable generalization; nonparametric models (KNN, DT) required more tuning.

## Key Figures and Tables

- Figure 6: Confusion matrices for all ten models → XGBoost had lowest total misclassifications (9 errors: 5 false positives, 4 false negatives).
- Figure 7: 5-fold cross-validation performance comparison → XGBoost top-ranked; NB high recall but poor precision and high Log Loss.
- Table 6: Dropout detection rates → XGBoost recall = 94.5%, precision = 93.2%.
- Table 7: Initial train-test split scores → XGBoost at 93.79% accuracy, MSE 6.21.

## Key Equations

None.

## Definitions

| Term / Acronym | Plain-English Definition |
| -------------- | ------------------------ |
| XGBoost | Extreme Gradient Boosting; an optimized ensemble algorithm that builds trees sequentially, correcting prior errors. |
| CRISP-DM | Cross-Industry Standard Process for Data Mining; a six-phase framework (business understanding to deployment) for data mining projects. |
| Log Loss | A metric that penalizes confident wrong predictions; lower values mean better-calibrated probability estimates. |
| 5-fold cross-validation | Data split into 5 parts; each part serves as validation once while the other 4 train the model, reducing overfitting. |
| Multicollinearity | High correlation between predictor variables; removed using Spearman correlation threshold ≥0.70. |

## Critical Citations

- [Baker & Yacef, 2009] — Foundational review defining Educational Data Mining as a field; situates the study's methodological framing.
- [Niyogisubizo et al., 2022] — Two-layer ensemble approach for dropout prediction; used for baseline comparison and ensemble justification.
- [Rodríguez-Hernández et al., 2021] — Systematic implementation of ANN for academic performance; informs neural network evaluation design.
- [Alhazmi & Sheneamer, 2023] — Large-scale (275k students) XGBoost study; supports XGBoost's generalizability claim.

## Relevance to Odin

**Topics:**

5.C — Financial Behavioral Profile Classification Algorithm

8.B — Anomaly Detection Algorithm

12.B — Evaluation of Algorithmic Modules

**Contribution to Odin:**

This paper provides a direct benchmark for algorithm selection in Odin's binary classification tasks, specifically financial behavioral profiling (e.g., income stability type) and anomalous spending detection (dropout vs. retained analog). The rigorous comparison of ten algorithms using both train-test split and 5-fold cross-validation demonstrates that XGBoost consistently outperforms alternatives on structured tabular data with mixed sociodemographic and performance features — a data structure similar to Odin's user transaction and profile attributes. Although the domain is student retention, the methodological finding (XGBoost > GB > ANN > others) and the use of Log Loss as a calibration metric directly inform Odin's classification module design and evaluation protocol.

**Directly justifies:**

- "XGBoost achieves 90.66% cross-validated accuracy and F1 of 90.72 on a binary classification task with balanced classes, outperforming GB (89.42%) and ANN (88.39%)."
- "Cross-validation reduced Decision Tree accuracy by ~6 percentage points (90.34% → 84.44%), demonstrating that single train-test splits overestimate performance — Odin must use k-fold validation for module evaluation."
- "Log Loss (0.26 for XGBoost) provides a more nuanced calibration measure than accuracy alone; Odin's anomaly detection module should report Log Loss alongside F1 to capture false positive costs."
- "Naïve Bayes produces high recall (97%) but excessive false positives (31), making it unsuitable for high-stakes classification where false alarms erode user trust."

**Limits of relevance:**

- Domain mismatch: student dropout prediction vs. personal finance anomaly detection; financial transaction patterns may differ in feature distribution and class imbalance.
- Small dataset (n=482); Odin may have larger user bases or different data sparsity characteristics.
- No temporal or sequential data; Odin's spending forecasting requires time-series models not evaluated here.
- No explainability analysis; deployment in financial systems may require interpretable models, which XGBoost provides only via SHAP (not discussed).

## Limitations

- Single institution dataset (MSU-Marawi) limits external validity to other Philippine HEIs, let alone personal finance users. [unacknowledged]
- No behavioral or engagement features (LMS activity, peer interaction) were included, which are known predictors of retention; Odin similarly lacks such data.
- 5-fold cross-validation used but not stratified or nested; class balance was natural, but more rigorous validation could improve generalizability estimates. [unacknowledged]
- Model interpretability not addressed; black-box nature of XGBoost may hinder adoption in contexts requiring explainability (e.g., financial alerts).
- Manual hyperparameter tuning was used; automated optimization might alter relative algorithm rankings.

## Remember This

- 🔑 **XGBoost at 90.66% accuracy** — best performer among ten classifiers on structured tabular data.
- 📌 Log Loss (0.26) shows well-calibrated probabilities — use it to evaluate Odin's anomaly alerts.
- 💡 Cross-validation cut Decision Tree's accuracy by 6% — never trust a single train-test split.
- ⚠️ Domain is student retention, not finance — methods transfer, but feature distributions differ.
