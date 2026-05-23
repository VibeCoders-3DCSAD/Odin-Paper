Exploratory Analysis of Audio Features for Dominant Feature
Identification: A Multimodal Machine Learning Evaluation of
Song Popularity Prediction Using Deep Neural Networks,
Clustering, and Regression Models

Joel de Goma
School of Information Technology
Mapua University
Makati, Metro Manila, Philippines
jcdegoma@mapua.edu.ph

Sean Fredrick Cruz
School of Information Technology
Mapua University
Makati, Metro Manila, Philippines
sfscruz@mymail.mapua.edu.ph

Mackleine Espino
School of Information Technology
Mapua University
Makati, Metro Manila, Philippines
mfespino@mymail.mapua.edu.ph

Jaime Rodolfo Tuason
School of Information Technology
Mapua University
Makati, Metro Manila, Philippines
jrctuason@mymail.mapua.edu.ph

Alberto Villaluz
School of Information Technology
Mapua University
Makati, Metro Manila, Philippines
acvillaluz@mapua.edu.ph

Abstract
With the vast collections of artist catalogues, music streaming ser-
vices have become more popular and accessible, and technology
has helped to shift the focus away from physical purchases. How-
ever, picking which songs will go viral is still a tough job since
audiences change all the time. The study analyzes song popularity
prediction within the context of Original Pilipino Music (OPM)
through various machine learning models, specifically focusing on
dominant audio features that influence listener engagement. Key
findings reveal that attributes such as tempo, energy, loudness, and
danceability strongly correlate with popularity, with high-energy
and rhythmically dynamic features often associated with popular
tracks. The research involved clustering techniques, feature ex-
traction, and dimensionality reduction (such as UMAP and LLE) to
identify patterns, demonstrating that mainstream and niche song
clusters could be distinguished by their distinct audio profiles. The
Deep Neural Network (DNN) model, enhanced with an attention
mechanism, showed improved prediction capabilities for song pop-
ularity, leveraging these dominant features effectively. In terms of
model performance, the DNN achieved high accuracy, underscoring
the potential of machine learning in capturing the audio elements
that appeal broadly across OPM listeners.

CCS Concepts
• Information systems; • Information retrieval; • Evaluation
of retrieval results; • Presentation of retrieval results;

This work is licensed under a Creative Commons Attribution 4.0 International License.
WSSE 2025, Okayama, Japan
© 2025 Copyright held by the owner/author(s).
ACM ISBN 979-8-4007-1577-8/2025/10
https://doi.org/10.1145/3779657.3779690

Keywords
Audio Features, Deep Neural Networks, Attention Mechanism, Clus-
tering, Feature Extraction, Machine Learning

ACM Reference Format:
Joel de Goma, Sean Fredrick Cruz, Mackleine Espino, Jaime Rodolfo Tuason,
and Alberto Villaluz. 2025. Exploratory Analysis of Audio Features for
Dominant Feature Identification: A Multimodal Machine Learning Evalua-
tion of Song Popularity Prediction Using Deep Neural Networks, Clustering,
and Regression Models. In 2025 The 7th World Symposium on Software En-
gineering (WSSE 2025), October 24–26, 2025, Okayama, Japan. ACM, New
York, NY, USA, 7 pages. https://doi.org/10.1145/3779657.3779690

1 Introduction
The global music industry has undergone a seismic shift driven by
streaming platforms which now hold most of music revenue. With
their immense libraries of artist catalogues, technology has worked
to move the burden away from physical purchases. However, pick-
ing which songs will go viral is still a tough job since audiences are
not static. Each year, technology brings the music industry closer
to AI Integration. This phenomenon has now touched every aspect
of music from when it is created to when it is distributed. This has
great significance for audio features (that provide appeals to listen-
ers), especially unique feature(s) in regional markets, profit from
AI, powerful commercials [1], etc.; thus, a critical understanding of
such switching landscapes is imperative. Musical taste is similar in
that it is conditioned often by the environment, the context, and
what an individual has gone through in life. Music prediction algo-
rithms and their validity are difficult to assess, as the matter of good
or bad preferences is very subjective [2]. The chorus, specifically, is
one structural feature of popular music that is particularly impor-
tant, since previous work finds it to be the ”most catchy” and ”most
salient” section of a song. While there are those that go beyond
merely assessing the audio of pop songs, this study limits its scope
to the choruses of the songs and attempts to ascertain how these
elements contribute to listener appeal.

