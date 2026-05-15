# Evidence‑Based Design for Odin: What the Literature Actually Says

*Synthesis of 70+ reviewed studies on personal finance management systems, forecasting, anomaly detection, user profiling, and budget recommendation, with specific algorithm recommendations, performance benchmarks, and cultural constraints for Filipino young professionals.*

---

## Part I: Overall System Direction – Beyond Financial Literacy

### 1.1 Do Not Build a Financial Literacy App

Financial literacy among Filipino young adults is statistically equivalent across employment types (Torres et al., 2025), yet higher literacy correlates with **lower likelihood of spending within income** (Cacnio & Romarate, 2024). Goal acceptance (β=0.924) and financial attitude (β=0.414) dominate behavior, while literacy has **no significant direct effect** (Dimaunahan et al., 2025; Aoun et al., 2026). **The system must scaffold behavior, not teach concepts.** Educational modules are a distraction.

### 1.2 Treat Cultural Obligations as Protected Categories, Not Anomalies

Kinship obligations (*utang na loob*, *paluwagan*, *og‑ogfo*) are non‑negotiable spending priorities that override personal savings (Rosario, 2025; Amrith, 2026; Casilan & Baclagan, 2024). Standard anomaly detectors flag these as outliers. **Dedicated, non‑negotiable expense categories** must be built in from the start, with a **cultural‑calendar override** to suppress false positives.

### 1.3 Mobile‑First Is Not a Preference – It Is the Only Viable Channel

With 92.8% mobile phone ownership but only 35.3% bank accounts (BSP, 2021), and only 34% of low‑income users understand digital security (Velez, 2025), the system must be **manual‑input, offline‑capable, and privacy‑by‑design**. Banking API integration would exclude the majority of target users. On‑device ML (Jayaprakashnarayan et al., 2026) is the architectural baseline.

### 1.4 Do Not Build Yet Another Expense Tracker

Most “budgeting” apps provide only tracking, not budgeting (Alenazi & Sas, 2023). Users abandon them because categorisation is ambiguous and entry is tedious (Cho, 2024). The system must implement **envelope‑based multiple budgets** with clear, culturally grounded categories (FIES/PCOICOP extended with *paluwagan*, remittances, SSS, etc.). Automated categorisation reduces manual friction by ~78% (Badiger et al., 2026).

### 1.5 Retention: Reduce Friction, Avoid Gamification

Users abandon budgeting because it is “tedious, time‑consuming, and stress‑inducing” (Cho, 2024). Gamification is under‑researched and not proven to drive long‑term retention (Prasetyo et al., 2023). What works: **automated categorisation** (78% effort reduction, Badiger et al.), **visual goal progress bars**, and **automated reminders** (Imawan et al., 2025). Value‑driven engagement (forecasts, alerts, goal tracking) outperforms extrinsic rewards.

### 1.6 Privacy, Security, and Trust Are Not Add‑Ons

Perceived trust shows the widest variability (SD=1.24) among adoption factors for Filipino digital wallet users (Bongado et al., 2025). Only 34% of low‑income users understand digital security features (Velez, 2025). **Explainable AI is essential** – but explanations can decrease trust in 23% of users (Hashemi et al., 2024). On‑device encryption and differential privacy (Jayaprakashnarayan et al., 2026) are baseline requirements.

---

## Part II: Module‑Specific Algorithm Recommendations

### Module 1: User Financial Behavioral Profile Classification

**Best algorithms:** XGBoost / LightGBM achieve **AUC‑ROC 0.90–0.93** on tabular financial data, outperforming deep neural networks (Martínez et al., 2025). For cold‑start, **fuzzy K‑means** (silhouette coefficient 0.690) and **RNN + human‑in‑the‑loop** (35% accuracy improvement) are effective (Duvalla, 2025; Yang, 2024).

**Critical features (Filipino‑specific):** income type, monthly expenses, goal acceptance (β=0.924), goal commitment (β=0.809) (Dimaunahan et al., 2025). **Observed transaction behavior** (loan use, deposit activity) predicts long‑term outcomes far better than self‑reported literacy (Cacnio & Romarate, 2024). Marital status (p=0.034) and employment type (Torres et al., 2025) are significant discriminators.

