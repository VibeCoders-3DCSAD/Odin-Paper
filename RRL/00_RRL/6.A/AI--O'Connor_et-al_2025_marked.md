Review
A Review of Electricity Price Forecasting Models in the
Day-Ahead, Intra-Day, and Balancing Markets

Ciaran O’Connor 1,*

, Mohamed Bahloul 2, Steven Prestwich 3,* and Andrea Visentin 3

1

SFI CRT in Artificial Intelligence, School of Computer Science & IT, University College Cork,
T12 YN60 Cork, Ireland

2 Water & Energy Transition Unit, Vlaamse Instelling voor Technologisch Onderzoek,

3

2400 Mol, Belgium; mohamed.bahloul@vito.be
Insight Centre for Data Analytics, School of Computer Science & IT, University College Cork,
T12 YN60 Cork, Ireland; andrea.visentin@ucc.ie

* Correspondence: 119226305@umail.ucc.ie (C.O.); s.prestwich@cs.ucc.ie (S.P.)

Abstract: Electricity price forecasting plays a fundamental role in ensuring efficient market
operation and informed decision making. With the growing integration of renewable
energy, prices have become more volatile and difficult to predict, increasing the necessity
of accurate forecasting in bidding, scheduling, and risk management. This paper provides
a comprehensive review of point forecasting models for electricity markets, covering
classical statistical approaches both with and without exogenous inputs, and modern
machine learning and deep learning techniques, including ensemble methods and hybrid
architectures. Unlike standard reviews focused solely on the day-ahead market, we assess
model performance across day-ahead, intra-day, and balancing markets, with each posing
unique challenges due to differences in time resolution, data availability, and market
structure. Through this market-specific lens, the paper merges insights from a broad set
of studies; identifies persistent challenges, such as data quality, model interpretability,
and generalisability; and outlines promising directions for future research. Our findings
highlight the strong performance of hybrid and ensemble models in the day-ahead market,
the dominance of recurrent neural networks in the intra-day market, and the relative
effectiveness of simpler statistical models such as LEAR in the balancing market, where
volatility and data sparsity remain critical challenges.

Keywords: electricity price forecasting; day-ahead market; intra-day market; balancing
market; machine learning; deep learning; hybrid models

1. Introduction

Electricity price forecasting (EPF) plays a fundamental role in energy markets, enabling
market participants to optimise trading strategies, mitigate financial risks, and maintain
grid stability. However, forecasting with accuracy has become increasingly difficult due to
the rapid expansion of renewable energy sources such as wind, solar, and hydroelectric
power. This challenge is especially evident in real-time markets such as the intra-day
market (IDM) and balancing market (BM), where forecast errors in renewables require real-
time corrections [1]. While policy incentives, declining technology costs, and regulatory
mechanisms like feed-in tariffs have accelerated renewable adoption [2,3], these energy
sources introduce significant variability and uncertainty into electricity markets. Unlike
traditional commodities, electricity cannot be stored efficiently, requiring real-time balanc-
ing of supply and demand. As a result, short-term price fluctuations are highly sensitive to

Academic Editors: Sebastijan Seme

and Klemen Sredenšek

Received: 30 May 2025

Revised: 7 June 2025

Accepted: 10 June 2025

Published: 12 June 2025

Citation: O’Connor, C.; Bahloul, M.;

Prestwich, S.; Visentin, A. A Review of

Electricity Price Forecasting Models in

the Day-Ahead, Intra-Day, and

Balancing Markets. Energies 2025, 18,

3097. https://doi.org/10.3390/

en18123097

Correction Statement: This article

has been republished with a minor

change. The change does not affect

the scientific content of the article and

further details are available within the

backmatter of the website version of

this article.

Copyright: © 2025 by the authors.

Licensee MDPI, Basel, Switzerland.

This article is an open access article

distributed under the terms and

conditions of the Creative Commons

Attribution (CC BY) license

(https://creativecommons.org/

licenses/by/4.0/).

Energies 2025, 18, 3097

https://doi.org/10.3390/en18123097

Energies 2025, 18, 3097

2 of 40

renewable generation forecasts, regulatory interventions, and unforeseen disruptions such
as generator outages or transmission constraints. These complexities make EPF particularly
challenging, as prices exhibit high volatility, non-linearity, and sudden spikes.

1.1. Point Forecasting Methods

EPF approaches can be broadly divided into point forecasts and probabilistic fore-
casts. Point forecasts generate single-valued predictions that are easy to interpret and
support parsimonious predictor–target relationships, typically under the assumption of
homoscedasticity. Historically, point forecasting has been dominated by statistical mod-
els due to their interpretability and ability to capture temporal dependencies. Classical
methods include autoregressive (AR) models, both without and with exogenous inputs
(ARX), which have been extended to autoregressive integrated moving average (ARIMA)
and its variants with seasonality (SARIMA) and exogenous inputs (ARIMAX). To account
for volatility, these are often paired with Generalised AR Conditional Heteroscedasticity
(GARCH) models, which model time-varying variance within a linear framework. More
recent developments incorporate regularisation techniques to improve generalisation in
high-dimensional settings. The Least Absolute Shrinkage and Selection Operator (LASSO)
utilises l1 regularisation to enhance linear regression, while the Lasso-Estimated AR (LEAR)
model extends AR frameworks using elastic nets to apply both l1 and l2 regularisation.
Although these methods remain widely used, they often struggle to capture the non-
linearities, regime shifts, and extreme price fluctuations that typify modern electricity
markets—particularly those with high renewable energy penetration [4].

To overcome the limitations of traditional statistical models, machine learning (ML)
and deep learning (DL) techniques have gained prominence in EPF, offering greater flexi-
bility for modelling complex, non-linear relationships. ML approaches such as Support
Vector Machine (SVM), Random Forest (RF), and gradient boosting algorithms (e.g., XGB,
LGBM) have shown strong performance in uncovering intricate patterns within market
data [5–7]. DL models, particularly recurrent neural networks (RNNs), have been widely
adopted in the day-ahead market (DAM) due to their ability to learn hierarchical feature
representations and capture temporal dependencies [8,9]. Despite their predictive power,
these models often require large datasets, entail significant computational costs, and are
prone to overfitting. In response, hybrid approaches that combine statistical, ML, and DL
components have gained traction, aiming to exploit the strengths of each paradigm. These
integrated models offer a promising path forward, balancing interpretability, computa-
tional cost, and accuracy to improve forecasting performance in increasingly volatile and
data-rich electricity markets.

1.2. Related Work and Literature Gap

EPF has been extensively studied, with early research focusing primarily on statistical
techniques within the DAM. The foundational reviews in [10,11] established the dominance
of statistical models, which remained the standard for over a decade. However, these
works predate the widespread adoption of ML, DL, and hybrid approaches that integrate
non-linear and data-driven techniques to further improve forecasting accuracy. More
recent surveys have updated the literature to reflect the growing use of ML and DL in
EPF [4,12–14]; yet a critical gap remains: most reviews continue to focus almost exclusively
on the DAM, neglecting the increasingly important IDM and BM.

These real-time markets pose unique challenges due to higher temporal resolution
and greater sensitivity to renewable energy fluctuations, making accurate forecasting
essential for managing supply–demand imbalances in systems with increasing renewable
penetration. Given the rapid evolution of forecasting methodologies and the growing

Energies 2025, 18, 3097

3 of 40

importance of the IDM and BM, there is a growing need for a comprehensive, cross-
market review. This paper addresses this gap by examining the progression from classical
statistical models to modern ML-based techniques across all three short-term markets. By
analysing emerging methodologies and distinct forecasting challenges in the DAM, IDM,
and BM, we aim to provide researchers and practitioners with a timely and structured
resource for navigating the evolving EPF landscape. The key novelty of this work lies
in its comprehensive, methodologically structured review of point forecasting models
across all three major short-term electricity markets—day-ahead, intra-day, and balancing—
highlighting how model performance and suitability vary with market structure, data
requirements, and volatility characteristics.

The structure of this paper is as follows: Section 2 provides a background of electricity
spot markets, the DAM, IDM, and BM. In Section 3, we provide an overview of statistical,
ML, DL, and hybrid models utilised in EPF. The key findings for predictive models in each
spot market are discussed in Section 4. Finally, Section 5 summarises our findings.

2. Background: Electricity Market Structure

EPF is highly dependent on market structure, as different electricity markets operate
on distinct time frames (see Figure 1) and temporal granularity, and exhibit varying levels of
price volatility. The financial instruments shown in Figure 1, including forwards, capacity
markets, and financial transmission rights, are described in more detail in Section 2.4.
Short-term electricity markets, including the DAM, IDM, and BM, play a crucial role in
electricity trading, each introducing unique forecasting challenges due to differences in
market mechanisms, trading frequency, and reliance on real-time data. Understanding these
market structures is essential for selecting appropriate forecasting models, as methodologies
must be tailored to each market’s unique characteristics. This section provides an overview
of short-term electricity markets, highlighting their structural differences and the specific
forecasting difficulties they present.

Financial

Forwards/
Capacity/
FTR

Physical

Day-Ahead

Intraday

Balancing

Dispatch

Years

Months

Weeks

Days

Hours

Minutes

Seconds

Real-time

Figure 1. Temporal granularity for each of the relevant markets.

2.1. Day-Ahead Market

The DAM functions as a forward scheduling mechanism in which participants commit
to electricity trades one day prior to delivery. Prices and trading volumes are determined
through market-clearing auctions based on forecasted supply and demand, typically using
optimisation algorithms such as EUPHEMIA in European markets [15,16]. While the DAM
displays more stable prices compared to real-time markets, forecasting remains challenging
due to the increasing penetration of renewable energy sources, particularly wind and solar.
These sources introduce volatility, as their generation depends on weather conditions,
complicating both supply and demand forecasts [17].

Energies 2025, 18, 3097

4 of 40

Early DAM forecasting methods relied on statistical time-series models, due to their
ability to capture temporal dependencies. However, these models struggle with non-linear
price dynamics and sudden regime shifts. ML and DL approaches have since demonstrated
strong performance by capturing complex, non-linear relationships within market data.
Techniques such as XGB and LSTM, and hybrid models such as LEAR-DNN, have proven
to be stand out performers, improving forecasting accuracy by incorporating multiple
influencing factors, including weather conditions, fuel prices, and demand trends [4,18–21].

2.2. Intra-Day Market

The IDM facilitates continuous trading, allowing market participants to adjust their
positions in response to real-time fluctuations in supply and demand. Unlike the DAM,
where trades are scheduled a day in advance, the IDM operates on shorter time frames,
with transactions occurring from a few hours up to 30 min before delivery. This high-
frequency trading environment is particularly sensitive to renewable generation variability,
unexpected outages, and shifting demand patterns, making accurate forecasting increas-
ingly important [22]. Forecasting in the IDM presents unique challenges due to the need
for real-time adaptation to evolving market conditions. Traditional statistical models,
while effective for longer time horizons, struggle to capture the higher-frequency, non-
stationary nature of IDM price dynamics. In line with the DAM, ML and DL approaches
have demonstrated strong performance in processing large datasets, detecting intricate
patterns, and effectively incorporating high-resolution temporal data [23–26]. These models
integrate diverse real-time data sources, enabling more precise short-term price predictions
in high-frequency trading environments, while hybrid approaches that combine statistical
and ML-based techniques are being increasingly explored to improve predictive accuracy,
model interpretability, and real-time bidding strategy optimisation [26–28].

2.3. Balancing Market

The BM operates in real time, ensuring that electricity supply matches actual system
demand. Unlike the DAM and IDM, where trades are scheduled in advance, the BM
responds to last-minute supply–demand imbalances, renewable energy fluctuations, and
generator outages, making it the most volatile market [1,29]. Operating on extremely short
time horizons (5 min), BM EPF is particularly challenging, as BM prices must reflect rapid
corrective actions taken by the transmission system operator [30]. While ML and DL models
have demonstrated strong forecasting performance in the DAM, and to a lesser extent in
the IDM, simpler statistical approaches have proven more effective for BM forecasting due
to their ability to handle sharp price spikes without overfitting [31,32]. In contrast, ML and
DL models, which excel in capturing complex patterns, often struggle with overfitting, and
have difficulty modelling high-frequency fluctuations and sudden regime shifts. To address
these limitations, hybrid approaches utilising statistical and ML models are being explored,
while real-time data integration, incorporating weather conditions, grid frequency, and
system constraints, remains a key focus for improving BM EPF [33,34].

Figure 2 illustrates the aligned trading timelines for the day-ahead, intra-day, and

balancing markets, including typical submission times and trading intervals.

Energies 2025, 18, 3097

5 of 40

12:00 Submission | 14:00 Prices Published

DAM

DAM Trading: 24 Hourly Intervals 00:00-00:00

12:00 14:00

00:00

Submission typically 5–60 mins before delivery | Prices published in real-time

IDM

BM

IDM Trading: Rolling 15–60 min periods

08:00
Submission typically 1–15 mins before delivery | Prices published in real-time

16:00

00:00

BM Trading: 5–15 min intervals

00:00

08:00

16:00

.
00:00

.
00:00

.
00:00

Figure 2. Aligned DAM, IDM, and BM trading timelines, with submission and trading details.
Created by the authors based on SEMOpx documentation and European market rules [35,36].

2.4. Other Electricity Markets

In addition to the DAM, IDM, and BM, several other markets play fundamental
roles in the overall trading of electricity. An overview of these markets and their unique
characteristics is provided below:

•

•

•

•

Forward market: Allows participants to hedge positions in DAM, IDM, and BM through
contracts-for-difference [37]. Contracts-for-difference enable participants to lock in a
strike price, providing protection against price volatility. Forecasting in this market
requires predicting long-term price trends and movements.
Ancillary markets: Support the power grid’s stability and reliability through services
like frequency regulation, spinning reserve, voltage control, and black start capabilities.
Accurate forecasting in ancillary markets ensures the availability of resources needed
to maintain grid stability. This involves sophisticated models considering real-time
operational data and dynamic supply and demand conditions [38].
Capacity market: Ensures sufficient generation capacity to meet peak demand. Ca-
pacity providers receive payments for committing to supply electricity or reduce
demand during peak periods, incentivising investment in new capacity [39]. Fore-
casting in the capacity market involves predicting peak demand periods and capacity
resource availability.
Financial transmission rights auctions: Manage congestion costs and provide financial
hedges against price differences across market zones. Financial transmission rights
entitle holders to payments based on price differences between locations. Forecasting
in this market involves predicting congestion patterns and price differentials, requiring
an understanding of grid operations and transmission constraints [40].

While the forward, ancillary, and capacity markets are integral to the broader func-
tioning of the electricity system, this review focuses exclusively on the DAM, IDM, and BM
due to their direct relevance to short-term price volatility, renewable integration challenges,
and real-time trading dynamics. Markets oriented toward long-term hedging, such as the
forward market and financial transmission rights auctions, are excluded, as their longer
time horizons and distinct pricing mechanisms fall outside the primary scope of this study.

Energies 2025, 18, 3097

6 of 40

3. Predictive Models

Accurate EPF requires models that can effectively capture diverse market dynamics,
accommodate high volatility, and adjust to real-time conditions. In this section, we review
key predictive models, including statistical, ML, DL, and hybrid approaches, highlighting
their application and suitability across each spot market. We begin by discussing statistical
models, distinguishing between those that rely solely on historical price data and those
that incorporate exogenous inputs. In contrast, ML and DL techniques are evaluated for
their strength in modelling complex, non-linear relationships inherent in volatile markets.
Drawing on insights from previous reviews [4,10–14,19], we assess the strengths and
limitations of these methods while extending the focus beyond the DAM to real-time
markets, namely, the IDM and BM, where forecasting challenges are amplified by shorter
decision windows and greater volatility.

3.1. Statistical Methods Without Exogenous Inputs

Statistical models that rely solely on historical price data are widely used in EPF to
identify underlying patterns such as trends, seasonality, and autocorrelation. Common tech-
niques include AR, ARIMA, GARCH, as well as simpler approaches like naive models and
exponential smoothing (ES). These methods have traditionally performed well in relatively
stable markets such as the DAM, where price dynamics tend to be more predictable [19,41].
However, in more volatile environments like the IDM and BM, where price shocks and
non-linear behaviours are frequent, these models often struggle to maintain forecasting
accuracy [31,32,42,43]. In this subsection, we review both simple and advanced statistical
methods without exogenous inputs, highlighting their applicability and limitations across
different market conditions.

3.1.1. Autoregressive Model

The AR model is a foundational time-series forecasting technique where the dependent
variable is regressed against its own lagged values, assuming a linear relationship. An AR
model of order p, denoted AR(p), expresses the current value yt as a linear combination of
its p previous values, denoted as

yt = ϕ0 +

p
∑
i=1

ϕiyt−i + ϵt,

(1)

where ϕ0 is an intercept term, ϕi are AR coefficients, and ϵt is white noise. AR models are
suitable for stationary time series which exhibit a constant mean and variance over time,
and serve as a building block for more complex models like ARMA and ARIMA.

AR models are particularly adept at capturing mean-reversion behaviour, a common
characteristic in electricity prices. However, in practice, simple AR models often struggle to
handle sudden volatility and price shocks, as evidenced by studies in the Indian DAM [44].
To address these limitations, combining AR with volatility models such as GARCH has
proven effective in enhancing accuracy in more turbulent settings. While the simplicity
of AR models makes them valuable baselines [45], they are frequently outperformed by
advanced methods, such as DL models like NBEATSx, that are better equipped to model
non-linear price dynamics. Moreover, evidence from Italy’s DAM suggests that incorpo-
rating external factors via extensions like ARX, in tandem with GARCH, is considerably
beneficial for improved forecast performance [46]. In the IDM, AR models demonstrate
limited forecasting accuracy due to their inability to capture time-varying cross-hour depen-
dencies [47], but their performance improves significantly when extended with exogenous
variables or hybrid approaches [48]. Their performance in the IDM is further improved with
regularisation and exogenous variables, often outperforming more complex models [49].

Energies 2025, 18, 3097

7 of 40

In the BM, AR models remain relatively underexplored, with moderately strong perfor-
mance, albeit in a short 3-month test period [43]. Overall, we see a trend of AR models
underperforming compared to more complex models which utilise exogenous outputs.

3.1.2. Autoregressive Integrated Moving Average Model