224WSSE 2025, October 24–26, 2025, Okayama, Japan

Joel de Goma et al.

Previous works on predicting the popularity of songs focus on
general classification models that classify songs as popular or not
popular over global datasets [3]. Yet, no study conducted with a
purposeful investigation of relevant audio features and their con-
tribution towards popularity in specific regional contexts, like the
Philippine market. There is also an opportunity to use a DNN as a
feature impact analysis prototype instead of using it as an overall
popularity predictor. With this approach, we can utilize the DNN
model in a new way—through an attention mechanism to indicate
the influence of features—to explain the feature interactions, as
well as the relative importance of features contributing to song
popularity.

Our approach bridges the gap between technical innovation and
commercial application. For an industry increasingly driven by
AI, this framework offers a scalable solution to mitigate financial
risks and a competitive advantage in the Philippines’ ever-evolving
music ecosystem.

2 Review of Related Literature
2.1 Audio Feature-Based Classification
In a study [4], an automatic OPM song genre classification system
is reported with the goal of improving hit songs for specific au-
dience targeting. Targeting ballad, alternative rock, and rock as
three genres, the researchers collected 380 OPM MIDI files and ex-
tracted 56 musical features. The classifiers are Linear Discriminant
Analysis, Classification and Regression Trees (CART), and Neural
Networks. It looks at each method in some detail (e.g., the discrim-
inant functions used by LDA; the tree and impurity reduction in
CART; backpropagation through gradient descent, etc.). With a
train/test split of 80/20, the study was able to reach an accuracy
of close to 100% classification with LDA showing the best results.
They also included confusion matrices along with success rates
for each classifier, demonstrating further potential of LDA and NN
for accurate cross-genre classification, particularly with respect to
melodic intervals. This indicates the potential application of both
application of genre-based playlist creation and audience targeting
in the music industry.

2.2 Use of Machine Learning in Predicting

Popularity

For song hit prediction, in [6] audio features and sentimental lyrics
were analyzed by applying machine learning models in R Studio.
Billboard Hot 100 Charts Spotify Open Lyrics Datasets This con-
sisted of extracting and pre-processing the data, followed by feature
selection, to create a prediction model. Confusion matrices were
used to evaluate 5 different machine learning algorithms on C4,
Naïve Bayes, and Logistic Regression output accuracies Addition-
ally, the weights of the parameters from Logistic Regression were
additionally analyzed to determine its effect on the model perfor-
mance. One of the best features for predicting hits was danceability.
In a wider discussion of its results compared to previous studies
(some of which had the exact same results as the new study), the
study also cautioned that although the results would be helpful in a
sound and lyrical feature-based ’hit-song formula’, to ever come up
with a final solution is not straightforward. One of the findings of

the study is consistent with its researcher’s intent to examine dom-
inant features is the important role of danceability for the models
to predict popularity. There are more extensive prediction models,
of course, but individual song features will have an iconic effect on
hit songs.

The work in [7] also approached song popularity prediction
within streaming services with a focus on the Top 50 Global Chart
of Spotify and framed it as a classification problem by predicting
whether a song will enter the chart or not, given the time frame
of a certain interval. The authors categorized predictive methods
into three generic types, social network data, acoustic data, and
historical chart data. We gathered daily acoustic features (energy,
tempo, key, etc.) for every song that made the Top 50 at least once
between November 2018 and April 2019 through Spotify’s Web API.
Multiple rounds of predictions were made using ensemble methods
(AdaBoost and Random Forest), probabilistic methods (Bernoulli
and Gaussian Naïve Bayes), and various SVM kernels. Accuracy
score of 89.09% when predicting a song’s position in days ahead
of time [5]. This shows why the research is relevant for artists,
labels & the music business, how the methodology can be applied
to different data types, and how it might improve in the future.

2.3 Deep Learning Techniques for Audio

Categorization

