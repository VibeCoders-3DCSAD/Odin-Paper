```yaml
paper_id: 10.63125/mbbfw637
designation: international
title: A SYSTEMATIC REVIEW OF DEMAND FORECASTING MODELS FOR RETAIL E-COMMERCE ENHANCING ACCURACY IN INVENTORY AND DELIVERY PLANNING
authors: Chowdhury, A. R.; Paul, R.; Rozony, F. Z.
year: 2025
venue: International Journal of Scientific Interdisciplinary Research
odin_topics:
  - 6.A
  - 6.B
  - 12.A
  - 12.B
shorthand_tags:
  - /predictive-modeling
  - /spending-forecasting
  - /evaluation
  - /algorithm-evaluation
tldr: A systematic review of 72 studies finds machine learning and deep learning models outperform traditional statistical methods for demand forecasting in retail e-commerce, especially with volatile data and external variables.
problem_and_motivation: Retail e-commerce faces volatile demand and complex logistics, requiring accurate forecasting. Existing literature lacks a comprehensive synthesis of forecasting models for inventory and delivery planning. This review addresses that gap by evaluating 72 studies to guide model selection.
approach:
  - Followed PRISMA guidelines for systematic review of 72 peer-reviewed articles from Scopus, Web of Science, IEEE Xplore, and ScienceDirect (2010–2024).
  - Used keyword combinations including “demand forecasting,” “retail e-commerce,” “machine learning,” and “deep learning” to identify relevant studies.
  - Categorized forecasting models into four groups: traditional statistical, machine learning, deep learning, and hybrid approaches.
  - Evaluated performance using accuracy metrics such as MAPE, RMSE, and MAE across diverse e-commerce datasets.
  - Extracted data on dataset characteristics, operational focus (inventory/logistics), and external variables (weather, sentiment, promotions).
findings:
  - Traditional statistical models (ARIMA, Holt-Winters) remain relevant for stable, seasonal demand but fail under nonlinearity and promotional spikes.
  - num: Machine learning models (random forests, gradient boosting) improve forecast accuracy by up to 20% over statistical methods in high‑SKU environments.
  - Deep learning models (LSTM, GRU, CNN) capture long‑range dependencies and outperform other methods for erratic and intermittent demand.
  - Hybrid ARIMA‑ML/DL models balance interpretability and accuracy, reducing forecasting error during flash sales and disruptions.
  - Integration of external data (weather, social media sentiment, clickstream) consistently improves forecast precision in volatile categories.
key_figures_tables:
  - "Figure 3: Major Techniques Used in Demand Forecasting → categorizes models into statistical, ML, DL, hybrid."
  - "Figure 5: Machine Learning Models for Nonlinear Demand Forecasting → tree‑based methods adapt well to promotions and seasonality."
  - "Figure 9: Impact of Forecasting Accuracy on Inventory Replenishment Decisions → better accuracy reduces stockouts and overstock."
  - "Table 1: Summary of findings → shows study counts, citations, and key contributions per model category."
key_equations:
  - equation: None.
    explanation: ""
definitions:
  - term: ARIMA
    definition: AutoRegressive Integrated Moving Average, a linear time series model.
  - term: LSTM
    definition: Long Short‑Term Memory, a recurrent neural network for sequence forecasting.
  - term: MAPE
    definition: Mean Absolute Percentage Error, a scale‑independent forecast accuracy metric.
  - term: SKU
    definition: Stock Keeping Unit, a unique product identifier for inventory management.
critical_citations:
  - None.
relevance:
  topics:
    - code: 6.A
      name: Predictive Modeling in Personal Finance Systems
      justification: Review evaluates predictive models (ARIMA, ML, DL) applicable to spending forecasts.
    - code: 6.B
      name: Spending Forecasting Algorithm
      justification: Directly examines forecasting algorithms and their comparative performance.
    - code: 12.A
      name: Evaluation Frameworks for Personal Finance Systems
      justification: Uses MAPE, RMSE, MAE as evaluation metrics for model accuracy.
    - code: 12.B
      name: Evaluation of Algorithmic Modules
      justification: Benchmarks multiple model categories across real‑world datasets.
  contribution: This systematic review provides a taxonomy of forecasting models that can directly inform the design of Odin’s spending forecasting module. Its comparative performance results (e.g., ML models improving accuracy by 20%) justify selecting hybrid architectures over pure statistical baselines. The evaluation metrics and benchmarking methodology offer a framework for testing Odin’s predictive algorithms. Insights on external data integration (weather, sentiment) suggest adding contextual features (e.g., Philippine holidays, remittance cycles) to improve personal spending forecasts.
  directly_justifies:
    - Machine learning models improve forecasting accuracy by up to 20% over statistical methods in volatile demand environments.
    - Integration of external data like weather and social media sentiment enhances demand forecast precision.
    - Hybrid ARIMA‑ML models balance interpretability and accuracy for short‑term forecasts.
    - Deep learning models (LSTM) capture long‑term dependencies and outperform baselines on intermittent demand.
  limits:
    - The review focuses on retail e‑commerce product demand, not personal financial spending behavior.
    - Most reviewed studies use proprietary e‑commerce datasets, limiting reproducibility for PFMS contexts.
    - Deep learning models require substantial computational infrastructure, which may not scale for lightweight PFMS.
  mapping_rationale: The paper was screened against Odin’s functional domains. Spending forecasting (6.A, 6.B) directly matches because the paper evaluates predictive models for demand. Evaluation frameworks (12.A, 12.B) apply due to extensive use of accuracy metrics and benchmarking. Behavioral profiling (5.A‑C) was rejected as the paper does not classify users. Anomaly detection (8.A‑B) and budget recommendation (7.A‑C) were rejected because the paper focuses on forecasting, not outlier detection or budget allocation. Mobile design and privacy topics were irrelevant.
limitations:
  - The review only includes English‑language peer‑reviewed studies, potentially missing relevant industry reports. [unacknowledged]
  - Performance comparisons across studies use different datasets and evaluation protocols, making direct aggregation difficult. [acknowledged in discussion]
  - The paper does not address real‑time deployment constraints or inference latency for forecasting models.
remember_this:
  - Forecasting accuracy can reduce inventory costs by up to 25%.
  - Machine learning models beat statistical methods by 20% in volatile settings.
  - Deep learning captures long‑term spending patterns better than ARIMA.
  - Hybrid models offer interpretability without sacrificing forecast precision.
```