The ARIMA model is a widely used time-series forecasting approach that combines
three components: the AR term captures temporal dependencies, as outlined in Equation (1);
the integrated (I) component achieves stationarity through differencing, ∇dyt = (1 −
B)dyt, to remove trends and ensure constant statistical properties; and the moving average
(MA) term models the impact of past forecast errors, yt = θ0 + ϵt + ∑q
j=1 θjϵt−j, where ϵt
denotes white noise. These components are unified into the ARIMA framework, denoted
ARIMA(p, d, q), and expressed compactly as

ϕp(B)∇dyt = θq(B)ϵt,

(2)

where ϕp(B) and θq(B) are polynomials in the backshift operator B. ARIMA has been
widely applied in EPF in the DAM, proving effective in handling non-stationary behaviour—
such as non-constant mean, variance, and seasonality—as demonstrated in markets like
Spain and California [50]. However, its fundamentally linear structure limits its ability
to capture non-linear dynamics, such as abrupt price spikes and regime shifts [51]. To
overcome these shortcomings, hybrid approaches, such as integrating wavelet transforms
with ARIMA, have been proposed to better manage volatility [52]. Despite these enhance-
ments, ARIMA models tend to excel only in linear settings and often require additional
techniques to handle complex non-linear patterns effectively [5]. Recent studies have high-
lighted ARIMA’s limitations when compared to advanced models like graph convolutional
networks, which can more effectively capture spatial dependencies and intricate non-linear
relationships, especially for short-term locational marginal price forecasting [53]. Moreover,
incorporating GARCH-type specifications into ARIMA frameworks has been shown to
improve forecast accuracy in the DAM, particularly for generating reliable density fore-
casts [44,46]. In the German IDM, ARIMA models perform well for daily average price
forecasting when applied to deseasonalised data, though their accuracy is largely depen-
dent on seasonal adjustments rather than the model’s inherent predictive strength [54]. The
incorporation of a seasonal component with SARIMA displays improved performance,
proving more capable at capturing intra-day price patterns, but its performance remains
limited in highly volatile trading periods, where more adaptive models like XGB and LSTM
demonstrate superior accuracy [55]. Beyond both the DAM and IDM, ARIMA struggles to
capture the real-time dynamics and extreme volatility characteristic of the BM [42], though
definitive conclusions are limited by short evaluation periods and the use of the mean
absolute percentage error (MAPE), which is unsuitable when prices are frequently close to
zero. Furthermore, in the Irish BM we see ARIMA outperformed by both more complex
ML and DL models, as well as the statistical model LEAR, across multiple metrics [32].
Overall, ARIMA struggles in all three spot markets, with particularly poor performance in
real-time markets, where models with exogenous inputs continue to standout.

3.1.3. Generalised Autoregressive Conditional Heteroscedasticity Model

The GARCH model is utilised in EPF to model time-varying volatility, capturing
volatility clustering by allowing the conditional variance to depend on past squared resid-
uals and variances, unlike standard time-series models that assume constant variance.
In a GARCH (p, q) model, the time series yt is typically assumed to follow yt = µt + ϵt,
where ϵt = σtzt, zt ∼ N (0, 1), and the conditional variance σ2
t evolves according to

Energies 2025, 18, 3097

8 of 40

t = α0 + ∑p
σ2
shocks, and βj models the persistence of volatility.

t−i + ∑q

j=1 βjσ2

i=1 αiϵ2

t−j. Here, α0 is a constant, αi captures the impact of lagged

GARCH models have been widely used to model volatility in deregulated electricity
markets [44,56]. Extensions such as the k-factor GIGARCH model, which incorporates long
memory and stochastic volatility, have demonstrated improved forecasting accuracy in
markets like the German DAM [57]. Enhanced versions, including EGARCH and TGARCH,
integrate additional market drivers, such as demand fluctuations and renewable energy
inputs, to better capture volatility clustering and asymmetry [46]. Moreover, recent studies
have shown that GARCH-t models coupled with LASSO feature selection can effectively
manage heteroscedasticity and, in some cases, even outperform certain ML approaches in
New Zealand’s DAM [58]. GARCH models, when applied in isolation, often underperform
in EPF due to their limited ability to capture complex market dynamics, and while their
use in the IDM and BM remains underexplored, their limitations in the DAM suggest they
are unlikely to perform well in more volatile real-time markets without integration with
AR-type or ML/DL methods.

3.1.4. Exponential Smoothing Model

ES is a simple yet effective forecasting method that assigns exponentially decreasing
weights to past observations, allowing recent data to have more influence on the forecast.
Variants like Holt’s linear method introduce a trend component, and Holt–Winters extends
this to incorporate seasonality, either additively or multiplicatively. More advanced ver-
sions, such as TBATS and ES-Transformers, further enhance performance by incorporating
trigonometric seasonality, Box–Cox transformations, and ARMA error structures.

Holt’s ES has demonstrated strong accuracy in forecasting residential electricity con-
sumption, often achieving a lower MAPE compared to alternative methods [59]. Building
on this foundation, recent innovations to ES incorporate Transformer architectures to en-
hance both long- and short-term forecasting performance [60]. Meanwhile, the TBATS
model extends traditional ES by integrating features like trigonometric seasonality and
ARMA error components, which has led to improved performance in contexts such as
Denmark’s DAM and photovoltaic system data [61,62]. However, TBATS can struggle in
scenarios lacking external regressors, ending up being outperformed by RNN models, more
suited to non-linear settings [63]. Hybrid models that combine ES with additional smooth-
ing and trend techniques, such as SVR-CDSES and Functional ARX (FARX), have also been
explored to improve long-term forecasts for energy demand and electricity prices [64,65].
Nonetheless, when applied to volatile markets like the BM, traditional ES methods fall short
in capturing rapid price fluctuations, echoing similar limitations observed with ARIMA
models [42]. Overall, ES is a simple and interpretable model, but it performs poorly in
the BM and, while its application in the IDM remains unexplored, its limited adaptability
suggests similarly weak performance in more volatile real-time markets.

3.1.5. Naive Model

A naive model serves as a simple baseline for EPF, typically using the previous t hours
of prices to forecast the next t hours or, in seasonal variants, replicate the price from the
corresponding period in the previous cycle. Common variants include a random walk
approach, where the most recent price is used as the next prediction, and seasonal naive
models, which assume that price patterns repeat at fixed intervals (e.g., daily or weekly
cycles). However, the definition of a naive model varies across studies, often dictated by the
specific market structure, or they are used as a benchmark to evaluate the performance of
more complex models. Despite their simplicity, naive models have proven effective in vari-
ous markets, such as the Lithuanian DAM, where a seasonal naive approach worked well

Energies 2025, 18, 3097

9 of 40

for seasonal patterns [66]. Naive models remain a widely used benchmark in the IDM, often
performing competitively despite their simplicity. In more volatile conditions, augmenting
them with LASSO has significantly improved accuracy [67]. Some implementations rely on
the most recent price of the corresponding hourly product, demonstrating strong perfor-
mance and often rivalling more complex statistical methods [68]. In trading applications,
they have shown economic value as a competitive baseline [69]. When leveraging DAM
prices as predictors, naive models remain a strong reference, though they are typically
outperformed by LASSO and ARX [25]. While they perform well under stable conditions,
they struggle with sudden price fluctuations and intra-day market volatility [48]. Despite
exhibiting significant forecasting errors for daily average and hourly prices, they accurately
capture general market behaviour in stable periods [54]. Additionally, in the continuous
trading regime, expert linear models show only marginal improvements over naive bench-
marks, reinforcing their relevance in real-time markets [70]. In the more real-time BM,
naive models remain a valuable baseline, especially for quick approximations, though
they are less accurate than models like ARIMA or LEAR [31,32]. A naive baseline remains
a popular choice in real-time markets due to their ability to quickly adapt to short-term
price fluctuations and leverage strong autocorrelations in high-frequency data, providing a
simple benchmark for evaluating more complex models.

3.2. Statistical Methods with Exogenous Inputs

Statistical models with exogenous inputs extend time-series models by incorporating
external predictors. Models such as ARX, ARIMAX, their variants FARX and SARIMAX,
along with transfer function (TF) and copula models, leverage additional information, such
as renewable generation, demand forecasts, and fuel prices, to improve accuracy.

3.2.1. ARX-Type Models

ARX models extend the traditional AR-based models from Section 3.1.1 by incorporat-
ing exogenous inputs to account for external factors influencing electricity prices. An ARX
model of order p, denoted ARX(p), expresses the current value yt as a linear combination
of its p previous values and q exogenous inputs xt, as follows:

yt = ϕ0 +

p
∑
i=1

ϕiyt−i +

q
∑
j=1

θjxt−j + ϵt,

(3)

where ϕ0 is an intercept term, ϕi represents AR coefficients, θj represents the coefficients
for the exogenous inputs xt−j, and ϵt is the error term. The FARX model introduces non-
parametric terms, allowing it to model complex, non-linear interactions between variables.
Incorporating exogenous variables like demand and fuel prices improves ARX models’
accuracy in DAM [46], while FARX models further reduce errors by integrating weather
data [65]. However, ML models generally outperform ARX in capturing complex price
dynamics [19]. ARX models have been effectively applied in the IDM, demonstrating
strong performance in forecasting price spreads and predicting the direction of price
changes, providing economic value in electricity trading [71]. However, their accuracy
can be improved by incorporating regularisation techniques such as LASSO, which help
mitigate overfitting in high-dimensional settings [25]. ARX models have also been explored
for predicting whether intra-day prices will exceed day-ahead prices, though they can
be outperformed by other linear models such as LASSO or elastic net in forecasting IDM
index values [72]. Further improvements have been demonstrated when ARX models
are combined with regularisation techniques to refine parameter selection and improve
predictive stability [73]. In the BM, as for AR models we see little attention on the use of
ARX models. Regarding the current literature, ARX models perform moderately well [43],

Energies 2025, 18, 3097

10 of 40

albeit with a short test period and unsuitably chosen MAPE metric. Overall, ARX models
improve upon AR models by incorporating exogenous inputs, particularly benefiting IDM
forecasting, where demand shifts and fuel prices influence prices. While they enhance
accuracy across markets, their edge is less pronounced in DAM, where ML and DL models
excel, and in BM, where gains over simpler methods are marginal.

3.2.2. ARIMAX Model

Like ARX, the ARIMAX model extends the ARX with the differenced (I) and MA
terms from the ARIMA model in Section 3.1.2. This can be further extended with the addi-
tion of seasonal components with SARIMAX, making it ideal for markets with recurring
seasonal patterns.

ARIMAX’s incorporation of exogenous variables, like demand and renewable energy,
results in improved accuracy over ARIMA [46]. The further use of seasonality in SARIMAX
models further improves their predictive power, especially in markets with strong seasonal
patterns like the Leipzig Power Exchange and European Power Exchange [74], as well as
Denmark’s DAM [61]. SARIMAX models perform well in capturing external factors but
are often outperformed by advanced models like LSTM during market volatility [75,76].
In the IDM, SARIMAX models demonstrated consistent and reliable performance for EPF,
outperforming DL approaches and effectively capturing extreme price fluctuation [72].
Though unexplored in the BM, ARIMAX and its variants are likely to outperform ARIMA
and AR models due to their ability to incorporate exogenous variables, a feature that has
contributed to their success in the DAM and IDM.

3.2.3. LASSO Models

LASSO is a linear regression technique that incorporates L1 regularisation to enforce
sparsity by shrinking some coefficients to exactly zero. This makes it well suited for
high-dimensional forecasting problems, such as EPF, where variable selection and model
interpretability are important. The LASSO estimate ˆβ is obtained by minimising the
penalised least squares objective:

ˆβ = arg min

β

(cid:32) T
∑
t=1

(yt − x⊤

t β)2 + λ

(cid:33)

|βj|

,

p
∑
j=1

(4)

where λ controls the degree of shrinkage.

LASSO performs well in the DAM but struggles with collinearity in highly correlated
data and is generally outperformed by bagging [48], as well as more complex ML and
DL models [77]. LASSO effectively captures the AR intra-day dependency structure of
electricity prices, providing strong forecasting performance while mitigating overfitting
through automatic parameter selection [47]. It consistently selects key explanatory vari-
ables, offering statistically robust insights into market dynamics and improving predictive
performance in continuous trading settings [25,78]. However, it struggles with collinear-
ity in highly correlated market data [48], where alternative regularisation methods like
Orthogonal Matching Pursuit show promise for improved stability [70]. While LASSO
balances complexity and accuracy when combined with bootstrap techniques for proba-
bilistic forecasting [79], it is often outperformed by more complex models like GRU and
LSTM, particularly when modelling spread values [68]. Additionally, it demonstrates
strong distributional fit but tends to underestimate volatility compared to neural network
(NN)-based approaches [80]. LASSO performs well in the DAM and IDM, but it struggles
with collinearity, volatility, and spread values, often being outperformed by bagging, ML,
and DL models, while in the BM, research remains focused on the LEAR model.

Energies 2025, 18, 3097

11 of 40

3.2.4. LEAR Models

The LEAR model, introduced as LASSO X in [81], combines AR with elastic net
regularisation, enabling automatic lag selection while handling multicollinearity among
predictors. Building on the AR structure outlined in Equation (1), where future values
are regressed on past lags, LEAR estimates the coefficients β by minimising the penalised
loss function:

ˆβ = argmin

β

(cid:32) T
∑
t=1

(yt − xtβ)2 + λ1

|βj| + λ2

β2
j

(5)

p
∑
j=1

(cid:33)

p
∑
j=1

Here, λ1 controls the L1 sparsity penalty, while λ2 introduces an L2 penalty from ridge
regression, enabling the model to retain correlated predictors while improving robustness.
LEAR remains a stand out performer in the DAM, and a standard baseline for new
proposed models, regardless of the proposed model being statistical, ML, DL, or a hy-
brid approach. In the DAM, LEAR displays strong performance, automating the variable
selection and handling of multicollinearity, leading to it outperforming traditional AR mod-
els [81]. Careful hyperparameter tuning is crucial for balancing complexity and preventing
overfitting, but regardless it has proved a strong performer against top DL architectures in
multiple markets [4]. LEAR excels in capturing distribution tails for risk management [82],
but combining it with other models like GARCH can further improve accuracy [58]. While
effective for probabilistic forecasting [83], LEAR is often outperformed by DL models in the
DAM [45,84,85]. In the BM, LEAR shows remarkable results, outperforming more complex
ML and DL models, which struggle with overfitting [32,86]. LEAR excels in the DAM as
a baseline model, while in the IDM, LASSO remains the preferred choice, with LEAR yet
to be tested. Despite outperforming traditional models, LEAR is often surpassed by DL
models in the DAM but outperforms more complex ML and DL approaches in the BM.

3.2.5. Transfer Function Model

The TF models the relationship between input variables and price changes, which
makes the TF model effective in markets with stable price dynamics and clear external
drivers. TF models capture relationships between prices and external variables, and have
been shown to improve EPF accuracy in Spain and California [87]. However, they struggle
with the high-frequency nature of hourly prices due to linear assumptions. Comparisons
show ML and DL models outperform TF models, highlighting the need for non-linear
approaches in EPF [19,88]. TF models remain untested in the IDM and BM but are unlikely
to perform well due to their volatility.

3.2.6. Copula Model

The copula model provides a flexible framework for capturing the dependence struc-
ture between multiple variables, without assuming a specific distribution. Copula models
effectively capture multivariate relationships in electricity markets, showing how renew-
able energy sources, especially wind, affect prices and volatility [89]. A DVINE copula
integrated into a spatio-temporal model enhances probabilistic forecasting by addressing
non-linear and non-stationary patterns, outperforming baseline models [90]. However,
like the TF model, the copula model remains untested in real-time markets, and its weak
performance in the DAM suggests it may struggle further.

3.3. Machine Learning Methods

ML models are increasingly utilised for EPF due to their ability to capture complex,
non-linear market dynamics without being limited by assumptions of stationarity. The
models discussed include K-Nearest Neighbors (KNN), Support Vector Regression (SVR),

Energies 2025, 18, 3097

12 of 40

RF, XGB, and LGBM. As electricity markets become more volatile, ML models are essential
for capturing non-linear patterns and adapting to rapid fluctuations in price dynamics.

3.3.1. K-Nearest Neighbours

KNN is a simple, non-parametric, instance-based learning algorithm. In the context of
EPF, KNN predicts the target value yt by identifying the k most similar past observations
in the feature space, typically using a distance metric such as Euclidean distance. For
real-valued feature vectors xt, xs ∈ Rd, this distance is defined as

d(xt, xs) =

(cid:118)
(cid:117)
(cid:117)
(cid:116)

d
∑
i=1

(xt,i − xs,i)2

(6)

To prevent features measured on different scales from dominating the distance computation,
normalisation to zero mean and unit variance is commonly applied. Once distances are
computed, the k nearest neighbours are selected, and the predicted value ˆyt is typically
the average of their observed values. The choice of k is critical: small values may lead to
overfitting, while large values can over-smooth the data, missing important local patterns.
In the DAM, KNN demonstrates mixed performance, with techniques like SVM
and principle component analysis (PCA) improving both accuracy and efficiency [91].
Feature selection methods [92,93] and the inclusion of meteorological data [94] further
enhance performance. Despite these improvements, KNN often underperforms compared
to advanced ensemble models like RF and XGB due to its sensitivity to neighbour selection
and distance metrics [77,86,95,96]. Its accuracy in predicting extreme price peaks can
be constrained by dataset imbalances [97]. In the IDM, KNN struggles with rapid price
fluctuations and high-frequency dynamics, underperforming against ensemble methods
like XGB and DL models [55]. In the BM, research is limited, but KNN’s challenges with
dataset imbalances remain [97]. Notably, it is outperformed by both more complex ML
models and simpler statistical approaches, with a performance gap that is less pronounced
in the DAM and IDM [32,86]. Overall, KNN’s instance-based approach lacks adaptability to
volatile, high-frequency markets, and it is consistently outperformed by ensemble methods.

3.3.2. Support Vector Regression

