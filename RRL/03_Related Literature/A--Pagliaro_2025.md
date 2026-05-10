Review
Artificial Intelligence vs. Efficient Markets: A Critical
Reassessment of Predictive Models in the Big Data Era

Antonio Pagliaro 1,2,3

1

2

3

INAF IASF Palermo, Via Ugo La Malfa, 153, I-90146 Palermo, Italy; antonio.pagliaro@inaf.it
Istituto Nazionale di Fisica Nucleare Sezione di Catania, Via Santa Sofia, 64, I-95123 Catania, Italy
ICSC—Centro Nazionale di Ricerca in HPC, Big Data e Quantum Computing, I-40121 Bologna, Italy

Abstract: This paper critically examines artificial intelligence applications in stock mar-
ket forecasting, addressing significant gaps in the existing literature that often overlook
the tension between theoretical market efficiency and empirical predictability. While nu-
merous reviews catalog methodologies, they frequently fail to rigorously evaluate model
performance across different market regimes or reconcile statistical significance with eco-
nomic relevance. We analyze techniques ranging from traditional statistical models to
advanced deep learning architectures, finding that ensemble methods like Extra Trees, Ran-
dom Forest, and XGBoost consistently outperform single classifiers, achieving directional
accuracy of up to 86% in specific market conditions. Our analysis reveals that hybrid ap-
proaches integrating multiple data sources demonstrate superior performance by capturing
complementary market signals, yet many models showing statistical significance fail to
generate economic value after accounting for transaction costs and market impact. By
addressing methodological challenges including backtest overfitting, regime changes, and
implementation constraints, we provide a novel comprehensive framework for rigorous
model assessment that bridges the divide between academic research and practical imple-
mentation. This review makes three key contributions: (1) a reconciliation of the Efficient
Market Hypothesis with AI-driven predictability through an adaptive market framework,
(2) a multi-dimensional evaluation methodology that extends beyond classification accu-
racy to financial performance, and (3) an identification of promising research directions in
explainable AI, transfer learning, causal modeling, and privacy-preserving techniques that
address current limitations.

Keywords: stock market prediction; machine learning; deep learning; artificial intelligence;
technical analysis; fundamental analysis; sentiment analysis

1. Introduction

The debate on the predictability of financial markets remains one of the most con-
troversial in economics. While the Efficient Market Hypothesis (EMH) maintains that
market movements should be theoretically unpredictable since all available information
is already reflected in asset prices, the emergence of increasingly sophisticated artificial
intelligence models has reopened this fundamental debate. The central thesis of this review
is that the interaction between advanced AI techniques and financial markets represents
not merely an incremental improvement over traditional methods but a paradigm shift in
our understanding of market dynamics and predictability.

This paradigm shift emerges from three key developments: First, modern AI systems
can detect complex, non-linear patterns in high-dimensional financial data that remain

Academic Editors: Jinwen Liang and

Jixin Zhang

Received: 19 March 2025

Revised: 17 April 2025

Accepted: 21 April 2025

Published: 23 April 2025

Citation: Pagliaro, A. Artificial

Intelligence vs. Efficient Markets: A

Critical Reassessment of Predictive

Models in the Big Data Era. Electronics

2025, 14, 1721. https://doi.org/

10.3390/electronics14091721

Copyright: © 2025 by the author.

Licensee MDPI, Basel, Switzerland.

This article is an open access article

distributed under the terms and

conditions of the Creative Commons

Attribution (CC BY) license

(https://creativecommons.org/

licenses/by/4.0/).

Electronics 2025, 14, 1721

https://doi.org/10.3390/electronics14091721

Electronics 2025, 14, 1721

2 of 48

invisible to conventional statistical approaches and human analysts. Second, the integration
of diverse data modalities—from price action and financial statements to sentiment analysis
and alternative data sources—creates a multidimensional perspective that transcends the
limitations of any single information stream. Third, the adaptive nature of modern learning
algorithms enables them to evolve alongside markets, potentially maintaining predictive
power even as market participants incorporate new information.

Despite the proliferation of financial prediction models, significant limitations per-
sist in existing approaches. Traditional statistical methods often rely on assumptions of
linearity and stationarity that poorly match financial market reality, while many machine
learning applications focus excessively on predictive accuracy without addressing eco-
nomic implementation constraints. The disconnect between statistical significance and
economic relevance represents a critical gap in current research, with numerous studies
reporting impressive classification metrics that fail to translate into profitable strategies
after accounting for transaction costs, market impact, and regime changes.

Existing reviews have primarily focused on the taxonomic classification of methods, of-
fering encyclopedic inventories of techniques without critical evaluation of their real-world
viability. Such reviews typically neglect three crucial dimensions: (1) rigorous cross-regime
evaluation to assess model consistency across different market conditions, (2) comprehen-
sive performance assessment beyond mere classification metrics, and (3) reconciliation of
empirical predictability with theoretical market efficiency principles. This review addresses
these specific limitations by developing an integrated evaluation framework that bridges
theoretical and practical considerations while providing a coherent explanation for the
apparent contradiction between market efficiency theory and documented AI predictability.
The practical significance of this shift extends beyond academic interest. Even marginal
improvements in forecast accuracy can translate into substantial financial gains when ap-
plied at scale. A mere 1% improvement in directional accuracy, when implemented across
a large investment portfolio with appropriate risk management, can generate significant
alpha while maintaining reasonable risk parameters. This explains why both academic re-
searchers and commercial entities have accelerated their exploration of AI-driven prediction
techniques despite theoretical objections based on market efficiency.

It is crucial to distinguish between two fundamental aspects of prediction model
evaluation: statistical performance (measured through metrics like directional accuracy,
precision, and recall) and economic performance (evaluated via financial metrics such as
Sharpe ratio, realized returns, and maximum drawdown). While statistical metrics provide
insights into a model’s classification capabilities, they do not necessarily translate into
economic value after accounting for transaction costs, market impact, execution slippage,
and other real-world constraints. Throughout this review, we carefully differentiate be-
tween these two evaluation dimensions, as models with impressive statistical performance
frequently fail to deliver meaningful economic value in practical implementation.

This review systematically evaluates the current state of AI applications in stock
market forecasting through a critical lens that recognizes both their potential and their
limitations. Unlike previous studies that have focused primarily on methodological tax-
onomies, we organize our analysis around the fundamental tension between increasing
model complexity and demonstrable financial performance. We evaluate methods not
merely on their statistical metrics but on their ability to generate consistent returns after
accounting for transaction costs, market impact, and changing market regimes.

The paper is structured as follows: Section 2 examines the theoretical foundations and
historical evolution of predictive models, highlighting the limitations of linear econometric
approaches and the theoretical basis for neural network applications. Section 3 presents
a comprehensive taxonomy of prediction techniques spanning statistical methods, pat-

Electronics 2025, 14, 1721

3 of 48

tern recognition, machine learning models, and sentiment analysis. Sections 4–7 analyze
each major category in depth, with particular attention to their empirical performance
across different markets and time periods. Section 8 explores hybrid and advanced ap-
proaches that combine multiple methodologies. Section 9 addresses the critical issue of
evaluation methodologies, emphasizing the importance of proper performance assessment
beyond simple accuracy metrics. Section 10 confronts the challenges and limitations fac-
ing AI-based prediction models, including theoretical constraints, methodological issues,
and implementation barriers. Finally, Section 11 outlines promising directions for future
research, suggesting pathways toward more robust, interpretable, and practically valuable
prediction systems. As illustrated in Figure 1, the various AI approaches to the prediction
of the stock market are deeply interconnected, with hybrid methods in the center that
integrate multiple techniques.

Figure 1. Interrelations of AI methods in stock market prediction. The diagram illustrates the connec-
tions between traditional ML approaches, deep learning, causal models, statistical methods, pattern
recognition, sentiment analysis, graph neural networks, and reinforcement learning, with hybrid
approaches at the center integrating multiple methodologies.

The central objective of this work is to provide a critical evaluation of AI applications

in stock market forecasting, addressing the following specific research questions:

1. How do ensemble methods compare to single classifiers in stock market prediction

across different market conditions and time horizons?

Electronics 2025, 14, 1721

4 of 48

2.

To what extent do hybrid approaches integrating multiple data sources improve
predictive performance compared to single-source models?

3. How can the apparent contradiction between the Efficient Market Hypothesis and
empirical evidence of AI-driven predictability be reconciled through an adaptive
market framework?

4. What evaluation framework best captures both statistical significance and economic

relevance in assessing prediction models?

By addressing these questions, we aim to provide researchers and practitioners with a
comprehensive understanding of the strengths, limitations, and practical applications of
various AI-based stock prediction methodologies.

2. Theoretical Foundations and Historical Evolution of Predictive Models
2.1. Limitations of Linear Econometric Models

Traditional financial econometrics relies heavily on linear models like the Autoregres-

sive Moving Average (ARMA), expressed as

Xt = c +

p
∑
i=1

ϕiXt−i + ϵt +

q
∑
i=1

θiϵt−i

(1)

where ϕi and θi represent autoregressive and moving average coefficients, respectively. This
formulation makes several critical assumptions that are often violated in financial markets.
Most importantly, ARMA models assume stationarity, where the statistical properties of
the time series (mean, variance, and autocorrelation) remain constant over time. Financial
time series are frequently non-stationary, exhibiting trends, seasonality, and structural
breaks. To address this limitation, the Integrated (I) component in ARIMA models applies
differencing operations (∆Xt = Xt − Xt−1) to transform non-stationary data into stationary
processes before applying ARMA modeling. Even with such adjustments, however, these
models exhibit critical limitations when applied to modern financial markets.

• Nonlinear Dynamics: ARMA fails to capture asymmetric volatility clustering ob-
served in S&P 500 returns, where negative shocks induce 43% greater volatility persis-
tence than positive shocks [1]. This violates the assumption of linear shock response.
• High-Dimensional Interactions: The 2010 Flash Crash demonstrated cross-asset
correlation jumps exceeding 0.8 within minutes, a phenomenon unmodelable through
pairwise linear coefficients [2].

2.2. Neural Network Paradigm Shift

The universal approximation theorem formalized by [3] established that feed-forward
networks with a single hidden layer can approximate any Borel measurable function to the
desired accuracy, providing the theoretical basis for financial applications:

f (x) = ϕ

(cid:33)

wi · xi + b

(cid:32) n
∑
i=1

(2)

where ϕ is a nonlinear activation function. Empirical validation came from a 2007 NYSE
study showing three-layer MLPs that reduce MSE prediction of the overnight gap by 62%
versus GARCH models [4].

Recurrent Architectures for Temporal Dependencies

Simple RNNs introduced memory through hidden state recursion:

ht = σ(Whhht−1 + Wxhxt + bh)

(3)

Electronics 2025, 14, 1721

5 of 48

where, in traditional RNN architectures, σ is typically the hyperbolic tangent (tanh) activa-
tion function rather than the logistic sigmoid. The tanh function is preferable for hidden
state updates as it produces zero-centered outputs in the range [−1, 1], helping to mitigate
vanishing gradient issues compared to the logistic sigmoid function, which outputs in the
range of [0, 1] and can lead to consistently positive activations that exacerbate gradient
vanishing problems when processing long sequences [5]. The severity of this gradient
vanishing problem depends on several factors including input data characteristics, network
architecture, and hyperparameter settings, with the practical sequence length limit varying
from dozens to hundreds of steps depending on the application domain. LSTM networks
solved this through gated memory cells:

ft = σ(Wf · [ht−1, xt] + b f )
it = σ(Wi · [ht−1, xt] + bi)
˜Ct = tanh(WC · [ht−1, xt] + bC)
Ct = ft ◦ Ct−1 + it ◦ ˜Ct
ot = σ(Wo · [ht−1, xt] + bo)
ht = ot ◦ tanh(Ct)

(Forget Gate)

(Input Gate)

(Cell State)

(Output Gate)

(4)

(5)

(6)

(7)

(8)

(9)

Applications to DAX index futures demonstrated accuracy of 82% in 10 min interval
predictions using 512-unit bidirectional LSTMs [6].

2.3. Modern Regularization Techniques

Deep networks’ propensity to overfit financial noise necessitated advanced regularization:

•

•

•

Temporal Dropout: The random masking of sequence elements during training im-
proved the NASDAQ-100 prediction Sharpe ratio by 0.47 [7].
Curriculum Learning: Phased training from daily to tick-level data enhanced S&P 500
volatility forecasting, with a 33% RMSE reduction [8].
Bayesian Hyperparameter Optimization: Tree-structured Parzen Estimators (TPEs)
optimized LSTM layers on crude oil futures, achieving 19% lower MAE than grid
search [9].

Attention Mechanisms

Transformer architectures revolutionized sequence modeling through self-attention:

Attention(Q, K, V) = softmax

(cid:18) QKT
√
dk

(cid:19)

V

(10)

where Q, K, and V represent query, key, and value matrices. Applied to FOREX markets,
Vaswani et al. [10] demonstrated that transformer-based models with multihead attention
mechanisms achieved a 57% reduction in prediction latency compared to LSTM networks
while simultaneously maintaining comparable predictive performance (89% precision).
This significant computational efficiency improvement was achieved through the transform-
ers’ inherently parallelizable architecture, which eliminates the sequential computation
requirements of recurrent models, allowing for faster inference without compromising
predictive quality [10].

2.4. Critical Assessment of Prior Research

Previous surveys on financial prediction models have often focused on the taxonomic
classification of methods rather than critical evaluations of their real-world applicability.
For instance, studies by Sezer et al. [11], Henrique et al. [12] categorized techniques compre-

Electronics 2025, 14, 1721

6 of 48

hensively but failed to address fundamental limitations in their evaluation methodologies,
particularly regarding proper statistical validation and economic significance testing.

Several critical limitations pervade the existing literature. First, many studies report im-
pressive classification accuracy without demonstrating corresponding economic value after ac-
counting for transaction costs, slippage, and market impact. Fernández-Rodríguez et al. [13]
demonstrated that many published neural network approaches showing statistical signifi-
cance failed to maintain profitability when realistic trading frictions were incorporated.

Second, methodological weaknesses in validation procedures are common, with many
studies employing standard k-fold cross-validation without accounting for temporal depen-
dencies in financial data, leading to information leakage and overly optimistic performance
estimates. López de Prado [14] highlighted how this methodological error has led to
numerous false discoveries in the financial machine learning literature.

Third, the reconciliation of predictive findings with market efficiency theories remains
inadequate in most research. Studies often report predictability without addressing the
theoretical implications for market efficiency or providing mechanisms through which
their findings coexist with semi-strong efficiency. This theoretical disconnection limits the
integration of machine learning advances into financial theory.

3. Taxonomy of Stock Market Prediction Techniques

Stock market prediction techniques can be broadly classified into four main categories:
statistical approaches, pattern recognition methods, machine learning models, and senti-
ment analysis.

3.1. Statistical Approaches

Statistical methods represent the earliest computational approaches to stock prediction.
These techniques focus on identifying statistical relationships and patterns in historical
price data. Common statistical models include the following:

• Autoregressive Integrated Moving Average (ARIMA): These models combine au-
toregressive (AR) components, which capture the momentum and mean reversion
effects in trading markets, with moving average (MA) components, which model
shock effects in time series.
Exponential Smoothing Model (ESM): This technique applies an exponential win-
dow function to time series data, giving greater weight to recent observations and
progressively less weight to older data points.

•

• Generalized Autoregressive Conditional Heteroskedastic (GARCH): This model
specifically addresses the volatility clustering observed in financial time series, where
periods of high volatility tend to cluster together.

While statistical models offer interpretability and theoretical grounding, they often
assume linearity, stationarity, and normality in the data—assumptions that frequently do
not hold in the complex, nonlinear domain of financial markets.

3.2. Pattern Recognition Methods

Pattern recognition approaches focus on identifying recurring visual patterns in stock

price charts. These methods include:

•

•

Perceptually Important Points (PIP): This technique reduces time series dimensions
by preserving salient points, allowing for more efficient pattern identification.
Template Matching: This approach matches patterns in current stock data with histor-
ical patterns that preceded specific market movements.

Electronics 2025, 14, 1721

7 of 48

• Chart Pattern Recognition: These methods identify familiar chart patterns like gaps,
spikes, flags, pennants, wedges, saucers, triangles, and head-and-shoulder formations
that technical analysts believe have predictive value.

Pattern recognition methods are particularly aligned with technical analysis, which has
a long history in financial forecasting. However, their effectiveness remains controversial
among academic researchers.

3.3. Machine Learning Models

Machine learning approaches have become increasingly dominant in stock forecasting
research. These methods can be divided into supervised and unsupervised learning
techniques.

3.3.1. Supervised Learning Methods

•

Support Vector Machines (SVMs): These algorithms define optimal hyperplanes for
separating data into different classes.

• Decision Trees and Random Forests: Tree-based algorithms that create hierarchical

decision structures based on feature values.

• Artificial Neural Networks (ANNs): Computational models inspired by the structure