The paper in [8] studies how AI and machine learning can be used to
determine song popularity based on features such as genre, chords,
and lyrics sentiment analysis. This work is a deviation from the con-
ventional approaches of evaluating the popularity of music based on
daily media platforms towards audio features and lyrics sentiments.
Based on artist familiarity data using two datasets (one dataset
consisted of Spotify song metadata and lyrics, whilst the other con-
sisted of artist familiarity values), the study conducted sentiment
and 14 profanity analyses to improve the efficiency of the dataset.
We compared six algorithms and conducted hyperparameter tun-
ing for optimum accuracy. The Spotify API was used to extract
metadata while the Lyrics Genius API was used for web scraping,
allowing real-time predictions to be done. Cross-validation with
k-fold and visualizations were used to explore the effects of the
input variables on track popularity. Using the Random Forest Clas-
sifier, which returns an accuracy of 85.06%, the study has identified
tempo, loudness, acoustics, and liveliness as top features affecting
song popularity. The use of sentiment analysis instead of profanity
was also highlighted, and genre, key, and mode were of less impor-
tance in this model. They noted limitations and areas for further
research, such as songs in languages other than English and more
artist features to enhance predictability. The dataset was filtered
down to only contain songs from the genres that we focus on which
included 200,000 records and 52 genre labels. The models that were
utilized in the study include Decision Trees, Naive Bayes classifiers,
linear SVMs, and Deep Neural Networks (DNNs), RNNs results
showed that the Naive Bayes classifier was the fastest classifier to
train, with only 2.18 seconds for the balanced set. The performance
from the neural network and RNN are comparably close together,
but again, the RNN did not help boost the accuracy of the original
NN. Neural networks showed the best overall performance while

225Exploratory Analysis of Audio Features for Dominant Feature Identification: A Multimodal Machine Learning
Evaluation of Song Popularity Prediction Using Deep Neural Networks, Clustering, and Regression Models

WSSE 2025, October 24–26, 2025, Okayama, Japan

decision trees performed the worst, Meanwhile, SVM and Naive
Bayes classifiers gained higher Average Precision values.

3 Methodology
This section will discuss the methodology used and created to iso-
late and determine the audio features with the most influence over
a song gaining popularity in the Philippines. The methodology con-
sists of four major components: Data Collection and Preprocessing,
Feature Extraction, Multi-Model Analysis, and Model Deployment
and Evaluation. Each of these components offers a systematic
methodology to dissect the key components that make music ap-
pealing to listeners. Every phase has been designed to ultimately
serve the study’s objective, which is to investigate the trends of the
feature importance in popular music trends, rather than building an
all-encompassing predictive model. This approach offers a cultur-
ally relevant and data-driven framework for understanding regional
music trends by isolating and analyzing dominant characteristics
in songs that have already been shown to be popular.

3.1 Dataset Collection
The data collection process begins by acquiring a meticulously cu-
rated dataset from a professional data scientist, which comprises
data about Spotify’s top trending songs from 2017 to 2023. This
dataset focuses on the top 200 songs each year over a span of five
years (2018-2023). The present dataset for 2024 was derived from
Spotify’s weekly top 200 charts, serving to supplement the histori-
cal dataset, as it reflects the latest in song popularity. The dataset
has also explicitly the top 200 songs from the week of ‘2024-10-28’
so the analysis can reflect the recent changes in listeners’ inter-
ests. This five-year period is significant, as previously mentioned
[9], it is a crucial time in the development of the history of music
streaming and consumption in the Philippines. The time frame
was chosen to observe trends in Music 29 popularity during the
pre-pandemic, pandemic, and post-pandemic eras. This also comes
at a time when there has been a lot of progress in the local OPM
scene, and streaming platforms in the country itself maturing as
well. Preprocessing — one of the most crucial stages that includes
several data operations like cleaning, normalization, and data trans-
formation to ensure consistency and reliability. Data cleaning also
eliminates inconsistencies, duplicity, and missing values giving you
a more precise dataset. Normalization techniques are also done so it
can therefore be possible to standardize all the values and compare
data points to one another. This step helps prepare the dataset
for further analysis and eliminates all the noise or irrelevant data
to help facilitate an easier representation of the trends in popular
music.

3.2 Data Preprocessing
Data preprocessing involved cleaning, normalizing, and structuring
the dataset for analysis, with additional integration of Spotify and
YouTube API data to obtain audio features and select social metrics.
In this phase, raw MP3 files were processed to focus specifically on
the chorus segments by calculating a time similarity matrix, ensur-
ing that analysis centers on the most memorable song components.

3.2.1 API Integration Layer. The API Integration Layer represents
a crucial step, as it will allow for more features to come, including