SVR aims to find a regression function f (xt) that predicts the target value yt within
a margin of tolerance ϵ, while maintaining model flatness and minimising prediction
error. This is achieved by minimising the norm ∥w∥2 of the weight vector w, subject to
constraints involving slack variables ξt and ξ∗
t that account for deviations beyond the
ϵ-insensitive tube. A regularisation parameter C balances the trade-off between model
complexity and tolerance to error, influencing the model’s ability to generalise. SVR
shows mixed performance across electricity markets and is generally outperformed in
the DAM by tree-based models such as RF and XGB, with studies in the Australian NEM
also reporting weaker results compared to NNs due to limited tunability and less efficient
optimisation [98]. However, hybrid approaches such as SOM-SVR and SVR-ARIMA have
shown improved handling of non-stationary behaviours [99,100], and radial basis function
(RBF) kernels have further enhanced accuracy [19]. Despite these enhancements, SVR still
struggles with extreme price spikes [9,101], though it performs competitively in locational
marginal price forecasting [102]. In the IDM, SVR achieves moderate accuracy but is often
outperformed by tree-based ensembles like XGB and DL models due to its limited ability
to adapt to high-frequency price fluctuations [55]. In the BM, SVR performs poorly, as
DL models with seasonal attention mechanisms capture extreme price fluctuations more
effectively [103]. A broader comparison of ML models highlights SVR’s limitations in

Energies 2025, 18, 3097

13 of 40

handling BM volatility, ranking it the weakest among top statistical and ML methods [32].
Overall, SVR’s performance declines from DAM to BM, with hybrid models improving
outcomes but still trailing ensemble and DL approaches in real-time markets.

3.3.3. Random Forest

RF is an ensemble learning algorithm that constructs multiple decision trees using
bootstrapped subsets of the training data and aggregates their predictions to improve accu-
racy and robustness. At each split, RF randomly selects a subset of features to determine
the best split, reducing correlation among trees and lowering variance. The final prediction
is computed as the average of the outputs from all N trees in the ensemble:

ˆyt =

1
N

N
∑
n=1

T(xt; Θn),

(7)

where T(xt; Θn) is the prediction from the n-th tree with parameters Θn.

RF demonstrates strong performance across the DAM, IDM, and BM, as well as in
broader energy demand forecasting applications [64]. Its ability to handle multi-output
tasks regarding prices and demand was demonstrated in the Spanish DAM [104]. RF
effectively captures intricate market dynamics, surpassing traditional statistical models and
remaining competitive against state-of-the-art ML methods [19,105]. Unlike models such
as SVR, which struggle with overfitting, RF benefits from its ensemble structure, which
reduces variance and improves generalisation. Online adaptive variants of RF address
concept drift, a key challenge in EPF, by adjusting to evolving market conditions and
improving real-time forecasting accuracy [95]. Additionally, hybrid RF models integrating
DL components further enhance prediction performance by refining feature extraction
and reducing forecasting errors, as demonstrated in the Nord Pool DAM [106,107]. In the
IDM, RF maintains competitive accuracy when paired with feature selection techniques
but is typically outperformed by gradient boosting models (e.g., XGB, LGBM), which
better handle short-term market fluctuations and extreme price spikes [55]. While RF
remains a stable and interpretable model, its reliance on bagging rather than boosting
results in slightly weaker adaptability in highly volatile intra-day trading conditions. RF is
well suited for real-time data streams and financial decision making [108], though it trails
behind models like LEAR and XGB in point-based forecasting metrics [32,86]. However, RF
remains competitive in financial performance evaluations, often achieving lower trading
risk and more stable profit margins than highly sensitive DL models [109]. Additionally,
RF’s lower computational complexity compared to DNNs makes it a more accessible choice
for operational forecasting. RF remains a strong model across the DAM, IDM, and BM,
balancing accuracy, interpretability, and scalability. It delivers reliable mid-term forecasts in
the DAM, but in the IDM, it lags behind boosting methods in handling short-term volatility.
In the BM, RF offers consistent performance with lower computational cost, though XGB
and LGBM better capture extreme price fluctuations for EPF.

3.3.4. Gradient Boosting

Gradient boosting algorithms, like XGB and LGBM, are efficient, high-performance
algorithms that build ensembles of decision trees sequentially, with each new tree correcting
the residuals of previous predictions, with the objective function

Obj =

n
∑
t=1

L(yt, ˆyt) +

M
∑
m=1

Ω( fm),

(8)

Energies 2025, 18, 3097

14 of 40

where L(yt, ˆyt) is the loss function and Ω( fm) represents an elastic net to penalise model
+ η fm(xt), and the final
complexity. Predictions are updated iteratively as ˆy
output is the initial mean point forecast y0 plus the sum of all tree predictions:

(m)
t = ˆy

(m−1)
t

ˆyt = y0 +

M
∑
m=1

η fm(xt).

(9)

While XGB employs level-wise tree growth, LGBM introduces a leaf-wise growth strategy
and efficiency features such as Gradient-based One-Side Sampling (GOSS) and Exclusive
Feature Bundling (EFB), enabling scalability to large datasets.

In the DAM, XGB consistently outperforms models like ARIMA, KNN, and SVR,
especially when combined with feature selection techniques or integrated into hybrid
frameworks with deep neural networks (DNNs) [107,110], improving wind speed fore-
casting with historical data [111], and showing high accuracy in capturing key variables
like renewable energy penetration [107]. XGB’s optimised hyperparameters reduce errors
in load forecasting [112], and its robustness is validated in short-term EPF [113]. In the
Nord Pool DAM, XGB surpasses models like SVM and RF due to its efficient boosting
process [106]. LGBM also performs well, excelling in smart manufacturing [114] and wind
power forecasting [115], efficiently handling large datasets. XGB and LGBM also perform
well, efficiently handling large datasets and outperforming models like DNN in the Irish
DAM [32]. In the IDM, XGB shows mixed results, underperforming simpler regularised
models due to challenges with hyperparameter tuning and capturing intra-day dependen-
cies [49]. It performs competitively against the naive benchmark for daily average prices
but struggles with short-term price peaks [54]. LSTM models outperform XGB by capturing
short-term volatility more effectively [55]. In the BM, both XGB and LGBM perform more
consistently, excelling in the UK BM in bidding and risk management [116], though they are
occasionally outperformed by simpler models [58]. XGB benefits from incorporating key
market variables like net imbalance volume and loss of load probability, though it is often
surpassed by DL models in handling extreme price fluctuations, with LGBM performing
poorer than the other statistical, ML, and DL models [103]. In the Irish BM, both XGB and
LGBM excel, outperforming other ML and DL models [86,109,117], only coming up short to
LEAR [32]. Overall, XGB demonstrates strong, versatile performance across the DAM, IDM,
and BM, with strengths in hybrid frameworks and real-time market adaptation, though its
effectiveness in the IDM is limited by intra-day complexity.

3.4. Deep Learning Methods

Over the past two decades, DL has emerged as a powerful extension of NNs, driven
by innovations such as Hinton’s efficient training of deep belief networks through greedy
layer-wise pretraining [118]. This breakthrough enabled the training of deeper networks
beyond traditional models like MLPs, leading to significant improvements in generalisa-
tion [119]. DL has since been widely applied across fields like image recognition [120],
speech recognition [121], and machine translation [122], with notable success in energy-
related applications, particularly wind power forecasting [123,124]. In EPF, DL models
such as DNNs, convolutional neural networks (CNNs), LSTMs, and gated recurrent units
(GRUs) have proven successful at capturing complex temporal dependencies.

Energies 2025, 18, 3097

15 of 40

3.4.1. Deep Neural Networks

DNNs are artificial neural networks (ANNs) with multiple hidden layers, allowing
them to model complex, non-linear relationships in EPF. For an input vector xt, each hidden
layer l applies a transformation utilising the layer’s weight W(l) and bias b(l):

Z(l) = σ

(cid:16)

W(l) ∗ Z(l−1) + b(l)(cid:17)

(10)

where σ(·) represents a non-linear activation function. The input layer uses Z(0) = xt,
with the final prediction typically given by a single-output neuron with linear activation:
ˆyt = W(L)Z(L−1) + b(L). Model parameters are learned by minimizing a loss function
using stochastic gradient descent or its variants, while overfitting is addressed through
techniques such as dropout and L1/L2 regularisation to enhance generalisation.

DNNs have shown strong performance in EPF, particularly in the DAM, where they
often outperform traditional statistical and ML methods [19]. However, their effectiveness
depends on proper hyperparameter tuning, as seen in studies where benchmark constraints
limited performance [125–127]. Enhancements such as incorporating inter-market fea-
tures [6] and training on order book data [128] have improved accuracy. Despite their
ability to model non-linear relationships, DNNs do not always outperform simpler models
in the DAM, with simpler models such as LASSO and tree-based methods often yielding
better point and probabilistic forecasts due to their interpretability and stability [14]. In
hybrid frameworks, DNNs perform well in multi-market settings [85], particularly when
combined with feature selection techniques like XGB, which improves model efficiency
and robustness [110]. In the IDM, while DNNs display some strong performance relative
to classical models like LASSO, RNN models such as LSTMs and GRUs outperform them
in capturing short-term price fluctuations, particularly when leveraging spread values
between day-ahead and intra-day prices [68]. In contrast, in the EPEX IDM, DNNs per-
formed similarly to LSTM-based models but were outperformed by LASSO based models
in probabilistic forecasting, underscoring potential challenges of DL in capturing price
volatility [80]. In more volatile markets like the BM, DNN models, despite their ability to
model non-linear relationships in the DAM, and IDM to a lesser degree, are often outper-
formed by simpler models such as LASSO and LEAR [32]. This is largely attributed to their
tendency to overfit and over-react to price spikes. In addition, tree-based methods such as
RF and XGB often yield better point and probabilistic forecasts [31,109]. Overall, DNNs
excel in the DAM, outperforming simpler statistical and ML models by capturing complex,
non-linear relationships, variable interactions, and temporal dependencies that are difficult
to model explicitly. However, in the IDM, they display mixed performance, being outper-
formed by LSTMs and GRUs, which better handle short-term price fluctuations. In the BM,
DNNs are outperformed by simpler, more interpretable models like LASSO, RF, and XGB,
which prove more capable of dealing with price spikes and issues surrounding overfitting.
While DNNs benefit from hybrid frameworks and feature selection, their computational
demands and susceptibility to overfitting present limitations in volatile, real-time markets.

3.4.2. Convolutional Neural Networks

CNNs are a class of DL models originally designed for spatial data but increasingly
applied to time-series forecasting due to their ability to extract local patterns and hierar-
chical features through convolutional operations. A CNN processes an input sequence
xt by applying a series of convolutional filters across the input to compute feature maps,
where the output of each layer is typically computed as in Equation (10). Pooling layers are
often used to reduce dimensionality and increase robustness to noise, while fully connected
layers translate the extracted features into final predictions.

Energies 2025, 18, 3097

16 of 40

In the DAM, CNNs have demonstrated strong performance, particularly in feature
extraction and capturing non-linear market dynamics [53,129]. Integrating CNNs with
dimensionality reduction techniques like PCA has been shown to reduce overfitting and
computational costs while maintaining competitive accuracy [129]. CNN autoencoders
have also proven effective, outperforming GRUs due to their efficient handling of high-
dimensional data [130]. However, CNNs tend to perform slightly worse than DNNs and
GRUs in certain EPF applications [19], likely due to their limited ability to capture long-
term dependencies without additional mechanisms like recurrent layers. Hybrid CNN
architectures have been proposed to address these limitations. For example, combining
1D-CNNs with self-attention mechanisms enhances forecasting accuracy by capturing
both local and long-range temporal dependencies [131]. However, these improvements
come at the cost of increased model complexity and computational overhead. In the IDM,
CNNs effectively capture local temporal dependencies and short-term price fluctuations.
However, they are consistently outperformed by attention-based models and LSTMs, which
better model intra-day patterns and adapt to market dynamics [55]. CNNs struggle with
the high-frequency nature of IDM data, as they lack the sequential memory capabilities
inherent in recurrent architectures. In the BM, CNNs have shown weaker performance
than other DL models, particularly in the UK market, where they underperform LSTMs,
GRUs, and the proposed SA-BiLSTM due to their limited ability to capture seasonality and
extreme price spikes, likely stemming from their spatially constrained filter design [103].
Overall, CNNs demonstrate moderate success in the DAM, leveraging their strength in
feature extraction to model non-linear patterns. However, their lack of temporal memory
mechanisms results in comparatively poorer performance in the IDM and BM, where
capturing long-term dependencies and extreme events is crucial. Hybrid architectures that
integrate CNNs with recurrent or attention-based layers have shown promise, but their
added complexity may limit their practical application in real-time EPF scenarios.

3.4.3. Long Short-Term Memory

LSTM networks, introduced by [132], are a type of RNN designed to capture long-term
dependencies in sequential data through a gating mechanism that regulates information
flow across time steps. Each LSTM cell maintains two key components: a hidden state
ht, which represents the output at time t; and a cell state ct, which stores long-term
contextual information. The cell state is updated via three gates, the forget gate ft, input
gate it, and output gate ot, which control what information is discarded, updated, and
exposed, respectively. The forget gate determines which parts of the previous cell state ct−1
are retained:

The input gate decides which new information is added to the cell state:

ft = σ(W f [ht−1, xt] + b f )

it = σ(Wi[ht−1, xt] + bi)

The output gate governs the contribution of the current cell state to the hidden state:

ot = σ(Wo[ht−1, xt] + bo)

The updated cell state is computed by blending retained and new information:

ct = ft ⊙ ct−1 + it ⊙ tanh(Wc[ht−1, xt] + bc)

(11)

(12)

(13)

(14)

Energies 2025, 18, 3097

Finally, the hidden state ht is updated as

ht = ot ⊙ tanh(ct)

17 of 40

(15)

Here, σ denotes the sigmoid activation function, and ⊙ denotes element-wise multiplication.
This gated structure enables LSTMs to retain and update information over long time
horizons, making them well suited where temporal dependencies and delayed effects
are common.

In the DAM, LSTM models have consistently outperformed statistical models, demon-
strating strong predictive performance when capturing complex temporal dependen-
cies [18,19,133]. Hybrid architectures, such as CNN-LSTM combinations, have improved
accuracy by improving feature extraction [134,135]. However, performance gains often
depend heavily on dataset size and the careful selection of hyperparameters [136,137]. In
markets like Turkey and New South Wales, LSTMs surpassed GRUs in capturing seasonal
and event-driven price fluctuations [138,139]. In the IDM, LSTMs exhibit mixed perfor-
mance. While outperforming classical models such as ARX in the Turkish IDM [68], LSTMs
are often matched or outperformed by GRUs due to the latter’s computational efficiency
and effective gating mechanisms [140]. In the German IDM, LSTMs demonstrated superior
performance for daily average and hourly price forecasting [54], but simpler linear models
still outperform LSTMs when intra-day volatility increases [80]. LSTMs similarly produce
varied results in the BM. In the Dutch BM, univariate LSTMs outperform their multivariate
counterparts and linear regression for short-term forecasts, though performance deterio-
rates for longer forecasting horizons [141]. In the Irish BM, LSTMs within multi-headed
DNN-RNN architectures, struggle to capture short-term price patterns, struggle with
overfitting, and are outperformed by statistical models like LEAR [32,109]. Conversely,
LSTMs achieve strong results in the UK BM, where non-linear price fluctuations are more
effectively captured [103], particularly when implemented with seasonal attention mecha-
nisms like SA-BiLSTM, which enhance the model’s ability to track extreme price events.
Recent advances in EPF increasingly integrate bidirectional LSTM (BiLSTM) networks
into hybrid frameworks that combine multi-stage preprocessing and ensemble learning
to capture complex bidirectional temporal dependencies, decompose noisy signals, and
adapt to evolving market dynamics—especially in high-volatility, high-frequency settings.
These models capture forward and backward temporal dependencies, offering a more
comprehensive understanding of market sequences. For example, ref. [101] proposed a
CatBoost-BiLSTM hybrid that combines gradient-boosted feature selection with bidirec-
tional recurrent learning, outperforming conventional ML models by improving input
relevance and temporal pattern capture. Attention mechanisms further enhance bidirec-
tional learning, as demonstrated by [142], who proposed a BiLSTM attention hybrid with
EEMD to improve spike detection and capture non-linear temporal volatility interactions
in DAM forecasts, achieving higher accuracy during price anomalies. Overall, LSTM and
BiLSTM models demonstrate strong performance in the DAM, particularly when enhanced
with hybrid architectures and attention mechanisms. However, their effectiveness in the
IDM and BM is mixed, often depending on market volatility, forecasting horizon, and
model design.

3.4.4. Gated Recurrent Units (GRUs)

GRUs are a simplified variant of LSTM networks that retain the ability to model
long-range dependencies while reducing computational complexity. Unlike LSTMs, which

Energies 2025, 18, 3097

18 of 40

use separate input and forget gates (see Section 3.4.3, Equations (11–14)), GRUs merge
these into a single update gate:

zt = σ(Wz[ht−1, xt] + bz)

They also introduce a reset gate:

rt = σ(Wr[ht−1, xt] + br)

The candidate activation ˜ht is computed as

˜ht = tanh(Wh[rt ⊙ ht−1, xt] + bh)

and the final hidden state is updated via

ht = (1 − zt) ⊙ ht−1 + zt ⊙ ˜ht

(16)

(17)

(18)

(19)

Here, σ denotes the sigmoid activation function and ⊙ denotes element-wise multiplication,
as in Section 3.4.3. By reducing the number of gates and removing the explicit cell state,
GRUs offer a more computationally efficient alternative to LSTMs.

GRUs have achieved superior accuracy over statistical and ML models in electricity
markets such as the Turkish DAM [18]. GRUs have also proven effective for short-term EPF
tasks [19], with applications showing that integrating GRUs with bagged regression trees
improves mid-term forecasting accuracy when handling non-linear market fluctuations [63].
In the New York electricity market, CNN-based models outperformed GRUs, indicating po-
tential limitations when forecasting high-dimensional price patterns [130]. However, GRU
models regain their competitive edge in hybrid architectures; for instance, in the Iranian
DAM, GRU models combined with stacked autoencoders achieved improved long-term
performance [140]. Additional enhancements, such as hyperparameter tuning and hybrid
approaches, further bolster performance, as seen in models leveraging periodic pattern
extraction techniques [58,143]. Hybrid models combining GRUs with tree-based methods
have improved accuracy by dynamically adjusting model weights based on intra-day
market patterns [144]. Additionally, ref. [145] introduced a GRU variant with noise-robust
training, improving forecast reliability in the DAM, particularly during periods of increased
renewable generation. In the Turkish IDM, GRUs achieved the lowest MAE and RMSE,
outperforming statistical models and highlighting their suitability for short-term intra-day
forecasting [68]. Their computational efficiency, combined with effective learning of hourly
price patterns, makes GRUs particularly useful for markets with high-frequency trading.
In the British BM, GRUs delivered competitive results but were ultimately outperformed
by SA-BiLSTM, which demonstrated superior accuracy due to its seasonal attention mecha-
nisms [103]. Overall, GRUs perform well across all three markets but display mixed results
in comparison to other DL architectures. While GRUs outperform LSTMs in computational
efficiency and show strong results in the DAM and IDM, they tend to struggle in the BM,
particularly during extreme price events, where models with stronger regularisation and
more capable of mitigating overfitting perform more reliably.