of biological neural networks.

• Deep Learning Models: More complex neural network architectures including Con-
volutional Neural Networks (CNNs), Recurrent Neural Networks (RNNs), and Long
Short-Term Memory (LSTM) networks.

• Gradient-Boosting Methods: Techniques like XGBoost and AdaBoost that create

strong predictive models by combining multiple weak learners.

3.3.2. Unsupervised Learning Methods

• K-means Clustering: Groups data points into clusters based on similarity.
• Hierarchical Clustering: Creates a hierarchy of clusters using either agglomerative or

•

divisive approaches.
Principal Component Analysis (PCA): Reduces dimensionality while preserving
data variance.

Machine learning models are particularly valuable for capturing nonlinear relation-
ships and complex patterns in financial data without requiring explicit theoretical models.

3.4. Sentiment Analysis

Sentiment analysis approaches leverage text data from news articles, social media,

company reports, and other textual sources to gauge market sentiment:

•

Lexicon-Based Methods: Use predefined dictionaries to assess the sentiment of words
and phrases.

• Machine Learning-Based Sentiment Analysis: Employs supervised learning to clas-

sify text sentiment.

• Deep Learning for Sentiment Analysis: Utilizes neural network architectures like
BERT (Bidirectional Encoder Representations from Transformers) for more nuanced
sentiment analysis.

Sentiment analysis provides a way to incorporate qualitative information and market
psychology into quantitative prediction models, potentially addressing factors not captured
in price and volume data alone.

Figure 2 demonstrates the typical data flow in modern stock prediction systems,
highlighting the progression from diverse data sources through various processing stages
to final decision support.

Electronics 2025, 14, 1721

8 of 48

Figure 2. Data flow in modern stock prediction systems. The pipeline demonstrates the progression
from diverse data sources through preprocessing and feature engineering to various modeling
approaches, followed by evaluation and decision support systems. Key performance impact factors
are highlighted at the bottom of the diagram.

4. Statistical Approaches in Stock Market Prediction

Statistical models have long served as the foundation for quantitative analysis in finan-
cial markets. Despite the emergence of more complex AI methods, statistical approaches
retain value for their interpretability and computational efficiency.

4.1. ARIMA Models

ARIMA models remain widely used for time series forecasting in finance. These
models integrate autoregressive (AR) components, differencing to achieve stationarity (I),
and moving average (MA) components. Studies by Ariyo et al. [15] demonstrated that
ARIMA models can still compete effectively with newer forecasting techniques, particularly
for short-term prediction. Devi et al. [16] applied ARIMA to predict the Nifty 50 Index,
finding that this approach provided reliable forecasts with relatively low error and volatility.
Key advantages of ARIMA models include their ability to capture short-term depen-
dencies in data and their theoretical foundation in time series analysis. However, limitations
include their assumption of linearity and difficulty in modeling longer-term dependencies.
Moreover, ARIMA models may struggle with financial time series that exhibit volatility
clustering or other complex, non-stationary behaviors.

Electronics 2025, 14, 1721

9 of 48

4.2. Exponential Smoothing Methods

Exponential smoothing methods apply weighted averages to time series data,
with weights decreasing exponentially as observations age. De Faria et al. [17] compared
adaptive exponential smoothing models with neural networks for predicting Brazilian
stock indices, finding comparable performance between the two approaches.

Exponential smoothing is particularly valuable for data with seasonal patterns or
trends, and it can adapt quickly to changes in the underlying data. However, like ARIMA,
traditional exponential smoothing methods may struggle with complex, nonlinear patterns
in financial data.

4.3. Regression Models

Various regression models have been applied to stock prediction. Bhuriya et al. [18]
compared linear, polynomial, and Radial Basis Function (RBF) regression models for pre-
dicting stock prices, finding that linear regression outperformed other regression techniques
in their study.

Dutta et al. [19] took an innovative approach by using logistic regression with finan-
cial ratios as independent variables to classify companies as “good” or “poor” based on
their one-year performance. This approach achieved a classification accuracy of 74.6%,
highlighting the value of fundamental analysis in stock prediction.

4.4. Limitations of Statistical Approaches

While statistical methods offer strong theoretical foundations and interpretability, they

face several key limitations in stock market prediction:

•

•

Linearity Assumptions: Many statistical methods assume linear relationships between
variables, whereas stock markets frequently exhibit nonlinear dynamics.
Stationarity Requirements: Models like ARIMA require data to be stationary, but fi-
nancial time series often display changing statistical properties over time.

• Difficulty with Exogenous Variables: Traditional time series models may struggle to
incorporate external factors such as news events or broader economic indicators.
Limited Capability for Pattern Recognition: Statistical models typically cannot cap-
ture complex visual patterns that technical analysts identify in price charts.

•

These limitations have motivated the development of more flexible machine learning

approaches that can better address the complexities of financial markets.

4.5. Data Considerations Across Prediction Studies

The quality, scope, and processing of input data fundamentally determine the perfor-
mance of stock prediction models. This section examines the data considerations across the
literature, highlighting best practices and challenges.

4.5.1. Common Data Sources

Prediction studies employ diverse data sources that can be categorized as follows:

• Market Data: The most commonly used data source includes historical price and vol-
ume information, typically at daily or intraday frequencies. Studies like [6] employed
minute-level data for S&P 500 constituents, while others like [20] utilized tick-by-tick
data for high-frequency prediction.
Fundamental Data: Financial statements, earnings reports, and accounting metrics
provide inputs for fundamental analysis. Dutta et al. [19] extracted financial ratios
from quarterly reports to classify stocks, while [21] combined fundamental metrics
with technical indicators.

•

Electronics 2025, 14, 1721

10 of 48

• News and Social Media: Textual data from financial news, social media, and company
announcements has gained prominence. Bollen et al. [22] analyzed 10 million tweets
to predict DJIA movements, while Ding et al. [23] processed financial news to extract
event embeddings for prediction.

• Alternative Data: Increasingly, studies incorporate non-traditional data sources.

Zhang et al. [24] utilized weather data to predict energy commodity prices.

4.5.2. Preprocessing Approaches

Data preprocessing significantly impacts model performance and typically involves

the following:

• Cleaning and Normalization: Financial time series often contain missing values and
outliers and require normalization. Common approaches include z-score standard-
ization, min–max scaling, and missing value imputation using methods like forward
filling or MICE (Multiple Imputation by Chained Equations).
Feature Engineering: Raw financial data are transformed into predictive features.
Technical indicators (e.g., RSI, MACD, Bollinger Bands) are commonly derived from
price data. Hu et al. [25] created Google Trends indicators by calculating search
intensity changes, while Chen and Chen [26] identified perceptually important points
in price series to reduce dimensionality.

•

• Dimensionality Reduction: Given the high-dimensional nature of financial data, tech-
niques like Principal Component Analysis (PCA) or autoencoders are often employed.
Bao et al. [27] utilized stacked autoencoders to compress high-dimensional features
before feeding them into LSTM networks.
Temporal Alignment: Aligning data from diverse sources with different frequencies
(e.g., daily price data with quarterly fundamentals) presents significant challenges.
Chen and Hao [21] addressed this through temporal aggregation and forward-filling
techniques.

•

4.5.3. Alternative Data Processing

Alternative data sources require specialized preprocessing:

•

•

•

Text Processing: News and social media data undergo tokenization, stemming, and em-
bedding generation. Mittal and Goel [28] applied sentiment dictionaries to classify
tweets, while more recent studies like Ding et al. [23] employed word embeddings
and neural language models.
Image Processing: Satellite imagery typically undergoes segmentation, feature extrac-
tion, and object detection before integration with financial data.
Sensor Data: IoT sensor data often require noise filtering, aggregation, and anomaly
detection. Ma et al. [29] processed industrial sensor data through Fourier transforma-
tions before using them to predict commodity price movements.

5. Pattern Recognition in Stock Market Analysis

Pattern recognition approaches attempt to identify recurring visual patterns in stock
price movements that may have predictive value. These methods are closely aligned with
technical analysis practices that have been used by traders for generations.

5.1. Perceptually Important Points

Fu et al. [30] proposed an approach to identifying patterns in time series data using
Perceptually Important Points (PIPs), which focus on key inflection points in price charts.
This technique reduces dimensionality while preserving the most salient features of the
time series, potentially allowing for more efficient pattern detection.

Electronics 2025, 14, 1721

11 of 48

Markowska-Kaczmar and Dziedzic [31] implemented a supervised feed-forward
neural network with PIPs to identify patterns in stock data. Their findings suggest that PIPs
can effectively discover patterns in shortened time series datasets, though the approach
may struggle if there are high-amplitude fluctuations between adjacent data points.

5.2. Template Matching

Template matching involves searching for predefined patterns in stock price charts that
typically precede specific market movements. Leigh et al. [32] developed a bull flag pattern
recognizer using template matching, finding that this approach generated profits that
exceeded random trading, challenging some aspects of the Efficient Market Hypothesis.

Cervelló-Royo et al. [33] extended this work by introducing dynamic parameters
for closing operations and using intraday data. Their approach demonstrated positive
performance on multiple stock indices, providing further evidence against the strictest
interpretations of market efficiency.

5.3. Advanced Pattern Recognition

Chen and Chen [26] developed a hybrid approach combining PIPs and template
matching to identify bull flag patterns, achieving superior performance compared to other
pattern recognition models. Their model generated unprecedented stock index returns
when applied to NASDAQ and TAIEX indices.

Arévalo et al. [34] extended previous template matching work by adding filters based
on Exponential Moving Averages (EMAs) and price ranges. This refined approach outper-
formed earlier methods, generating higher profits with lower risk.

More recently, Kim et al. [20] built a Pattern-Matching Trading System (PMTS) based
on Dynamic Time Warping (DTW), applying it to the KOSPI 200 index. Their approach
generated solid annualized returns, with patterns proving especially profitable near market
clearing times.

5.4. Effectiveness and Limitations

Pattern recognition methods have shown promising results in multiple studies,
but their effectiveness remains controversial in academic finance. Some researchers argue
that the identification of predictive patterns contradicts the Efficient Market Hypothesis,
while others suggest that pattern recognition may simply be capturing temporary market
inefficiencies or risk premiums.

Key limitations of pattern recognition approaches include the following:

•

Subjectivity: Pattern definitions may vary between analysts, leading to inconsistent
results.

• Overfitting Risk: Systems may be optimized to recognize patterns in historical data

that lack predictive value for future movements.

• Changing Market Dynamics: Patterns that were predictive in the past may lose

•

effectiveness as market structures and participant behaviors evolve.
Limited Theoretical Foundation: Unlike statistical models, pattern recognition often
lacks strong theoretical justification in financial economics.

Despite these limitations, pattern recognition continues to play a significant role in

algorithmic trading systems, particularly for short-term trading strategies.

6. Machine Learning Approaches

Machine learning approaches have gained particular prominence in stock market
prediction research due to their ability to capture complex, nonlinear relationships without

Electronics 2025, 14, 1721

12 of 48

requiring explicit theoretical models. These methods can be broadly categorized into
supervised and unsupervised learning techniques.

6.1. Supervised Learning Methods
6.1.1. Support Vector Machines

Support Vector Machines (SVMs) have been widely applied in stock prediction due
to their effectiveness in high-dimensional spaces and robust performance on classification
tasks. Huang et al. [35] applied SVMs to predict the direction of stock market movement,
achieving accuracies superior to other prediction methods.

Shen et al. [36] proposed an approach combining statistical correlation analysis with
SVMs, exploiting relationships among global markets and other products to predict the
next day’s trend in stock prices. Their model achieved 77.6% prediction accuracy on the
DJIA index, with even higher accuracy for longer-term predictions.

6.1.2. Decision Trees and Random Forests

Decision trees and their ensemble variants like Random Forests have proven particu-

larly effective for stock prediction.

Ensemble methods combine multiple learning algorithms:

• Random Forest: An ensemble of decision trees that has demonstrated strong perfor-
mance across multiple stock prediction studies. Lohrmann and Luukka [37] applied
Random Forest to classify intraday S&P 500 returns with high accuracy.

• Gradient Boosting: Methods like XGBoost and AdaBoost have shown excellent perfor-
mance in stock prediction. Dey et al. [38] applied XGBoost to predict stock direction,
achieving accuracies of 87–99% for the long-term prediction of Apple and Yahoo stocks.
Bagging Methods: Ampomah et al. [39] evaluated tree-based ensemble machine
learning models in predicting stock price direction, finding that ensemble methods
consistently outperformed individual classifiers.

•

Ensemble methods generally provide superior performance compared to individual
classifiers as they can reduce overfitting and capture more complex patterns in the data.
The improved performance of ensemble methods like Random Forest and XGBoost appears
consistent across different markets and time periods.

Ballings et al. [40] benchmarked ensemble methods against single classifiers for pre-
dicting stock price direction, finding that Random Forest consistently outperformed other
algorithms.

Basak et al. [41] compared tree-based classifiers for predicting stock market direction,
finding that Random Forest and gradient-boosted decision trees (using XGBoost) facilitated
accurate predictions. Their approach achieved high accuracy for medium- to long-run
prediction of stock price direction.

Khan et al. [42] compared nine machine learning models for stock market prediction,
finding that Random Forest achieved the highest accuracy of 91.27% using their proposed
strategy involving 15 min time intervals. Their work also emphasized the importance
of evaluating models based on financial performance metrics rather than classification
accuracy alone.

Recent comparative studies have demonstrated the superiority of ensemble methods
beyond traditional Random Forests for stock prediction tasks. Pagliaro [43] found that
Extra Trees Classifier models achieve superior accuracy (86.1%) compared to Random Forest
methods (73%) when predicting significant stock price changes over 10-day windows.

The superior performance of Extra Trees Classifier models stems from their unique
randomized threshold selection process, which offers a favorable bias–variance tradeoff
compared to traditional Random Forest methods. Unlike Random Forest, which optimizes

Electronics 2025, 14, 1721

13 of 48

threshold values when splitting nodes, Extra Trees randomly selects thresholds and chooses
the best among these random splits. This additional source of randomization acts as an
effective regularization mechanism, significantly reducing variance (overfitting) while
introducing only a small increase in bias. For high-dimensional, noisy financial data with
non-stationary characteristics, this regularization effect is particularly beneficial as it en-
hances model robustness against spurious patterns and outliers. However, this comes with
potential disadvantages, including reduced model interpretability and possibly suboptimal
performance in highly structured datasets where optimal threshold selection might capture
genuine patterns more effectively than randomized approaches.

This approach showed particular efficacy in volatile market conditions, outperform-
ing buy-and-hold strategies by 14.35% during the high-interest rate environment of
2022–2023 [43].

However, it is important to note that these figures typically represent “gross” predic-
tion accuracy before accounting for transaction costs, slippage, and other implementation
frictions. Studies that incorporate these real-world trading constraints, such as those
by [6,43], demonstrate that net performance metrics are substantially lower, with reduc-
tions in realized returns of 15–40% compared to theoretical performance. This highlights
the importance of evaluating models based on their post-cost economic performance rather
than relying solely on statistical accuracy metrics.

6.1.3. Artificial Neural Networks

Artificial Neural Networks (ANNs) have been extensively studied for stock prediction
due to their flexibility and capacity to model complex patterns. Qiu and Song [44] used an
ANN optimized with a genetic algorithm to predict the direction of the Japanese Nikkei
225 index, achieving an accuracy of 81.27%.

Moghaddam et al. [45] applied feed-forward ANNs with different architectures to
predict the NASDAQ index, finding that networks with multiple hidden layers achieved
superior performance compared to simpler architectures.

6.1.4. Deep Learning Models

Deep learning models have shown particular promise for stock prediction in re-

cent years.

•

• Recurrent Neural Networks (RNNs): Bernal et al. [32] implemented Echo State Net-
works (a subclass of RNNs) to predict S&P 500 stock prices, outperforming traditional
techniques with very low test error.
Long Short-Term Memory (LSTM): Di Persio and Honchar [46] compared basic RNNs,
LSTM, and Gated Recurrent Units (GRUs) for Google stock price prediction, finding
that LSTM outperformed other variants with 72% accuracy on a five-day horizon.
• Convolutional Neural Networks (CNNs): Sezer and Ozbayoglu [47] developed a
CNN-based approach for financial trading, converting time series data to image
representations to leverage the CNN’s pattern recognition capabilities.

Wu and Chen [48] compared ARIMA and LSTM models for stock price prediction,
finding that ARIMA showed comparable accuracy to LSTM for long-term predictions,
though LSTM generally performed better in capturing complex patterns.

6.2. Unsupervised Learning Methods

Unsupervised learning methods identify patterns and correlations in data without

requiring labeled examples.

Electronics 2025, 14, 1721

14 of 48

• Clustering Methods: Powell et al. [49] compared K-means clustering with SVM for
stock prediction, finding similar performance between the two approaches. The study
highlighted the importance of distance metric selection for clustering effectiveness.