audio and social engagement data. This layer is built on top of
Spotify and YouTube APIs to fetch some useful high dimensional
data for every song. Audio features: The audio features extracted
from the Spotify API are listed below; The tempo, energy, danceabil-
ity, and other characteristics about the song’s sound profile. Also,
similar to Twitter but with more granular social media engagement
metrics per track, the YouTube API provides access to the YouTube
view counts, determining the number of times a tune has been
viewed, which also means how popular and how far a certain tune
has gotten through listeners [10].

3.2.2 Audio Processing. Once the data has been obtained, audio
processing steps become the main attention. In this step, we down-
load a raw audio file for each of the songs in the 1,000 gathered in
the dataset, i.e., download mp3 files. These files are the building
blocks for more in-depth feature analyses and chorus extraction
stages. The audio processing phase converts each file so that they
can be analyzed consistently in terms of format, sample rate, and
file corruption. This may also include normalization of levels as
well as deletion of metadata which can interfere with extraction of
features. Quality audio data provision is crucial for this analysis
at ensuring contained tracks are representative of 31 their distinc-
tive characteristics which is vital for reliable feature extraction and
modeling in later stages.

3.2.3 Chorus Extraction. The chorus detection algorithm in this
study aims to isolate the most repeated section of each song, typ-
ically the chorus, which is often the most emotionally resonant
and memorable part. The process begins by transforming the audio
into a chromagram, which represents pitch over time and simplifies
pattern recognition. This chromatic representation is then used
to construct a time-time similarity matrix, identifying segments
of the song that are similar to each other. To enhance detection
precision, the algorithm also employs a time-lag similarity matrix,
optimizing the recognition of repeated patterns. After constructing
these matrices, thresholding and denoising are applied to eliminate
minor repetitions and highlight significant, repetitive sequences. Fi-
nally, the algorithm identifies and counts these repeated segments,
selecting the most frequent and strongest similarity scores as the
best candidate for the chorus, thereby ensuring a focused analysis
on the song’s most impactful portion.

3.3 Feature Extraction
As shown in Table 1, the researchers extracted 16 main audio fea-
tures after processing the audio, which we used for the next analysis.
Features such as danceability, energy, loudness, etc., each contribute
uniquely to understanding the appeal of a song. The feature ex-
traction focuses on sounds that correlate with the trend in pop
music. The Librosa library was employed to load each song, which
subsequently calculates key audio features listed in the table below.
With every feature extracted, they are stored in the Data Frame
with each row for each song.

The preprocessing steps ensure the data’s suitability for machine
learning analysis. Interquartile Range (IQR) filtering eliminates
outliers by removing values beyond 1.5 times the IQR from the first
and third quartiles, ensuring a more homogeneous dataset. Min-
Max Scaling standardizes features to a range of 0 to 1, maintaining

226WSSE 2025, October 24–26, 2025, Okayama, Japan

Joel de Goma et al.

Audio Feature

Key
melody_pitch_profile
tempo
beat_strength
chord_progressions
timbre
loudness
energy
spectral_centroid
spectral_bandwidth
zero_crossing_rate
danceability
instrumentalness
valence
acousticness
liveness
Audio Feature

Table 1: Key Audio Features Extracted

Value

Indicates the song’s harmonic scale, affecting its mood and structure
Captures the contour and emotional quality of the melody
Measures the song’s speed in beats per minute, impacting energy
Reflects the intensity of the beat, influencing rhythm
Represents the sequence of chords, shaping harmony
The unique tone quality, distinguishing different sounds
Measures the overall volume, indicating intensity
Shows the intensity and activity level, with higher values for livelier tracks
Indicates sound brightness, with higher values for sharper tones
Measures frequency range, with wider bandwidth for richer sound
Reflects signal noisiness, with higher rates for percussive sounds
Shows how suitable a track is for dancing
Shows whether a track contains no vocals
Measures the musical positiveness of a track
Measures whether a track is acoustic or not
Shows whether the track was performed live or not
Value

consistency across attributes for comparability. Categorization or-
ganizes YouTube view counts into four classes based on thresholds,
facilitating structured analysis of popularity levels. Oversampling,
utilizing the SMOTE algorithm, balances the dataset by increasing
underrepresented categories, ensuring robust training and reliable
model outcomes.