3.4.5. Temporal Fusion Transformers

Temporal Fusion Transformers (TFTs) are attention-based DL models specifically de-
signed for multi-horizon time-series forecasting, combining recurrent and Transformer-style
self-attention layers to capture both short-term dynamics and long-range dependencies.
TFTs employ variable selection networks to filter relevant input features and utilise an
interpretable multi-head attention mechanism to weigh temporal patterns dynamically. For

Energies 2025, 18, 3097

each time-step t, the attention score is computed as αt = softmax

19 of 40

(cid:19)

(cid:18)

QK⊤√
dk

, where Q and K

are learned query and key matrices, and dk is the dimensionality of the key vectors.

TFT models have demonstrated strong performance in forecasting applications, out-
performing ARIMA, LSTM, and XGB in photovoltaic power prediction, owing to their
interpretability and ability to capture complex temporal relationships via static covariates
and dynamic variables [146]. In energy consumption forecasting, TFTs outperform LSTMs
and temporal convolutional networks, delivering lower error rates and greater stability in
Poland and Nord Pool’s DAMs [147,148]. However, these models are prone to overfitting
when applied to smaller datasets, necessitating careful regularisation [145]. While TFT
applications in the IDM are limited, a study in the Nord Pool market shows their ability to
capture short-term price dynamics using domain-specific features like renewable forecasts
and cross-border flows [72], though simpler models like LSTM and GRUs often achieve
comparable performance in intra-day markets due to the rapid price fluctuations and
reduced availability of relevant exogenous predictors. TFT models have shown strong
performance in the BM, outperforming LSTM variants and statistical models in forecast-
ing imbalance prices by leveraging adaptive and seasonal attention mechanisms to track
extreme price spikes and volatility [103]. Overall, TFTs perform well across each spot
market, demonstrating strong results in the DAM and BM due to their flexible handling of
dynamic temporal patterns. In the IDM and BM, TFT models remain underutilised, and
although they show promise in capturing intra-day dynamics, they are outperformed by
other DL models.

3.4.6. DeepAR

DeepAR is a probabilistic forecasting model based on AR RNNs, where each time
series is modelled conditionally on its past values and covariates. At each time step t,
DeepAR predicts the distribution of the next value yt given the history yt−n and exogenous
inputs xt by learning the parameters of a likelihood function, often Gaussian or negative
binomial, with the model trained to maximize the likelihood of observed sequences.

DeepAR has proven effective at capturing seasonality and trends, outperforming
traditional methods [149]. In DAM EPF, it handles large sets of related time series, though
is outperformed by models incorporating heteroscedasticity [145]. In the Nord Pool IDM,
DeepAR displays weak performance, being outperformed by LR, ARX, SARIMAX, and
TFT [72]. Overall, DeepAR remains largely underexplored in each spot market, with poor
results in both the DAM and IDM, with no testing having occurred in any BM to date.

3.4.7. Prophet

Prophet is a decomposable time-series forecasting model designed to capture non-
linear trends with seasonality and holiday effects using a generalised additive model
framework. The model expresses the time series as yt = g(t) + s(t) + h(t) + ϵt, where g(t)
models the trend, s(t) represents periodic seasonality using Fourier series, h(t) accounts for
holiday effects, and ϵt is the error term. Prophet automatically detects change points in the
trend and fits them using piecewise linear or logistic growth curves, making it especially
useful for datasets with strong seasonal components and structural shifts.

In the Italian DAM, Prophet was applied alongside seasonal and trend decomposition
using LOESS (STL), improving forecast accuracy by isolating important patterns and
reducing noise [150]. Extensions such as Neural Prophet have incorporated DL techniques
to handle lagged variables and AR terms, resulting in improved short- and long-term
electricity load predictions through better seasonality and trend extraction [151]. Prophet
has also been employed for univariate forecasting of exogenous variables, such as weather,
where it enhanced real-time EPF performance by effectively modelling both periodic

Energies 2025, 18, 3097

20 of 40

and non-periodic patterns [97]. Despite these applications, Prophet remains relatively
unexplored in the IDM and BM, where higher volatility and shorter forecasting horizons
present challenges that the model’s simplistic structure may struggle to handle. The
model’s reliance on predefined seasonal patterns makes it less adaptive to the dynamic
price behaviour characteristic of real-time markets, limiting its utility for EPF applications.

3.5. Hybrid Models

Hybrid models integrate statistical, ML, and DL techniques to utilise the comple-
mentary strengths of each approach in EPF. These models are particularly effective in
capturing the complex, non-linear, and volatile dynamics of electricity markets. By combin-
ing the interpretability of linear models, the adaptability of ML, and the sequential learning
capabilities of DL, hybrid frameworks offer a flexible and robust forecasting solution.

3.5.1. Statistical Hybrid Models

Hybrid statistical models combine the interpretability of classical time-series tech-
niques with the flexibility and non-linearity of ML or DL components. These models are
typically designed to leverage the strengths of AR structures—well suited for capturing lin-
ear dependencies—while enhancing adaptability to volatility and non-stationarity through
non-linear elements or regularisation schemes. One common class of hybrid models inte-
grates exogenous input models with regularisation techniques. For instance, FARX-LASSO
and fARX-EN models extend the ARX framework by introducing LASSO or elastic net
regularisation, which help control overfitting and improve predictive robustness in high-
dimensional settings [19]. These models retain a linear structure for interpretability, while
penalising uninformative inputs and multicollinearity. Another prominent hybrid family
includes combinations of linear AR forecasting and conditional variance modelling. The
ARIMA-GARCH hybrid remains effective for jointly modelling linear autocorrelation and
non-linear volatility, particularly in high-volatility environments like electricity markets
with frequent price spikes [44]. These models allow for simultaneous mean and variance
forecasting, improving both point and risk-aware forecasts. Statistical–ML hybrids further
improve performance by pairing linear decomposition with non-linear learning. Examples
include Wavelet-ARIMA with RBF networks (WARIMA-RBF) and Self-Organising Maps
with SVR (SOM-SVR). These models decompose the time series into components (e.g.,
trend, seasonality, noise) and apply non-linear learners to each, capturing both global and
local price dynamics [4]. DL has also been integrated with statistical baselines to optimise
parameter selection and capture deeper temporal patterns. The DNN–LEAR hybrid, for
example, combines DNNs with LASSO–elastic net AR, improving accuracy in DAM EPF
while preserving model interpretability through sparse feature selection [4].

Recent contributions have proposed hybrids tailored to specific market or data chal-
lenges. In the U.S. DAM and BM (PJM and NYISO), [152] introduced a SARIMA–LSTM
model augmented with wavelet decomposition, effectively combining seasonal AR forecast-
ing with LSTM networks to handle both periodic and non-linear structures. In the CAISO
market, ref. [153] demonstrated that combining robust PCA for outlier detection with
linear regression improves forecast accuracy in heteroscedastic environments. Outside of
deregulated markets, ref. [154] proposed a novel hybrid for Cameroon’s regulated system:
a WOA-GMHES(1,N) model, blending Whale Optimisation Algorithms and Grey Holt ES.
This model shows high accuracy under data scarcity conditions, highlighting hybridisa-
tion’s potential in resource-constrained environments. Overall, statistical hybrid models
offer a flexible and modular approach to EPF, allowing researchers to tailor models to spe-
cific market conditions—such as volatility, high dimensionality, or data irregularities—by
integrating linear structure, regularisation, and non-linear learning in a unified framework.

Energies 2025, 18, 3097

21 of 40

3.5.2. Machine Learning Hybrid Models

ML hybrid models combine diverse predictive algorithms—often spanning tree-based
ensembles, NNs, and decomposition techniques—to enhance the accuracy, robustness, and
adaptability of EPF. These hybrids are particularly suited to environments with high volatil-
ity, non-linear patterns, or limited data interpretability, leveraging the complementary
strengths of different ML models. Several hybrid models integrate feature selection, signal
decomposition, and non-linear regressors. For instance, ref. [106] proposed a hybrid that
combines automatic relevance determination with Extra Trees Regression, effectively captur-
ing the trend, seasonality, and volatility in DAMs by isolating relevant inputs and reducing
overfitting through ensemble learning. Similarly, ref. [155] employed a decomposition-
enhanced hybrid using variational mode decomposition (VMD) and ensemble empirical
mode decomposition (EEMD) with an extreme learning machines optimised by differential
evolution. This model excelled in handling non-linear dynamics in markets such as Spain
and Australia, outperforming baseline ML and statistical models.

Other hybrid frameworks aim to bridge short- and long-term forecasting capabilities.
Ref.
[156] developed a Fourier-augmented hybrid that integrates data-driven ML with
market-based predictive signals. By applying Fourier analysis, the model isolates domi-
nant frequency components, improving accuracy across both high-frequency volatility and
long-term trends, making it particularly effective in balancing signal noise and seasonal
price cycles. At the microgrid and household levels, ML hybrids have been used to model
consumption patterns influenced by dynamic pricing. Ref. [157] introduced a hybrid based
on XGB, optimised for real-time residential demand prediction. By treating electricity price
as an exogenous input, the model captures user sensitivity to price signals, significantly
improving accuracy for short-horizon load forecasting—critical for demand-response and
smart grid applications. In a large-scale DAM context, ref. [110] proposed a three-stage
hybrid for Shandong’s market in China, integrating a day-similarity algorithm, XGB-based
feature selection, and an adaptively optimised DNN. This architecture achieved high accu-
racy in 96-point forecasting by leveraging historical analogues and deep feature abstraction,
illustrating the benefit of combining similarity-based reasoning with supervised learning.
Robustness to data quality issues has also been addressed through hybridisation.
The OANQR model by [158] combines outlier detection, VMD, and non-crossing quantile
regression, targeting the high volatility and distributional asymmetry of the Singapore
DAM. This model produces probabilistic forecasts that remain stable even in the presence
of price shocks and data anomalies. Finally, more comprehensive hybrid frameworks incor-
porate multiple predictive paradigms. Ref. [159] proposed an ensemble architecture that
merges RF, SVM, LSTM, ARIMA, and ES. This full-spectrum hybrid leverages strengths
from statistical, tree-based, and DL models, achieving state-of-the-art performance across
electricity and financial price series. Its ability to adapt to dynamic market conditions
highlights the utility of ensemble-of-hybrids strategies in volatile multi-scale forecasting
environments. In summary, ML hybrid models excel in scenarios demanding adaptability,
high-dimensional learning, and robust treatment of noise or non-stationarity. These archi-
tectures are increasingly effective in both aggregate market forecasting (DAM) and granular
applications (residential demand), particularly when they combine signal decomposition,
advanced feature selection, and optimised non-linear learning.

3.5.3. Deep Learning Hybrid Models

DL hybrid models fuse convolutional, recurrent, and attention-based architectures
with statistical and ML techniques to capture complex temporal, spatial, and feature inter-
actions in EPF. These models are particularly adept at managing high-frequency volatility,
extracting multi-scale patterns, and improving accuracy through learned representations

Energies 2025, 18, 3097

22 of 40

and ensemble strategies. Early hybrid designs leveraged CNNs for local pattern recognition
and paired them with traditional learners. For instance, the CNN–SVR model applies con-
volutional layers for feature extraction before regression with SVM, improving short-term
EPF accuracy through non-linear kernel adaptation [8]. Similarly, CNN-LSTM hybrids have
shown strong performance in the Iranian DAM by capturing both spatial correlations and
sequential dependencies [9]. Recurrent hybrid models remain central to DL-based EPF. The
GRU–LSTM architecture combines GRUs and LSTM cells to simultaneously model short-
and long-term dependencies, improving accuracy in DAM EPF [106]. Extensions of this
idea include combinations with trend-aware models: Ref. [151] proposed an LSTM–Neural
Prophet hybrid that captures AR trends alongside deep temporal dependencies, while [160]
introduced a Prophet–LSTM model optimised with a back propagation NN to improve
convergence and reduce forecast error.

Hybrid stacking ensembles have further extended DL models by integrating them
into multi-model frameworks. For example, ref. [161] developed a hybrid stacking model
combining XGB, CatBoost, LGBM, NODE, GRU, and LSTM, using LASSO as a meta-learner,
achieving high short-term accuracy in the Australian DAM by balancing tree-based inter-
pretability and recurrent network flexibility. A similar high-performance framework was
proposed by [162], where a CNN–GRU hybrid with attention mechanisms outperformed
both standalone DL and Transformer models in the DAM by prioritising relevant tempo-
ral features. Attention-based hybrids are gaining traction for their ability to selectively
weight key time steps or features. In the Ontario DAM, ref. [131] integrated multi-head
self-attention with a 1D-CNN and a mutual information–based feature selection strategy,
improving both computational efficiency and accuracy. Similarly, ref. [163] introduced
TriConvGRU, a hybrid combining convolutional and recurrent layers to extract multi-scale
temporal–spatial features, outperforming statistical and DL models in the same market.
Hybrid DL frameworks are also proving useful in real-time markets. In Denmark’s DK1
IDM, ref. [55] proposed a model that combines LSTM-based forecasting with a rule-based
trading strategy, achieving profitable outcomes by leveraging real-time IDM and DAM
price signals for renewable energy trading. Multi-source and multi-market forecasting
has benefited from DL hybridisation, as ref. [164] introduced a hybrid for Spain’s DAM
and derivatives market that combines ANNs for price, wind, and solar forecasts with a
temperature-adjusted similar-day demand predictor, achieving accurate 2–10 day forecasts.
In the French EPEX DAM, ref. [165] proposed the DF-RNN hybrid, jointly optimising
time-series decomposition and sequence forecasting, yielding superior mid- and long-term
performance. Cross-market generalisability has been explored through decomposition-
based DL hybrids. Ref. [166] introduced a hybrid integrating STL with GRU and LGBM,
demonstrating high interpretability and accuracy in both the U.S. PJM frequency regulation
BM and the Australian Queensland DAM.

Multi-layered architectures have proven effective, such as a CNN–BiLSTM–AR hybrid
from [167] that combines convolutional layers for local pattern extraction, BiLSTM for
sequential learning, and an AR component for linear trend reinforcement. Applied to the
UK and German DAMs, the model showed notable improvements in forecast accuracy,
aided by hyperparameter tuning for architectural balance. Transformer-based hybrids
have extended these capabilities, with [168] introducing a Transformer–BiLSTM model
that integrates self-attention with bidirectional sequence modelling to capture long-range
dependencies and short-term volatility, outperforming standalone LSTM and GRU models
in DAM settings. Ensemble bi-forecasting architectures offer a novel path toward inter-
val prediction, with [169] proposing a hybrid for the Australian DAM combining a deep
belief network (DBN), BiLSTM, and Improved Complete EEMD with Adaptive Noise,
which, using a multiple-input multiple-output structure and a linear operator mechanism,

Energies 2025, 18, 3097

23 of 40

achieved high-accuracy point and interval forecasts while maintaining interpretability.
Ref. [170] developed a hybrid BiLSTM-GRU model that outperformed traditional and
DL baselines in forecasting NYISO BM prices by capturing both long- and short-term
dependencies. Advanced bidirectional hybrid approaches are also being applied to the BM,
where volatility is pronounced. In the British BM, ref. [103] demonstrated that BiLSTM-
based ensembles—such as CEEMD–RF–IRSA–BiLSTM and TVFEMD–RF–CNN–ISCA–
BiLSTM—achieved superior performance over traditional ML models. These frameworks
integrate decomposition (CEEMD, TVFEMD), ensemble learning (RF), optimisation strate-
gies (IRSA, ISCA), and DL, producing highly robust forecasts under dynamic conditions.
Advanced hybrid models—particularly those combining BiLSTM with attention mecha-
nisms and signal decomposition techniques—excel at capturing both local fluctuations and
global market trends to address complex conditions in DAM and BM. By integrating DL’s
ability to model non-linearity and long-range dependencies with complementary methods
like decomposition (for noise reduction) and structured ensembles (for robustness), these
frameworks consistently outperform standalone models, demonstrating superior accuracy
in short- and mid-term EPF across diverse market structures.

4. Discussion

EPF has evolved into a multidisciplinary challenge, shaped by growing market com-
plexity, renewable integration, and the demands of high-frequency trading and grid balanc-
ing. This discussion aims to connect insights from the preceding review of statistical, ML,
DL, and hybrid models across the DAM, IDM, and BM. Rather than evaluating models
in isolation, we examine their performance through the lens of market-specific dynam-
ics, forecasting objectives, and methodological trade-offs. Particular attention is given to
the suitability of each modelling paradigm under different volatility levels and temporal
constraints, as well as the persistent challenges posed by evaluation metric selection and
model generalisability.

4.1. Overview

The trends in Tables 1 and 2 show a progression from statistical methods, predomi-
nantly used in earlier studies such as [43,44], to more sophisticated ML approaches. How-
ever, from 2017 and 2018 onwards, there has been a marked shift toward DL models. These
methods have been primarily applied to the DAM and, to a lesser extent, the IDM and BM.
Table 3 extends this analysis beyond EPF to include applications in wind power, photo-
voltaic, and load forecasting, with models like CatBoost-BiLSTM and attention mechanisms
showing strong adaptability and success in managing high-dimensional datasets [143].

Focusing in more depth, Table 1, for EPF pre-2020, reveals a clear evolution in method-
ological approaches and market focus. The DAM dominates the literature, reflecting its
central role in electricity trading. Early forecasting efforts primarily relied on statistical
models such as ARIMA, ARX, and GARCH, which were effective at capturing linear trends
and seasonal patterns. However, these models struggled to handle the increasing non-
linearity and volatility brought about by the integration of renewable energy sources. As
market dynamics grew more complex and datasets became larger, the focus shifted toward
models with built-in regularisation, such as LASSO and LEAR, as well as ML techniques
better suited to capturing non-linear price behaviours. From around 2017 onwards, DL
models began to emerge, often in hybrid configurations that combined statistical, ML,
and DL elements to improve performance and interpretability. While statistical models
remained relevant, the broader trend reflects a growing reliance on data-driven non-linear
and hybrid approaches to address the increasing volatility and complexity of markets.