• Association Rule Learning: Wu et al. [50] proposed a model combining K-means
clustering with the AprioriAll algorithm to extract frequent patterns and predict stock
trends, outperforming other approaches in terms of average returns.

• Hybrid Unsupervised Approaches: Babu et al. [51] proposed a clustering method
called HAK that combines Hierarchical Agglomerative Clustering and reverse
K-means clustering to predict the impact of financial reports on stocks, outperforming
SVMs in terms of accuracy.

Unsupervised learning approaches are particularly valuable for identifying market
regimes and segmenting stocks into groups with similar behavior patterns. These insights
can then inform supervised learning models or trading strategies.

6.3. Comparative Analysis of Machine Learning Models

Several studies have conducted comparative analyses of multiple machine learning

models for stock prediction.

Patel et al. [52] compared ANNs, SVMs, Random Forest, and naive Bayes for predicting
stock price direction, finding that Random Forest generally outperformed other techniques.
Chong et al. [53] conducted a systematic analysis of deep learning networks for stock
market prediction, finding that deeper architectures typically outperformed shallower
networks and traditional methods.

Khan et al. [42] compared nine machine learning models using both traditional method-
ology and a novel 15 min time interval strategy. With the traditional methodology, logistic
regression achieved the highest accuracy (85.51%), while, with the proposed strategy,
Random Forest achieved the highest accuracy (91.27%).

These comparative studies highlight that no single model consistently outperforms all
others across all markets and time periods. Performance depends on data characteristics,
feature selection, hyperparameter tuning, and evaluation metrics. However, ensemble meth-
ods like Random Forest and gradient-boosting approaches tend to perform well consistently.
While our literature analysis consistently shows that ensemble methods outperform
single classifiers across various studies, it is important to qualify this generalization. The su-
periority of ensemble methods is not universal and can be highly dataset-dependent and
context-specific. Under certain market conditions—particularly during stable, trending
regimes with clear patterns—simpler single models may perform competitively while of-
fering advantages in interpretability, computational efficiency, and ease of implementation.
For instance, Wu and Chen [48] demonstrated that ARIMA models can match LSTM per-
formance for long-term predictions in trending markets, and Qiu and Song [44] found that
optimized single ANNs outperformed certain ensemble methods during periods of low
volatility. Furthermore, the advantage of ensemble methods may diminish when dealing
with extremely high-frequency data, where latency considerations become paramount, or in
markets with very limited historical data, where ensemble diversity cannot be effectively
leveraged. Future comparative studies should systematically evaluate model performance
across different market regimes, volatility environments, and data characteristics to develop
more nuanced guidelines for model selection based on specific forecasting contexts.

7. Sentiment Analysis for Stock Prediction

Sentiment analysis leverages textual data to gauge market sentiment and incorporate
qualitative information into quantitative prediction models. This approach recognizes that

Electronics 2025, 14, 1721

15 of 48

stock markets are influenced not just by financial metrics but also by market psychology
and public perception.

7.1. News-Based Sentiment Analysis

News articles provide valuable insights into company developments and market

conditions.

Schumaker and Chen [54] analyzed the effects of breaking news on stock prices within
20 min after release, using an SVM derivative model with different textual representations.
They found that the noun phrases method performed better than bag of words and named
entities models.

Kalyanaraman et al. [55] developed a sentiment analysis model to gauge sentiments
from news articles and feed the output into machine learning algorithms. Their approach
achieved an accuracy of 81.82% for predicting stock prices.

Lee et al. [56] analyzed Form 8-K reports (important updates regarding companies) to
predict stock price movements, finding that incorporating text analysis improved model
accuracy by 10%. Their research also found that the effect of sentiment analysis on these
reports diminishes quickly with time, suggesting they are most valuable for short-term
predictions.

7.2. Social Media-Based Sentiment Analysis

Social media platforms provide real-time insights into public sentiment.
Bollen et al. [22] analyzed Twitter data using Google Profile of Mood States and
Opinion Finder to understand correlations with DJIA closing prices. By applying a Self-
Organizing Fuzzy Neural Network to approximately 10 million tweets, they achieved an
accuracy of 87.6% in predicting daily DJIA values.

Mittal and Goel [28] extended this work with a larger dataset of over 400 million
tweets, achieving an accuracy of 75% and finding that both “calmness” and “happiness”
were predictive indicators over a range of three to four days.

Pagolu et al. [57] implemented a sentiment analysis model based on Twitter data using
N-gram and Word2vec techniques, achieving 70% accuracy and noting a 71.82% correlation
between price and sentiments.

7.3. Search Volume Analysis

Search volume data provide insights into public interest and attention:
Hu et al. [25] incorporated Google Trends data into neural network models for predict-
ing stock market direction. Their approach combined an improved sine cosine algorithm
with back propagation neural networks, achieving hit ratios of 86.81% for the S&P 500
Index and 88.98% for the Dow Jones Industrial Average Index when including Google
Trends data.

Preis et al. [58] showed that search volume data from Google Trends could be used to
detect early warning signs of stock market movements. Their work demonstrated that changes
in search behavior preceded market movements, providing valuable predictive information.

7.4. Combined Sentiment Approaches

Several studies have combined multiple sentiment sources for improved prediction.
Ding et al. [23] proposed a hybrid approach combining sentiment analysis with neural
network models for S&P 500 index prediction. Their deep convolutional neural network
was trained to predict short- and long-term influences of news events, achieving accuracies
of 64.21% for index prediction and 65.48% for individual stock price prediction.

Electronics 2025, 14, 1721

16 of 48

Ren et al. [59] developed a model combining support vector machines with senti-
ment analysis techniques for Shanghai Stock Exchange prediction, achieving an accuracy
of 89.93%.

Sentiment analysis approaches offer a valuable complement to traditional technical
and fundamental analysis, particularly for short-term prediction horizons. By incorporating
public mood and attention metrics, these models can capture aspects of market behavior
not reflected in price and volume data alone.

8. Hybrid and Advanced Approaches

As stock market prediction techniques have evolved, researchers have increasingly
focused on hybrid approaches that combine multiple methodologies to overcome the limi-
tations of individual techniques. These hybrid models often achieve superior performance
by leveraging the strengths of different approaches.

8.1. Hybrid Technical Models

Many hybrid models combine different technical prediction approaches.
Wang et al. [60] proposed a hybrid model combining the Exponential Smoothing
Method (ESM), ARIMA, and Backpropagation Neural Network (BPNN) for weekly stock
price prediction. This hybrid model outperformed individual constituent models on both
the Shenzhen Integrated Index and DJIA, with a directional accuracy of 70.16%.

Rather et al. [61] developed a hybrid model integrating linear (ARIMA, ESM) and
non-linear (RNN) approaches, with weights determined by a genetic algorithm. Their
hybrid approach achieved lower Mean Absolute Error and Mean Squared Error compared
to constituent models.

Lv et al. [62] evaluated various machine learning algorithms and deep neural network
models using S&P 500 and CSI 300 Index Component Stocks. Their findings indicated that
traditional machine learning algorithms performed better on directional indicators without
transaction costs, while deep neural networks performed better when transaction costs
were considered.

8.2. Multimodal Data Integration

Some hybrid approaches integrate fundamentally different data types.
Yoshihara et al. [63] combined Deep Belief Networks (DBNs) with RNN-RBM to
predict long-term stock price changes based on significant events, achieving lower test
error rates compared to individual models.

Ding et al. [23] developed a neural tensor network for learning event embeddings and
a deep CNN to model the influences of events on stock price movements, demonstrating a
6% improvement in S&P 500 index prediction compared to state-of-the-art approaches.

Hu et al. [25] integrated Google Trends data with neural networks optimized by an im-
proved sine cosine algorithm. Their ISCA-BPNN model with Google Trends data achieved
hit ratios of 86.81% for the S&P 500 Index and 88.98% for the DJIA Index, demonstrating
the value of search volume data for prediction.

8.3. Combined Technical and Fundamental Analysis

Some approaches integrate technical and fundamental analysis.
Dutta et al. [19] demonstrated the utility of fundamental analysis through financial
ratios to separate good stocks from poor stocks, comparing their one-year return against
benchmark indices.

Chen and Hao [21] utilized a weighted support vector machine and K-nearest neighbor
approach to predict Chinese stock market indices, incorporating both technical indicators
and fundamental data.

Electronics 2025, 14, 1721

17 of 48

Shen et al. [36] exploited correlations among global markets and other products to
predict stock prices, achieving 77.6% accuracy on DJIA prediction and up to 85% for
longer-term predictions.

8.4. Advanced Deep Learning Architectures

Recent research has focused on increasingly sophisticated deep learning architectures.
Fischer and Krauss [6] applied LSTM networks to financial market predictions, demon-
strating superior performance compared to Random Forests, deep neural networks, and lo-
gistic regression.

Sezer et al. [11] developed a CNN-based algorithmic trading model using image
representations of financial time series data, achieving consistent profitability across multi-
ple markets.

Bao et al. [27] proposed a deep learning framework using stacked autoencoders and
LSTM, finding that their approach outperformed traditional machine learning methods for
stock price prediction.

8.5. Graph Neural Networks for Stock Prediction

An emerging trend involves using graph neural networks to model relationships

between stocks.

Wang et al. [64] proposed a model integrating knowledge graphs, Graph Convo-
lutional Networks (GCNs), and community detection for stock price prediction. This
approach overcame the limitations of existing models by accounting for deeper influencing
factors and leveraging relationships between stocks.

Zhang [65] developed a conceptual–temporal graph CNN model (CT-GCNN) for pre-
dicting stock price movements, exploring movements in both time and concept dimensions
and accounting for linkage effects among stocks within the same conceptual segment.

These graph-based approaches represent a promising direction for stock prediction by
explicitly modeling the complex relationships between different stocks and market sectors.

8.6. Reinforcement Learning for Trading

Reinforcement learning (RL) approaches have gained attention for developing trading

strategies.

Jang and Seong [66] proposed a deep reinforcement learning approach for stock
portfolio optimization, connecting with modern portfolio theory using a 3D convolutional
neural network for feature extraction and Deep Deterministic Policy Gradient (DDPG) for
portfolio optimization.

Wu et al. [67] developed a novel GAN with piecewise linear representation for predict-
ing market trading actions (buying, selling, and holding), outperforming LSTM-based ap-
proaches.

Reinforcement learning offers particular promise for portfolio optimization and trad-
ing strategy development as it can directly optimize for financial objectives rather than
intermediate metrics like prediction accuracy.

9. Evaluation Methodologies

The evaluation of stock prediction models presents unique challenges compared to
typical machine learning tasks. While classification metrics like accuracy are commonly
reported, they may not directly translate to profitable trading strategies. This section
explores various approaches to model evaluation.

Electronics 2025, 14, 1721

18 of 48

9.1. Classification Performance Metrics

The evaluation of stock prediction models requires the careful selection of appro-
priate metrics based on the prediction task formulation. While stock forecasting can be
approached as either a regression problem (predicting actual price/return values) or a
classification problem (predicting directional movement or discrete categories), classifi-
cation metrics have become prevalent in the literature due to the practical importance of
directional accuracy for many trading strategies. Classification metrics are most appropri-
ate when the research question focuses on directional movement or categorical outcomes
(e.g., buy/sell/hold signals), while regression metrics (RMSE, MAE, R2) and financial
performance metrics are more suitable when precise value forecasts or economic outcomes
are the primary concern. It is important to recognize that each metric type has inherent
limitations: classification metrics may obscure the magnitude of errors, while regression
metrics might fail to capture the economic significance of directional accuracy.

Standard classification metrics widely used in the stock prediction literature include

the following:

• Accuracy: The percentage of correct predictions, typically calculated as (TP + TN)/(TP +

•

•

•

TN + FP + FN).
Precision: The proportion of true positive predictions out of all positive predictions,
calculated as TP/(TP + FP).
Recall: The proportion of true positive predictions out of all actual positives, calculated
as TP/(TP + FN).
F1 Score: The harmonic mean of precision and recall, providing a balance between the
two metrics.

• Area Under the ROC Curve (AUC): Measures the model’s ability to distinguish

between classes across different threshold settings.

These metrics provide valuable insights into a model’s classification performance,

but they do not necessarily indicate financial performance.

9.2. Financial Performance Metrics

Several studies have emphasized the importance of evaluating models based on

financial performance metrics.

• Returns: Measures investment performance, including cumulative return, annual

•

return, and risk-adjusted return.
Sharpe Ratio: Evaluates risk-adjusted performance by comparing excess returns
to volatility.

• Maximum Drawdown: Shows the largest peak-to-trough decline in portfolio value,

indicating downside risk.

• Win Rate: Calculates the percentage of profitable trades, indicating the consistency of

•

returns.
Profit Factor: Indicates the ratio of gross profits to gross losses, indicating the overall
profitability of a strategy.

Khan et al. [42] demonstrated that models with similar classification accuracy can pro-
duce significantly different financial outcomes. Their simulated trading results showed that
Random Forest generated the highest returns despite not having the highest classification
accuracy in their traditional methodology.

Electronics 2025, 14, 1721

19 of 48

9.3. Statistical vs. Economic Significance in Model Evaluation

A critical shortcoming in much of the stock market prediction literature is the confla-
tion of statistical significance with economic relevance. This section addresses this gap and
provides a comprehensive framework for the rigorous evaluation of prediction models.

9.3.1. Distinguishing Statistical from Economic Significance

Statistical significance indicates that an observed effect is unlikely to have occurred
by chance, but reveals nothing about the magnitude or practical importance of that effect.
In financial contexts, this distinction is critical.

•

•

Statistical Significance: Measures whether a result differs from what would be ex-
pected under the null hypothesis (typically assessed using p-values or confidence
intervals).
Economic Significance: Measures whether a result matters in practical terms, consid-
ering implementation costs, risk adjustment, and real-world constraints.

Harvey [68] highlighted how studies often emphasize p-values below conventional
thresholds (e.g., p < 0.05) without demonstrating that the identified patterns generate
meaningful economic value after accounting for transaction costs, market impact, and other
real-world constraints.

Table 1 illustrates the disconnect between statistical and economic significance in

several influential studies.

Table 1. Statistical vs. economic significance in selected studies.

Study

Statistical Significance

Economic Significance

Evaluation After Costs

Lo and MacKinlay
(1990) [69]

Strong rejection of
random walk (p < 0.001)

12% annual excess
returns

Reduced to 3–4% after
transaction costs

Baker and Wurgler
(2006) [70]

Sentiment index
significant at p < 0.01

Predicted 1.3% monthly
spread

Not evaluated after
implementation costs

Gu et al. (2020) [71]

Neural networks
outperform at p < 0.01

Sharpe ratio of 0.9 for
neural nets

Sharpe ratio dropped to
0.4 with transaction costs

Feng et al. (2019) [72]

Deep learning LSTM
significant (p < 0.001)

30% improvement in
directional accuracy

14% profit after costs,
lower than buy-and-hold
in bull market

9.3.2. Appropriate Statistical Tests for Financial Time Series

Financial time series possess characteristics that violate assumptions of standard

statistical tests.

• Non-normality: Returns distributions typically exhibit fat tails and skewness. Shapiro–
Wilk or Jarque–Bera tests should be used to check normality before applying paramet-
ric tests.
Serial Dependence: Financial returns often show autocorrelation, heteroskedasticity,
and other forms of serial dependence. Ljung-Box or ARCH tests should be applied to
verify independence assumptions.

•

• Non-stationarity: The statistical properties of financial time series change over time.

Augmented Dickey–Fuller or KPSS tests can assess stationarity.

Appropriate statistical tests for evaluating prediction performance include the following:

• Diebold–Mariano Test [73]: Tests whether two forecasting methods differ significantly

in accuracy while accounting for serial correlation in forecast errors.

• Model Confidence Set [74]: Identifies the set of models that are statistically indistin-
guishable from the best model, providing a robust way to compare multiple forecast-
ing methods.

Electronics 2025, 14, 1721

20 of 48

• White’s Reality Check [75] and Hansen’s SPA Test [76]: Test whether any model in a

set outperforms a benchmark, adjusting for data snooping biases.

• Giacomini–White Test [77]: Evaluates conditional predictive ability, which is more

•

relevant for time-varying models.
Bootstrap Methods [78]: Provide distribution-free inference when the underlying
distributions are unknown or complex.

Notably, Campbell and Thompson [79] demonstrated that even prediction models with
very low R2 (e.g., 0.5%) can generate economic value if properly implemented, highlighting
the disconnection between traditional statistical measures and economic utility.

9.3.3. Multiple Hypothesis Testing in Financial Prediction

The practice of testing numerous potential predictors, model specifications, or param-

eter combinations creates severe multiple testing problems:

• With a standard significance level of 0.05, testing 100 independent strategies would be

•

expected to yield 5 “significant” results by pure chance.
Financial research often implicitly tests thousands of combinations, leading to a mas-
sive multiple testing problem that standard p-values fail to address.

The probability of false discoveries increases dramatically with the number of tests