3.4 Model Analysis
This phase centers on feature importance, clustering, and dimen-
sionality reduction techniques to pinpoint dominant attributes for
song popularity. Correlation analysis identifies relationships among
features, while mutual information reveals both linear and non-
linear dependencies. Dimensionality reduction via Locally Linear
Embedding (LLE) and Uniform Manifold Approximation and Pro-
jection (UMAP) further clarifies feature clusters by preserving local
and global structures. Clustering models, including Agglomerative
Clustering and K-means, highlight feature distributions, showing
patterns in rhythmic and harmonic characteristics across songs. Fac-
tor Analysis refines the dataset by emphasizing core features that
impact popularity, offering insights into latent structures within the
data. Factor Analysis condenses the dataset into a limited number
of factors and shows the features which contribute most to each
factor. However, in Factor Analysis, it focuses on the key features
affecting the songs which are most influential in a large dataset. It
assists to uncover these X factors that drive the core characteristics
behind making a song appealing, thus aligning with the purpose of
framework in identifying universals X factor of appeal.

Correlation analysis and mutual information quantified rela-
tionships among audio and social features, identifying informative
inputs for dimensionality reduction and clustering. LLE preserved
local data structures, projecting high-dimensional features into
clusters based on similarities, showing that 90% of features are

genre-agnostic. Agglomerative clustering, using LLE findings, hier-
archically grouped features into a dendrogram, illustrating associa-
tions. UMAP revealed hidden structures, clustering similar genres
based on shared attributes, even across diverse sources.

UMAP integrates local and global cluster structures, revealing
relationships between features. K-means clustering, known for its
scalability and versatility, partitions data into distinct clusters based
on proximity to cluster centers. Principal Component Analysis
(PCA) on raw feature weights highlights their distribution, helping
to understand the variability in audio characteristics across songs.

3.5 Model Development
Six models were chosen based on their complementary strengths
in feature selection, interpretability, and prediction. The varying
degrees of complexity inherent in these regression models facilitate
an examination of linear as well as non-linear feature interactions,
which leads to a better insight on the potential drivers and inhibition
factors of a song‘s success. The models used are Random Forest,
XGBoost, Decision Tree, Support Vector Machine (SVM), Logistic
Regression, and the DNN using Attention Mechanism.

3.6 Training and Testing
Training and testing procedures utilized the Adam optimizer with
a learning rate of 0.001 and categorical cross entropy as the loss
function. The model was trained over 100 epochs with a batch
size of 32, employing early stopping based on validation loss to
prevent overfitting. The training process leveraged both dropout
and batch normalization techniques to enhance generalization ca-
pability across the diverse audio feature space.

For the Data Splitting Strategy, the dataset was divided with
an 80/20 ratio and a fixed random state of 42 for reproducibility.
This random sampling approach ensures consistent results across
multiple runs while maintaining representative distribution of all
popularity classes in both training and test sets.

227Exploratory Analysis of Audio Features for Dominant Feature Identification: A Multimodal Machine Learning
Evaluation of Song Popularity Prediction Using Deep Neural Networks, Clustering, and Regression Models

WSSE 2025, October 24–26, 2025, Okayama, Japan

Figure 1: Feature Extraction Result

Evaluation metrics included accuracy, precision, recall, and F1-
score for classification performance, alongside mean-squared error
(MSE) and R-squared for assessing the model’s predictive perfor-
mance and consistency. These comprehensive metrics provide mul-
tiple perspectives on model effectiveness, with accuracy indicating
overall correctness and precision-recall metrics balancing false pos-
itives and negatives across the four popularity classes.

3.7 Evaluation
The model was evaluated based on accuracy, precision, recall, and
F1 score to determine its performance. Each metric provides a dif-
ferent perspective on model performance, with accuracy indicating
overall correctness, precision, and recall balancing false positives
and negatives, and the F1 score providing a harmonic mean of the
latter two. The model’s evaluation phase identifies which approach
yields the highest predictive power for song popularity.

4 Results and Discussion
This section presents the results from feature extraction and multi-
model analysis, along with interpretations of how each model con-
tributed to identifying dominant audio features that correlate with
song popularity.

4.1 Feature Extraction Results
As shown in Figure 1, feature extraction process identified key audio
attributes, including tempo, energy, loudness, and danceability, as
primary indicators associated with song popularity. Through the
application of the Interquartile Range (IQR) method, outliers were
removed to create a more normalized dataset. Min-max scaling was
then applied to ensure consistency in the feature range, followed
by a comprehensive clustering and dimensionality reduction to
highlight relationships among key audio features. The identified
features were then analyzed for their predictive value, with energy
and loudness emerging as particularly influential in determining
song popularity within the sample.

