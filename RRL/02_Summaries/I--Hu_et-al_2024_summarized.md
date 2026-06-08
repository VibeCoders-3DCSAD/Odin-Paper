# A User Profile System for the Finance Platform of Commerce

## Metadata

```yaml
---
paper_id: "10.1145/3718391.3718436"
designation: international
title: "A User Profile System for the Finance Platform of Commerce"
authors: "Hu, Z.; Qiu, Y.; Hu, S.; Cheng, Z.; Qiu, S."
year: 2024
venue: "2024 the 12th International Conference on Information Technology (ICIT)"
odin_topics: ["F.1", "F.2"]
shorthand_tags: ["/profiling-role", "/classification-vs-clustering", "/classifier-candidates"]
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

K-means clustering groups users by shared characteristics, enabling precise marketing and risk control in a finance platform user profile system.

## Problem and Motivation

Generic web information fails to address individual user needs, making accurate user representation essential. As competition intensifies, customer churn rises and loyalty declines, requiring precise marketing and risk control. Prior user profile systems lacked comprehensive integration of internal and external multi-source data tailored to financial platforms.

## Approach

- Data acquisition combines explicit (user input) and implicit (behavior logging) methods; implicit yields richer data.
- Data processing steps include word segmentation, data filtering, and normalization to standardize raw data.
- Tags are categorized as fact tags (statistical, e.g., purchase frequency) or model tags (derived from business problems).
- Tag weighting uses objective methods (entropy weight, correlation coefficient) or subjective methods (Delphi, AHP).
- User profile models include text mining (TF-IDF, topic models), classification (ANN, KNN, SVM), and clustering (K-means, DBSCAN, HAC).
- The system architecture has four layers: data collection, data storage, middle (processing/integration), and data visualization.
- A sample K-means algorithm groups users by distance to centroids, iteratively updating centroids until convergence.

## Findings

- The user profile system enables precise marketing, risk control, and informed decision-making in financial institutions.
- K-means clustering segments users into K groups based on shared characteristics such as income, expenditure, and transaction history.
- The system includes individual user profiles, group user profiles, behavior trend analysis, and tag management modules.
- Cross-industry data integration enriches profile accuracy and creates a virtuous cycle of model improvement.

## Key Figures and Tables

- Table 1: User characteristics (basic info, financial info, working info, transaction info) → defines the feature set used for profiling.
- Figure 1: Four-layer user profile model (data collection, storage, middle, visualization) → shows end-to-end system architecture.
- Figure 2: System functionalities (User Profile, User Group Profile, Tag Information modules) → maps three core feature groups.

## Key Equations

$$uw_{ij} = tf_{ij} \times idf_i$$
*Unnormalized term weight equals term frequency times inverse document frequency.*

$$idf_i = \log \frac{\#documents\ in\ collection}{\#documents\ containing\ term\ i}$$
*Rare terms get higher weight in the concept vector.*

$$similarity(c_j, d_k) = c_j \circ d_k = \sum_{i=1}^{n} w_{ij} \times d_{jk}$$
*Cosine‑like similarity between a concept and a document as dot product of weight vectors.*

## Definitions

| Term / Acronym | Plain-English Definition |
| -------------- | ------------------------ |
| User profile (portrait) | A structured representation of a user’s characteristics, behaviors, and preferences derived from data. |
| Explicit acquisition | User manually provides personal data (high quality, low volume). |
| Implicit acquisition | System logs user behavior without active input (rich data, user‑transparent). |
| Fact tag | A tag derived directly from statistical analysis of raw data (e.g., purchase frequency). |
| Model tag | A tag built from fact tags to address specific business problems. |
| K-means clustering | An unsupervised algorithm that partitions users into K groups by minimizing distance to group centroids. |
| TF-IDF | Term Frequency–Inverse Document Frequency: a numerical statistic reflecting how important a word is to a document. |

## Critical Citations

- [Cooper, n.d.] — Origin of Persona concept, the foundation of modern user profiling.
- [Armstrong et al., 1995] — WebWatcher system that shifted from individual to group user profiles via behavior logging.
- [Chen et al., 2021] — Two‑stage classification model for predicting demographic attributes from search engine data.
- [Kobsa, 1993] — Early framework for adaptive user models with stereotypes and default initialization.

## Relevance to Odin

**Topics:**

F.1 — User Behavioral Profiling in Filipino Personal Finance Contexts

F.2 — Profile Classification Algorithm

**Contribution to Odin:**

This paper directly informs Odin’s user profile classification module by demonstrating how clustering (K-means) can segment users based on shared financial and behavioral characteristics. Although Odin requires a classification algorithm (not unsupervised clustering), the paper’s discussion of tag weighting methods (entropy, Delphi) and multi‑layer data processing (explicit + implicit acquisition) provides design justification for feature selection and cold‑start profiling. The system architecture separating individual profiles, group profiles, and behavior trends supports Odin’s need for behavior‑driven profile updates over time.

**Directly justifies:**

- "K-means clustering, an unsupervised learning algorithm, groups users by minimizing the distance to centroids across features such as income, expenditure, and transaction history."
- "User profiling enables precise marketing and risk control in financial platforms by analyzing behavior and preferences without account‑manager dependency."
- "Fact tags (statistical aggregates) and model tags (derived via business logic) with weighting methods like entropy weight or analytic hierarchy process improve profile accuracy."
- "Individual user profiles, group user profiles, and behavior trend analysis are three core modules of a complete user profile system."

**Limits of relevance:**

- Study context is Chinese enterprise commerce finance, not Filipino personal budget management.
- K-means is a clustering method, whereas Odin requires a classification algorithm for assigning users to predefined behavioral profiles.
- No empirical validation or accuracy metrics are provided for the profile system.
- Implicit data collection (logging behavior) raises privacy considerations not addressed in the paper; Odin relies on manual input only.

## Limitations

- No quantitative evaluation of the user profile system’s accuracy, precision, or business impact is reported.
- The paper does not address cold‑start scenarios where new users have insufficient history for clustering. [unacknowledged]
- Profile update mechanisms (how to handle changing user behavior over time) are not discussed. [unacknowledged]
- Privacy or informed consent for implicit data collection is not considered, a critical gap for personal finance apps.
- The sample K-means algorithm lacks guidance on choosing K or validating cluster quality.

## Remember This

- 🔑 K-means groups users by minimizing distance to centroids – unsupervised, no labeled data needed.
- 📌 Individual + group profiles + behavior trends = three core modules for financial user profiling.
- 💡 Tags split into fact (statistical) and model (business‑derived) – weights set via entropy or Delphi methods.
- ⚠️ No empirical validation – system design only, no accuracy numbers to cite.