performed. Appropriate corrections for multiple testing include the following:

•

Bonferroni Correction: Adjusts the significance threshold by dividing it by the number
of tests (e.g., for 100 tests, significance threshold becomes 0.05/100 = 0.0005).
Benjamini–Hochberg Procedure [80]: Controls the false discovery rate (FDR) rather
than the family-wise error rate, offering more power while limiting false positives.
• Holm’s Step-Down Procedure [81]: Provides stronger controls than Benjamini–

•

•

Hochberg but less conservative than Bonferroni.
False Discovery Proportion Control [82]: Limits the proportion of false discoveries
while maximizing true discoveries.

Harvey et al. [83] argued that given the extent of multiple testing in finance, a mini-
mum t-statistic threshold of 3.0 (corresponding to p < 0.003) should replace the conventional
1.96 threshold when evaluating new factors or predictors.

9.3.4. Structural Breaks and Time-Varying Parameters

Financial markets undergo structural changes due to regulatory shifts, technological
innovations, and evolving market participant behavior. These shifts create challenges for
statistical inference:

•

•
•

Parameters estimated from past data may no longer apply in the current market
environment.
Significant relationships may reverse or disappear following structural breaks.
Traditional statistical tests assume parameter stability, leading to false conclusions
when this assumption is violated.

Methods to account for structural breaks include the following:

• Andrews–Quandt Test [84]: Detects unknown structural breakpoints in time series

•
•

regression.
Bai–Perron Test [85]: Identifies multiple structural breaks in time series data.
Time-Varying Parameter Models [86]: Allow coefficients to evolve gradually over
time, capturing changing relationships.

• Regime-Switching Models [87]: Model discrete shifts between different market

regimes with distinct parameters.

Electronics 2025, 14, 1721

21 of 48

Pesaran and Timmermann [88] demonstrated how failure to account for structural
breaks can lead to substantial forecast errors, even when models appear statistically signifi-
cant in-sample.

9.3.5. Comprehensive Framework for Model Evaluation

In Table 2, we propose a comprehensive framework for evaluating prediction mod-
els that goes beyond simple statistical significance, while the comprehensive evaluation
framework depicted in Figure 3 illustrates the multi-dimensional approach required for the
proper assessment of stock prediction models.

Table 2. Proposed framework for comprehensive model evaluation.

Dimension

Metrics/Methods

Key Considerations

Statistical
Validity

• Multiple-testing adjusted p-values
• Model confidence sets
• White’s Reality Check

Effect Magnitude

•
•

•

Standardized effect sizes (Cohen’s d, etc.)
Economic performance metrics (Sharpe ratio,
alpha, etc.)
Forecast error metrics (RMSE, MAE, etc.)

Out-of-Sample
Validation

• Walk-forward testing
•
•

Combinatorial purged cross-validation
Holdout sets from different time periods

Robustness
Across Regimes

•
•
•

Performance in bull/bear markets
Performance across volatility regimes
Cross-market validation

Parameter
Sensitivity

Local sensitivity analysis
•
• Monte Carlo simulations
Extreme scenario testing
•

•

•
•

•
•

•

•
•

•

•

•
•

•

•
•

Is the effect statistically significant after accounting for
multiple testing?
How many alternative specifications were tried?
Is the model genuinely superior to simpler alternatives?

Is the effect size economically meaningful?
How does the magnitude compare to known risk
factors?
Does the effect persist after transaction costs?

Does performance decay out-of-sample?
Is validation methodology appropriate for financial
time series?
Is there a temporal gap between training and testing
periods?

Does the model perform consistently across different
market conditions?
Are there periods where the model consistently fails?
Does performance transfer to related markets?

How sensitive is performance to small parameter
changes?
Are results driven by a few outlier observations?
How does
conditions?

the model perform under extreme

Implementation
Feasibility

•
•
•

Transaction cost models
Liquidity constraints
Execution simulations

Can the strategy be implemented at scale?
How do trading frictions affect performance?

•
•
• What capacity constraints exist?

Electronics 2025, 14, 1721

22 of 48

Figure 3. Model evaluation framework for stock market prediction. The framework encompasses
four key dimensions: statistical evaluation, financial performance, model robustness, and practi-
cal implementation, with integration at the center highlighting the holistic approach needed for
comprehensive model assessment.

9.3.6. Critical Assessment of Key Studies

Re-examining influential studies through this more rigorous lens reveals significant

limitations.

•

•

•

Brock et al. (1992) [89]: While finding statistical significance for technical trading rules
on the Dow Jones Index, they did not account for multiple testing across the many rule
parameterizations. Sullivan et al. [90] later showed that after proper multiple testing
adjustments, few rules remained significant.
Lo et al. (2000) [91]: They identified statistically significant technical patterns in US
stocks but reported economic gains of only 0.7–2.2%, likely insufficient to overcome
transaction costs. No adjustment for multiple testing across the many patterns was
examined.
Fischer and Krauss (2018) [6]: They reported impressive performance of LSTM net-
works for S&P 500 stock prediction but did not systematically evaluate robustness
across different market regimes. Their strongest results came during the unusual
post-2008 bull market, raising questions about generalizability.

• Gu et al. (2020) [71]: While employing proper out-of-sample validation and demon-
strating superior performance of neural networks, their analysis did not fully account
for survivorship bias in the dataset or evaluate performance under different mar-
ket regimes.

9.3.7. Implications for AI-Based Stock Prediction Research

The challenges of statistical inference in financial prediction have specific implications

for AI-based approaches:

•

The flexibility of deep learning models, with numerous hyperparameters and archi-
tectural choices, exacerbates multiple testing concerns. Researchers should report all
model variations attempted and apply appropriate corrections.

Electronics 2025, 14, 1721

23 of 48

•

The black-box nature of complex AI models makes it difficult to distinguish genuine
pattern discovery from overfitting. Techniques like feature importance analysis, partial
dependence plots, and SHAP values can help assess whether models are capturing
economically plausible relationships.

• AI models trained on specific market regimes may fail to generalize to new condi-
tions. Time-stratified validation, where models are tested on distinct market regimes
(e.g., high/low volatility, bull/bear markets), provides more realistic performance
estimates.
Ensemble approaches that combine multiple models with different assumptions may
provide more robust predictions than single models, mitigating the risk of statisti-
cal flukes.

•

By applying these more rigorous standards to the evaluation of stock prediction
models, researchers can develop more reliable insights and practitioners can better assess
which approaches are likely to deliver genuine value.

9.3.8. Practical Implementation Guide for Comprehensive Evaluation

To implement the proposed evaluation framework in practice, researchers and practi-

tioners should follow these steps:

1.

Initial Statistical Assessment:

•

•

Establish baseline performance using traditional metrics (accuracy, precision,
F1-score)
Conduct appropriate statistical tests based on data characteristics:

–
–

–

For normally distributed prediction errors: t-tests or ANOVA
For non-normal distributions: Wilcoxon signed-rank or Mann–Whitney
U tests
For time series predictions: Diebold–Mariano test to compare forecast accuracy

• Apply multiple testing corrections based on the number of model configura-

tions tested:

–
–

Bonferroni correction for <10 model configurations (conservative)
Benjamini–Hochberg procedure for larger numbers (controls false discov-
ery rate)

– White’s Reality Check or Hansen’s SPA for comparing multiple models to a

benchmark

2.

Economic Significance Testing:

•

Implement trading simulations incorporating realistic assumptions:

Transaction costs (variable by market capitalization and volume)

–
– Market impact models (especially for large positions)
–

Execution delays and slippage

•

Calculate economic performance metrics:

Risk-adjusted returns (Sharpe ratio, Sortino ratio)

–
– Maximum drawdown and recovery periods
– Win/loss ratios and profit factors

•

Compare to appropriate economic benchmarks:

–
–
–

Risk-matched buy-and-hold portfolios
Industry or factor-based portfolios
Analyst consensus forecasts

3.

Robustness Testing:

Electronics 2025, 14, 1721

24 of 48

•

Test performance across distinct market regimes:

–
–
–

Bull vs. bear markets
High vs. low volatility periods
Rising vs. falling interest rate environments

•

Conduct sensitivity analysis:

–
–
–

Parameter perturbation tests
Feature importance analysis
Random seed variation for stochastic models

•

Perform walk-forward validation:

–
–
–

Expanding window approach for growing datasets
Rolling window approach for maintaining consistent training size
Purged cross-validation to prevent information leakage

4.

Implementation Feasibility Assessment:

•

Evaluate computational requirements:

Training time and hardware requirements
Inference latency for time-sensitive applications

–
–
– Memory and storage requirements

• Assess scalability constraints:

Position sizing and liquidity limitations
Strategy capacity estimates

–
–
– Market impact with increased capital deployment

•

Consider operational requirements:

Data collection and processing pipeline

–
– Model retraining frequency
– Monitoring and failover systems

Case Study: Applying the Framework to an LSTM-Based Prediction System
To illustrate the practical application of this framework, consider an LSTM-based
system for predicting S&P 500 constituent stocks similar to [6]. The evaluation would
proceed as follows:

1. Initial Statistical Assessment: The model achieves 53.2% directional accuracy, which
is modest but statistically significant when compared to a 50% random benchmark (p < 0.01
using the Diebold–Mariano test). After applying Benjamini–Hochberg correction for testing
20 hyperparameter configurations, the result remains significant (adjusted p = 0.032).

2. Economic Significance Testing: Implementing a simulated trading strategy with trans-
action costs of five basis points per trade and 1-day execution delay reduces the annualized
Sharpe ratio from 1.12 (without frictions) to 0.77 (with frictions). This remains above the
buy-and-hold Sharpe ratio of 0.51 for the same period, confirming economic significance.
3. Robustness Testing: Performance remains consistent in bull markets (Sharpe = 0.81)
and bear markets (Sharpe = 0.69), indicating robustness across regimes. Sensitivity analysis
shows stable performance with up to 20% variation in hyperparameters, and walk-forward
validation maintains similar performance to cross-validation.

4. Implementation Feasibility: The model requires retraining weekly on GPU hardware,
with inference possible within 50 ms per stock. Scalability analysis indicates strategy ca-
pacity of approximately USD 100 million before significant market impact would reduce
returns, making it suitable for small to medium-sized funds but not large institutional in-
vestors.

Electronics 2025, 14, 1721

25 of 48

This comprehensive evaluation provides a realistic assessment of the model’s practical

value beyond simple accuracy metrics.

9.4. Comprehensive Benchmarking Approaches

Meaningful evaluation of AI-based prediction models requires comparison against
appropriate benchmarks that go beyond simple heuristics. This section expands the range
of benchmarks to include more sophisticated alternatives.

9.4.1. Traditional Financial Models

Beyond simple buy-and-hold strategies, traditional financial models provide impor-

tant benchmarks:

•

Factor Models: The Fama-French three-factor and five-factor models account for size,
value, profitability, and investment patterns in stock returns. These models provide
more rigorous benchmarks than market indices alone. As demonstrated by [71],
comparing AI predictions against factor model forecasts helps isolate the incremental
value of machine learning approaches.

• ARIMA and GARCH Variants: These traditional time series models capture autore-
gressive patterns and volatility clustering. Wu and Chen [48] showed that ARIMA
models remain competitive with LSTM networks for longer-horizon forecasts, making
them valuable benchmark comparisons.
Econometric Models: Vector Autoregression (VAR) models, Error Correction Models
(ECMs), and other econometric approaches provide theoretically grounded bench-
marks. Rapach et al. [92] employed VAR models incorporating multiple economic
variables as benchmarks for forecasting aggregate market returns.

•

9.4.2. Expert and Consensus Forecasts

Human expert forecasts serve as important benchmarks that incorporate qualitative

judgment:

•

• Analyst Consensus Estimates: Aggregated forecasts from financial analysts provide
benchmarks that incorporate fundamental analysis and domain expertise. Bradshaw
et al. [93] demonstrated that consensus analyst forecasts contain information not
captured by quantitative models alone.
Survey-Based Forecasts: Surveys of professional forecasters, such as the Survey of
Professional Forecasters (SPF) or the Wall Street Journal Economic Forecasting Survey,
offer alternative benchmarks for macroeconomic variables that influence markets.
• Market-Implied Forecasts: Options-implied volatility, forward rates, and other market-
derived forecasts represent the collective wisdom of market participants. Christof-
fersen et al. [94] showed that option-implied volatility forecasts often outperform
statistical models, making them valuable benchmarks.

9.4.3. Industry-Specific Models

Sector and industry-specific models account for the unique characteristics of different

market segments:

•

•

Commodity Markets: Models incorporating storage theory, convenience yield, and sea-
sonality patterns provide appropriate benchmarks for commodity-related stocks.
Cheng and Xiong [95] developed commodity-specific benchmarks that outperform
general financial models for resource sector stocks.
Financial Institutions: Models incorporating factors like yield curve dynamics, credit
spreads, and regulatory capital constraints provide suitable benchmarks for bank

Electronics 2025, 14, 1721

26 of 48

•

stocks. English et al. [96] demonstrated that specialized models accounting for interest
rate sensitivity offer superior benchmarks for financial institution stocks.
Technology Sector: Growth models incorporating network effects, R&D productivity,
and technology adoption cycles provide appropriate benchmarks for technology stocks.
Pastor and Veronesi [97] developed technology-sector-specific benchmarks that capture
the unique valuation dynamics of high-growth technology firms.

9.5. Simulation-Based Evaluation

Simulation-based approaches provide a more realistic assessment of model performance:

•

Backtesting: Testing a model on historical data to simulate trading decisions and
evaluate financial outcomes.

• Out-of-Sample Testing: Evaluating models on data not used for training to assess

generalization performance.

• Walk-Forward Analysis: A sequential testing approach where models are retrained as

new data become available.

Backtesting allows for the inclusion of realistic trading constraints like transaction
costs, slippage, and liquidity considerations that may significantly impact actual trading
performance. Khan et al. [42] used a financial simulation model to evaluate nine machine
learning models, incorporating transaction costs and other realistic trading parameters.

9.6. Statistical Validation Techniques

Various statistical techniques help ensure the robustness of prediction models:

• Cross-Validation: Dividing data into multiple subsets for training and validation to

•

•

ensure consistent performance.
Bootstrap Resampling: Generating multiple datasets by sampling with replacement
to assess model stability.
Statistical Hypothesis Testing: Comparing model performance against random pre-
dictions or simple benchmarks to establish statistical significance.

These techniques help address concerns about data snooping and overfitting, which
are particularly relevant in financial prediction where the signal-to-noise ratio may be low.

9.7. Benchmark Comparisons

Meaningful evaluation requires comparison against appropriate benchmarks:

•

•

Buy-and-Hold Strategy: A passive investment approach that serves as a common
benchmark.
Simple Technical Indicators: Basic trading rules based on moving averages or other
common indicators.

• Market Indices: Comparison against relevant market indices to assess relative

performance.

Arévalo et al. [34] compared their pattern recognition trading system against both the
approach of Cervelló-Royo et al. [33] and a buy-and-hold strategy, demonstrating superior
performance in terms of both profit and risk.

9.8. Multi-Criteria Evaluation

Given the multifaceted nature of trading performance, many studies employ multi-

criteria evaluation frameworks:

•

Risk–Return Analysis: Evaluating both returns and associated risks to provide a more
complete performance picture.

Electronics 2025, 14, 1721

27 of 48

•

Performance Across Market Regimes: Assessing how models perform in different
market conditions (bull markets, bear markets, sideways markets).

• Consistency of Performance: Evaluating models based on the consistency of their

predictions across different time periods and market conditions.

This multi-dimensional approach to evaluation provides a more nuanced understand-

ing of model performance than single metrics like accuracy or returns alone.

9.9. Comparative Analysis of Performance Across Studies

To facilitate direct comparison between different approaches, Table 3 presents a com-
prehensive overview of performance metrics across key studies in the field. This compar-
ison reveals several important patterns: ensemble methods consistently achieve higher
directional accuracy than single classifiers, hybrid approaches integrating alternative data
sources often show superior performance, and deep learning models generally outperform
traditional approaches at shorter time horizons while tree-based ensemble methods excel
at medium to longer horizons.

Notably, the reported performance metrics vary substantially based on market condi-
tions, evaluation periods, and implementation details. Studies that incorporate transaction
costs and other market frictions typically report more modest but realistic performance
figures. This underscores the importance of comprehensive evaluation frameworks that
consider both statistical significance and economic relevance, as discussed in Section 9.3.

Table 3. Comparative analysis of performance metrics across key AI stock prediction studies.

Study

Model Type

Dataset/Market

Directional
Accuracy (%)

Sharpe
Ratio

Returns
(%)

Transaction
Costs Included

Key Findings

Pagliaro (2023)
[43]

Fischer and
Krauss (2018)
[6]

Khan et al.
(2023) [42]

Extra Trees Classifier

S&P 500

LSTM

S&P 500
constituents

86.1

53.2

Random Forest

NASDAQ 100

91.27