Energies 2025, 18, 3097

24 of 40

Post-2020 EPF sees a clear methodological shift toward hybrid techniques and an
expanding focus on real-time markets such as the IDM and BM, as seen in Table 2. While
the DAM continues to be widely studied, there is a growing emphasis on addressing
the volatility and rapid fluctuations inherent in real-time markets. From 2022 onward,
the focus on more real-time markets accelerated, with an increasing number of studies
targeting IDM and BM explicitly. However, they remain comparatively underexplored,
highlighting a valuable opportunity for future research into unified forecasting frameworks
that can support operational decision making across the full spectrum of electricity markets.
Statistical and ML models remain popular, but DL architectures like LSTMs and GRUs have
gained traction for their ability to capture non-linear dependencies and temporal patterns.
More recent studies also introduce Transformer-based architectures and seasonal-trend-
aware models, reflecting the field’s ongoing evolution toward robust, high-resolution, and
real-time predictive approaches. Furthermore, the growing adoption of hybrid models
highlights the rising complexity of electricity markets, positioning them as the leading
approach for balancing interpretability, accuracy, and adaptability markets.

Table 1. Literature on predictive models for EPF before 2020. Interest in DAM dominates. The ✓ is
the approach presented herein.

Reference

Nogales et al. 2002 [87]
Contreras et al. 2003 [50]
Sansom et al. 2003 [98]
Cuaresma et al. 2004 [51]
Conejo et al. 2005 [52]
Knittel et al. 2005 [56]
Zhou et al. 2006 [171]
Fan et al. 2007 [99]
Garcia et al. 2008 [88]
Diongue et al. 2009 [57]
Lin et al. 2010 [172]
Che et al. 2010 [100]
Jakavsa et al. 2011 [74]
Mei et al. 2014 [108]
Klaeboe et al. 2015 [43]
Poplawski et al. 2015 [42]
Ziel et al. 2016 [47]
Uniejewski et al. 2016 [81]
Girish et al. 2016 [44]
Feijoo et al. 2016 [91]
Gonzalez et al. 2016 [104]
Yang et al. 2017 [5]
Lago et al. 2018 [19]
Rita et al. 2018 [66]
Ugurlu et al. 2018 [18]
Kuo et al. 2018 [138]
Chinnathambi et al. 2018 [133]
Jiang et al. 2018 [173]
Chang et al. 2018 [139]
Zhang et al. 2018 [174]
Kath et al. 2018 [69]
Zhu et al. 2018 [136]
Johannesen et al. 2019 [94]
Zhou et al. 2019 [137]

Statistical
✓
✓

✓
✓
✓
✓

✓
✓
✓
✓
✓
✓
✓
✓
✓
✓
✓
✓
✓
✓
✓
✓
✓

✓
✓
✓
✓

ML

DL

Hybrid

DAM IDM

BM Other

✓

✓

✓
✓

✓

✓

✓
✓
✓
✓

✓

✓
✓
✓

✓

✓

✓
✓

✓

✓
✓
✓

✓

✓
✓
✓
✓
✓
✓
✓

✓

✓

✓
✓
✓
✓
✓
✓
✓
✓
✓
✓
✓
✓
✓

✓

✓
✓
✓
✓
✓
✓
✓
✓
✓
✓
✓
✓
✓

✓
✓
✓

✓
✓
✓

✓

✓

Energies 2025, 18, 3097

25 of 40

Table 1. Cont.

Reference

Xu et al. 2019 [7]
Zahid et al. 2019 [8]
Chang et al. 2019 [175]
Zahid et al. 2019 [8]
Atef et al. 2019 [125]
Luo et al. 2019 [126]
Lago et al. 2019 [6]
Karabiber et al. 2019 [61]
Johannesen et al. 2019 [94]
Schnurch et al. 2019 [128]
Oksuz et al. 2019 [68]
Uniejewski et al. 2019 [25]
Maciejowska et al. 2019 [71]
Ali et al. 2019 [92]
Schnurch et al. 2019 [128]

Statistical
✓

ML

✓

✓
✓

✓
✓

✓
✓

✓

✓

✓
✓
✓
✓

✓

Hybrid
✓
✓
✓
✓

✓

DL
✓
✓
✓
✓
✓
✓
✓
✓

✓
✓

✓

DAM IDM

BM Other

✓
✓
✓
✓
✓
✓
✓
✓
✓
✓

✓
✓
✓

✓
✓
✓

Table 2. Literature on predictive models for EPF after 2020. Real-time markets begin to attract
attention. The ✓ is the approach presented herein.

Reference

Marcjasz et al. 2020 [67]
Lucas et al. 2020 [116]
Khan et al. 2020 [129]
Narajewski et al. 2020 [78]
Li et al. 2021 [21]
Lago et al. 2021 [4]
Kara et al. 2021 [105]
Ozen et al. 2021 [48]
Wang et al. 2022 [95]
Lehna et al. 2022 [75]
Narajewski et al. 2022 [31]
Tschora et al. 2022 [82]
Xie et al. 2022 [107]
Zhang et al. 2022 [101]
Meng et al. 2022 [135]
Yang et al. 2022 [53]
Kotsias et al. 2022 [72]
Iqbal et al. 2022 [63]
Beltran et al. 2022 [96]
Jkedrzejewski et al. 2022 [14]
Alkawaz et al. 2022 [106]
Rezaei et al. 2022 [140]
Yang et al. 2022 [130]
Serafin et al. 2022 [79]
Heidarpanah et al. 2023 [9]
Bille et al. 2023 [46]
Xiong et al. 2023 [144]
Kapoor et al. 2023 [58]
Marcjasz et al. 2023 [83]
Olivares et al. 2023 [45]
Gunduz et al. 2023 [84]
Stefenon et al. 2023 [150]

Statistical
✓

✓
✓
✓

✓

✓
✓
✓

✓

✓
✓
✓
✓

✓

✓
✓

✓

✓
✓
✓
✓

ML

DL

Hybrid

DAM IDM

BM Other

✓

✓

✓

✓

✓

✓

✓

✓

✓

✓

✓

✓
✓
✓
✓

✓
✓
✓

✓

✓

✓

✓

✓

✓
✓

✓
✓
✓
✓
✓
✓
✓
✓
✓
✓
✓

✓
✓

✓

✓
✓
✓
✓
✓
✓

✓
✓

✓
✓

✓
✓
✓

✓
✓

✓
✓
✓

✓
✓
✓
✓
✓
✓
✓

✓

✓

✓
✓
✓
✓

✓
✓
✓
✓
✓

✓
✓
✓
✓
✓

✓
✓
✓
✓
✓
✓
✓
✓

Energies 2025, 18, 3097

26 of 40

Table 2. Cont.

Reference

Poggi et al. 2023 [54]
Molin et al. 2023 [141]
Yang et al. 2024 [85]
Kilicc et al. 2024 [55]
Ghimire et al. 2024 [176]
Bozlak et al. 2024 [76]
Lisi et al. 2024 [65]
Kitsatoglou et al. 2024 [77]
Peng et al. 2024 [97]
Huang et al. 2024 [110]
Pourdaryaei et al. 2024 [131]
Shi et al. 2024 [145]
Englund et al. 2024 [49]
O’Connor et al. 2024 [32]
Uniejewski et al. 2024 [73]
Bozlak et al. 2024 [76]
Yang et al. 2024 [85]
Deng et al. 2024 [103]
Jiang et al. 2024 [148]
Guo et al. 2024 [152]
Nyangon et al. 2024 [153]
Sapnken et al. 2024 [154]
Chen et al. 2024 [161]
Laitsos et al. 2024 [162]
Ehsani et al. 2024 [163]
Mubarak et al. 2024 [167]
Khan et al. 2024 [168]
Nie et al. 2024 [169]
Hajigholam et al. 2024 [170]
Nickelsen et al. 2025 [70]
Agakishiev et al. 2025 [80]
O’Connor et al. 2025 [86]
O’Connor et al. 2025 [109]
Chen et al. 2025 [158]
Yan et al. 2025 [165]
Cu et al. 2025 [166]

Statistical
✓
✓
✓
✓

✓
✓
✓

✓
✓
✓
✓
✓

✓
✓
✓
✓

✓
✓

✓
✓
✓
✓
✓

✓

ML

DL

Hybrid

DAM IDM

BM Other

✓
✓
✓
✓
✓

✓
✓
✓
✓
✓

✓

✓
✓
✓
✓
✓

✓
✓
✓
✓
✓
✓
✓
✓

✓

✓
✓
✓
✓

✓
✓

✓
✓
✓

✓
✓
✓

✓

✓

✓

✓
✓
✓
✓
✓

✓
✓

✓
✓

✓
✓
✓
✓
✓
✓

✓

✓

✓

✓

✓
✓
✓
✓
✓
✓
✓
✓

✓
✓

✓

✓
✓
✓

✓
✓
✓

✓
✓
✓
✓

✓
✓
✓
✓
✓
✓

✓
✓
✓

✓
✓
✓
✓
✓

✓

✓
✓

✓

✓

✓

✓

✓

✓

✓

✓

✓
✓

✓

Table 3. Literature on predictive models used outside of EPF or with EPF. When papers look at
EPF and external fields, they unilaterally look at the DAM with the external market. The ✓ is the
approach presented herein.

Reference

Statistical

Zhu et al. 2018 [136]
Ali et al. 2019 [92]
Mujeeb et al. 2019 [127]
Ashfaq et al. 2019 [93]
Cai et al. 2020 [111]
Salinas et al. 2020 [149]
Rafi et al. 2021 [113]
Memarzadeh et al. 2021 [134]
Lopez et al. 2022 [146]
Ishak et al. 2022 [59]
Cantillo et al. 2022 [102]
Arrieta et al. 2022 [90]

✓

✓
✓
✓

✓
✓

✓

DL
✓

✓
✓
✓
✓
✓
✓
✓

ML
✓
✓
✓
✓
✓
✓
✓

✓

✓

Hybrid

DAM IDM

BM Other

✓
✓
✓

✓

✓

✓
✓

✓

✓

✓
✓
✓
✓
✓
✓
✓
✓
✓
✓
✓
✓

Energies 2025, 18, 3097

27 of 40

Table 3. Cont.

Reference

Durante et al. 2022 [89]
Qinghe et al. 2022 [112]
Suvarna et al. 2022 [114]
Lopez et al. 2022 [146]
Shohan et al. 2022 [151]
Bashir et al. 2022 [160]
Woo et al. 2022 [60]
Gellert et al. 2022 [62]
Seyed et al. 2023 [115]
Nazir et al. 2023 [147]
Rao et al. 2023 [64]
Gomez et al. 2023 [142]
Parizad et al. 2024 [157]
Zhang et al. 2024 [143]
Williams et al. 2025 [159]
Belenguer et al. 2025 [164]

Statistical
✓
✓

✓

✓
✓
✓
✓

✓
✓

✓
✓

ML

DL

Hybrid

DAM IDM

BM Other

✓
✓
✓

✓
✓

✓
✓
✓

✓

✓✓
✓
✓
✓
✓
✓
✓

✓
✓
✓
✓
✓
✓

✓
✓

✓
✓
✓

✓
✓

✓

✓

✓
✓

✓

✓
✓
✓
✓
✓
✓
✓
✓
✓
✓
✓
✓
✓
✓
✓
✓

The literature summarised in Table 3 highlights the dominant approaches in cross-
domain forecasting, where EPF is paired with applications such as wind power, load,
photovoltaic, and consumption forecasting. Notably, in all cases where EPF is considered,
the focus is exclusively on the DAM, reflecting the lower barrier for entry towards forecast-
ing the market. A significant number of these studies employ hybrid models to capture
the complex, non-linear, and temporal patterns common across domains, underscoring the
overlapping characteristics of effective EPF, and settings with similar predictors.

4.2. Forecasting Methods

The landscape of EPF is shaped by a diverse range of modelling techniques, each
with varying strengths depending on market structure, volatility, and data availabil-
ity. This section categorises these methods into three groups—statistical, ML, and DL
models—highlighting their roles, performance, and suitability across the DAM, IDM,
and BM.

4.2.1. Statistical Models

In the evolving landscape of EPF, classical statistical models such as AR, ARIMA, and
GARCH continue to serve as valuable benchmarks but often fall short in capturing the
full complexity of modern markets. AR and ARIMA models are particularly effective in
structured environments like the DAM, where they capture mean reversion and linear
trends, especially when extended with exogenous inputs (ARX, ARIMAX) or volatility
models (GARCH). However, they have seen a decline in rankings with the prevalence
of ML and DL models, which are proving more capable of modelling markets that are
growing increasingly complex, where non-linearities, regime shifts, and price spikes are
more prevalent. ES methods, including TBATS and ES-based hybrids, offer simplicity and
interpretability but tend to underperform in volatile or real-time conditions unless enhanced
by architectures like the ES Transformer. While enhancements like SARIMAX, hybrid
wavelet-based extensions, and regularisation improve accuracy, these models are generally
outperformed by ML and DL approaches, which better capture cross-hour dependencies,
non-linear dynamics, and price volatility. Regularised models like LASSO and LEAR excel
in the DAM and IDM due to their robustness and feature selection capabilities. LEAR,
in particular, emerges as a strong contender in the BM, outperforming more complex

Energies 2025, 18, 3097

28 of 40

models by avoiding overfitting—a common issue for both ML and DL methods in short,
noisy datasets. TF and copula models, while theoretically appealing for capturing complex
dependencies, remain largely untested in real-time markets and have shown limited success,
even in the DAM. The widespread use of naive models as benchmarks, especially in the
IDM and BM, reflects their practical utility in real-time forecasting due to their simplicity
and responsiveness, though their accuracy lags behind more advanced methods. Overall,
the literature indicates that while statistical models still hold relevance—particularly in
hybrid structures—the future of EPF lies in flexible, data-driven models that integrate
exogenous inputs, capture temporal dynamics, and adapt to the increasingly volatile nature
of electricity markets.

4.2.2. Machine Learning Models

In the DAM, ML models like KNN, SVR, RF, and XGB show varied performance, with
KNN often struggling due to its sensitivity to neighbour selection and dataset imbalances,
which hinder its ability to capture extreme price peaks. In contrast, ensemble models like
RF and XGB excel, proving more capable at handling complex market dynamics. RF, in
particular, stands out for its strong performance across the DAM, IDM, and BM, showing
the ability to capture multi-output tasks and adapt to evolving market conditions through
online variants. XGB performs well in capturing key variables like renewable energy
penetration but faces challenges in the IDM due to difficulties with hyperparameter tuning,
intra-day dependencies, short-term price fluctuations, and extreme volatility, where DL
models like LSTM or GRU show superior performance in capturing short-term volatility.
XGB excels in the BM [116], particularly for bidding and risk management, though it is
sometimes outperformed by simpler models like LEAR [32]. Overall, while RF and XGB
deliver strong performance in both the DAM and real-time markets, their adaptability to
capturing intra-day volatility and extreme price movements remains limited compared
to DL models, reinforcing the growing dominance of hybrid and data-driven approaches
in EPF.

4.2.3. Deep Learning Models

DL models have made significant strides in EPF, particularly in the DAM, where they
consistently outperform statistical and ML models, proving more capable at capturing
complex, non-linear relationships and temporal dependencies. DNNs excel in multi-market
settings when combined with feature selection techniques like XGB, improving both model
efficiency and robustness. However, their performance can be hindered by hyperparameter
tuning challenges, and despite their power, simpler models such as LASSO and tree-
based methods often provide superior forecasts due to their interpretability and lower
computational cost. In the IDM, while DNNs show some strong performance, they are
frequently outperformed by RNNs like LSTMs and GRUs, which handle short-term price
fluctuations more effectively. This is particularly evident in real-time markets, where
DL models struggle to adapt to rapid price changes without more advanced attention
mechanisms. In the BM, DL models often lag behind ML models, and simpler statistical
models due to persistent issues capturing the extreme volatility and sudden price spikes
characteristic of these markets, leading to consistent overfitting. Despite their strong
performance in the DAM, the lack of adaptability in real-time, high-volatility markets limits
the broader application of DL models in the IDM and BM. Simpler models with built in
regularisation prove to be better suited for capturing short-term volatility in these markets,
although potential remains for statistical-DL hybrid models which remain underexplored
in the BM. Overall, while DL models are powerful tools for modelling non-linear dynamics

Energies 2025, 18, 3097

29 of 40

in the DAM, their performance in the IDM and BM is mixed, often requiring enhancements
such as attention mechanisms or hybrid architectures to fully leverage their potential.

4.2.4. Hybrid Models

Hybrid models have emerged as a powerful class of tools in EPF, addressing the
limitations of standalone statistical, ML, and DL models. Statistical hybrid models, such as
ARIMA-GARCH and FARX-LASSO, effectively combine the linear interpretability of AR
frameworks with enhanced handling of volatility, non-stationarity, and multicollinearity
through the integration of regularisation techniques and conditional variance modelling.
These models are particularly effective in structured markets like the DAM, where period-
icity and large datasets support decomposition-based approaches. Similarly, statistical–ML
hybrids, including combinations like WARIMA-RBF and SOM-SVR, apply non-linear learn-
ers to decomposed components of the time series, achieving improved accuracy through
multi-resolution learning. More recent innovations extend hybridisation to incorporate
PCA, evolutionary algorithms, and attention mechanisms, demonstrating versatility even
in data-scarce or noisy environments. In ML/DL hybrids, architectures exploit the comple-
mentary strengths of tree-based ensembles, RNNs, and signal decomposition methods to
model non-linearities and short-term volatility across all market types. ML-based hybrids,
such as XGB with adaptive DNNs or ensemble frameworks integrating RF, SVM, and
ARIMA, have shown exceptional performance in DAM settings. These models leverage
feature selection, Fourier/wavelet decomposition, and robust regularisation to improve
generalisability and interpretability. DL hybrid models push these boundaries further
by fusing CNNs, LSTMs, GRUs, and attention mechanisms into complex multi-layered
or ensemble-based systems capable of tracking high-frequency patterns and structural
shifts in the IDM and BM. Notably, BiLSTM-based hybrids integrated with decomposition
techniques and meta-heuristic optimisation strategies have demonstrated state-of-the-art
performance in volatile, real-time markets such as the British BM. Hybrid models con-
sistently outperform standalone approaches across markets, especially when addressing
market-specific challenges like seasonality, noise, data sparsity, and regime shifts. Their
ability to balance accuracy, interpretability, and adaptability has established them as the
dominant paradigm in DAM and IDM forecasting. However, applications in BM remain
underexplored, representing a key opportunity for future research.