**Evidence‑based recommendation:** XGBoost or LightGBM for users with >50 transactions. For cold‑start, fuzzy clustering or confidence‑weighted rule assignment based on demographics + goal commitment.

---

### Module 2: Spending Forecasting

**Best algorithm:** LSTM ranks first in 58.97% of deep learning comparisons (Hall & Rasheed, 2025) and reduces RMSE/MAE by 10‑20% over regression on longitudinal expenditure data (Lee et al., 2026). Hybrid CNN‑LSTM achieves MAPE 0.514% on periodic time series (Aguiar‑Pérez & Pérez‑Juárez, 2023).

**Cold‑start and fallback:** On small datasets (0‑2,173 samples), RNNs outperform gradient‑boosted trees by 50 percentage points. LightGBM matches LSTM accuracy on large datasets but trains 100‑1,000× faster (Hall & Rasheed, 2025). LightGBM dominates intermittent, zero‑inflated data (M5 competition) – relevant for manual per‑category entries (Tjøstheim, 2025). ARIMA is a statistical baseline but is outperformed by deep learning on non‑linear series by up to 40× lower RMSE (Kontopoulou et al., 2023). Hybrid ARIMA‑LSTM improves accuracy by 20‑35% (Shuryhin & Zinovatna, 2024).

**Evaluation metrics:** MAPE (38 studies), RMSE (36 studies) (Kara & Şengüler, 2025). **Walk‑forward validation** (not k‑fold) is mandatory (Pagliaro, 2025).

**Evidence‑based recommendation:** LSTM as primary for users with ≥3 months history. Cold‑start: ARIMA or Prophet. Intermittent categories: LightGBM. Benchmark against simple linear model to avoid overfitting (Song et al., 2025).

---

### Module 3: Intelligent Budget Recommendation

**Best optimization methods:** Goal programming (preemptive priority + weighted deviation) balances conflicting objectives with near‑zero deviation – ideal for protecting non‑negotiable categories (Aboud, 2025). Linear programming with user‑defined category weights maximises savings under constraints (de Zarzà et al., 2024). SQP converges in under 100 iterations (mobile‑real‑time); GA requires 500 generations for global robustness (Gulbakyt et al., 2025).

**Learning‑based methods:** Fuzzy K‑means + neural collaborative filtering achieves Precision@5 = 0.85, adapting in real time (Yang, 2024). Contextual bandit / RL achieved 41% adoption rate for personalised suggestions (Bhavana et al., 2025).

**Constraint‑aware design:** Hill saturation functions model diminishing returns – excess budget in a category yields lower marginal value (Lu et al., 2025). Monte Carlo simulation reports confidence intervals for constraint satisfaction.

**Explanation trade‑off (critical):** Axiom‑based explanations improve understanding in 72.4% of users and perceived fairness in 30%, but **decrease trust in 23%** (Hashemi et al., 2024). **Make explanations optional and measure trust impact.**

**Evidence‑based recommendation:** Goal programming or SQP for deterministic, constraint‑based allocation with minimum floors for essential/protected categories. Add neural collaborative filtering or context bandit as data accrues. Provide optional, simple explanations.

---

### Module 4: Anomaly Detection

**Best unsupervised method:** Isolation Forest is preferred for PFMS because it operates without labeled data, scales O(n log n) (mobile‑feasible), assumes anomalies are rare and structurally distinct (D’Souza et al., 2026). Pre‑filtering captures 94% of anomalies while reducing data volume by 76% (Martínez et al., 2025). Bhavana et al. (2025) report 95% accuracy with Isolation Forest + Autoencoders.

**Deep learning alternatives:** LSTM‑based prediction error (LSTM‑NDT) uses non‑parametric dynamic thresholding – integrates with forecasting module (Boniol et al., 2024). Reconstruction methods (VAE, AE, GAN) offer entity‑level explanation at higher cost (Wang et al., 2025).

**Best ensemble (deployment):** Rule‑based screening + Isolation Forest + LSTM autoencoder achieves 91.7% sensitivity and 3.8% false positive rate on personal transaction streams, with on‑device latency 43–127ms (Jayaprakashnarayan et al., 2026).