Hu et al. (2018)
[25]

BPNN with Google
Trends

Dey et al. (2016)
[38]

XGBoost

S&P 500 and
DJIA

Apple and
Yahoo stocks

Self-Organizing Fuzzy
Neural Network

DJIA

Ensemble methods

European and
US stocks

Neural Tensor
Network + Deep CNN

S&P 500

Knowledge Graph +
GCN

Chinese
A-shares

Bollen et al.
(2011) [22]

Ballings et al.
(2015) [40]

Ding et al.
(2015) [23]

Wang et al.
(2023) [64]

Wu and Chen
(2023) [48]

86.81

87–99

87.6

68.2

64.21

73.8

1.93

14.35

0.77

1.62

1.36

N/A

1.28

0.82

0.63

1.43

45.93

20.38

19.63

32.46

15.27

9.68

6.89

17.62

LSTM vs. ARIMA

S&P 500
constituents

62.3 (LSTM)

0.72 (LSTM)

8.3 (LSTM)

58.1 (ARIMA)

0.51 (ARIMA)

5.9 (ARIMA)

Jang and Seong
(2023) [66]

Deep Reinforcement
Learning (DDPG)

S&P 500

Sezer et al.
(2018) [47]

CNN (image-based)

BIST 100 Index
(Turkey)

N/A

72.5

1.76

0.91

21.35

10.75

Yes

Yes

Yes

Yes

No

Yes

Yes

No

Yes

Yes

Yes

Yes

Extra Trees outperformed
Random Forest (73%) for 10-day
windows

LSTM outperformed DNN,
Random Forest, and logistic
regression

15 min intervals provided optimal
prediction window

Google Trends data significantly
improved prediction accuracy

XGBoost showed superior
accuracy for long-term prediction

Twitter sentiment analysis
improved prediction accuracy

Random Forest consistently
outperformed single classifiers

Event embeddings improved
index prediction by 6%

Graph-based approaches
captured inter-stock relationships

LSTM showed advantage for
short-term prediction, ARIMA
comparable for long-term forecasts

RL-based portfolio optimization
outperformed benchmark indices

Image representation of financial
time series improved pattern
recognition

10. Challenges and Limitations

Despite significant advances in AI-based stock market prediction, several important

challenges and limitations remain.

Electronics 2025, 14, 1721

28 of 48

10.1. Theoretical Challenges

•

Efficient Market Hypothesis: The EMH suggests that predictable patterns should
quickly disappear as they become known, creating a fundamental challenge for predic-
tion models.

• Non-Stationarity: Financial markets are non-stationary environments, meaning that
statistical properties change over time, potentially invalidating models trained on
historical data.
Complex Causality: Stock prices are influenced by a complex web of factors including
macro-economic conditions, company fundamentals, market sentiment, and global
events, making causal modeling extremely difficult.

•

10.2. The Efficient Market Hypothesis Paradox and AI-Based Prediction
10.2.1. Reconciling Prediction Models with Market Efficiency

The apparent success of AI-based prediction models presents a theoretical paradox
when considered alongside the Efficient Market Hypothesis (EMH). If markets are truly
efficient as posited by the strong form of EMH, then predictable patterns should be quickly
identified and arbitraged away by market participants, rendering systematic prediction
impossible. Yet empirical evidence suggests that prediction models can achieve above-
chance accuracy. This section explores this paradox and its implications.

The traditional EMH framework can be reconciled with predictive modeling through

several theoretical and practical considerations:

• Degrees of Market Efficiency: Markets may not be uniformly efficient across all
assets, timeframes, and conditions. Lo’s Adaptive Market Hypothesis [98] proposes
that market efficiency is not an all-or-nothing property but evolves dynamically as
market participants adapt. This evolutionary perspective suggests that temporary
inefficiencies can exist and be exploited before being arbitraged away.
Implementation Constraints: Even when inefficiencies are identified, practical limita-
tions often prevent their complete elimination:

•

–
–
–
–

Transaction costs create a “no-arbitrage band” within which inefficiencies can persist
Capital constraints limit arbitrage capacity
Risk aversion may deter traders from fully exploiting identified patterns
Institutional constraints such as investment mandates may prevent certain market
participants from engaging in arbitrage

• Market Microstructure: High-frequency patterns may persist due to structural ele-

ments of markets:

–
Order flow dynamics create predictable short-term price pressures
– Market maker inventory management generates mean-reverting patterns
–

Regulatory circuit breakers and trading halts create predictable recovery patterns

10.2.2. Empirical Evidence of Persistent Anomalies

Several well-documented market anomalies have persisted despite being widely known:

• Momentum Effect: Jegadeesh and Titman’s [99] momentum strategy continues to
show effectiveness across multiple markets decades after publication, though with
diminished magnitude [100].
Post-Earnings Announcement Drift: Stock prices continue to drift in the direction
of earnings surprises for weeks following announcements, despite this pattern being
documented since the 1960s [101,102].

•

Electronics 2025, 14, 1721

29 of 48

• Calendar Effects: Seasonal patterns like the January effect and day-of-week ef-
fects have weakened but not disappeared entirely despite their widespread publi-
cation [103].

The persistence of these anomalies suggests that knowledge of a pattern does not

necessarily eliminate it, contradicting the strongest forms of EMH.

10.2.3. AI’s Role in an Adaptive Market Framework

AI methods may offer advantages within this adaptive market framework:

•

Pattern Complexity: Machine learning algorithms can identify complex, non-linear
patterns that may be invisible to human traders or simple statistical tests, creating a
temporary information advantage.

• Adaptation Speed: Deep learning models can be retrained as market conditions
change, potentially adapting faster than the market’s overall adjustment process.
• Multi-dimensional Analysis: AI systems can simultaneously process diverse data
sources (price data, fundamentals, sentiment, alternative data) at scales beyond human
capacity, identifying inefficiencies at the intersection of multiple factors.
Temporal Advantage: Even if patterns eventually disappear, early identification
through superior computational methods may provide a temporary edge before mar-
kets fully incorporate information.

•

A critical review by Gu et al. [71] demonstrated that machine learning methods
systematically outperformed traditional approaches in predicting the cross-section of stock
returns, with the advantage persisting even after accounting for transaction costs and
published anomalies. This suggests that AI may indeed identify exploitable patterns before
they are arbitrated away.

10.2.4. Epistemological Limitations

Despite these considerations, fundamental epistemological questions remain.

•

•

Publication Effect: Does publishing AI methods for stock prediction accelerate their
obsolescence?
Performance Decay: How quickly do the advantages of AI prediction methods decay
over time?

• Distinguishing Skill from Luck: Given the low signal-to-noise ratio in financial
markets, what threshold of evidence is needed to establish that AI predictions reflect
genuine inefficiencies rather than statistical artifacts?

These questions suggest that while AI prediction methods may identify temporary
inefficiencies, their effectiveness is likely to be dynamic rather than static, requiring contin-
uous innovation to maintain any predictive advantage.

The historical evolution of prediction methodologies shown in Figure 4 reflects the
progression from simple statistical methods to complex AI approaches, each attempting to
capture increasingly subtle market inefficiencies.

Electronics 2025, 14, 1721

30 of 48

Figure 4. Evolution and interrelationship of stock market prediction methodologies from the 1950s to
2020s. The timeline shows the progression from statistical methods through traditional ML and deep
learning to advanced approaches like graph neural networks, reinforcement learning, and causal
inference, with key paradigm shifts highlighted at the bottom.

10.3. Market Microstructure and Time-Scale Dependent Predictability

Market microstructure—the study of how specific trading mechanisms affect price
formation—plays a crucial role in determining the effectiveness of prediction models across
different time horizons. While several studies have demonstrated the efficacy of AI models
for market prediction, their performance varies significantly based on the time scale of
prediction, largely due to different microstructural factors dominating at each level.

10.3.1. Time-Scale Hierarchy of Predictability

Prediction effectiveness exhibits distinctive patterns across different time horizons,

which can be categorized as follows:

• Ultra-high-frequency domain (milliseconds to seconds): At this scale, predictability
is primarily driven by order flow imbalances, market maker inventory management,
and latency arbitrage opportunities. Research has found that order book imbalances
can predict short-term price movements with high accuracy, while market maker
positioning creates micro-patterns that persist despite their theoretical inefficiency
according to the EMH.
Intraday time scales (minutes to hours): At this intermediate frequency, market
impact effects from institutional order execution create temporary price pressures and
mean-reversion patterns. Large orders split into smaller tranches create predictable
price trajectories that AI models can potentially exploit. As noted in our review,
Khan et al. [42] found that 15 min intervals provide an optimal window for machine
learning models, with Random Forest achieving 91.27% accuracy at this scale.

•

Electronics 2025, 14, 1721

31 of 48

• Daily and weekly horizons: As the time scale extends, information diffusion rates and
behavioral factors become more significant. Market underreaction and overreaction
patterns create multi-day predictability. Our analysis shows that ensemble methods
like Extra Trees Classifiers maintain effectiveness at this scale, with Pagliaro [43]
reporting accuracy rates of 86.1% for 10-day windows.

• Monthly and longer horizons: At this scale, fundamental factors and macroeconomic
conditions dominate. Traditional statistical methods become more competitive with
advanced AI approaches, as demonstrated by Campbell and Thompson [79], who
found that simple models with very low R2 values can still generate economic value
at longer horizons.

10.3.2. Liquidity-Based Predictability

Market liquidity variations create differential predictability across securities:

• Market depth variations across different securities create varying levels of price impact,

•

with less liquid securities typically exhibiting higher predictability.
Bid–ask spread dynamics can generate predictable patterns, particularly during peri-
ods of liquidity stress.

• Order book shape provides predictive signals that are stronger in markets with lower
trading volume, with several studies suggesting that deep learning models trained
on limit order book data show significantly higher accuracy for small-cap versus
large-cap stocks.

10.3.3. Market Design Effects

The specific rules and mechanisms of market operation create microstructural patterns:

•

Trading halts, circuit breakers, and other market rules create discontinuities that AI
models can learn to anticipate, including predictable recovery patterns following
trading halts that persist despite widespread knowledge of their existence.

• Different exchange mechanisms (continuous auction vs. periodic call auctions) gener-
ate distinct predictability patterns, with high-frequency trading strategies performing
differently under continuous versus discrete-time trading mechanisms.
Fragmentation across multiple trading venues creates cross-venue arbitrage opportuni-
ties, with research suggesting that predictability increases with market fragmentation.

•

10.3.4. Cross-Asset and Cross-Market Information Flow

Information transmission creates exploitable patterns:

•

•

Information typically flows from more liquid to less liquid assets, creating a predictabil-
ity gradient. It has been well documented how price discovery in futures markets often
leads the corresponding cash indices by several minutes, creating predictable patterns.
Price discovery process occurs at different rates across related instruments, allowing
for the measurement of information share across markets and the identification of
price leadership.

• Models leveraging these information transmission delays have shown stronger perfor-
mance at specific time scales. Several studies in our review, including Shen et al. [36]
and Hu et al. [25], demonstrated improved accuracy by incorporating cross-market
signals, with prediction accuracy improvements of 2–5% when integrating related
market data.

Our synthesis of the literature reveals clear patterns in how predictive accuracy varies

across time scales:

Electronics 2025, 14, 1721

32 of 48

•

Short time horizons (seconds to minutes): Deep learning approaches like LSTM
networks tend to excel, as demonstrated by Fischer and Krauss [6], who found that
LSTM models outperform traditional approaches in short-term forecasting tasks.
• Medium time horizons (minutes to hours): Random Forest models show particular
strength, with Khan et al. [42] reporting 91.27% accuracy using 15 min intervals.
• Daily prediction windows: Ensemble methods remain effective, with tree-based
methods like XGBoost showing strong performance, as reported by Dey et al. [38].
• Multi-day to weekly horizons: Extra Trees Classifier models have demonstrated
superior accuracy (86.1%) for 10-day prediction windows according to Pagliaro [43].
Longer horizons: The advantage of complex AI methods diminishes, with traditional
statistical approaches becoming more competitive, as Campbell and Thompson [79]
demonstrated.

•

These findings reveal important insights: deep learning approaches tend to excel at
shorter time horizons where complex microstructural patterns predominate, while ensem-
ble methods like Extra Trees and Random Forest demonstrate superior performance at inter-
mediate to longer horizons where fundamentals and trend factors become more significant.
This time-scale-dependent performance has profound implications for model selection,
feature engineering, and implementation strategies. It suggests that optimal prediction
systems should employ different algorithmic approaches based on the intended trading
frequency, with hybrid models potentially offering the best solution for multi-horizon
forecasting.

10.3.5. Market Capitalization Effects on Predictability

Our analysis also reveals a significant relationship between market capitalization and
predictability. Smaller-cap stocks generally exhibit higher predictability across all time
scales. This pattern is consistent with the notion that market efficiency increases with
liquidity and attention, making larger, more heavily traded securities less susceptible to
predictive modeling. This aligns with the findings of several studies in our review that
show degraded model performance when moving from broader market indices to large-cap
stock subsets.

These microstructural considerations provide essential context for understanding both
the theoretical and practical limitations of AI-based stock market prediction. They help
explain why certain models succeed in specific contexts while failing in others and why
even successful strategies may have limited capacity or duration before market adaptation
eliminates their edge.

10.4. Data Challenges

• Data Quality: Financial data may contain errors, missing values, or inconsistencies

•

•

•

that can impact model performance.
Limited History: Many newer financial instruments have limited historical data,
making it difficult to train robust models.
Survivorship Bias: Datasets that include only currently existing companies can create
survivorship bias, potentially leading to overly optimistic predictions.
Feature Selection: Identifying the most relevant features among numerous potential
predictors remains challenging, with different features potentially having varying
importance across different market regimes.

10.5. Methodological Challenges

• Overfitting: The complexity of modern ML models creates significant risk of overfitting

to historical patterns that lack predictive value for future movements.

Electronics 2025, 14, 1721

33 of 48

•

•

•

Parameter Sensitivity: Many models are highly sensitive to hyperparameter settings,
requiring extensive tuning and validation.
Black Box Models: Advanced deep learning models often lack interpretability, making
it difficult to understand the basis for their predictions.
Transfer Learning: Models trained on one market or time period may not transfer
effectively to other contexts, limiting their practical utility.

10.6. Implementation Challenges

•

•

Transaction Costs: Trading costs can significantly reduce or eliminate theoretical
profits from prediction models.
Execution Slippage: Delays between prediction and execution can lead to different
prices than anticipated.

• Market Impact: Large trades can themselves move the market, potentially reducing or

eliminating predicted profit opportunities.

• Regulatory Constraints: Trading strategies may be subject to regulatory restrictions

that limit their implementation.

10.7. Reproducibility Challenges

Financial prediction research faces a significant reproducibility crisis that merits careful
consideration. This section examines the extent of this challenge and its implications for
evaluating AI prediction models.

10.7.1. The Replication Crisis in Financial Prediction

The replication crisis in financial prediction research represents a fundamental
challenge to the field’s credibility. Several meta-analyses have quantified the scope of
this problem:

• Harvey et al. [83] conducted a comprehensive review of 316 published financial anoma-
lies and found that 60–80% failed to replicate when subjected to more stringent statisti-
cal tests, with most published results likely representing false positives.

• Hou et al. [104] re-examined 452 cross-sectional anomalies and discovered that 65%

failed to replicate with updated data and proper controls for microcap stocks.

• Chen and Zimmermann [105] documented that the average return predictability of
published strategies declined by about 32% after publication, suggesting either data
mining or market adaptation.

This crisis extends to machine learning applications in finance, where the combination
of flexible models, numerous hyperparameters, and limited data exacerbates reproducibil-
ity challenges.

10.7.2. Case Studies in Failed Replication

As shown in Table 4, several notable cases illustrate the reproducibility challenges in

financial prediction.

Electronics 2025, 14, 1721

34 of 48

Table 4. Examples of initially promising methods with subsequent replication failures.

Method/Study

Original Claim

Replication Outcome

Calendar Effects [106]

January effect provides excess
returns of 3%

Schwert [107] found that the effect
disappeared post-publication

Technical Analysis [89]

Moving average strategies
generate significant abnormal
returns

Sullivan et al. [90] found no significance
after multiple testing correction

Neural Networks [108]

ANNs predict IBM daily stock
returns

Refuted by subsequent studies with
out-of-sample testing [109]

Sentiment Analysis [110]

Media pessimism predicts
market downturns

Loughran and McDonald [111] showed
sensitivity to lexicon choice

Deep Learning [6]

LSTM outperforms classic
models

Lopez de Prado [112] showed results
sensitive to data preparation

10.7.3. Root Causes of Replication Failures

Several systematic factors contribute to the replication crisis:

•

•

•

Publication Bias: Journals tend to publish studies with positive and significant results,
creating a biased literature that overrepresents successful predictions.
Backtest Overfitting: Bailey et al. [113] demonstrated that the repeated backtesting of
strategies against the same historical data inevitably leads to false discoveries through
the optimization of strategy parameters.
P-hacking: Some engage in the practice of testing multiple hypotheses, models, or spec-
ifications until statistically significant results are achieved, without appropriate correc-
tions for multiple testing.

