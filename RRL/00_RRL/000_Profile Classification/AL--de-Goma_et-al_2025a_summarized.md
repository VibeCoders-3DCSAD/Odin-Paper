# Exploratory Analysis of Audio Features for Dominant Feature Identification: A Multimodal Machine Learning Evaluation of Song Popularity Prediction Using Deep Neural Networks, Clustering, and Regression Models

## Metadata

```yaml
---
paper_id: "10.1145/3779657.3779690"
designation: algorithm-specific
title: "Exploratory Analysis of Audio Features for Dominant Feature Identification: A Multimodal Machine Learning Evaluation of Song Popularity Prediction Using Deep Neural Networks, Clustering, and Regression Models"
authors: "de Goma, J.; Cruz, S. F.; Espino, M.; Tuason, J. R.; Villaluz, A."
year: 2025
venue: "2025 The 7th World Symposium on Software Engineering (WSSE 2025)"
odin_topics: []
shorthand_tags: []
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

Tempo, energy, loudness, and danceability are the dominant audio features for predicting OPM song popularity, with Random Forest achieving 93.98% test accuracy.

## Problem and Motivation

No prior study has systematically investigated which audio features drive song popularity specifically in the Philippine (OPM) market. Understanding these features helps artists, producers, and streaming services align with regional listener preferences. Existing work focused on global datasets or general classification, leaving a gap in culturally specific audio feature analysis for the Philippines.

## Approach

- Dataset: 1,000 top Spotify songs from 2018–2023 plus 2024 weekly chart, covering pre‑pandemic, pandemic, and post‑pandemic eras.
- Preprocessing: Chorus extraction via time‑lag similarity matrix; IQR outlier removal; Min‑Max scaling; SMOTE oversampling.
- Features: 16 audio features extracted with Librosa (tempo, energy, loudness, danceability, spectral centroid, etc.).
- Dimensionality reduction: LLE and UMAP to preserve local/global structures and visualize clusters.
- Clustering: Agglomerative and K‑means to group songs by audio similarity.
- Models: Random Forest, XGBoost, Decision Tree, SVM, Logistic Regression, and DNN with attention mechanism.
- Evaluation: Accuracy, precision, recall, F1‑score; 80/20 train/test split with random state 42.

## Findings

1. Random Forest achieved **93.98% test accuracy** (83.1% validation) – the best among all models.
2. XGBoost followed with 93.97% test accuracy (75.38% validation); standard DNN reached 91.62% test (62.56% validation).
3. Attention‑based DNN with PCA scored 90.84% test (53.84% validation); with ICA dropped to 53.93% test.
- Logistic Regression performed poorly (61.25% test, 27.70% validation); SVM was similarly weak.
- Top features by Mutual Information: Spectral Centroid, Speechiness, Loudness; Instrumentalness and Acousticness contributed minimally.
- All models failed to predict mid‑tier popularity classes (2 and 3) due to data skew and non‑audio factors (lyrics, artist reputation).

## Key Figures and Tables

- Figure 1: Feature extraction result → tempo, energy, loudness, danceability are primary indicators.
- LLE plot (no number): central dense clusters → common popular features across genres; peripheral points → niche or unique audio profiles.
- K‑means PCA plot: six clusters; central clusters (2,4,6) show balanced tempo/energy; peripheral clusters (0,8) show specialized traits.

## Key Equations

None.

## Definitions

| Term / Acronym | Plain-English Definition |
| -------------- | ------------------------ |
| OPM | Original Pilipino Music – music originating from the Philippines. |
| DNN | Deep Neural Network – a neural network with multiple hidden layers. |
| LLE | Locally Linear Embedding – a dimensionality reduction method that preserves local neighborhood structure. |
| UMAP | Uniform Manifold Approximation and Projection – a nonlinear dimensionality reduction technique for visualizing clusters. |
| IQR | Interquartile Range – a measure of statistical dispersion used to remove outliers. |
| SMOTE | Synthetic Minority Over‑sampling Technique – creates synthetic samples for imbalanced classes. |
| Attention mechanism | A neural network component that weights input features by their importance to the prediction. |

## Critical Citations

- [Araujo et al., 2019] – Foundational study on predicting music popularity on streaming platforms.
- [Abundo & Monterola, 2009] – Prior OPM genre classification using audio features, establishing domain context.
- [Yang et al., 2017] – Revisited audio‑based hit song prediction with CNNs, informing the DNN approach.

## Relevance to Odin

**Topics:**

None — contextual only.

**Contribution to Odin:**

This paper does not relate to personal finance, budgeting, spending behavior, or any of Odin's functional domains. The machine learning techniques (DNN, clustering, feature importance, attention mechanisms) are domain‑agnostic, but the paper provides no evidence, findings, or claims applicable to financial behavioral profiling, spending forecasting, budget recommendation, anomaly detection, expense categorization, or any other Odin module. No direct justification for any Odin design decision can be drawn from this work.

**Directly justifies:**

None.

**Limits of relevance:**

- The domain is music popularity prediction, not personal financial management.
- Data consists of audio features and YouTube view counts, with no financial transactions or user behavior.
- Problem formulation (hit song prediction) has no parallel in budget management or expense tracking.
- No evaluation of algorithm performance on financial data or under constraints relevant to Odin (e.g., cold start, irregular income, manual entry).

## Limitations

- Chorus‑only analysis may miss predictive information from verses or bridges. [acknowledged]
- Popularity metric limited to YouTube views; other platforms (Spotify streams, social media) excluded.
- Models consistently fail to predict mid‑tier popularity classes, indicating that non‑audio factors dominate those cases. [acknowledged]
- Dataset size (1,000 songs) is modest; no explicit validation on independent OPM test sets. [unacknowledged]
- No comparison to human judgment or industry benchmarks; practical utility for artists/labels is unquantified.

## Remember This

- 🔑 Random Forest hit **93.98%** test accuracy – best among six models on OPM song data.
- 📌 Top predictive audio features: spectral centroid, speechiness, loudness – not instrumentalness or acousticness.
- ⚠️ All models failed on mid‑tier popularity – audio alone cannot predict moderate success.
- 💡 Central clusters in LLE/UMAP show that popular OPM songs share core audio traits across genres.