4.3. Input Data Requirements and Model Sensitivities

The effectiveness of electricity price forecasting models is closely tied to the quality
and availability of input data. Classical statistical methods, particularly univariate models
like AR or ARIMA, primarily rely on historical price data and tend to be relatively robust
to missing values or incomplete datasets, making them suitable when exogenous inputs
are limited or unavailable. In contrast, models such as ARX, SARIMAX, and LEAR extend
these frameworks by incorporating exogenous variables—including demand forecasts,
renewable generation, and fuel prices—which enhances accuracy but increases sensitiv-
ity to data quality. Machine learning models, including tree-based ensembles like XGB
and LGBM, generally require extensive and well-structured feature sets; while they are
more flexible in handling missing data through internal mechanisms such as imputation
or feature importance weighting, their performance still depends on the relevance and
completeness of input features. Deep learning models, particularly recurrent architectures
like LSTM and GRU, demand large volumes of high-quality, multivariate time-series data
to effectively capture temporal dynamics. These models are highly sensitive to missing or
noisy inputs, often requiring careful preprocessing such as normalization, interpolation,
and feature engineering. Consequently, the choice of forecasting model must consider not

Energies 2025, 18, 3097

30 of 40

only predictive performance but also the feasibility of obtaining the necessary input data,
especially in real-time markets where data granularity and timeliness are critical.

4.4. Forecasting Across the Day-Ahead, Intra-Day, and Balancing Markets

The DAM remains the most extensively studied and methodologically mature among
electricity spot markets, largely due to its structured nature, longer forecasting horizon, the
availability of multiple public datasets, and relatively lower dependence on high-frequency
or real-time exogenous variables. Statistical models such as AR, ARIMA, and seasonal
variants have historically performed well in this context, especially when enhanced with
exogenous inputs, volatility models like GARCH, or regularisation techniques such as
LASSO, ridge, and elastic nets. ML models, particularly tree-based ensembles like XGB and
RF, also demonstrate strong and consistent performance in the DAM, balancing accuracy
and computational efficiency. DL methods—especially RNN variants such as LSTM, GRU,
and hybrid CNN-LSTM architectures—outperform statistical approaches by capturing
long-term dependencies and complex non-linear patterns, particularly when integrated
with attention mechanisms and decomposition techniques. The DAM’s relatively stable
temporal structure allows these models to capitalise on seasonality and trend information,
making it an ideal environment for methodological innovation and benchmarking.

In contrast, the IDM presents greater forecasting challenges due to its high-frequency
nature, limited lead time, and susceptibility to short-term volatility driven by renewables,
load fluctuations, and market trading behaviour. Many models that perform well in the
DAM struggle in the IDM, particularly time-series models like ARIMA and SARIMA,
which lack the flexibility to respond to fast-changing conditions. While ML models such
as XGB and LASSO have found moderate success, their performance is often hindered by
difficulties in capturing intra-day dependencies and abrupt price changes. DL models like
LSTM and GRU perform better in this space, particularly when paired with feature selec-
tion or hybrid decomposition methods. The lack of consistently available high-resolution
exogenous data further limits model performance in the IDM, underscoring the need for
models that can adapt rapidly with minimal prior information. The BM is the least studied
and most volatile of the three, with very short forecasting horizons and a high degree of
unpredictability due to its inherent stochastic nature, diminishes the effectiveness of many
conventional approaches. Simpler models like naive benchmarks often perform competi-
tively by capitalising on strong autocorrelations in real-time prices. Hybrid approaches and
DL models with attention mechanisms—particularly BiLSTM-based ensembles and Trans-
former hybrids—are beginning to show promise in the BM by capturing rapid price spikes
and noise patterns more effectively. Notably, statistical models like LEAR consistently
outperform more complex DL architectures, likely due to their robustness, lower tendency
to overfit, and better handling of sparse and volatile data. While hybrid and DL-based
models are advancing, the BM still lacks methodological consensus, with contrasting model
performance, proving an attractive avenue for future research.

4.5. Regional Trends in Model Usage

While electricity price forecasting methodologies are broadly applicable, their de-
ployment often reflects regional market characteristics, regulatory structures, and data
availability. For instance, SARIMAX and TBATS models have seen notable application in
European markets such as Denmark and Germany, where strong seasonal patterns and
structured DAM environments favour statistical approaches. In contrast, markets like
the Irish and British balancing markets favour simpler models such as LEAR and naive
baselines due to their robustness in high-volatility, low-data settings. In New Zealand,
GARCH models with feature selection have outperformed some ML models, likely due

Energies 2025, 18, 3097

31 of 40

to their capacity to model volatility in deregulated markets with limited real-time data.
Meanwhile, advanced DL and hybrid methods are more frequently explored in research
on the Chinese, Iranian, and North American markets, where larger datasets and more
computational resources are available. These regional trends suggest that model selection
is often shaped less by universal performance and more by local constraints, including data
resolution, market rules, and integration of renewables.

4.6. Evaluation Metrics—Persistent Issues

The selection of evaluation metrics in EPF continues to present methodological chal-
lenges, particularly when applied uniformly across markets with varying volatility, time
resolution, and regulatory conditions. Commonly used metrics such as mean absolute
error (MAE), mean squared error (MSE), and mean absolute percentage error (MAPE)
offer simplicity and interpretability but fall short in capturing the nuanced demands of
different forecasting environments. MAE, while less sensitive to outliers than MSE, is
scale-dependent and under-penalises large errors—an issue in volatile markets like the BM,
where sudden price spikes can have significant financial consequences. MSE, by contrast,
exaggerates the impact of extreme deviations, which may overstate model deficiencies in
high-variance settings, where even accurate models occasionally miss rare events. Both met-
rics also obscure the comparative effectiveness of models across different market contexts
due to their unstandardised nature. MAPE, despite its popularity in industry, performs
poorly when actual prices approach zero, which frequently occurs in real-time and high-
renewable-penetration markets. This results in undefined or disproportionately inflated
error values, rendering the metric unreliable. The symmetric MAPE (sMAPE) attempts to
address this instability but introduces interpretational difficulties of its own. The relative
MAE (rMAE), which compares model performance to a benchmark such as a naive or
LASSO model, offers more informative context for evaluation, especially in the IDM and
BM, where simple models often provide strong baselines. However, its usefulness hinges
on the appropriateness of the benchmark, which varies substantially across studies. The
weighted MAE (WMAE) introduces the possibility of assigning economic or operational
importance to certain observations, such as peak-hour prices, but its limited adoption in
academic work highlights a disconnect between research practice and operational priorities.
A persistent issue across the literature is the uniform application of these metrics regardless
of the forecast horizon, data granularity, or intended use of the forecast, whether for trading,
scheduling, or regulatory compliance. For example, using the same metrics to evaluate
more stable DAM forecasts and volatile IDM and BM forecasts fails to account for the
different risk profiles and error tolerances involved. Until a more context-sensitive and
application-aware framework is widely adopted, the evaluation of EPF models will remain
fragmented and potentially misleading, hindering the development of robust, transferable,
and operationally relevant forecasting solutions.

5. Conclusions

This review has mapped the evolution of EPF methodologies, with a focus on the DAM,
IDM, and BM. The field has progressed from early reliance on linear statistical models, such
as ARIMA, ARX, and GARCH, to ML, DL, and hybrid architectures capable of modelling
complex, non-linear market dynamics. While the DAM remains the most thoroughly
studied and methodologically developed market, the IDM and BM have gained increasing
attention due to their operational relevance in real-time forecasting, particularly in the
context of renewable integration and system flexibility. Our analysis highlights that no
single class of models consistently outperforms others across all market contexts. However,
hybrid approaches, combining the interpretability of statistical models with the adaptability

Energies 2025, 18, 3097

32 of 40

of ML and DL, frequently demonstrate strong performance. These frameworks, particularly
when enhanced with decomposition techniques, feature selection, attention mechanisms,
and ensembles, offer a balance between accuracy and flexibility. However, they often
come with added complexity, higher computational demands, and reduced transparency,
which can limit their deployment in operational settings. Significant challenges remain,
particularly in volatile and data-scarce environments, including the IDM and BM.

Statistical models, while efficient and interpretable, struggle to capture regime shifts
and rapid fluctuations. DL models, including LSTM, GRU, and Transformer-based architec-
tures, require large volumes of high-quality data and are prone to overfitting in low-data
or high-noise environments. Additionally, the inconsistent availability of high-frequency
exogenous variables, such as renewable generation forecasts, demand anomalies, and
cross-border flows, limits forecasting accuracy and generalisability across market types
and geographies. Compounding these issues is the lack of standardisation in back-testing
and real-time evaluation protocols, with inappropriate use of metrics like MAPE limiting
the evaluation and comparison of models. These challenges are exacerbated by the lack
of standardised benchmarks, open datasets, and reproducible code for hybrid models,
creating additional barriers for testing these approaches across different geographies or
market types, particularly when transitioning from DAM to real-time applications.

Looking ahead, the future of EPF lies in the development of models that are not
only accurate but also scalable, interpretable, and robust across diverse market structures.
Improving model performance in the IDM and BM, integrating higher-resolution exoge-
nous data, and adapting successful hybrid strategies from DAM, load, and photovoltaic
forecasting represent valuable directions. Equally important is the creation of standardised
benchmarking frameworks, the availability of open datasets, and systematic multi-market
validation to facilitate practical deployment. As electricity markets grow increasingly de-
centralised, data-driven, and renewable-centric, robust forecasting will remain fundamental
to facilitating efficient trading, reliable system operations, and agile market design.

In parallel with methodological advances, the use of forecast price values continues
to expand across electricity markets. Promising applications include strategic bidding in
wholesale and balancing markets, real-time dispatch optimisation, and portfolio risk man-
agement. In retail and prosumer contexts, forecast prices support demand-side response,
tariff design, and local energy trading. Additionally, system operators and aggregators
are increasingly leveraging forecasted prices for congestion management, reserve alloca-
tion, and ancillary service scheduling. As market mechanisms grow more dynamic and
decentralised, the integration of accurate and interpretable price forecasts into operational
decision making will be essential for achieving flexibility, efficiency, and resilience across
electricity systems.

Author Contributions: Study conception and design: C.O. and A.V.; acquisition, analysis, drawing
figures, and interpretation of data: C.O. and A.V.; drafting of manuscript: C.O., A.V. and S.P.; critical
revision: C.O., A.V. and S.P.; Review & Editing: M.B. All authors have read and agreed to the
published version of the manuscript.

Funding: This work was conducted with the financial support of Science Foundation Ireland under
Grant Nos. 12/RC/2289-P2 and 18/CRT/6223, which are co-funded under the European Regional
Development Fund. This research was partially supported by the EU’s Horizon Digital, Industry, and
Space program under grant agreement ID 101092989-DATAMITE. For the purpose of Open Access,
the author has applied a CC BY public copyright license to any Author Accepted Manuscript version
arising from this submission.

Institutional Review Board Statement: Not applicable.

Informed Consent Statement: Not applicable.

Energies 2025, 18, 3097

33 of 40

Data Availability Statement: The data was sourced from the SEMO and SEMOpx websites, compris-
ing historical and forward-looking data dating from 2019 to 2022. For interested readers the data for
the DAM and BM can be accessed here https://github.com/ciaranoc123/Balance-Market-Forecast.

Conflicts of Interest: The authors declare no conflicts of interest.

References

1.

2.

Ortner, A.; Totschnig, G. The future relevance of electricity balancing markets in Europe-A 2030 case study. Energy Strategy Rev.
2019, 24, 111–120. [CrossRef]
Koecklin, M.T.; Longoria, G.; Fitiwi, D.Z.; DeCarolis, J.F.; Curtis, J. Public acceptance of renewable electricity generation and
transmission network developments: Insights from Ireland. Energy Policy 2021, 151, 112185. [CrossRef]

3. Meles, T.H.; Ryan, L. Adoption of renewable home heating systems: An agent-based model of heat pumps in Ireland. Renew.

4.

5.

6.

7.

8.

9.

Sustain. Energy Rev. 2022, 169, 112853. [CrossRef]
Lago, J.; Marcjasz, G.; De Schutter, B.; Weron, R. Forecasting day-ahead electricity prices: A review of state-of-the-art algorithms,
best practices and an open-access benchmark. Appl. Energy 2021, 293, 116983. [CrossRef]
Yang, Z.; Ce, L.; Lian, L. Electricity price forecasting by a hybrid model, combining wavelet transform, ARMA and kernel-based
extreme learning machine methods. Appl. Energy 2017, 190, 291–305. [CrossRef]
Lago, J.; De Ridder, F.; Vrancx, P.; De Schutter, B. Forecasting day-ahead electricity prices in Europe: The importance of considering
market integration. Appl. Energy 2018, 211, 890–903. [CrossRef]
Xu, J.; Baldick, R. Day-ahead price forecasting in ERCOT market using neural network approaches. In Proceedings of the Tenth
ACM International Conference on Future Energy Systems, Phoenix, AZ, USA, 25–28 June 2019; pp. 486–491.
Zahid, M.; Ahmed, F.; Javaid, N.; Abbasi, R.A.; Zainab Kazmi, H.S.; Javaid, A.; Bilal, M.; Akbar, M.; Ilahi, M. Electricity price and
load forecasting using enhanced convolutional neural network and enhanced support vector regression in smart grids. Electronics
2019, 8, 122. [CrossRef]
Heidarpanah, M.; Hooshyaripor, F.; Fazeli, M. Daily electricity price forecasting using artificial intelligence models in the Iranian
electricity market. Energy 2023, 263, 126011. [CrossRef]

10. Aggarwal, S.K.; Saini, L.M.; Kumar, A. Electricity price forecasting in deregulated markets: A review and evaluation. Int. J. Electr.

Power Energy Syst. 2009, 31, 13–22. [CrossRef]

11. Weron, R. Electricity price forecasting: A review of the state-of-the-art with a look into the future.

Int. J. Forecast. 2014,

30, 1030–1081. [CrossRef]

12. Zhang, F.; Fleyeh, H. A review of single artificial neural network models for electricity spot price forecasting. In Proceedings of
the 2019 16th International Conference on the European Energy Market (EEM), Ljubljana, Slovenia, 18–20 September 2019; IEEE:
Piscataway, NJ, USA, 2019; pp. 1–6.

13. Acaro ˘glu, H.; García Márquez, F.P. Comprehensive review on electricity market price and load forecasting based on wind energy.

14.

Energies 2021, 14, 7473. [CrossRef]
J˛edrzejewski, A.; Lago, J.; Marcjasz, G.; Weron, R. Electricity price forecasting: The dawn of machine learning. IEEE Power Energy
Mag. 2022, 20, 24–31. [CrossRef]

15. Newbery, D.; Strbac, G.; Viehoff, I. The benefits of integrating European electricity markets. Energy Policy 2016, 94, 253–263.

16.

[CrossRef]
Ilea, V.; Bovo, C. European day-ahead electricity market coupling: Discussion, modeling, and case study. Electr. Power Syst. Res.
2018, 155, 80–92.

17. Martinez-Anido, C.B.; Brinkman, G.; Hodge, B.M. The impact of wind power on electricity prices. Renew. Energy 2016, 94, 474–487.

[CrossRef]

18. Ugurlu, U.; Oksuz, I.; Tas, O. Electricity price forecasting using recurrent neural networks. Energies 2018, 11, 1255. [CrossRef]
19. Lago, J.; De Ridder, F.; De Schutter, B. Forecasting spot electricity prices: Deep learning approaches and empirical comparison of

traditional algorithms. Appl. Energy 2018, 221, 386–405. [CrossRef]

20. Chen, Y.; Wang, Y.; Ma, J.; Jin, Q. BRIM: An accurate electricity spot price prediction scheme-based bidirectional recurrent neural

network and integrated market. Energies 2019, 12, 2241. [CrossRef]

21. Li, W.; Becker, D.M. Day-ahead electricity price prediction applying hybrid models of LSTM-based deep learning methods and

22.

feature selection algorithms under consideration of market coupling. Energy 2021, 237, 121543. [CrossRef]
Shinde, P.; Amelin, M. A literature review of intraday electricity markets and prices. In Proceedings of the 2019 IEEE Milan
PowerTech, Milan, Italy, 23–27 June 2019; pp. 1–6.

Energies 2025, 18, 3097

34 of 40

23. Monteiro, C.; Ramirez-Rosado, I.J.; Fernandez-Jimenez, L.A.; Conde, P. Short-term price forecasting models based on artificial

neural networks for intraday sessions in the Iberian electricity market. Energies 2016, 9, 721. [CrossRef]

24. Andrade, J.R.; Filipe, J.; Reis, M.; Bessa, R.J. Probabilistic price forecasting for day-ahead and intraday markets: Beyond the

statistical model. Sustainability 2017, 9, 1990. [CrossRef]

25. Uniejewski, B.; Marcjasz, G.; Weron, R. Understanding intraday electricity markets: Variable selection and very short-term price

forecasting using LASSO. Int. J. Forecast. 2019, 35, 1533–1547. [CrossRef]

26. Narajewski, M.; Ziel, F. Ensemble forecasting for intraday electricity prices: Simulating trajectories. Appl. Energy 2020, 279, 115801.

[CrossRef]

27. Koch, C.; Hirth, L. Short-term electricity trading for system balancing: An empirical analysis of the role of intraday trading in

balancing Germany’s electricity system. Renew. Sustain. Energy Rev. 2019, 113, 109275. [CrossRef]

28. Birkeland, D.; AlSkaif, T. Research areas and methods of interest in European intraday electricity market research—A systematic

literature review. Sustain. Energy Grids Netw. 2024, 38, 101368. [CrossRef]

29. Zachmann, G.; Hirth, L.; Heussaff, C.; Schlecht, I.; Mühlenpfordt, J.; Eicke, A. The Design of the European Electricity Market–Current