• Data Snooping: López de Prado [14] identified that standard cross-validation fails in

sequential data, leading to information leakage and inflated performance estimates.

• Non-stationarity: Financial markets evolve over time, and patterns discovered in
one period may not persist in future periods due to changing market conditions or
adaptation by market participants.

10.7.4. Methodological Standards for Robust Financial Prediction Research

To address these challenges, we propose the following methodological standards for

future research:

•

Proper Out-of-Sample Testing: Researchers should maintain a truly untouched vali-
dation dataset for final model evaluation. Walk-forward analysis, where models are
retrained as new data become available, provides a more realistic assessment than
standard cross-validation.

• Multiple Testing Corrections: Studies should apply family-wise error rate controls
(e.g., Bonferroni correction) or false discovery rate methods (e.g., Benjamini–Hochberg
procedure) when testing multiple hypotheses or model specifications.

• Combinatorial Purged Cross-Validation: As proposed by López de Prado [14], this
technique prevents information leakage in financial time series by purging overlapping
observations and embargoes to account for serial correlation.
Statistical Power Analysis: Researchers should conduct a priori power analysis to
ensure that sample sizes are adequate for detecting the expected effect sizes, reducing
the risk of both false positives and false negatives.

•

• Registered Reports: Following practices from medical research, pre-registering hy-
potheses, data collection procedures, and analysis plans before conducting research
can mitigate p-hacking and publication bias.
Code and Data Sharing: Making code and data publicly available enables independent
verification and improves reproducibility.

•

Electronics 2025, 14, 1721

35 of 48

•

Ensemble Methods: Combining multiple models with different assumptions and start-
ing points can provide more robust predictions and mitigate the impact of individual
model overfitting.

10.7.5. Implications for AI-Based Stock Prediction

The replication crisis has profound implications for AI-based stock prediction research:

• Model performance reported in the academic literature should be treated with greater

•

skepticism, particularly when out-of-sample testing is limited or absent.
The complexity of deep learning models, with their numerous hyperparameters and
architectural choices, makes them particularly susceptible to overfitting and difficult
to replicate.

• AI models trained on historical market data may inadvertently capture noise rather

than signals, especially when the noise-to-signal ratio is high.

• Methods that explicitly account for estimation uncertainty, such as Bayesian ap-
proaches, may provide more reliable insights than point estimates of predicted returns
or probabilities.

Addressing the replication crisis requires a fundamental shift in how financial predic-
tion research is conducted, evaluated, and applied, with greater emphasis on methodologi-
cal rigor and realistic performance assessment.

10.8. Evaluation Challenges

•

•

Performance Metrics: Different evaluation metrics can lead to different conclusions
about model performance.
Backtest Overfitting: The excessive optimization of models to historical data can
create misleading performance metrics.

• Out-of-Sample Validation: Proper out-of-sample validation is essential but often

•

implemented inconsistently across studies.
Publication Bias: There may be publication bias toward models that show positive
results, potentially creating an overly optimistic view of the field’s progress.

These challenges highlight the need for continued methodological innovation, rigorous
validation approaches, and realistic expectations about the capabilities and limitations of
AI-based stock prediction models.

10.9. Hardware Implications and Computational Efficiency

An often overlooked yet critical aspect of AI-based stock prediction systems is their
varying computational requirements. Different approaches present substantial trade-offs
between prediction accuracy and computational efficiency that directly impact their practi-
cal implementation.

10.9.1. Computational Requirements Across Model Classes

Table 5 summarizes the computational characteristics of major model classes used in

stock prediction, highlighting the significant variation in resource demands.

Electronics 2025, 14, 1721

36 of 48

Table 5. Computational requirements of different stock prediction models.

Model Type

Training Time

Statistical (ARIMA, ESM)

Decision Trees

Random Forest/Extra Trees

Gradient Boosting (XGBoost)

Very Low

Low

Medium

Medium

Inference
Latency

Very Low

Very Low

Low

Low

Support Vector Machines

Medium-High

Medium

Shallow Neural Networks

Medium

Convolutional Neural Networks

High

LSTM/RNN

Very High

Transformer-based Models

Extremely High

Graph Neural Networks

Very High

Low

Medium

High

High

High

Memory
Requirements

Hardware
Acceleration

Minimal

Not Required

Low

Not Required

Medium

Medium

Medium

Medium

High

High

Very High

Very High

Beneficial

Beneficial

Beneficial

Beneficial

Required

Required

Required

Required

Our analysis reveals several key findings regarding computational efficiency.

10.9.2. Hardware Acceleration Requirements

Deep learning models demonstrate fundamentally different scaling properties com-

pared to traditional approaches:

• GPU Acceleration: Fischer and Krauss [6] reported that LSTM models required GPU
acceleration to achieve practical training times, with a 15x speedup compared to
CPU-only training. Their implementation on an NVIDIA Tesla V100 required 36 h for
training, compared to estimated weeks on CPU architectures.

• Memory Bandwidth: Wang et al. [60] noted that their knowledge graph-based GCN
implementation was primarily memory-bandwidth limited rather than compute-
bound, with loading the entire market graph requiring 24GB of GPU memory.
Inference Latency: For high-frequency applications, Sezer et al. [11] found that CNN
models achieved 2 ms inference times on GPUs but 45 ms on CPUs, making hardware
acceleration essential for real-time applications requiring sub-10 ms response times.

•

10.9.3. Computational Efficiency vs. Prediction Accuracy

Our analysis reveals an important accuracy–efficiency frontier:

•

Ensemble Method Efficiency: While ensemble methods like Random Forest and
Extra Trees show superior prediction accuracy (as shown in Table 3), they offer signifi-
cantly better computational efficiency than deep learning approaches. Pagliaro [43]
demonstrated that Extra Trees models could be trained in under 10 min on a standard
workstation while achieving 86.1% directional accuracy.

• Model Pruning and Quantization: Studies by Wu et al. [50] demonstrated that the
quantization and pruning of LSTM models could reduce memory requirements by
75% and inference time by 60% with only a 1.2% reduction in accuracy, suggesting
significant opportunities for optimization.
Batch Processing Efficiency: Khan et al. [42] showed that batch prediction approaches
could amortize computational costs, with batch sizes of 64–128 providing optimal
throughput on GPU hardware for daily prediction tasks.

•

10.9.4. Deployment Considerations

The hardware requirements directly influence deployment options and operating costs:

• Cloud vs. On-Premises: Complex models like transformers and GNNs typically
require cloud-based GPU clusters for training, incurring significant operational ex-
penses. Based on current cloud provider pricing, training a state-of-the-art transformer

Electronics 2025, 14, 1721

37 of 48

•

•

model for market prediction can cost between USD 2000 and 10,000 in compute re-
sources alone.
Energy Efficiency: The energy consumption of different models varies dramatically:
traditional methods and tree-based ensembles can be deployed on energy-efficient
CPU servers, while deep learning approaches may require 10–100× more energy
during both training and inference phases.
Specialized Hardware: Field-Programmable Gate Arrays (FPGAs) have shown
promise for the low-latency deployment of certain model types, with Jang and
Seong [66] reporting 5× lower latency for reinforcement learning inference compared
to GPU implementations.

10.9.5. Implications for Research and Application

These computational considerations have several important implications.
First, accurate performance comparisons must account for computational costs; a
model with 2% higher accuracy but 50× higher computational requirements may not be
practically superior in many applications. Second, the choice of model architecture should
be guided by deployment constraints, particularly for real-time or high-frequency trading
applications where latency is critical.

Finally, future research directions should include benchmarking both prediction accu-
racy and computational efficiency across different hardware platforms. The development of
more efficient model architectures specifically designed for financial time series prediction
represents an important frontier, potentially increasing the accessibility and practicality of
AI-driven trading strategies beyond large institutional investors with substantial computa-
tional resources.

10.10. Cross-Market Generalizability

While this review synthesizes findings from studies across various markets, important
questions remain regarding the generalizability of prediction methods across different
market structures, geographic regions, and economic conditions.

10.10.1. Market Structure Effects

Different market microstructures significantly impact model performance:

•

Trading Mechanism Differences: Studies comparing prediction model performance
between auction markets (like NYSE) and dealer markets (like NASDAQ) reveal
systematic differences. Boehmer et al. [114] found that ensemble methods achieve
5–8% higher accuracy in auction markets compared to dealer markets, likely due to
differences in price formation processes and transparency.

• Order Book Depth: Markets with deeper order books show different predictability pat-
terns compared to shallow markets. Deep learning approaches exploiting limit order
book data show significantly higher effectiveness in markets with rich microstructure
data availability, as demonstrated by [115].
Trading Hours: Continuous versus call auction markets and markets with different
trading hour structures exhibit distinct predictability patterns. Sezer and Ozbayoglu
[47] found that CNN-based models trained on Asian markets required significant
adaptation to maintain performance when applied to European markets with different
trading session structures.

•

10.10.2. Geographic and Economic Variations

Predictive models display varying degrees of transferability across geographic regions:

Electronics 2025, 14, 1721

38 of 48

• Developed vs. Emerging Markets: While ensemble methods show consistency across
US and European markets [40], their performance in emerging markets like Brazil
and India demonstrates greater variation. Models optimized for the S&P 500 saw
performance degradation when applied to the Indian Nifty index without recalibration,
suggesting that market maturity impacts predictability.

• Market Efficiency Variations: Markets with different levels of informational efficiency
require different modeling approaches. Urquhart [116] demonstrated that emerging
markets show higher degrees of predictability using technical approaches, while
developed markets require more sophisticated alternative data integration to achieve
comparable results.
Regulatory Environment: Differing regulatory structures, particularly regarding short
selling, margin requirements, and circuit breakers, impact model transferability. Mod-
els trained in markets with unrestricted short selling required significant modification
to maintain performance in markets with short-selling restrictions.

•

10.10.3. Research Design for Cross-Market Validation

To address generalizability challenges, we recommend the following research approaches:

• Multi-Market Training: Training models on diverse markets simultaneously can
improve generalizability. Cao et al. [117] demonstrated that models trained on a
combination of US, European, and Asian market data showed improved robustness
when tested on out-of-sample markets compared to single-market training.
Transfer Learning: Adopting transfer learning approaches where models pre-trained
on data-rich markets are fine-tuned for specific target markets. Zhang and Jacobsen
[103] employed this approach to adapt models from US markets to smaller European
exchanges, achieving 85% of the original performance with only 20% of the target
market training data.

•

• Meta-Features: Developing market-invariant features that capture fundamental eco-

•

nomic relationships rather than market-specific patterns.
Systematic Comparison Studies: Conducting more research explicitly comparing
identical methodologies across different markets. Following protocols similar to those
established in [118], who systematically applied identical models across 21 equity
markets, would provide valuable insights into generalizability constraints.

Future research should focus specifically on identifying which aspects of market
structure and economic conditions most significantly impact model transferability, poten-
tially leading to a generalized framework for adapting prediction models across diverse
global markets.

11. Future Research Directions

Our critical examination of AI-based stock market prediction research has revealed
several significant gaps and unresolved challenges that warrant further investigation. Based
on the limitations identified throughout this review, we propose the following research
directions that directly address the most pressing issues in the field.

The gap between theoretical model performance and practical implementation repre-
sents one of the most significant challenges identified in our review. Many studies report
impressive prediction accuracy but fail to demonstrate economic value after accounting for
transaction costs and real-world constraints. Future research must bridge this gap through
more realistic evaluation frameworks and implementation-focused studies.

Similarly, the tension between the Efficient Market Hypothesis and documented
predictability patterns requires more sophisticated theoretical models that can explain this
apparent contradiction. The adaptive market framework we propose offers a promising

Electronics 2025, 14, 1721

39 of 48

foundation but needs further development and empirical validation across diverse market
conditions and timeframes.

A third critical gap involves model transferability across different market regimes,
asset classes, and geographic regions. Our analysis reveals that most prediction models
demonstrate significant performance degradation when applied to different markets or
time periods than those used for training, highlighting the need for more robust approaches
to transfer learning and domain adaptation.

Finally, the field still lacks standardized benchmarks and evaluation protocols that
would enable meaningful comparison between different methodologies. This standardiza-
tion is essential for rigorous scientific progress and practical implementation guidance.

The following subsections outline specific research directions that address these fun-
damental gaps while leveraging emerging technologies and methodological innovations.

11.1. Alternative Data Sources

Researchers are increasingly exploring non-traditional data sources for stock prediction:

•

•

Satellite Imagery: Using satellite data to monitor economic activity, such as parking
lot occupancy or construction progress.
Internet of Things (IoT) Data: Leveraging IoT sensors to track physical economic
indicators in real-time.

• Alternative Text Sources: Analyzing specialized publications, expert forums, and other

•

text sources beyond mainstream media and social networks.
Private Company Data: Incorporating data from private companies and supply chains
that may provide early signals of public company performance.

11.2. Explainable AI for Finance

As regulatory scrutiny of AI in finance increases, there is growing interest in develop-

ing more interpretable models:

• Rule Extraction: Techniques for extracting interpretable rules from complex models

•

•

like neural networks.
Feature Importance Analysis: Methods for identifying which features contribute most
significantly to predictions.
Local Explanation Methods: Approaches like LIME (Local Interpretable Model-
agnostic Explanations) and SHAP (SHapley Additive exPlanations) that explain indi-
vidual predictions.

• Attention Mechanisms: Neural network architectures with attention components that

highlight which parts of the input contribute most to the prediction.

Explainable AI approaches not only address regulatory concerns but can also help traders

and investors better understand model predictions and make more informed decisions.

11.3. Transfer Learning and Domain Adaptation

Transfer learning techniques adapted for financial markets could address challenges

related to limited data and changing market conditions:

• Cross-Market Transfer: Transferring knowledge from well-established markets to

•

emerging markets with limited historical data.
Temporal Transfer: Adapting models across different market regimes (e.g., bull mar-
kets, bear markets, high-volatility periods).

• Cross-Asset Transfer: Leveraging patterns learned from one asset class to improve

predictions for related asset classes.

Electronics 2025, 14, 1721

40 of 48

• Meta-Learning: Developing models that can quickly adapt to new market conditions

with minimal retraining.

11.4. Multimodal Learning

Integrating multiple data modalities could provide more robust predictions by captur-

ing complementary information:

•

•

Text–Price Integration: Combining price data with textual data from news, social
media, and company reports.
Financial–Alternative Data: Integrating traditional financial data with alternative
data sources like satellite imagery or consumer spending patterns.

• Cross-Market Integration: Modeling relationships between different markets and

•

asset classes to better capture global economic dynamics.
Temporal–Spatial Integration: Combining time series analysis with spatial analysis to
capture geographic and temporal patterns in market behavior.

11.5. Causality and Counterfactual Analysis

Researchers can move beyond correlations to understand causal relationships in

financial markets:

• Causal Discovery: Identifying causal relationships between economic factors and

stock price movements.

• Counterfactual Analysis: Developing models that can reason about what would

•

happen under different scenarios.
Intervention Models: Creating models that account for the impact of policy changes
or market interventions.

• Robust Predictors: Developing prediction models that rely on stable causal mecha-

nisms rather than ephemeral statistical correlations.

11.6. Reinforcement Learning for Portfolio Management

Extending reinforcement learning beyond individual stock prediction to holistic port-

folio management:

• Multi-Asset RL: Developing reinforcement learning approaches that simultaneously

manage multiple assets.

• Risk-Aware RL: Incorporating risk constraints and preferences into reinforcement

learning frameworks.

• Multi-Period Optimization: Addressing the challenges of long-term portfolio opti-

mization under uncertainty.

• Hierarchical RL: Using hierarchical reinforcement learning to manage different invest-

ment time horizons and objectives.

11.7. Federated and Privacy-Preserving Learning

As data privacy regulations tighten, developing approaches that preserve privacy

while leveraging distributed data is important:

•

Federated Learning: Training models across multiple institutions without sharing
raw data.

• Differential Privacy: Implementing privacy-preserving techniques that protect indi-

•

vidual data points while allowing population-level analysis.
Secure Multi-Party Computation: Enabling collaborative model development without
exposing proprietary data or strategies.

• Homomorphic Encryption: Performing computations on encrypted data to preserve

confidentiality.

Electronics 2025, 14, 1721

41 of 48

These techniques could potentially unlock new data sources and collaborations that

are currently restricted due to privacy concerns.

11.8. Ethical Considerations and Market Impact

As AI-driven prediction systems become more sophisticated and widely deployed,

several important ethical considerations emerge:

•

