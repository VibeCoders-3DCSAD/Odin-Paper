# Optimized Random Forest Classifier for Students Lifestyle Prediction Using Behavioral Data: A Machine Learning Approach

## Metadata

```yaml
---
paper_id: "10.54554/jtec.2025.17.02.004"
designation: algorithm-specific
title: "Optimized Random Forest Classifier for Students Lifestyle Prediction Using Behavioral Data: A Machine Learning Approach"
authors: "Ram, M. L.; Agoylo, J. C. Jr."
year: 2025
venue: "Journal of Telecommunication, Electronic and Computer Engineering"
odin_topics: ["5.C", "12.B"]
shorthand_tags: ["/classifier-candidates", "/classifier-tradeoffs", "/classifier-eval-metrics", "/eval-ml-design"]
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

Random Forest with 30–40 trees predicts lifestyle categories from behavioral data with **75.07% accuracy** on real-world student responses, but perfectly overfits training data beyond 30 trees.

## Problem and Motivation

Existing machine learning studies on student behavior focus on academic performance or mental health, leaving comprehensive lifestyle classification underexplored. Understanding lifestyle categories (e.g., fitness enthusiast, health-conscious) can enable personalized health interventions and behavioral analytics. No prior work had validated a Random Forest classifier on real student inputs after training on a large lifestyle dataset.

## Approach

- Dataset: Half a Million Lifestyle Dataset from Kaggle (500,000 records) with 9 behavioral features (gender, age, health-conscious rating, screen time, social media influence, eco-consciousness, stress management, professional trainings, time management).
- Preprocessing: Dropped missing rows, selected 9 columns, converted gender to numeric (1=male, 2=female).
- Algorithm: Random Forest classifier with parameter optimization; tested tree counts from 10 to 100.
- Validation: Trained on 500k records, then tested on 93 Filipino students who provided behavioral inputs via a Python-based program.
- Evaluation metrics: Accuracy, precision, recall, F1 score; also computational complexity analysis O(T·N·log N·F).

## Findings

1. Model achieved **75.07% accuracy** on 93 real-world student predictions, with precision 75.16%, recall 75.07%, and F1 74.40%.
2. Training accuracy reached 100% with ≥30 trees, indicating severe overfitting; test accuracy plateaued at ~75% regardless of more trees.
3. Optimal tree count was 30–40, balancing computational efficiency and generalization.
4. Classification distribution among 93 students: 50 Health-Conscious, 41 Fitness Enthusiast, 1 Eco-Friendly, 1 Social Media Influencer.
- Random Forest trained in 2.5 minutes on standard hardware, demonstrating practical feasibility for large-scale behavioral classification.

## Key Figures and Tables

- Figure 3: Test accuracy vs. number of trees → test accuracy stabilizes at 75% after 20 trees; training accuracy hits 100% at 30 trees.
- Table 1: Model performance metrics → Accuracy 0.7507, Precision 0.7516, Recall 0.7507, F1 0.7440.
- Table 2: Prediction results for 93 students → 50 Health-Conscious, 41 Fitness Enthusiast, 1 each Eco-Friendly and Social Media Influencer.

## Key Equations

$$Accuracy = \frac{TP + TN}{TP + TN + FP + FN}$$
*Correct predictions divided by all predictions.*

$$Precision = \frac{TP}{TP + FP}$$
*Of predicted positives, how many were actually positive.*

$$Recall = \frac{TP}{TP + FN}$$
*Of actual positives, how many were correctly identified.*

$$F1\ Score = 2 \times \frac{Precision \times Recall}{Precision + Recall}$$
*Harmonic mean balancing precision and recall.*

$$O(T \cdot N \cdot \log N \cdot F)$$
*Random Forest time complexity where T=trees, N=samples, F=features.*

## Definitions

| Term / Acronym | Plain-English Definition |
| -------------- | ------------------------ |
| Random Forest (RF) | Ensemble of decision trees that votes on final classification. |
| Overfitting | Model memorizes training data but fails on new data. |
| Precision | Proportion of correct positive predictions among all positive predictions. |
| Recall (Sensitivity) | Proportion of actual positives correctly identified. |
| F1 Score | Harmonic mean of precision and recall; balances both. |
| TP | True Positive — correctly predicted positive class. |
| TN | True Negative — correctly predicted negative class. |
| FP | False Positive — incorrectly predicted positive (Type I error). |
| FN | False Negative — incorrectly predicted negative (Type II error). |

## Critical Citations

- [Jayaprakash et al., 2020] — First demonstration of Random Forest for student academic performance prediction, establishing baseline for classifier application.
- [Chaturvedi et al., 2021] — Prior work on student lifestyle query classification using ensemble learning, directly comparable domain.
- [Ram et al., 2025] — Same research group’s clustering study on student performance; validates methodology continuity.

## Relevance to Odin

**Topics:**

5.C — Financial Behavioral Profile Classification Algorithm

12.B — Evaluation of Algorithmic Modules

**Contribution to Odin:**

This paper directly supports Odin’s financial behavioral profiling module by demonstrating how a Random Forest classifier can be optimized to predict user categories from behavioral features. The analysis of overfitting (100% training accuracy vs. 75% test accuracy) provides a concrete caution: Odin’s classification module must limit tree depth or number of trees to avoid memorizing user histories instead of learning general patterns. The use of standard evaluation metrics (accuracy, precision, recall, F1) aligns with Odin’s planned module evaluation framework. Although the domain is lifestyle rather than finance, the methodology for tuning a classifier on user-reported behavioral data transfers directly to profiling Filipino young professionals by spending behavior.

**Directly justifies:**

- "Random Forest with 30–40 trees achieves 75.07% accuracy on behavioral classification, but exceeding 30 trees causes perfect training overfitting without test accuracy gain."
- "Testing accuracy plateaus at ~75% after 20 trees while training accuracy climbs to 100% — increasing trees beyond an optimal threshold does not improve generalization."
- "Precision (75.16%) and recall (75.07%) remained closely balanced, indicating the classifier did not favor false positives over false negatives."
- "A Random Forest model trained on 500,000 records processed 93 real-world user inputs within 2.5 minutes, confirming practical deployability on standard hardware."
- "Self-reported behavioral data carries inherent bias; future work must address this limitation when deploying classification models in production."

**Limits of relevance:**

- Domain is lifestyle (health, fitness, social media) not financial spending — behavioral patterns may not transfer directly to budget adherence or expense categorization.
- Study population is students (age ~18–25), whereas Odin targets young professionals aged 20–40; income stability and financial obligations differ.
- Data came from a global Kaggle dataset plus 93 Filipino students; the classification categories (Fitness Enthusiast, etc.) have no financial analogue.
- Model was not tested on cold-start conditions (users with no history); all 93 students provided full behavioral inputs at once.

## Limitations

- Self-reported behavioral data introduces potential bias and inaccuracy; no objective validation of user responses. [unacknowledged]
- Predefined lifestyle categories (Fitness Enthusiast, Health-Conscious, Eco-Friendly, Social Media Influencer) may not capture the full complexity of individual behaviors.
- Student sample size of 93 is small for generalizing to broader Filipino population; no demographic breakdown beyond gender conversion.
- No comparison against alternative classifiers (e.g., SVM, neural networks) to establish Random Forest’s relative advantage.
- Model was tested only on students from a single university (Southern Leyte State University), limiting geographic generalizability.

## Remember This

- 🔑 **75.07% accuracy** on real-world student data — Random Forest works for behavioral classification.
- ⚠️ 100% training accuracy but only 75% test — adding trees past 30 causes overfitting without gain.
- 📌 Optimal trees = 30–40 — more computation doesn’t improve test performance.
- 💡 Precision and recall both ~75% — no severe false-positive or false-negative bias.
- 🔍 No cold-start evaluation — unknown if method works for new users with zero history.