**Evaluation metrics:** VUS‑ROC recommended for time‑series anomaly detection (robust to label noise) (Boniol et al., 2024). AUC‑PR (not AUC‑ROC) for imbalanced rare‑event data (Martínez et al., 2025; George et al., 2023).

**Critical cultural gap:** Existing methods treat all distributional outliers as anomalies – they will flag culturally obligated spending spikes (Christmas, fiesta, *paluwagan*, family remittances) as false positives. **No algorithm in the literature addresses this.** Must implement a **cultural‑calendar override** or **user‑confirmed exemption categories**.

**Evidence‑based recommendation:** Primary: Isolation Forest. Secondary: LSTM prediction error. Deployment: ensemble (rule‑based + Isolation Forest + optional LSTM AE). **Add cultural‑calendar pre‑filter** to suppress false positives on legitimate seasonal/obligation spikes.

---

## Part III: Evaluation Framework (What the Literature Demands)

| Dimension | Method / Metric | Precedent / Source |
|-----------|----------------|---------------------|
| Forecasting accuracy | MAPE, RMSE, walk‑forward validation | Kara & Şengüler (2025); Pagliaro (2025) |
| Anomaly detection | VUS‑ROC or AUC‑PR | Boniol et al. (2024); Martínez et al. (2025) |
| Classification (profiling) | AUC‑ROC, Precision@K | Martínez et al. (2025); Yang (2024) |
| Usability | System Usability Scale (SUS) | Imawan et al. (2025) – 4.6/5 with 50 users |
| Software quality | ISO/IEC 25010 (functional suitability, performance, security, etc.) | Bhavana et al. (2025); Al‑E'mari et al. (2025) |
| Sample size | 50 users (minimum for early‑stage PFMS) | Imawan et al. (2025); Yadav et al. (2025) |
| Trust impact of explanations | Measure before/after; separate from SUS/Hashemi protocol | Hashemi et al. (2024) |

**Missing from literature:** No study applies ISO 25010 and SUS jointly to a PFMS with multiple intelligent ML modules in a Philippine mobile deployment context. Odin’s evaluation plan directly addresses this gap.

---

## Part IV: Summary Table – Algorithms, Metrics, Constraints

| Module | Primary Algorithm | Fallback / Cold‑Start | Evaluation Metric | Key Filipino‑Specific Constraint |
|--------|------------------|----------------------|-------------------|----------------------------------|
| User Profile Classification | XGBoost / LightGBM | Fuzzy K‑means + human‑in‑the‑loop | AUC‑ROC | Include marital status, goal commitment, observed transaction behavior |
| Spending Forecasting | LSTM (≥3 months) | ARIMA / Prophet (<2k transactions); LightGBM (intermittent) | MAPE, RMSE, walk‑forward | Semi‑monthly pay cycles, seasonal spikes |
| Budget Recommendation | Goal programming or SQP | Neural collaborative filtering (after >500 interactions) | Precision@5, adoption rate | Protect culturally obligated categories (floors, not variables) |
| Anomaly Detection | Isolation Forest | LSTM prediction error; ensemble (Isolation Forest + rule‑based) | VUS‑ROC, AUC‑PR, sensitivity | **Must add cultural‑calendar override** to avoid false positives |

---

## Part V: The Central Evidence Gap (What Odin Must Contribute)

No system reviewed in the 70+ papers has been:

1. **Validated on Filipino young professional spending data** (manual transaction entry, not bank APIs)
2. **Grounded in FIES/PCOICOP categories** extended with culturally protected categories (*paluwagan*, *utang na loob*, remittances)
3. **Evaluated with walk‑forward validation** on time‑series forecasting in a mobile‑first PFMS context
4. **Designed to distinguish culturally obligated spending spikes** from genuine budget overages

Odin’s development – combining XGBoost profiling, LSTM forecasting with ARIMA fallback, goal‑programming budget recommendation, Isolation Forest anomaly detection with cultural‑calendar override, and ISO 25010 + SUS evaluation on a 50‑user Filipino sample – directly addresses every gap identified in the literature.

---

*End of evidence‑based synthesis*