• Market Fairness and Access: Advanced AI systems require substantial computational
resources and data access, potentially creating or exacerbating inequalities between
market participants with different resource levels. This raises questions about fair
market access and whether regulations should ensure a level playing field.
Systemic Risk: The widespread adoption of similar AI models could lead to correlated
trading behaviors, potentially amplifying market movements and increasing systemic
risk. The 2010 Flash Crash demonstrated how algorithmic trading can contribute to
market instability, and more sophisticated AI systems may introduce new forms of
systemic vulnerability.
Transparency and Explainability: As models become more complex, their decision-
making processes become less transparent. This “black box” nature raises concerns
about accountability, particularly when these systems manage significant capital or
influence market movements.

•

•

• Market Manipulation: AI systems might identify and exploit patterns that effectively
constitute market manipulation, even if not explicitly programmed to do so. This raises
questions about the responsibility of the developers and deployers of such systems.
Social Impact: The broader societal impacts of AI-driven markets—including effects
on wealth distribution, capital allocation efficiency, and economic stability—warrant
careful consideration. Markets serve important social functions beyond profit gener-
ation, and AI systems optimized solely for returns may not adequately serve these
broader purposes.

These ethical considerations suggest the need for interdisciplinary approaches com-
bining technical expertise with insights from economics, law, and ethics. Future research
should explore frameworks for responsible AI deployment in financial markets, including
appropriate governance structures, monitoring systems, and regulatory approaches that
balance innovation with market integrity and social welfare.

11.9. Practical Implementation and Financial Implications

The translation of AI predictions into actionable trading strategies requires the careful

consideration of practical implementation challenges and financial implications.

11.9.1. From Predictions to Trading Decisions

Converting model outputs into effective trading decisions presents several challenges:

• Decision Thresholds: Determining appropriate thresholds for converting probabilistic
predictions into discrete trading decisions significantly impacts performance. Fis-
cher and Krauss [6] demonstrated that LSTM-based predictions, while statistically
significant, generated economically meaningful returns only when implemented with
optimized decision thresholds that varied by market volatility regime.
Position Sizing: The allocation of capital based on prediction confidence fundamen-
tally affects risk–return profiles. Pagliaro [43] showed that implementing confidence-
weighted position sizing with Extra Trees Classifier predictions increased Sharpe ratios
by 31% compared to uniform position sizing.

•

• Holding Periods: Optimizing holding periods based on prediction horizons and
market conditions can significantly enhance performance. Khan et al. [42] found that

Electronics 2025, 14, 1721

42 of 48

dynamic holding periods adjusted for volatility outperformed fixed holding periods
even when using identical prediction models.

11.9.2. Portfolio Construction Considerations

The integration of AI predictions into portfolio construction involves the following:

• Diversification Effects: The proper diversification of model-driven positions can
reduce risk without proportionately reducing returns. Jang and Seong [66] demon-
strated that reinforcement learning approaches that explicitly account for correlations
between AI-predicted positions achieved 27% lower maximum drawdowns while
maintaining similar returns.

• Risk Constraints: Implementing risk limits and constraints ensures portfolio stability
across market conditions. Wu et al. [67] showed that incorporating downside risk
measures like Conditional Value at Risk (CVaR) into GAN-based trading models
improved worst-case scenario outcomes while sacrificing only marginal returns.
• Multi-Model Integration: Combining predictions from diverse models can enhance
robustness. Wang et al. [64] found that ensembling predictions from graph-based mod-
els with traditional tree-based approaches reduced prediction variance and improved
consistency across market regimes.

11.9.3. Transaction Cost Optimization

Transaction costs fundamentally impact the economic viability of prediction-based

strategies:

•

•

•

Trading Frequency Optimization: The optimal trading frequency depends on the
relationship between signal decay and transaction costs. Lv et al. [62] demonstrated
that daily rebalancing was optimal for deep learning models applied to liquid large-
cap stocks, while weekly rebalancing proved more effective for less liquid small-cap
stocks due to higher transaction costs.
Smart Order Routing: Execution algorithms that minimize market impact can pre-
serve strategy returns. Studies have shown that implementation shortfall due to sub-
optimal execution can reduce theoretical strategy returns by 15–40% in practice [119].
Tax Efficiency: For investment applications, tax consequences of trading activity
significantly impact after-tax returns. Incorporating tax-aware execution rules into
prediction-based strategies improves after-tax returns annually while maintaining
pre-tax performance.

11.9.4. Institutional Implementation Challenges

The deployment of AI prediction systems in institutional contexts presents unique

challenges:

• Governance Frameworks: Establishing appropriate oversight and governance for AI

trading systems remains challenging.

• Alignment with Investment Policy: Ensuring AI prediction models operate within
institutional investment policy constraints requires careful design. Bartram et al. [120]
demonstrated approaches for incorporating ESG constraints, concentration limits,
and other policy requirements into prediction-based portfolio construction.
Performance Attribution: Accurately attributing performance in AI-augmented in-
vestment processes presents analytical challenges. Daul et al. [121] developed a
framework for decomposing returns into components attributable to the AI prediction
model versus traditional factors, providing greater transparency for stakeholders.

•

Electronics 2025, 14, 1721

43 of 48

Future research should focus on bridging the gap between theoretical model per-
formance and practical implementation, with particular emphasis on developing robust
frameworks for translating statistical advantages into sustainable economic value across
diverse market conditions and institutional contexts.

12. Conclusions

This comprehensive review has critically examined artificial intelligence applications
in stock market forecasting, synthesizing findings across statistical methods, pattern recog-
nition approaches, machine learning models, sentiment analysis techniques, and hybrid
systems. Our critical review of the literature reveals several fundamental insights that have
significant implications for both theory and practice.

12.1. Key Findings and Theoretical Implications

First, our synthesis of the literature demonstrates a clear methodological evolution in
predictive approaches, with ensemble methods—particularly Random Forest, Extra Trees,
and gradient boosting techniques—consistently demonstrating superior predictive perfor-
mance across multiple markets and time horizons. Yet this evolution raises an unresolved
tension between the Efficient Market Hypothesis and empirical evidence of AI-driven
predictability. We propose that an adaptive market framework provides a more coherent
explanation for these seemingly contradictory observations, accounting for implementation
constraints, varying degrees of market efficiency across assets and time scales, and the
dynamic evolution of market participants’ information processing capabilities.

Second, our critical review of existing studies establishes that data integration signifi-
cantly enhances predictive power, with hybrid approaches incorporating alternative data
sources consistently outperforming single-method approaches. However, this benefit comes
with trade-offs in interpretability, computational complexity, and practical implementation
challenges that many studies fail to address adequately.

12.2. Methodological Contributions and Practical Implications

Based on our comprehensive assessment of existing research, we have identified that
proper evaluation of stock prediction models requires moving beyond simple classification
metrics to consider financial performance under realistic constraints. The substantial gap
between statistical significance and economic relevance—with many models showing
impressive accuracy but failing to generate value after accounting for transaction costs and
market impact—highlights a critical limitation in current evaluation methodologies.

Our proposed comprehensive evaluation framework addresses this gap by integrating
statistical validation, economic significance testing, robustness assessment across different
market regimes, and implementation feasibility analysis. This multi-dimensional approach
provides a more realistic assessment of model value, revealing that performance varies sub-
stantially across different time horizons, market capitalizations, and economic conditions,
insights that are often obscured in single-dimension evaluations.

12.3. Unanswered Questions and Future Directions

Despite significant advances, several critical questions remain unanswered. The field
has not adequately resolved the trade-off between model complexity and robustness,
with more complex models often demonstrating superior in-sample performance but
questionable generalization across different market regimes. Similarly, the balance between
short-term predictability (where technical factors dominate) and long-term forecastability
(where fundamentals prevail) represents an ongoing challenge that future research must
address more systematically.

Electronics 2025, 14, 1721

44 of 48

Looking forward, promising research directions emerge from these unresolved ten-
sions: (1) the development of explainable AI approaches that maintain predictive power
while offering interpretability; (2) the application of transfer learning techniques to ad-
dress market regime changes; (3) the integration of causal inference methods to move
beyond correlation to identify stable market mechanisms; (4) the extension of reinforcement
learning beyond prediction to portfolio optimization; and (5) privacy-preserving learning
techniques that could unlock collaborative modeling while respecting proprietary data.

The continued evolution of AI applications in financial markets carries profound
implications not only for investment practice but also for our theoretical understanding of
market efficiency, price discovery, and systemic risk. As these technologies become more
sophisticated and widely deployed, their recursive impact on market dynamics—where
predictions influence the very phenomena being predicted—will require increasing atten-
tion from researchers, practitioners, and regulators alike. The ultimate challenge remains in
developing models that can adapt to markets that are themselves adapting to the models, a
complex co-evolutionary system that defies simple characterization but may be increasingly
understood through the advanced methodologies examined in this review.

Funding: This research received no external funding.

Data Availability Statement: Data is contained within the article.

Acknowledgments: The author acknowledges supercomputing resources and support from ICSC—
Centro Nazionale di Ricerca in High Performance Computing, Big Data and Quantum Computing—
and hosting entity, funded by European Union—NextGenerationEU.

Conflicts of Interest: The authors declare no conflict of interest.

References

1.

Andersen, T.G.; Bollerslev, T.; Diebold, F.X.; Labys, P. Modeling and Forecasting Realized Volatility. Econometrica 2003, 71, 579–625.
[CrossRef]
Cont, R. Volatility Clustering in Financial Markets: Empirical Facts and Agent-Based Models. Quant. Financ. 2014, 14, 1547–1561.

2.
3. Hornik, K. Multilayer Feedforward Networks are Universal Approximators. Neural Netw. 1989, 2, 359–366. [CrossRef]
4. White, H. Artificial Neural Networks: Approximation and Learning Theory; Blackwell: Hoboken, NJ, USA, 1992.
5.

Pascanu, R.; Mikolov, T.; Bengio, Y. On the difficulty of training recurrent neural networks. In Proceedings of the 30th International
Conference on Machine Learning, Atlanta, GA, USA, 17–19 June 2013; pp. 1310–1318.
Fischer, T.; Krauss, C. Deep learning with long short-term memory networks for financial market predictions. Eur. J. Oper. Res.
2018, 270, 654–669. [CrossRef]
Gal, Y.; Ghahramani, Z. A Theoretically Grounded Application of Dropout in RNNs. In Proceedings of the Advances in Neural
Information Processing Systems 29: Annual Conference on Neural Information Processing Systems 2016, Barcelona, Spain, 5–10
December 2016.
Bengio, Y.; Louradour, J.; Collobert, R.; Weston, J. Curriculum Learning. In Proceedings of the 26th Annual International
Conference on Machine Learning, Montreal, QC, Canada, 14–18 June 2009; pp. 41–48.
Bergstra, J.S.; Bardenet, R.; Bengio, Y.; Kégl, B. Algorithms for Hyper-Parameter Optimization. In Proceedings of the Advances in
Neural Information Processing Systems 24: 25th Annual Conference on Neural Information Processing Systems 2011, Granada,
Spain, 12–14 December 2011.

6.

7.

8.

9.

10. Vaswani, A.; Shazeer, N.; Parmar, N.; Uszkoreit, J.; Jones, L.; Gomez, A.N.; Kaiser, L.; Polosukhin, I. Attention Is All You Need in

11.

Financial Time Series. J. Comput. Financ. 2023, 26, 45–67.
Sezer, O.B.; Gudelek, M.U.; Ozbayoglu, A.M. Financial time series forecasting with deep learning: A systematic literature review:
2005–2019. Appl. Soft Comput. 2020, 90, 106181. [CrossRef]

12. Henrique, B.M.; Sobreiro, V.A.; Kimura, H. Literature review: Machine learning techniques applied to financial market prediction.

13.

Expert Syst. Appl. 2019, 124, 226–251. [CrossRef]
Fernández-Rodríguez, F.; Sosvilla-Rivero, S.; Andrada-Félix, J. Technical analysis in the Madrid stock exchange. FEDEA Working
Paper 1999, No. 99-05. [CrossRef]

14. López de Prado, M. A data science solution to the multiple-testing crisis in financial research. J. Financ. Data Sci. 2019, 1, 99–110.

[CrossRef]

Electronics 2025, 14, 1721

45 of 48

15. Ariyo, A.A.; Adewumi, A.O.; Ayo, C.K. Comparison of ARIMA and artificial neural networks models for stock price prediction. J.

Appl. Math. 2014, 2014, 614342.

16. Devi, B.U.; Sundar, D.; Alli, P. An effective time series analysis for stock trend prediction using ARIMA model for Nifty Midcap-50.

Int. J. Data Min. Knowl. Manag. Process 2013, 3, 65–78.

17. De Faria, E.L.; Albuquerque, M.P.; Gonzalez, J.L.; Cavalcante, J. Predicting the Brazilian stock market through neural networks

and adaptive exponential smoothing methods. Expert Syst. Appl. 2009, 36, 12506–12509. [CrossRef]

18. Bhuriya, D.; Kausha, G.; Sharma, A.; Singh, U. Stock market prediction using a linear regression. In Proceedings of the 2017
International conference of Electronics, Communication and Aerospace Technology (ICECA), Coimbatore, India, 20–22 April
2017; pp. 510–513.

19. Dutta, A.; Bandopadhyay, G.; Sengupta, S. Prediction of stock performance in Indian stock market using logistic regression. Int. J.

Bus. Inf. 2012, 7, 105–136.

20. Kim, S.; Lee, H.S.; Ko, H.; Jeong, S.H.; Byun, H.W.; Oh, K.J. Pattern matching trading system based on the dynamic time warping

algorithm. Sustainability 2018, 10, 4641. [CrossRef]

21. Chen, Y.; Hao, Y. A feature weighted support vector machine and K-nearest neighbor algorithm for stock market indices

prediction. Expert Syst. Appl. 2017, 80, 340–355. [CrossRef]

22. Bollen, J.; Mao, H.; Zeng, X. Twitter mood predicts the stock market. J. Comput. Sci. 2011, 2, 1–8. [CrossRef]
23. Ding, X.; Zhang, Y.; Liu, T.; Duan, J. Deep learning for event-driven stock prediction. In Proceedings of the 24th International

Conference on Artificial Intelligence (IJCAI), Buenos Aires, Argentina, 25–31 July 2015; pp. 2327–2333.

24. Zhang, D.; Dai, X.; Wang, Q.; Lau, C.K.M. Impacts of weather conditions on the US commodity markets systemic interdependence

across multi-timescales. Energy Econ. 2023, 123, 106732. [CrossRef]

25. Hu, H.; Tang, L.; Zhang, S.; Wang, H. Predicting the direction of stock markets using optimized neural networks with Google

Trends. Neurocomputing 2018, 285, 188–195. [CrossRef]

26. Chen, T.L.; Chen, F.Y. An intelligent pattern recognition model for supporting investment decisions in stock market. Inf. Sci. 2016,

346, 261–274. [CrossRef]

27. Bao, W.; Yue, J.; Rao, Y. A deep learning framework for financial time series using stacked autoencoders and long-short term

memory. PLoS ONE 2017, 12, e0180944. [CrossRef]

28. Mittal, A.; Goel, A. Stock Prediction Using Twitter Sentiment Analysis; CS229; Stanford University: Stanford, CA, USA, 2012;

Volume 15.

29. Ma, L.; Wang, X.; Wang, X.; Wang, L.; Shi, Y.; Huang, M. TCDA: Truthful Combinatorial Double Auctions for Mobile Edge

30.

Computing in Industrial Internet of Things. IEEE Trans. Mob. Comput. 2022, 21, 4125–4138. [CrossRef]
Fu, T.C.; Chung, F.L.; Luk, R.; Ng, C.M. Preventing meaningless stock time series pattern discovery by changing perceptually
important point detection. In Fuzzy Systems and Knowledge Discovery: Second International Conference, FSKD 2005, Changsha, China,
27–29 August 2005, Proceedings, Part I 2; Springer: Berlin/Heidelberg, Germany, 2005; pp. 1171–1174.

31. Markowska-Kaczmar, U.; Dziedzic, M. Discovery of technical analysis patterns. In Proceedings of the 2008 International

Multiconference on Computer Science and Information Technology, Wisla, Poland, 20–22 October 2008; pp. 137–142.

32. Leigh, W.; Frohlich, C.J.; Hornik, S.; Purvis, R.L.; Roberts, T.L. Trading with a stock chart heuristic. IEEE Trans. Syst. Man Cybern.

Part Syst. Humans 2008, 38, 93–104. [CrossRef]

33. Cervelló-Royo, R.; Guijarro, F.; Michniuk, K. Stock market trading rule based on pattern recognition and technical analysis:

Forecasting the DJIA index with intraday data. Expert Syst. Appl. 2015, 42, 5963–5975. [CrossRef]

34. Arévalo, R.; García, J.; Guijarro, F.; Peris, A. A dynamic trading rule based on filtered flag pattern recognition for stock market

price forecasting. Expert Syst. Appl. 2017, 81, 177–192. [CrossRef]

35. Huang, W.; Nakamori, Y.; Wang, S.Y. Forecasting stock market movement direction with support vector machine. Comput. Oper.

36.