Proposals and Ways Ahead; European Parliament: Luxembourg, 2023.

30. Dumas, J.; Boukas, I.; de Villena, M.M.; Mathieu, S.; Cornélusse, B. Probabilistic forecasting of imbalance prices in the belgian
context. In Proceedings of the 2019 16th International Conference on the European Energy Market (EEM), Ljubljana, Slovenia,
18–20 September 2019; IEEE: Piscataway, NJ, USA, 2019; pp. 1–7.

31. Narajewski, M. Probabilistic forecasting of German electricity imbalance prices. Energies 2022, 15, 4976. [CrossRef]
32. O’Connor, C.; Collins, J.; Prestwich, S.; Visentin, A. Electricity Price Forecasting in the Irish Balancing Market. Energy Strategy Rev.

2024, 54, 101436. [CrossRef]

33. Van der Veen, R.A.; Hakvoort, R.A. The electricity balancing market: Exploring the design challenge. Util. Policy 2016, 43, 186–194.

[CrossRef]

34. Eicke, A.; Ruhnau, O.; Hirth, L. Electricity balancing as a market equilibrium. Energy Econ. 2021, 102, 105455. [CrossRef]
35.
36.

SEMO. Markets and Timelines. Available online: https://www.sem-o.com/markets (accessed on 9 June 2025).
Silva-Rodriguez, L.; Sanjab, A.; Fumagalli, E.; Virag, A.; Gibescu, M. Short term wholesale electricity market designs: A review of
identified challenges and promising solutions. Renew. Sustain. Energy Rev. 2022, 160, 112228. [CrossRef]

37. Peura, H.; Bunn, D.W. Renewable power and electricity prices: The impact of forward markets. Manag. Sci. 2021, 67, 4772–4788.

[CrossRef]

38. Rancilio, G.; Rossi, A.; Falabretti, D.; Galliani, A.; Merlo, M. Ancillary services markets in europe: Evolution and regulatory

trade-offs. Renew. Sustain. Energy Rev. 2022, 154, 111850. [CrossRef]

39. Cramton, P.; Ockenfels, A.; Stoft, S. Capacity market fundamentals. Econ. Energy Environ. Policy 2013, 2, 27–46. [CrossRef]
40.

Sarkar, V.; Khaparde, S.A. A comprehensive assessment of the evolution of financial transmission rights. IEEE Trans. Power Syst.
2008, 23, 1783–1795. [CrossRef]

41. Maciejowska, K.; Weron, R. Short-and mid-term forecasting of baseload electricity prices in the UK: The impact of intra-day price

relationships and market fundamentals. IEEE Trans. Power Syst. 2015, 31, 994–1005. [CrossRef]

42. Popławski, T.; Dudek, G.; Łyp, J. Forecasting methods for balancing energy market in Poland. Int. J. Electr. Power Energy Syst.

2015, 65, 94–101. [CrossRef]

43. Klæboe, G.; Eriksrud, A.L.; Fleten, S.E. Benchmarking time series based forecasting models for electricity balancing market prices.

Energy Syst. 2015, 6, 43–61. [CrossRef]

44. Girish, G.P. Spot electricity price forecasting in Indian electricity market using autoregressive-GARCH models. Energy Strategy

Rev. 2016, 11, 52–57. [CrossRef]

45. Olivares, K.G.; Challu, C.; Marcjasz, G.; Weron, R.; Dubrawski, A. Neural basis expansion analysis with exogenous variables:

Forecasting electricity prices with NBEATSx. Int. J. Forecast. 2023, 39, 884–900. [CrossRef]

46. Billé, A.G.; Gianfreda, A.; Del Grosso, F.; Ravazzolo, F. Forecasting electricity prices with expert, linear, and nonlinear models.

Int. J. Forecast. 2023, 39, 570–586. [CrossRef]

47. Ziel, F. Forecasting electricity spot prices using lasso: On capturing the autoregressive intraday structure. IEEE Trans. Power Syst.

2016, 31, 4977–4987. [CrossRef]

48. Özen, K.; Yıldırım, D. Application of bagging in day-ahead electricity price forecasting and factor augmentation. Energy Econ.

2021, 103, 105573. [CrossRef]

49. Englund, A. Evaluation of Machine Learning Models for Intraday Price Forecasting in the Renewable Energy Sector. Master’s

Thesis, Uppsala University, Uppsala, Sweden, 2024.

50. Contreras, J.; Espinola, R.; Nogales, F.J.; Conejo, A.J. ARIMA models to predict next-day electricity prices. IEEE Trans. Power Syst.

2003, 18, 1014–1020. [CrossRef]

Energies 2025, 18, 3097

35 of 40

51. Cuaresma, J.C.; Hlouskova, J.; Kossmeier, S.; Obersteiner, M. Forecasting electricity spot-prices using linear univariate time-series

models. Appl. Energy 2004, 77, 87–106. [CrossRef]

52. Conejo, A.J.; Plazas, M.A.; Espinola, R.; Molina, A.B. Day-ahead electricity price forecasting using the wavelet transform and

ARIMA models. IEEE Trans. Power Syst. 2005, 20, 1035–1042. [CrossRef]

53. Yang, Y.; Tan, Z.; Yang, H.; Ruan, G.; Zhong, H.; Liu, F. Short-term electricity price forecasting based on graph convolution

network and attention mechanism. IET Renew. Power Gener. 2022, 16, 2481–2492. [CrossRef]

54. Poggi, A.; Di Persio, L.; Ehrhardt, M. Electricity price forecasting via statistical and deep learning approaches: The german case.

AppliedMath 2023, 3, 316–342. [CrossRef]

55. Kılıç, D.K.; Nielsen, P.; Thibbotuwawa, A. Intraday Electricity Price Forecasting via LSTM and Trading Strategy for the Power

Market: A Case Study of the West Denmark DK1 Grid Region. Energies 2024, 17, 2909. [CrossRef]

56. Knittel, C.R.; Roberts, M.R. An empirical examination of restructured electricity prices. Energy Econ. 2005, 27, 791–817. [CrossRef]
57. Diongue, A.K.; Guegan, D.; Vignal, B. Forecasting electricity spot market prices with a k-factor GIGARCH process. Appl. Energy

2009, 86, 505–510. [CrossRef]

58. Kapoor, G.; Wichitaksorn, N. Electricity price forecasting in New Zealand: A comparative analysis of statistical and machine

59.

learning models with feature selection. Appl. Energy 2023, 347, 121446. [CrossRef]
Ishak, I.; Othman, N.S.; Harun, N.H. Forecasting electricity consumption of Malaysia’s residential sector: Evidence from an
exponential smoothing model. F1000Research 2022, 11, 54. [CrossRef]

60. Woo, G.; Liu, C.; Sahoo, D.; Kumar, A.; Hoi, S. Etsformer: Exponential smoothing transformers for time-series forecasting. arXiv

2022, arXiv:2202.01381.

61. Karabiber, O.A.; Xydis, G. Electricity price forecasting in the Danish day-ahead market using the TBATS, ANN and ARIMA

methods. Energies 2019, 12, 928. [CrossRef]

62. Gellert, A.; Fiore, U.; Florea, A.; Chis, R.; Palmieri, F. Forecasting electricity consumption and production in smart homes through

63.

statistical methods. Sustain. Cities Soc. 2022, 76, 103426. [CrossRef]
Iqbal, R.; Mokhlis, H.; Khairuddin, A.S.M.; Ismail, S.; Muhammad, M.A. Optimized Gated Recurrent Unit for Mid-Term Electricity
Price Forecasting. Comput. Syst. Sci. Eng. 2022, 43. [CrossRef]

64. Rao, C.; Zhang, Y.; Wen, J.; Xiao, X.; Goh, M. Energy demand forecasting in China: A support vector regression-compositional

data second exponential smoothing model. Energy 2023, 263, 125955. [CrossRef]

65. Lisi, F.; Shah, I. Joint component estimation for electricity price forecasting using functional models. Energies 2024, 17, 3461.

[CrossRef]

66. Beigaite, R.; Krilaviˇcius, T.; Man, K.L. Electricity Price Forecasting for Nord Pool Data. In Proceedings of the 2018 International
Conference on Platform Technology and Service (PlatCon), Jeju, Republic of Korea, 29–31 January 2018; pp. 1–6. [CrossRef]
67. Marcjasz, G.; Uniejewski, B.; Weron, R. Beating the naïve—Combining LASSO with naïve intraday electricity price forecasts.

Energies 2020, 13, 1667. [CrossRef]

68. Oksuz, I.; Ugurlu, U. Neural network based model comparison for intraday electricity price forecasting. Energies 2019, 12, 4557.

[CrossRef]

69. Kath, C.; Ziel, F. The value of forecasts: Quantifying the economic gains of accurate quarter-hourly electricity price forecasts.

Energy Econ. 2018, 76, 411–423. [CrossRef]

70. Nickelsen, D.; Müller, G. Bayesian hierarchical probabilistic forecasting of intraday electricity prices. Appl. Energy 2025,

380, 124975. [CrossRef]

71. Maciejowska, K.; Nitka, W.; Weron, T. Day-ahead vs. Intraday—Forecasting the price spread to maximize economic benefits.

Energies 2019, 12, 631. [CrossRef]

72. Kotsias, P.C. Forecasting Electricity Prices for Intraday Markets with Machine Learning: An exploratory comparison of the state

of the art. IET Conf. Proc. 2022, 2024.

73. Uniejewski, B. Regularization for electricity price forecasting. arXiv 2024, arXiv:2404.03968. [CrossRef]
74.

Jakaša, T.; Androˇcec, I.; Sprˇci´c, P. Electricity price forecasting—ARIMA model approach.
In Proceedings of the 2011 8th
international conference on the European energy market (EEM), Zagreb, Croatia, 25–27 May 2011; IEEE: Piscataway, NJ, USA,
2011; pp. 222–225.

75. Lehna, M.; Scheller, F.; Herwartz, H. Forecasting day-ahead electricity prices: A comparison of time series and neural network

models taking external regressors into account. Energy Econ. 2022, 106, 105742. [CrossRef]

76. Bozlak, Ç.B.; Ya¸sar, C.F. An optimized deep learning approach for forecasting day-ahead electricity prices. Electr. Power Syst. Res.

2024, 229, 110129. [CrossRef]

77. Kitsatoglou, A.; Georgopoulos, G.; Papadopoulos, P.; Antonopoulos, H. An ensemble approach for enhanced Day-Ahead price

forecasting in electricity markets. Expert Syst. Appl. 2024, 256, 124971. [CrossRef]

Energies 2025, 18, 3097

36 of 40

78. Narajewski, M.; Ziel, F. Econometric modelling and forecasting of intraday electricity prices. J. Commod. Mark. 2020, 19, 100107.

79.

[CrossRef]
Serafin, T.; Marcjasz, G.; Weron, R. Trading on short-term path forecasts of intraday electricity prices. Energy Econ. 2022,
112, 106125. [CrossRef]

80. Agakishiev, I.; Härdle, W.K.; Kopa, M.; Kozmik, K.; Petukhina, A. Multivariate probabilistic forecasting of electricity prices with

trading applications. Energy Econ. 2025, 141, 108008. [CrossRef]

81. Uniejewski, B.; Nowotarski, J.; Weron, R. Automated variable selection and shrinkage for day-ahead electricity price forecasting.

Energies 2016, 9, 621. [CrossRef]

82. Tschora, L.; Pierre, E.; Plantevit, M.; Robardet, C. Electricity price forecasting on the day-ahead market using machine learning.

Appl. Energy 2022, 313, 118752. [CrossRef]

83. Marcjasz, G.; Narajewski, M.; Weron, R.; Ziel, F. Distributional neural networks for electricity price forecasting. Energy Econ. 2023,

125, 106843. [CrossRef]

84. Gunduz, S.; Ugurlu, U.; Oksuz, I. Transfer learning for electricity price forecasting. Sustain. Energy Grids Netw. 2023, 34, 100996.

[CrossRef]

85. Yang, Y.; Guo, J.; Li, Y.; Zhou, J. Forecasting day-ahead electricity prices with spatial dependence.

Int. J. Forecast. 2024,

40, 1255–1270. [CrossRef]

86. O’Connor, C.; Bahloul, M.; Rossi, R.; Prestwich, S.; Visentin, A. Conformal Prediction for Electricity Price Forecasting in the

Day-Ahead and Real-Time Balancing Market. arXiv 2025, arXiv:cs.LG/2502.04935.

87. Nogales, F.J.; Contreras, J.; Conejo, A.J.; Espínola, R. Forecasting next-day electricity prices by time series models. IEEE Trans.

Power Syst. 2002, 17, 342–348. [CrossRef]

88. García González, J.; Barquín Gil, J.; Dueñas Martínez, P. A Hybrid Approach for Modeling Electricity Price Series in the Medium
Term. 2008. Available online: https://www.researchgate.net/publication/255586295_A_hybrid_approach_for_modeling_
electricity_price_series_in_the_medium_term (accessed on 9 June 2025).

89. Durante, F.; Gianfreda, A.; Ravazzolo, F.; Rossini, L. A multivariate dependence analysis for electricity prices, demand and

renewable energy sources. Inf. Sci. 2022, 590, 74–89. [CrossRef]

90. Arrieta-Prieto, M.; Schell, K.R. Spatio-temporal probabilistic forecasting of wind power for multiple farms: A copula-based

91.

hybrid model. Int. J. Forecast. 2022, 38, 300–320. [CrossRef]
Feijoo, F.; Silva, W.; Das, T.K. A computationally efficient electricity price forecasting model for real time energy markets. Energy
Convers. Manag. 2016, 113, 27–35. [CrossRef]

92. Ali, M.; Khan, Z.A.; Mujeeb, S.; Abbas, S.; Javaid, N. Short-term electricity price and load forecasting using enhanced support
vector machine and K-nearest neighbor. In Proceedings of the 2019 Sixth HCT Information Technology Trends (ITT), Ras Al
Khaimah, United Arab Emirates, 20–21 November 2019; IEEE: Piscataway, NJ, USA, 2019; pp. 79–83.

93. Ashfaq, T.; Javaid, N. Short-term electricity load and price forecasting using enhanced KNN. In Proceedings of the 2019
International Conference on Frontiers of Information Technology (FIT), Islamabad, Pakistan, 16–18 December 2019; IEEE:
Piscataway, NJ, USA, 2019; pp. 266–2665.
Johannesen, N.J.; Kolhe, M.; Goodwin, M. Deregulated electric energy price forecasting in nordpool market using regression
techniques. In Proceedings of the 2019 IEEE Sustainable Power and Energy Conference (iSPEC), Beijing, China, 21–23 November
2019; IEEE: Piscataway, NJ, USA, 2019; pp. 1932–1938.

94.

95. Wang, P.; Xu, K.; Ding, Z.; Du, Y.; Liu, W.; Sun, B.; Zhu, Z.; Tang, H. An online electricity market price forecasting method via

random forest. IEEE Trans. Ind. Appl. 2022, 58, 7013–7021. [CrossRef]

96. Beltrán, S.; Castro, A.; Irizar, I.; Naveran, G.; Yeregui, I. Framework for collaborative intelligence in forecasting day-ahead

electricity price. Appl. Energy 2022, 306, 118049. [CrossRef]

97. Peng, Y.; Wang, Z.; Castillo, I.; LaGrande, G.; Jiang, S. A New Modeling Framework for Real-Time Extreme Electricity Price

98.

99.

Forecasting. IFAC-PapersOnLine 2024, 58, 899–904. [CrossRef]
Sansom, D.C.; Downs, T.; Saha, T.K. Evaluation of support vector machine based forecasting tool in electricity price forecasting
for Australian national electricity market participants. J. Electr. Electron. Eng. Aust. 2003, 22, 227–233.
Fan, S.; Mao, C.; Chen, L. Next-day electricity-price forecasting using a hybrid network.
1, 176–182. [CrossRef]

IET Gener. Transm. Distrib. 2007,

100. Che, J.; Wang, J. Short-term electricity prices forecasting based on support vector regression and auto-regressive integrated

moving average modeling. Energy Convers. Manag. 2010, 51, 1911–1917. [CrossRef]

101. Zhang, F.; Fleyeh, H.; Bales, C. A hybrid model based on bidirectional long short-term memory neural network and Catboost for

short-term electricity spot price forecasting. J. Oper. Res. Soc. 2022, 73, 301–325. [CrossRef]

102. Cantillo-Luna, S.; Moreno-Chuquen, R.; Chamorro, H.R.; Riquelme-Dominguez, J.M.; Gonzalez-Longatt, F. Locational marginal

price forecasting using svr-based multi-output regression in electricity markets. Energies 2022, 15, 293. [CrossRef]

Energies 2025, 18, 3097

37 of 40

103. Deng, S.; Inekwe, J.; Smirnov, V.; Wait, A.; Wang, C. Seasonality in deep learning forecasts of electricity imbalance prices. Energy

Econ. 2024, 137, 107770. [CrossRef]

104. González, C.; Mira, J.M.; Ojeda, J.A. Applying Multi-Output Random Forest Models to Electricity Price Forecast. 2016. Available
online: https://www.researchgate.net/publication/308384009_Applying_Multi-Output_Random_Forest_Models_to_Electricity_
Price_Forecast (accessed on 9 June 2025).

105. Kara, M.; Atici, K.B.; Ulucan, A. Price and volatility forecasting in electricity with support vector regression and random forest.
In Applied Operations Research and Financial Modelling in Energy: Practical Applications and Implications; Springer: Berlin/Heidelberg,
Germany, 2021; pp. 101–124.

106. Alkawaz, A.N.; Abdellatif, A.; Kanesan, J.; Khairuddin, A.S.M.; Gheni, H.M. Day-ahead electricity price forecasting based on

hybrid regression model. IEEE Access 2022, 10, 108021–108033. [CrossRef]

107. Xie, H.; Chen, S.; Lai, C.; Ma, G.; Huang, W. Forecasting the clearing price in the day-ahead spot market using eXtreme Gradient

Boosting. Electr. Eng. 2022, 104, 1607–1621. [CrossRef]

108. Mei, J.; He, D.; Harley, R.; Habetler, T.; Qu, G. A random forest method for real-time price forecasting in New York electricity
market. In Proceedings of the 2014 IEEE PES General Meeting|Conference & Exposition, Chicago, IL, USA, 14–17 April 2014;
IEEE: Piscataway, NJ, USA, 2014; pp. 1–5.