Factor Analysis (FA) in this study aggregates related audio fea-
tures into composite factors that represent broader musical traits,
enhancing the interpretability of feature contributions to song pop-
ularity. Key factors emerged: FA1 (Spectral Characteristics), which
captures features like energy and spectral centroid, representing

sound sharpness; FA2 (Tonal and Rhythmic Qualities), embody-
ing key, beat strength, and chord progressions that shape a song’s
harmonic and rhythmic appeal; and FA3 and FA4 (Rhythm and
Melody), which emphasize pacing and melody, crucial for creat-
ing memorable tracks. Factors FA5 and FA6, contributing minimal
insight, were excluded to refine the model’s focus on impactful
traits. This structuring helps clarify how energetic, rhythmically
steady, and melodically catchy elements enhance a song’s appeal,
particularly in popular genres.

The correlation matrix reveals strong positive relationships,
such as between Spectral Bandwidth and Spectral Centroid (both
frequency-related) and between Loudness and Energy (indicating
that louder songs often feel more intense). Notable negative cor-
relations include Loudness and Instrumentalness, suggesting that
instrumental tracks are typically quieter. Mutual Information (MI)
analysis complements this by identifying which features most in-
form the target variable (popularity as measured by YouTube views).
Top features by MI include Spectral Centroid, Speechiness, and
Loudness, implying that tonal brightness, vocal presence, and en-
ergy are key to listener appeal. Danceability, Energy, and Liveness
provide moderate predictive value, while features like Instrumen-
talness and Acousticness contribute minimally.

At the top of the MI rankings are Spectral Centroid, Speechiness,
and Loudness, suggesting that these attributes are closely tied to
listener engagement; for instance, Spectral Centroid reflects tonal
”brightness,” indicating that sharper tonal qualities may enhance
appeal. Mid-range features like Danceability, Energy, and Liveness
also contribute to predictive power, suggesting that rhythmic qual-
ities, tempo, and a ”live” feel positively affect listener preference.
Lower-ranked features, including Chord Progressions, Melody Pitch
Profile, and Zero Crossing Rate, provide structural or harmonic
information but show less impact on listener engagement com-
pared to tonal and rhythmic elements. The lowest MI scores belong
to Instrumentalness, Acousticness, and Key, indicating that these
features are relatively weak predictors of popularity.

Most of the data points are highly concentrated in clusters, but
more so on the right side of the LLE plot. Since this shows that all
these information points belong together, patterns being typical
across popular clusters probably represent the basic features of
songs irrespective of their genre, which is quite aligned with the
objectives of finding commonalities that make songs successful.

228WSSE 2025, October 24–26, 2025, Okayama, Japan

Joel de Goma et al.

The clusters that are closer to the center show some overlapping,
suggesting that these sets of songs share a core audio feature and
may therefore be appealing across the different groups of listeners.
Most probably, the central clusters are representative of common
traits of popular music, where the songs tend to have broadly re-
latable features. On the other hand, clusters lying far from the
center could depict more unique characteristics, perhaps unique
or niche qualities of the audio features. For example, the songs
in Cluster 0 could be different from those in Cluster 6 regarding
rhythmic structures or tonal qualities that would distinguish them
in the dataset. The points that form less dense areas around the
edges, particularly those spread out towards the bottom of the plot,
indicate songs with more unique feature combinations. These songs
may include uncommon tonal or rhythmic qualities, or distinctive
audio profiles, setting them apart from the majority. This gradi-
ent from dense central clusters to more dispersed points shows
that UMAP has successfully highlighted both mainstream patterns
and unique deviations within the audio features. The K-Means
clustering results, visualized on two principal components, reveal
six distinct clusters representing groups of songs with similar au-
dio characteristics. Three clusters (Clusters 2, 4, and 6) form a
densely packed central concentration, suggesting that many songs
share common audio features, such as balanced tempo, energy, and
rhythm, likely resonating with broad listener preferences. These
central clusters contain overlapping characteristics, indicating a
wide acceptance of these core features. On the periphery, clusters
like Cluster 0 and Cluster 8 are more spread out, suggesting these
songs have unique or specialized audio traits that may appeal to
specific audiences. Cluster variation provides further insights, with
tighter clusters (e.g., Cluster 6) indicating homogeneity in audio
characteristics, while broader clusters like Cluster 4 display more
diversity, potentially reflecting sub-genre differences within the
group.

