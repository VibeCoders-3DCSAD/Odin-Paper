```markdown
# Single and Multiple Separate LSTM Neural Networks for Multiple Output Feature Purchase Prediction

## Metadata

```yaml
---
paper_id: "10.3390/electronics12122616"
designation: algorithm-specific
title: "Single and Multiple Separate LSTM Neural Networks for Multiple Output Feature Purchase Prediction"
authors: "Ćirić, M.; Predić, B.; Stojanović, D.; Ćirić, I."
year: 2023
venue: "Electronics"
odin_topics: ["D.1", "D.2"]
shorthand_tags: ["/lstm-multi-output", "/lstm-vs-alternatives", "/lstm-spending-applied", "/forecasting-methods", "/spending-time-series", "/per-category-forecast"]
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

Dedicated LSTM networks predict product categories 15–50% better recall than a single multivariate LSTM, but a single LSTM predicts next purchase day more accurately.

## Problem and Motivation

Existing purchase prediction methods struggle to simultaneously predict both the timing and product category of a customer’s next purchase. Accurate multi-output prediction enables personalized marketing and inventory planning. Prior work lacked a systematic comparison of single versus multiple separate LSTM architectures for this multi-output task.

## Approach

- Dataset: 7.5M transactions from a medical device and drug company, aggregated to ~1M orders from ~10,100 customers with ≥4 orders.
- Three datasets based on minimum purchases per customer: 5+, 20+, and 100+ purchases.
- Input features: time series of days between consecutive purchases, plus multi-hot encoded vectors of 100 GPI drug groups or 16 drug categories.
- Outputs: next purchase day (regression) and binary vector indicating which drug groups/categories appear in the next purchase.
- Compared single multivariate LSTM (predicts both outputs together) vs two separate LSTM networks (one for categories, one for day).
- LSTM cell includes forget gate to solve vanishing gradient problem (see Figure 4).
- Evaluation metrics: accuracy, precision, recall for Realized Purchases (RP) and Unrealized Purchases (UP) classes.
- Additional per-customer analysis: minimum correctly predicted and maximum incorrectly predicted categories.

## Findings

1. Dedicated LSTM for product categories improved RP recall by **15–50%** across all datasets compared to the single multivariate LSTM.
2. For next purchase day prediction, the single multivariate LSTM outperformed separate networks on nearly all metrics (accuracy, precision, recall).
3. Using 100 fine-grained drug groups gave higher prediction metrics than using 16 aggregated drug categories.
4. On the 100+ dataset with dedicated LSTM: 95.7% of customers had at least one purchased category correctly predicted; 51.19% had at least four correct.
5. For the same setup: 81.17% of customers had no more than one incorrectly predicted category; 99.63% had no more than four incorrect.
- LSTM consistently outperformed SimpleRNN (e.g., RP recall 62.33% vs 46.02% for drug groups).

## Key Figures and Tables

- Figure 2: Histogram of orders per customer → majority of customers made 200 or fewer purchases.
- Figure 3: Orders per drug group → highly imbalanced; some groups ordered much more frequently than others.
- Table 1: LSTM vs SimpleRNN on 100+ dataset → LSTM better on all metrics (accuracy 97.27% vs 96.03%).
- Figure 5: Results for 100+ dataset → dedicated network dramatically improves category recall; single network better for day prediction.
- Figure 8: Minimum correctly predicted categories → 95.7% of customers get at least one correct category.

## Key Equations

$$i_t = \sigma(W_{xi}x_t + W_{hi}h_{t-1} + W_{ci}c_{t-1} + b_i)$$
*Input gate: decides what new information to store.*

$$f_t = \sigma(W_{xf}x_t + W_{hf}h_{t-1} + W_{cf}c_{t-1} + b_f)$$
*Forget gate: controls what to discard from cell state.*

$$c_t = f_t c_{t-1} + i_t \tanh(W_{xc}x_t + W_{hc}h_{t-1} + b_c)$$
*Cell state update: forget old, then add new candidate values.*

$$o_t = \sigma(W_{xo}x_t + W_{ho}h_{t-1} + W_{co}c_t + b_o)$$
*Output gate: determines what to output based on cell state.*