109. O’Connor, C.; Collins, J.; Prestwich, S.; Visentin, A. Optimising quantile-based trading strategies in electricity arbitrage. Energy

AI 2025, 20, 100476. [CrossRef]

110. Huang, S.; Shi, J.; Wang, B.; An, N.; Li, L.; Hou, X.; Wang, C.; Zhang, X.; Wang, K.; Li, H.; et al. A hybrid framework for day-ahead

electricity spot-price forecasting: A case study in China. Appl. Energy 2024, 373, 123863. [CrossRef]

111. Cai, R.; Xie, S.; Wang, B.; Yang, R.; Xu, D.; He, Y. Wind speed forecasting based on extreme gradient boosting. IEEE Access 2020,

8, 175063–175069. [CrossRef]

112. Qinghe, Z.; Wen, X.; Boyan, H.; Jong, W.; Junlong, F. Optimised extreme gradient boosting model for short term electric load

demand forecasting of regional grid system. Sci. Rep. 2022, 12, 19282. [CrossRef]

113. Rafi, S.H.; Mahdi, M.M. A short-term load forecasting technique using extreme gradient boosting algorithm. In Proceedings
of the 2021 IEEE PES Innovative Smart Grid Technologies-Asia (ISGT Asia), Brisbane, Australia, 5–8 December 2021; IEEE:
Piscataway, NJ, USA, 2021; pp. 1–5.

114. Suvarna, M.; Pravin, P.; Yap, K.S.; Wang, X. Application of machine learning and big data for smart energy management in
manufacturing. In Computer Aided Chemical Engineering; Elsevier: Amsterdam, The Netherlands, 2022; Volume 49, pp. 1699–1704.
115. Malakouti, S.M. Use machine learning algorithms to predict turbine power generation to replace renewable energy with fossil

fuels. Energy Explor. Exploit. 2023, 41, 836–857. [CrossRef]

116. Lucas, A.; Pegios, K.; Kotsakis, E.; Clarke, D. Price forecasting for the balancing energy market using machine-learning regression.

Energies 2020, 13, 5420. [CrossRef]

117. O’Connor, C.; Prestwich, S.; Visentin, A. Conformal Prediction Techniques for Electricity Price Forecasting. In Proceedings of
the International Workshop on Advanced Analytics and Learning on Temporal Data, Vilnius, Lithuania, 9–13 September 2024;
Springer: Berlin/Heidelberg, Germany, 2024; pp. 1–17.

118. Hinton, G.E.; Osindero, S.; Teh, Y.W. A Fast Learning Algorithm for Deep Belief Nets. Neural Comput. 2006, 18, 1527–1554.

[CrossRef]

119. Goodfellow, I.; Bengio, Y.; Courville, A. Deep Learning; MIT Press: Cambridge, MA, USA, 2016.
120. Krizhevsky, A.; Sutskever, I.; Hinton, G.E. Imagenet classification with deep convolutional neural networks. Adv. Neural Inf.

Process. Syst. 2012, 25. [CrossRef]

121. Hinton, G.; Deng, L.; Yu, D.; Dahl, G.E.; Mohamed, A.r.; Jaitly, N.; Senior, A.; Vanhoucke, V.; Nguyen, P.; Sainath, T.N.; et al. Deep
neural networks for acoustic modeling in speech recognition: The shared views of four research groups. IEEE Signal Process. Mag.
2012, 29, 82–97. [CrossRef]

122. Bahdanau, D.; Cho, K.; Bengio, Y. Neural machine translation by jointly learning to align and translate. arXiv 2014, arXiv:1409.0473.
123. Wang, H.; Wang, G.; Li, G.; Peng, J.; Liu, Y. Deep belief network based deterministic and probabilistic wind speed forecasting

approach. Appl. Energy 2016, 182, 80–93. [CrossRef]

124. Coelho, I.M.; Coelho, V.N.; Luz, E.J.d.S.; Ochi, L.S.; Guimaraes, F.G.; Rios, E. A GPU deep learning metaheuristic based model for

time series forecasting. Appl. Energy 2017, 201, 412–418. [CrossRef]

125. Atef, S.; Eltawil, A.B. A comparative study using deep learning and support vector regression for electricity price forecasting in
smart grids. In Proceedings of the 2019 IEEE 6th International Conference on Industrial Engineering and Applications (ICIEA),
Tokyo, Japan, 12–15 April 2019; IEEE: Piscataway, NJ, USA, 2019; pp. 603–607.

126. Luo, S.; Weng, Y. A two-stage supervised learning approach for electricity price forecasting by leveraging different data sources.

Appl. Energy 2019, 242, 1497–1512. [CrossRef]

Energies 2025, 18, 3097

38 of 40

127. Mujeeb, S.; Javaid, N. ESAENARX and DE-RELM: Novel schemes for big data predictive analytics of electricity load and price.

Sustain. Cities Soc. 2019, 51, 101642. [CrossRef]

128. Schnürch, S.; Wagner, A. Machine learning on epex order books: Insights and forecasts. arXiv 2019, arXiv:1906.06248.
129. Khan, Z.A.; Fareed, S.; Anwar, M.; Naeem, A.; Gul, H.; Arif, A.; Javaid, N. Short term electricity price forecasting through
In Web, Artificial Intelligence and Network Applications: Proceedings of the Workshops of the 34th
convolutional neural network.
International Conference on Advanced Information Networking and Applications (WAINA-2020); Springer: Berlin/Heidelberg, Germany,
2020; pp. 1181–1188.

130. Yang, H.; Schell, K.R. QCAE: A quadruple branch CNN autoencoder for real-time electricity price forecasting. Int. J. Electr. Power

Energy Syst. 2022, 141, 108092. [CrossRef]

131. Pourdaryaei, A.; Mohammadi, M.; Mubarak, H.; Abdellatif, A.; Karimi, M.; Gryazina, E.; Terzija, V. A new framework for
electricity price forecasting via multi-head self-attention and CNN-based techniques in the competitive electricity market. Expert
Syst. Appl. 2024, 235, 121207. [CrossRef]

132. Hochreiter, S. Long Short-Term Memory; Neural Computation MIT-Press: Cambridge, MA, USA, 1997.
133. Chinnathambi, R.A.; Plathottam, S.J.; Hossen, T.; Nair, A.S.; Ranganathan, P. Deep neural networks for day-ahead electricity price
markets. In Proceedings of the 2018 IEEE Electrical Power and Energy Conference (EPEC), Toronto, ON, Canada, 10–11 October
2018; IEEE: Piscataway, NJ, USA, 2018; pp. 1–6.

134. Memarzadeh, G.; Keynia, F. Short-term electricity load and price forecasting by a new optimal LSTM-NN based prediction

algorithm. Electr. Power Syst. Res. 2021, 192, 106995. [CrossRef]

135. Meng, A.; Wang, P.; Zhai, G.; Zeng, C.; Chen, S.; Yang, X.; Yin, H. Electricity price forecasting with high penetration of renewable

energy using attention-based LSTM network trained by crisscross optimization. Energy 2022, 254, 124212. [CrossRef]

136. Zhu, Y.; Dai, R.; Liu, G.; Wang, Z.; Lu, S. Power market price forecasting via deep learning. In Proceedings of the IECON 2018-44th
Annual Conference of the IEEE Industrial Electronics Society, Washington, DC, USA, 21–23 October 2018; IEEE: Piscataway, NJ,
USA, 2018; pp. 4935–4939.

137. Zhou, S.; Zhou, L.; Mao, M.; Tai, H.M.; Wan, Y. An optimized heterogeneous structure LSTM network for electricity price

forecasting. IEEE Access 2019, 7, 108161–108173. [CrossRef]

138. Kuo, P.H.; Huang, C.J. An electricity price forecasting model by hybrid structured deep neural networks. Sustainability 2018,

10, 1280. [CrossRef]

139. Chang, Z.; Zhang, Y.; Chen, W. Effective adam-optimized LSTM neural network for electricity price forecasting. In Proceedings
of the 2018 IEEE 9th International Conference on Software Engineering and Service Science (ICSESS), Beijing, China, 23–25
November 2018; IEEE: Piscataway, NJ, USA, 2018; pp. 245–248.

140. Rezaei, N.; Rajabi, R.; Estebsari, A. Electricity price forecasting model based on gated recurrent units. In Proceedings of the 2022
IEEE International Conference on Environment and Electrical Engineering and 2022 IEEE Industrial and Commercial Power
Systems Europe (EEEIC/I&CPS Europe), Prague, Czech Republic, 28 June–1 July 2022; IEEE: Piscataway, NJ, USA, 2022; pp. 1–5.

141. Molin, L. Predicting Electricity Imbalance Prices. Ph.D. Thesis, Tilburg University, Tilburg, The Netherlands, 2023.
142. Gomez, W.; Wang, F.K.; Amogne, Z.E. Electricity Load and Price Forecasting Using a Hybrid Method Based Bidirectional Long

Short-Term Memory with Attention Mechanism Model. Int. J. Energy Res. 2023, 2023, 3815063. [CrossRef]

143. Zhang, S.; Robinson, E.; Basu, M. Wind power forecasting based on a novel gated recurrent neural network model. Wind. Energy

Eng. Res. 2024, 1, 100004. [CrossRef]

144. Xiong, X.; Qing, G. A hybrid day-ahead electricity price forecasting framework based on time series. Energy 2023, 264, 126099.

[CrossRef]

145. Shi, W.; Wang, Y.F. A robust electricity price forecasting framework based on heteroscedastic temporal Convolutional Network.

Int. J. Electr. Power Energy Syst. 2024, 161, 110177. [CrossRef]

146. López Santos, M.; García-Santiago, X.; Echevarría Camarero, F.; Blázquez Gil, G.; Carrasco Ortega, P. Application of temporal

fusion transformer for day-ahead PV power forecasting. Energies 2022, 15, 5232. [CrossRef]

147. Nazir, A.; Shaikh, A.K.; Shah, A.S.; Khalil, A. Forecasting Energy Consumption Demand of Customers in Smart Grid Using

Temporal Fusion Transformer. Results Eng. 2023, 17, 100888. [CrossRef]

148. Jiang, H.; Pan, S.; Dong, Y.; Wang, J. Probabilistic electricity price forecasting based on penalized temporal fusion transformer.

J. Forecast. 2024, 43, 1465–1491. [CrossRef]

149. Salinas, D.; Flunkert, V.; Gasthaus, J.; Januschowski, T. DeepAR: Probabilistic forecasting with autoregressive recurrent networks.

Int. J. Forecast. 2020, 36, 1181–1191. [CrossRef]

150. Stefenon, S.F.; Seman, L.O.; Mariani, V.C.; Coelho, L.d.S. Aggregating prophet and seasonal trend decomposition for time series

forecasting of Italian electricity spot prices. Energies 2023, 16, 1371. [CrossRef]

Energies 2025, 18, 3097

39 of 40

151. Shohan, M.J.A.; Faruque, M.O.; Foo, S.Y. Forecasting of electric load using a hybrid LSTM-neural prophet model. Energies 2022,

15, 2158. [CrossRef]

152. Guo, Y.; Du, Y.; Wang, P.; Tian, X.; Xu, Z.; Yang, F.; Chen, L.; Wan, J. A hybrid forecasting method considering the long-term

dependence of day-ahead electricity price series. Electr. Power Syst. Res. 2024, 235, 110841. [CrossRef]

153. Nyangon, J.; Akintunde, R. Principal component analysis of day-ahead electricity price forecasting in CAISO and its implications

for highly integrated renewable energy markets. Wiley Interdiscip. Rev. Energy Environ. 2024, 13, e504. [CrossRef]

154. Sapnken, F.E.; Tazehkandgheshlagh, A.K.; Diboma, B.S.; Hamaidi, M.; Noumo, P.G.; Wang, Y.; Tamba, J.G. A whale optimization
algorithm-based multivariate exponential smoothing grey-holt model for electricity price forecasting. Expert Syst. Appl. 2024,
255, 124663. [CrossRef]

155. Zhang, T.; Tang, Z.; Wu, J.; Du, X.; Chen, K. Short term electricity price forecasting using a new hybrid model based on two-layer

decomposition technique and ensemble learning. Electr. Power Syst. Res. 2022, 205, 107762. [CrossRef]

156. Gabrielli, P.; Wüthrich, M.; Blume, S.; Sansavini, G. Data-driven modeling for long-term electricity price forecasting. Energy 2022,

244, 123107. [CrossRef]

157. Parizad, B.; Ranjbarzadeh, H.; Jamali, A.; Khayyam, H. An intelligent hybrid machine learning model for sustainable forecasting

of home energy demand and electricity price. Sustainability 2024, 16, 2328. [CrossRef]

158. Chen, Z.; Zhang, B.; Du, C.; Yang, C.; Gui, W. Outlier-adaptive-based non-crossing quantiles method for day-ahead electricity

price forecasting. Appl. Energy 2025, 382, 125328. [CrossRef]

159. Williams, D.; Johnson, M.; Smith, J.; Rodriguez, S.; Deshmukh, A.; Brown, E. Developing a Hybrid Price Forecasting Model using
Machine Learning and Time Series Analysis. Available online: https://www.researchgate.net/publication/388960526 (accessed
on 9 June 2025).

160. Bashir, T.; Haoyong, C.; Tahir, M.F.; Liqiang, Z. Short term electricity load forecasting using hybrid prophet-LSTM model

optimized by BPNN. Energy Rep. 2022, 8, 1678–1686. [CrossRef]

161. Chen, J.; Xiao, J.; Xu, W. A hybrid stacking method for short-term price forecasting in electricity trading market. In Proceedings
of the 2024 8th International Conference on Information Technology, Information Systems and Electrical Engineering (ICITISEE),
Yogyakarta, Indonesia, 29–30 August 2024; IEEE: Piscataway, NJ, USA, 2024; pp. 1–5.

162. Laitsos, V.; Vontzos, G.; Bargiotas, D.; Daskalopulu, A.; Tsoukalas, L.H. Data-driven techniques for short-term electricity price

forecasting through novel deep learning approaches with attention mechanisms. Energies 2024, 17, 1625. [CrossRef]

163. Ehsani, B.; Pineau, P.O.; Charlin, L. Price forecasting in the Ontario electricity market via TriConvGRU hybrid model: Univariate

vs. multivariate frameworks. Appl. Energy 2024, 359, 122649. [CrossRef]

164. Belenguer, E.; Segarra-Tamarit, J.; Pérez, E.; Vidal-Albalate, R. Short-term electricity price forecasting through demand and

renewable generation prediction. Math. Comput. Simul. 2025, 229, 350–361. [CrossRef]

165. Yan, W.; Wang, P.; Xu, R.; Han, R.; Chen, E.; Han, Y.; Zhang, X. A novel mid-and long-term time-series forecasting framework for

electricity price based on hierarchical recurrent neural networks. J. Frankl. Inst. 2025, 362, 107590. [CrossRef]

166. Cu, Y.; Wang, K.; Zhang, L.; Liu, Z.; Liu, Y.; Mo, L. A Time Series Decomposition-Based Interpretable Electricity Price Forecasting

Method. Energies 2025, 18, 664. [CrossRef]

167. Mubarak, H.; Abdellatif, A.; Ahmad, S.; Islam, M.Z.; Muyeen, S.; Mannan, M.A.; Kamwa, I. Day-Ahead electricity price
forecasting using a CNN-BiLSTM model in conjunction with autoregressive modeling and hyperparameter optimization. Int. J.
Electr. Power Energy Syst. 2024, 161, 110206. [CrossRef]

168. Khan, A.A.A.; Ullah, M.H.; Tabassum, R.; Kabir, M.F. A transformer-BILSTM based hybrid deep learning approach for day-ahead
electricity price forecasting. In Proceedings of the 2024 IEEE Kansas Power and Energy Conference (KPEC), Manhattan, KS, USA,
25–26 April 2024; IEEE: Piscataway, NJ, USA, 2024; pp. 1–6.

169. Nie, Y.; Li, P.; Wang, J.; Zhang, L. A novel multivariate electrical price bi-forecasting system based on deep learning, a multi-input

multi-output structure and an operator combination mechanism. Appl. Energy 2024, 366, 123233. [CrossRef]

170. Hajigholam Saryazdi, A. A Novel Hybrid Deep learning Model for Electricity Price Forecasting. 2024. Available online:

https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5166713 (accessed on 9 June 2025).

171. Zhou, M.; Yan, Z.; Ni, Y.; Li, G.; Nie, Y. Electricity price forecasting with confidence-interval estimation through an extended

ARIMA approach. IEE Proc.-Gener. Transm. Distrib. 2006, 153, 187–195. [CrossRef]

172. Lin, W.M.; Gow, H.J.; Tsai, M.T. An enhanced radial basis function network for short-term electricity price forecasting. Appl.

Energy 2010, 87, 3226–3234. [CrossRef]

173. Jiang, L.; Hu, G. Day-ahead price forecasting for electricity market using long-short term memory recurrent neural network. In
Proceedings of the 2018 15th International Conference on Control, Automation, Robotics and Vision (ICARCV), Singapore, 18–21
November 2018; IEEE: Piscataway, NJ, USA, 2018; pp. 949–954.

174. Zhang, W.; Cheema, F.; Srinivasan, D. Forecasting of electricity prices using deep learning networks. In Proceedings of the 2018
IEEE PES Asia-Pacific Power and Energy Engineering Conference (APPEEC), Kota Kinabalu, Malaysia, 7–10 October 2018; IEEE:
Piscataway, NJ, USA, 2018; pp. 451–456.

Energies 2025, 18, 3097

40 of 40

175. Chang, Z.; Zhang, Y.; Chen, W. Electricity price prediction based on hybrid model of adam optimized LSTM neural network and

wavelet transform. Energy 2019, 187, 115804. [CrossRef]

176. Ghimire, S.; Deo, R.C.; Casillas-Pérez, D.; Salcedo-Sanz, S. Two-step deep learning framework with error compensation technique

for short-term, half-hourly electricity price forecasting. Appl. Energy 2024, 353, 122059. [CrossRef]

Disclaimer/Publisher’s Note: The statements, opinions and data contained in all publications are solely those of the individual
author(s) and contributor(s) and not of MDPI and/or the editor(s). MDPI and/or the editor(s) disclaim responsibility for any injury to
people or property resulting from any ideas, methods, instructions or products referred to in the content.