4.2 Prototype result
The random forest classifier was able to get 93.98% accuracy in the
test dataset and around 83.1% in the validation dataset. This model
was able to perform quite well given the PCA features. As you can
see in the confusion matrix, most of the prediction revolves around
the classes of ‘0’ or the “low view count” class. This is due to the
skewness of the distribution of the current trending songs in the
Philippines. However, as we can further see, the Random Forest
failed to predict classes 3 and 2 for its entirety and was only able to
predict 3 out of 5 in the class of ‘1’.

The logistic regression was only able to get around 61.25% accu-
racy in the test score, whilst having around 27.70% in the valida-
tion dataset. This result is quite low given that the random forest
classifier was able to get at least 83.1% of the validation dataset.
Furthermore, this logistic regression was able to detect only class 3
data but failed to detect class 2. This class, due to its rareness, gives
the research more impact in discerning whether the model works,
as desired, irrespective of its accuracy. For the decision tree, it was
able to get around 82.46% of accuracy in the test score, while having
59.48% in the validation dataset. While this is quite an acceptable
accuracy, only having around 22.98% difference, the highest accu-
racy of the random forest classifier is still persistent. For the SVM,

it was able to get at most 67.02% in the test dataset having only
32.82% in the validation dataset. This is a very poor performance for
the SVM as also seen in the confusion matrix. For the XGBoost, we
have 93.97% accuracy in the test dataset and 75.38% in the validation
dataset. This is the second-highest performance model we have
before the random forest classifier. As you can see, the same works
with the random forest have not been able to predict the 3rd class
correctly as well as the 2nd class.

The consistent failure of top-performing models (Random Forest
and XGBoost) to predict Classes 2 and 3 reflects several charac-
teristics of the Philippine music landscape. These moderate-high
view count classes represent songs in transition between niche
and mainstream appeal, making them inherently harder to classify
based solely on audio features. Mid-tier popularity often depends
on cultural factors including lyrics, artist reputation, social me-
dia trends-not captured in the model. Additionally, the Philippine
streaming market exhibits a ”winner-takes-all” pattern where songs
either achieve massive popularity or remain in lower tiers, with
fewer songs occupying the middle ground. Our clustering analysis
supports this, showing that Classes 2-3 contain more diverse audio
profiles, suggesting they represent genre-crossing tracks that don’t
conform to clear audio patterns. This aligns with music industry
research indicating that moderate success is often more dependent
on non-audio factors than extreme success or failure.

The normal DNN was able to get at most 91.62% accuracy in
the test dataset while only having 62.56% in the validation dataset.
While this is considered a good performance in terms of our over-
all tested models, it’s still ranked 3 before the SVM in terms of
validation performance.

For the attention-based neural network using PCA, we concluded
with 90.84% in the test dataset and 53.84% in the validation dataset.
For the attention-based neural network using ICA, we concluded
with 53.93% accuracy in the test dataset and 31.79% accuracy in the
dataset.

5 CONCLUSION
The researchers conducted this study to explore the most dominant
audio features that characterize the top songs in the case of the
Philippines (our dataset contains top Spotify songs between 2018
and 2023). By utilizing data processing, feature extraction, and
other machine learning models, the study reveals important audio
features that appeal to Filipino listeners. Key features such as tempo,
energy, melody, and loudness were highlighted as influential in
determining a song’s appeal. By employing techniques like Locally
Linear Embedding (LLE), Uniform Manifold Approximation and
Projection (UMAP), and Agglomerative and Means Clustering, this
research was able to uncover patterns and relationships within the
dataset, providing a nuanced understanding of feature importance
in the Philippine music industry.

The study’s implementation of a Deep Neural Network (DNN)
prototype with an attention mechanism illustrated how machine
learning can be leveraged to prioritize features based on their influ-
ence, demonstrating a practical application of feature analysis in
music. Beyond mapping regional music, these findings will help
artists, producers, and industry personnel to catch up with their

229Exploratory Analysis of Audio Features for Dominant Feature Identification: A Multimodal Machine Learning
Evaluation of Song Popularity Prediction Using Deep Neural Networks, Clustering, and Regression Models

WSSE 2025, October 24–26, 2025, Okayama, Japan

listeners regarding what they like to listen to; they will tell how to
be in line with the listeners of those regions.