$$h_t = o_t \tanh(c_t)$$
*Hidden state: filtered cell state as final output.*

## Definitions

| Term / Acronym | Plain-English Definition |
| -------------- | ------------------------ |
| LSTM | Long Short-Term Memory – a recurrent neural network that learns what to remember and forget over long sequences. |
| GPI | Generic Product Identifier – 14-character hierarchical drug classification system with 7 tiers of drug information. |
| Multi-hot encoding | A binary vector where multiple positions can be 1 to indicate simultaneous presence of several categories. |
| Realized Purchases (RP) | Class for drug groups/categories that actually appear in the next purchase. |
| Unrealized Purchases (UP) | Class for drug groups/categories that do not appear in the next purchase. |

## Critical Citations

- [Hochreiter & Schmidhuber, 1997] – Original LSTM paper that solved the vanishing gradient problem.
- [Giles et al., 2001] – Noisy time series prediction using recurrent neural networks; cited for foreign exchange forecasting.
- [Martínez et al., 2018] – Machine learning framework for purchase prediction in non-contractual settings.
- [Cirqueira et al., 2019] – LSTM for online retail that also noted difficulty predicting product categories.

## Relevance to Odin

**Topics:**

D.1 — Predictive Modeling in Personal Finance Systems

D.2 — LSTM as the Spending Forecasting Algorithm

**Contribution to Odin:**

This paper directly informs Odin’s spending forecasting module by comparing single versus multiple separate LSTM architectures for multi-output prediction (next purchase timing and product category). The finding that dedicated networks dramatically improve category recall (15–50% higher) while a single network better predicts purchase day provides a design justification for Odin’s LSTM implementation: if Odin forecasts only spending amounts (a regression task similar to purchase day prediction), a single LSTM may suffice; if Odin also predicts which categories will have spending, a dedicated classifier per category may be warranted. Although the domain is medical supplies, the methodology for transforming transaction histories into time-series input features and the comparative evaluation of LSTM architectures are directly transferable to Odin’s per-category spending prediction.

**Directly justifies:**

- "Dedicated LSTM neural networks for product category prediction achieve 15–50% higher recall for realized purchases compared to a single multivariate LSTM predicting both timing and categories simultaneously."
- "For next purchase day prediction, a single multivariate LSTM outperforms separate networks, indicating that multi-output models trade off accuracy across outputs."
- "Using 100 fine-grained product categories yields higher prediction metrics than 16 broader categories, suggesting that granular category definitions improve LSTM performance."
- "95.7% of customers with at least 100 historical purchases had at least one correctly predicted purchased drug category using a dedicated LSTM."
- "LSTM neural networks solve the vanishing gradient problem, enabling them to capture long-term dependencies in sequential purchase data – a key advantage over SimpleRNN."

**Limits of relevance:**

- Domain is medical drug purchases, not general consumer spending; category recurrence and purchase cycles may differ from personal finance.
- Dataset requires at least 5 purchases per customer; cold-start performance (new users with no history) is not evaluated.
- Prediction target is binary category presence, not spending amounts – Odin forecasts monetary values per category.
- No evaluation of mobile deployment constraints (compute, battery, latency) – assumes server-side training.

## Limitations

- Cold-start performance not evaluated – customers with few purchases (e.g., 5+ dataset) show lower recall. [unacknowledged]
- Binary classification of category presence ignores purchase quantity or amount – Odin needs amount prediction. [unacknowledged]
- GPI classification system is domain-specific; generalizability to non-hierarchical financial categories is unproven.
- No comparison to non-LSTM baselines beyond SimpleRNN (e.g., ARIMA, Prophet) – advantage over classical methods not quantified.
- Data imbalance (Figure 3) may bias predictions toward frequent drug groups; Odin would face similar category imbalance.

## Remember This

- 🔑 Dedicated LSTM improves category recall by **15–50%** over a single multi-output LSTM.
- 📌 Single LSTM better predicts purchase day – separate networks hurt timing accuracy.
- 🧠 95.7% of frequent buyers got at least one correct category prediction.
- ⚠️ No cold-start evaluation – results require 5+ historical purchases per user.
```