Res. 2005, 32, 2513–2522. [CrossRef]
Shen, S.; Jiang, H.; Zhang, T. Stock Market Forecasting Using Machine Learning Algorithms. Master’s Thesis, Department of
Electrical Engineering, Stanford University, Stanford, CA, USA, 2012.

37. Lohrmann, C.; Luukka, P. Classification of intraday S&P500 returns with a random forest. Int. J. Forecast. 2019, 35, 390–407.
38. Dey, S.; Kumar, Y.; Saha, S.; Basak, S. Forecasting to classification: Predicting the direction of stock market price using Xtreme

Gradient Boosting. Working Paper, 2016.

39. Ampomah, E.K.; Qin, Z.; Nyame, G. Evaluation of tree-based ensemble machine learning models in predicting stock price

direction of movement. Information 2020, 11, 332. [CrossRef]

40. Ballings, M.; Van den Poel, D.; Hespeels, N.; Gryp, R. Evaluating multiple classifiers for stock price direction prediction. Expert

Syst. Appl. 2015, 42, 7046–7056. [CrossRef]

41. Basak, S.; Kar, S.; Saha, S.; Khaidem, L.; Dey, S.R. Predicting the direction of stock market prices using tree-based classifiers. North

Am. J. Econ. Financ. 2018, 47, 552–567. [CrossRef]

Electronics 2025, 14, 1721

46 of 48

42. Khan, A.H.; Shah, A.; Ali, A.; Shahid, R.; Zahid, Z.U.; Sharif, M.U.; Jan, T.; Zafar, M.H. A performance comparison of machine

learning models for stock market prediction with novel investment strategy. PLOS ONE 2023, 18, e0286362. [CrossRef]

43. Pagliaro, A. Forecasting Significant Stock Market Price Changes Using Machine Learning: Extra Trees Classifier Leads. Electronics

2023, 12, 4551. [CrossRef]

44. Qiu, M.; Song, Y. Predicting the direction of stock market index movement using an optimized artificial neural network model.

PLoS ONE 2016, 11, e0155133. [CrossRef] [PubMed]

45. Moghaddam, A.H.; Moghaddam, M.H.; Esfandyari, M. Stock market index prediction using artificial neural network. J. Econ.

Financ. Adm. Sci. 2016, 21, 89–93. [CrossRef]

46. Di Persio, L.; Honchar, O. Recurrent neural networks approach to the financial forecast of Google assets. Int. J. Math. Comput.

47.

Simul. 2017, 11, 7–13.
Sezer, O.B.; Ozbayoglu, A.M. Algorithmic financial trading with deep convolutional neural networks: Time series to image
conversion approach. Appl. Soft Comput. 2018, 70, 525–538. [CrossRef]

48. Wu, H.; Chen, S.; Ding, Y. Comparison of ARIMA and LSTM for stock price prediction. Financ. Eng. Risk Manag. 2023, 6, 01026.
49. Powell, N.; Foo, S.Y.; Weatherspoon, M. Supervised and unsupervised methods for stock trend forecasting. In Proceedings of the

2008 40th Southeastern Symposium on System Theory (SSST), New Orleans, LA, USA, 16-18 March 2008; pp. 203–205.

50. Wu, K.P.; Wu, Y.P.; Lee, H.M. Stock trend prediction by using K-means and AprioriAll algorithm for sequential chart pattern

mining. J. Inf. Sci. Eng. 2014, 30, 669–686.

51. Babu, M.S.; Geethanjali, N.; Satyanarayana, B. Clustering approach to stock market prediction. Int. J. Adv. Netw. Appl. 2012,

3, 1281.

52. Patel, J.; Shah, S.; Thakkar, P.; Kotecha, K. Predicting stock and stock price index movement using trend deterministic data

preparation and machine learning techniques. Expert Syst. Appl. 2015, 42, 259–268. [CrossRef]

53. Chong, E.; Han, C.; Park, F.C. Deep learning networks for stock market analysis and prediction: Methodology, data representations,

54.

and case studies. Expert Syst. Appl. 2017, 83, 187–205. [CrossRef]
Schumaker, R.P.; Chen, H. Textual analysis of stock market prediction using breaking financial news: The AZFin text system.
ACM Trans. Inf. Syst. (Tois) 2009, 27, 12. [CrossRef]

55. Kalyanaraman, V.; Kazi, S.; Tondulkar, R.; Oswal, S. Sentiment analysis on news articles for stocks. In Proceedings of the 2014 8th

Asia Modelling Symposium, Taipei, Taiwan, 23–25 September 2014; pp. 57–62.

56. Lee, H.; Surdeanu, M.; MacCartney, B.; Jurafsky, D. On the importance of text analysis for stock price prediction. In Proceedings
of the 9th International Conference on Language Resources and Evaluation (LREC), Reykjavik, Iceland, 26–31 May 2014;
pp. 1170–1175.

57. Pagolu, V.S.; Reddy, K.N.; Panda, G.; Majhi, B. Sentiment analysis of Twitter data for predicting stock market movements. In
Proceedings of the 2016 International Conference on Signal Processing, Communication, Power and Embedded System (SCOPES),
Paralakhemundi, India, 3–5 October 2016; pp. 1345–1350.

58. Preis, T.; Moat, H.S.; Stanley, H.E. Quantifying trading behavior in financial markets using Google Trends. Sci. Rep. 2013, 3, 1684.

[CrossRef]

59. Ren, R.; Wu, D.D.; Liu, T. Forecasting stock market movement direction using sentiment analysis and support vector machine.

IEEE Syst. J. 2018, 13, 760–770. [CrossRef]

60. Wang, J.J.; Wang, J.Z.; Zhang, Z.G.; Guo, S.P. Stock index forecasting based on a hybrid model. Omega 2012, 40, 758–766. [CrossRef]
61. Rather, A.M.; Agarwal, A.; Sastry, V.N. Recurrent neural network and a hybrid model for prediction of stock returns. Expert Syst.

Appl. 2015, 42, 3234–3241. [CrossRef]

62. Lv, D.; Yuan, S.; Li, M.; Xiang, Y. An empirical study of machine learning algorithms for stock daily trading strategy. Math. Probl.

Eng. 2019. [CrossRef]

63. Yoshihara, A.; Fujikawa, K.; Seki, K.; Uehara, K. Predicting stock market trends by recurrent deep neural networks. In Proceedings

of the Pacific Rim International Conference on Artificial Intelligence, Gold Coast, Australia, 1–5 December 2014; pp. 759–769.

64. Wang, T.; Guo, J.; Shan, Y.; Zhu, Y. A knowledge graph–GCN–community detection integrated model for large-scale stock price

prediction. Appl. Soft Comput. 2023, 145, 110595. [CrossRef]

65. Zhang, F. Conceptual-temporal graph convolutional neural network model for stock price movement prediction and application.

66.

Soft Comput. 2023, 27, 6329–6344.
Jang, J.; Seong, N. Deep reinforcement learning for stock portfolio optimization by connecting with modern portfolio theory.
Expert Syst. Appl. 2023, 218, 119556. [CrossRef]

67. Wu, J.L.; Tang, X.R.; Hsu, C.H. A prediction model of stock market trading actions using generative adversarial network and

piecewise linear representation approaches. Soft Comput. 2023, 27, 8209–8222. [CrossRef]

68. Harvey, C.R. Presidential address: The scientific outlook in financial economics. J. Financ. 2017, 72, 1399–1440. [CrossRef]
69. Lo, A.W.; MacKinlay, A.C. When are contrarian profits due to stock market overreaction? Rev. Financ. Stud. 1990, 3, 175–205.

[CrossRef]

Electronics 2025, 14, 1721

47 of 48

70. Baker, M.; Wurgler, J. Investor sentiment and the cross-section of stock returns. J. Financ. 2006, 61, 1645–1680. [CrossRef]
71. Gu, S.; Kelly, B.; Xiu, D. Empirical asset pricing via machine learning. Rev. Financ. Stud. 2020, 33, 2223–2273. [CrossRef]
72.

Feng, F.; Chen, H.; He, X.; Ding, J.; Sun, M.; Chua, T.S. Enhancing stock movement prediction with adversarial training. In
Proceedings of the 28th International Joint Conference on Artificial Intelligence, Macao, China, 10–16 August 2019; pp. 5843–5849.

73. Diebold, F.X.; Mariano, R.S. Comparing predictive accuracy. J. Bus. Econ. Stat. 1995, 13, 253–263. [CrossRef]
74. Hansen, P.R.; Lunde, A.; Nason, J.M. The model confidence set. Econometrica 2011, 79, 453–497. [CrossRef]
75. White, H. A reality check for data snooping. Econometrica 2000, 68, 1097–1126. [CrossRef]
76. Hansen, P.R. A test for superior predictive ability. J. Bus. Econ. Stat. 2005, 23, 365–380. [CrossRef]
77. Giacomini, R.; White, H. Tests of conditional predictive ability. Econometrica 2006, 74, 1545–1578. [CrossRef]
78. Politis, D.N.; Romano, J.P. Multivariate density estimation with general flat-top kernels of infinite order. J. Multivar. Anal. 1999,

68, 1–25. [CrossRef]

79. Campbell, J.Y.; Thompson, S.B. Predicting excess stock returns out of sample: Can anything beat the historical average? Rev.

Financ. Stud. 2008, 21, 1509–1531. [CrossRef]

80. Benjamini, Y.; Hochberg, Y. Controlling the false discovery rate: A practical and powerful approach to multiple testing. J. R. Stat.

Soc. Ser. (Methodological) 1995, 57, 289–300. [CrossRef]

81. Holm, S. A simple sequentially rejective multiple test procedure. Scand. J. Stat. 1979, 6, 65–70.
82. Romano, J.P.; Shaikh, A.M.; Wolf, M. Control of the false discovery rate under dependence using the bootstrap and subsampling.

Test 2007, 17, 417. [CrossRef]

83. Harvey, C.R.; Liu, Y.; Zhu, H. ... and the cross-section of expected returns. Rev. Financ. Stud. 2016, 29, 5–68.
84. Andrews, D.W. Tests for parameter instability and structural change with unknown change point. Econometrica 1993, 61, 821–856.

[CrossRef]

85. Bai, J.; Perron, P. Estimating and testing linear models with multiple structural changes. Econometrica 1998, 66, 47–78. [CrossRef]
86. Primiceri, G.E. Time varying structural vector autoregressions and monetary policy. Rev. Econ. Stud. 2005, 72, 821–852. [CrossRef]
87. Hamilton, J.D. A new approach to the economic analysis of nonstationary time series and the business cycle. Econometrica 1989,

57, 357–384. [CrossRef]

88. Pesaran, M.H.; Timmermann, A. Selection of estimation window in the presence of breaks. J. Econom. 2007, 137, 134–161.

[CrossRef]

89. Brock, W.; Lakonishok, J.; LeBaron, B. Simple technical trading rules and the stochastic properties of stock returns. J. Financ. 1992,

90.

47, 1731–1764. [CrossRef]
Sullivan, R.; Timmermann, A.; White, H. Data-snooping, technical trading rule performance, and the bootstrap. J. Financ. 1999,
54, 1647–1691. [CrossRef]

91. Lo, A.W.; Mamaysky, H.; Wang, J. Foundations of technical analysis: Computational algorithms, statistical inference, and

empirical implementation. J. Financ. 2000, 55, 1705–1765. [CrossRef]

92. Rapach, D.E.; Strauss, J.K.; Zhou, G. Out-of-sample equity premium prediction: Combination forecasts and links to the real

economy. Rev. Financ. Stud. 2010, 23, 821–862. [CrossRef]

93. Bradshaw, M.T.; Drake, M.S.; Myers, J.N.; Myers, L.A. A re-examination of analysts’ superiority over time-series forecasts of

annual earnings. Rev. Account. Stud. 2012, 17, 944–968. [CrossRef]

94. Christoffersen, P.; Jacobs, K.; Chang, B.Y. Forecasting with option-implied information. Handb. Econ. Forecast. 2013, 2, 581–656.
95. Cheng, I.H.; Xiong, W. The financialization of commodity markets. Annu. Rev. Financ. Econ. 2013, 5, 419–441.
96. English, W.B.; Van den Heuvel, S.J.; Zakrajšek, E. Interest rate risk and bank equity valuations. J. Monet. Econ. 2018, 98, 80–97.

[CrossRef]

97. Pastor, L.; Veronesi, P. Technological revolutions and stock prices. Am. Econ. Rev. 2009, 99, 1451–1483. [CrossRef]
98. Lo, A.W. The adaptive markets hypothesis: Market efficiency from an evolutionary perspective. J. Portf. Manag. 2004, 30, 15–29.

99.

[CrossRef]
Jegadeesh, N.; Titman, S. Returns to buying winners and selling losers: Implications for stock market efficiency. J. Financ. 1993, 48,
65–91. [CrossRef]

100. Bhattacharya, D.; Li, W.H.; Sonaer, G. Has momentum lost its momentum? Rev. Quant. Financ. Account. 2020, 55, 1145–1179.

[CrossRef]

101. Bernard, V.L.; Thomas, J.K. Post-earnings-announcement drift: Delayed price response or risk premium? J. Account. Res. 1989, 27,

1–36. [CrossRef]

102. Ke, B.; Ramalingegowda, S. Do institutional investors exploit the post-earnings announcement drift? J. Account. Econ. 2005, 39,

25–53. [CrossRef]

103. Zhang, C.Y.; Jacobsen, B. The Halloween indicator, “Sell in May and go away”: Everywhere and all the time. J. Int. Money Financ.

2021, 110, 102268. [CrossRef]

104. Hou, K.; Xue, C.; Zhang, L. Replicating anomalies. Rev. Financ. Stud. 2020, 33, 2019–2133. [CrossRef]

Electronics 2025, 14, 1721

48 of 48

105. Chen, A.Y.; Zimmermann, T. Publication bias and the cross-section of stock returns. Rev. Asset Pricing Stud. 2022, 12, 454–488.
106. Lakonishok, J.; Smidt, S. Are seasonal anomalies real? A ninety-year perspective. Rev. Financ. Stud. 1988, 1, 403–425. [CrossRef]
107. Schwert, G.W. Anomalies and market efficiency. Handb. Econ. Financ. 2003, 1, 939–974.
108. White, H. Economic prediction using neural networks: The case of IBM daily stock returns. In Proceedings of the IEEE 1988

International Conference on Neural Networks, San Diego, CA, USA, 24-27 July 1988; pp. 451–458.

109. Bishop, C.M. Neural Networks for Pattern Recognition; Oxford University Press: Oxford, UK, 1995.
110. Tetlock, P.C. Giving content to investor sentiment: The role of media in the stock market. J. Financ. 2007, 62, 1139–1168. [CrossRef]
111. Loughran, T.; McDonald, B. When is a liability not a liability? Textual analysis, dictionaries, and 10-Ks. J. Financ. 2011, 66, 35–65.

[CrossRef]

112. López de Prado, M. Advances in Financial Machine Learning; John Wiley & Sons: Hoboken, NJ, USA, 2018.
113. Bailey, D.H.; Borwein, J.M.; López de Prado, M.; Zhu, Q.J. Pseudo-mathematics and financial charlatanism: The effects of backtest

overfitting on out-of-sample performance. Not. Am. Math. Soc. 2014, 61, 458–471. [CrossRef]

114. Boehmer, E.; Jones, C.M.; Zhang, X. Potential pilot problems: Treatment spillovers in financial regulatory experiments. J. Financ.

Econ. 2019, 134, 355–373.

115. Zhang, Z.; Zohren, S.; Roberts, S. DeepLOB: Deep convolutional neural networks for limit order books. IEEE Trans. Signal Process.

2019, 67, 3001–3012. [CrossRef]

116. Urquhart, A. The inefficiency of Bitcoin. Econ. Lett. 2016, 148, 80–82. [CrossRef]
117. Cao, J.; Chen, J.; Hull, J.C. A neural network approach to understanding implied volatility movements. Quant. Financ. 2020, 20,

781–797. [CrossRef]

118. Huck, N. Large data sets and machine learning: Applications to statistical arbitrage. Eur. J. Oper. Res. 2019, 278, 330–342.

[CrossRef]

119. Frazzini, A.; Israel, R.; Moskowitz, T.J. Trading costs. J. Financ. Econ. 2018, 138, 293–316. [CrossRef]
120. Bartram, S.M.; Branke, J.; Motahari, M. Artificial Intelligence in Asset Management; CFA Institute Research Foundation: Char-

lottesville, VA, 2021.

121. Daul, S.; Jaisson, T.; Nagy, A. Performance attribution of machine learning methods for stock returns prediction. J. Financ. Data

Sci. 2022, 8, 86–104. [CrossRef]

Disclaimer/Publisher’s Note: The statements, opinions and data contained in all publications are solely those of the individual
author(s) and contributor(s) and not of MDPI and/or the editor(s). MDPI and/or the editor(s) disclaim responsibility for any injury to
people or property resulting from any ideas, methods, instructions or products referred to in the content.