Considering the findings and limitations of this study, a number
of recommendations are made to develop the current framework
further and expand its applicability. This framework can be ex-
panded upon in future research to study music preference in other
areas of the world, enabling a global, comparative analysis, and
allowing some degree of differentiation of the attractiveness of
music in different cultural dimensions. This study focused only on
chorus sections present in popular songs as they are easier to mem-
orize, and therefore included. However, the use of other sections
e.g. verses and bridges can provide a broader perspective on other
potential features affecting the popularity of songs.

In addition, broadening the social metrics beyond just YouTube
to incorporate streaming data from other platforms and social me-
dia may also provide a more comprehensive indication of audi-
ence engagement and traction. The DNN model’s high accuracy
demonstrates the potential for further development using advanced
machine learning techniques, such as ensemble methods, to com-
plement feature dimensionality analysis and improve interpretation
of feature importance in music popularity prediction. Future re-
search can further advance knowledge of audio feature impacts in
the emerging field of music analytics by exploring these areas.This
study conducted a comparative evaluation of Convolutional Neu-
ral Networks (CNN), Long Short-Term Memory Networks (LSTM),
and CNN-LSTM hybrid models for sentiment analysis on online
learning-related tweets in the Philip- pines. The results demon-
strate that the CNN-LSTM hybrid model outperforms standalone
CNN and LSTM models by effectively capturing both spatial and
sequential dependencies in textual data.

References
[1] C. S. Araujo, M. Cristo, and R. Giusti. 2019. Predicting Music Popularity on

Streaming Platforms. DOI:https://doi.org/10.5753/sbcm.2019.10436.

[2] J.-P. Briot and F. Pachet. 2018. Deep learning for music generation: challenges
and directions. Neural Computing and Applications. DOI:https://doi.org/10.1007/
s00521-018-3813-6.

[3] SoftwareEngenius. 2020. Song Trending Year Predictor using Machine Learning
(CNN, SVR, and more!). Retrieved December 19, 2020 from https://www.youtube.
com/watch?v$=$-7X1N9FOhEk.

[4] C. S. Abundo and C. Monterola. 2009. Automatic musical genre classification of
OPM songs. Proceedings of the Samahang Pisika ng Pilipinas, 27, SPP-2009-PA-28.
Retrieved from https://proceedings.spp-online.org/article/view/SPP-2009-PA-28.
[5] M. Abisado, M. Yongson, and Ma. Ian De Los Trinos. 2021. Towards the Develop-
ment of Music Mood Classification of Original Pilipino Music (OPM) Songs
Based on Audio and Lyrics Keyword. In Proceedings of the 2021 5th Inter-
national Conference on E-Society, E-Education and E-Technology. DOI:https:
//doi.org/10.1145/3485768.3485786.

[6] S. Arora, R. Rani, and N. Saxena. 2022. Music Stream Analysis for the Prediction of
Song Popularity using Machine Learning and Deep Learning Approach. In 2022
3rd International Conference on Computing, Analytics and Networks (ICAN), Ra-
jpura, Punjab, India, 1–5. DOI:https://doi.org/10.1109/ICAN56228.2022.10006843.
[7] A. H. Raza and K. Nanath. 2020. Predicting a Hit Song with Machine Learning:
Is There an Apriori Secret Formula? In 2020 International Conference on Data
Science, Artificial Intelligence, and Business Analytics (DATABIA). DOI:https:
//doi.org/10.1109/databia50434.2020.9190613.

[8] R. Giusti et al. 2019. Predicting Music Popularity on Streaming Platforms Evalua-
tion and Collaborative Monitoring of Streets and Roads Conditions by Means
of Smartphone Sensors View Project Predicting Music Popularity Using Music
Charts. DOI:https://doi.org/10.5753/sbcm.2019.10436.

[9] L.-C. Yang, S.-Y. Chou, J.-Y. Liu, Y.-H. Yang, and Y.-A. Chen. 2017. Revisiting
the problem of audio-based hit song prediction using convolutional neural net-
works. In IEEE Conference Publication. Retrieved from https://ieeexplore.ieee.
org/document/7952230.

[10] H. Terasawa, M. Matsubara, V. Goudarzi, and M. Sadakata. 2021. Music in Quar-
antine: Connections between changes in lifestyle, psychological states, and
musical behaviors during COVID-19 pandemic. Frontiers in Psychology 12.
DOI:https://doi.org/10.3389/fpsyg.2021.689505.

230