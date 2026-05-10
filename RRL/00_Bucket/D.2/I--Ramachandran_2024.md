International Journal of Neural Networks and Deep Learning (IJNNDL)
Volume 1, Issue 1, January-June 2024, pp. 1-10. Article ID: IJNNDL_01_01_001
Available online at https://iaeme.com/Home/issue/IJNNDL?Volume=1&Issue=1
Journal ID: 3851-5221

© IAEME Publication

THE EVOLUTION OF RECURRENT NEURAL
NETWORKS IN HANDLING LONG-TERM
DEPENDENCIES IN SEQUENTIAL DATA

Dr. K K Ramachandran
Director/ Professor: Management/Commerce/International Business, DR. G R D College of
Science, Coimbatore, India.

ABSTRACT

Recurrent Neural Networks (RNNs) have undergone significant evolution in their
ability  to  handle  long-term  dependencies  in  sequential  data.  This  paper  reviews  the
development  of  RNN  architectures,  from  early  vanilla  models  to  more  advanced
structures like Long Short-Term Memory (LSTM) networks and Gated Recurrent Units
(GRUs).  The  challenges  associated  with  capturing
long-term  dependencies,
particularly the vanishing and exploding gradient problems, are discussed, along with
the innovations that have overcome these limitations. The paper also examines recent
advancements  such  as  attention  mechanisms  and  transformer  models,  which  have
further enhanced the capability of RNNs. A comparative analysis of these architectures
is provided, demonstrating their effectiveness in various applications, including natural
language  processing,  time-series  forecasting,  and  speech  recognition.  The  findings
highlight the continued relevance of RNNs in sequential data tasks while pointing to
future research directions that could further improve their performance.

Keywords:  Recurrent  Neural  Networks,  Long-Term  Dependencies,  Sequential  Data,
LSTM,  GRU,  Attention  Mechanisms,  Transformer  Models,  Vanishing  Gradient
Problem, Time-Series Forecasting, Natural Language Processing.

Cite this Article: Dr. K K Ramachandran, The Evolution of Recurrent Neural Networks
in  Handling  Long-Term  Dependencies  in  Sequential  Data.  International  Journal  of
Neural Networks and Deep Learning (IJNNDL), 1(1), 2024, pp. 1-10.
https://iaeme.com/Home/issue/IJNNDL?Volume=1&Issue=1

https://iaeme.com/Home/journal/IJNNDL

1

editor@iaeme.com

The Evolution of Recurrent Neural Networks in Handling Long-Term Dependencies in
Sequential Data

1. INTRODUCTION

1.1 Overview of Recurrent Neural Networks (RNNs)
Recurrent Neural Networks (RNNs) represent a class of artificial neural networks specifically
designed to process sequential data, where the order of the data points is critical to the task at
hand.  Unlike  traditional  feedforward  neural  networks,  RNNs  are  equipped  with  connections
that  form  directed  cycles,  enabling  them  to  maintain  a  "memory"  of  previous  inputs.  This
memory  allows  RNNs  to  model  temporal  dynamics  and  dependencies,  making  them
particularly well-suited for tasks such as time-series forecasting, natural language processing,
and speech recognition. The key feature of RNNs is their ability to take into account not only
the current input but also the history of previous inputs, thereby capturing the context necessary
for making predictions based on sequences of data.

1.2 Importance of Handling Long-Term Dependencies in Sequential Data

Handling long-term dependencies in sequential data is one of the most significant challenges in
the design and implementation of RNNs. Long-term dependencies occur when the prediction
of an element in a sequence depends on information from distant past elements. For instance,
understanding the meaning of a word in a sentence might require knowledge of a word that
appeared  much  earlier  in  the  text.  However,  vanilla  RNNs,  which  are  the  simplest  form  of
RNNs, struggle with retaining useful information over long sequences due to issues such as the
vanishing and exploding gradient problems. These issues cause the gradients used to update the
network's weights to diminish or explode as they are propagated through many layers, making
it  difficult  for  the  network  to  learn  from  long-term  dependencies  effectively.  Consequently,
without mechanisms to handle these dependencies, RNNs may fail to capture important patterns
in sequential data, leading to suboptimal performance in tasks that require a deep understanding
of context over time.

1.3 Objectives and Scope of the Research

The  primary  objective  of  this  research  is  to  explore  the  evolution  of  RNN  architectures  in
addressing the challenge of handling long-term dependencies in sequential data. The study aims
to review the development of RNNs from their inception to the introduction of advanced models
such  as  Long  Short-Term  Memory  (LSTM)  networks  and  Gated  Recurrent  Units  (GRUs),
which were specifically designed to overcome the limitations of vanilla RNNs. Additionally,
this paper seeks to analyze how these advancements have improved the performance of RNNs
in various applications that require the processing of sequential data. The scope of this research
is focused on providing a concise yet comprehensive overview of the key innovations in RNN
architectures, with a particular emphasis on their impact on long-term dependency handling.
Through this exploration, the paper will highlight both the successes and the ongoing challenges
in the field, offering insights into future directions for RNN research and development.

https://iaeme.com/Home/journal/IJNNDL

2

editor@iaeme.com

Dr. K K Ramachandran

2. LITERATURE REVIEW

2.1 Early Approaches to Sequential Data in Neural Networks

Before  the  advent  of  Recurrent  Neural  Networks  (RNNs),  early  approaches  to  processing
sequential  data  in  neural  networks  were  largely  inadequate  for  capturing  temporal
dependencies.  Traditional  feedforward  neural  networks  were  ill-suited  for  tasks  involving
sequences  because  they  lacked  mechanisms  to  remember  or  leverage  previous  inputs.
Researchers initially attempted to address this limitation by using time-delay neural networks
(TDNNs), which were designed to handle temporal sequences by incorporating a fixed number
of past inputs as additional features (Waibel et al., 1989). However, TDNNs were constrained
by  the  fixed  window  size,  which  limited  their  ability  to  model  long-term  dependencies
effectively. Another approach was the use of Markov models, such as Hidden Markov Models
(HMMs),  which  were  probabilistic  models  that  could  capture  temporal  dependencies  by
modeling  the  sequence  of  states.  While  HMMs  were  successful  in  applications  like  speech
recognition,  they  struggled  with  complex  dependencies  due  to  their  reliance  on  first-order
Markov assumptions and limited ability to represent long-term context (Rabiner, 1989).

2.2 Development of Recurrent Neural Networks

The  limitations  of  earlier  models  in  handling  sequential  data  led  to  the  development  of
Recurrent Neural Networks (RNNs) in the 1980s, which introduced a significant breakthrough
in  sequence  modeling.  RNNs,  as  proposed  by  Elman  (1990),  were  designed  with  recurrent
connections that allowed the network to maintain a hidden state, effectively acting as a dynamic
memory that could retain information from previous inputs. This architecture enabled RNNs to
capture temporal dependencies over varying lengths of sequences, making them more flexible
than fixed-window models like TDNNs. The core idea was that the hidden state, updated at
each time step, could carry forward relevant information, allowing the network to consider both
current and past data when making predictions. Despite their theoretical potential, early RNNs
encountered significant practical challenges, particularly the vanishing and exploding gradient
problems identified by Hochreiter (1991) and Bengio et al. (1994). These issues arose during
the training process when gradients propagated through many time steps, leading to gradients
that either shrank to near zero (vanishing) or grew exponentially (exploding), making it difficult
for the network to learn long-term dependencies.

2.3 Advances in RNN Architectures for Long-Term Dependencies

To overcome the limitations of vanilla RNNs, particularly their inability to effectively manage
long-term  dependencies  due  to  vanishing  and  exploding  gradients,  significant  advancements
were made in RNN architectures. The most notable development was the introduction of Long
Short-Term  Memory  (LSTM)  networks  by  Hochreiter  and  Schmidhuber  (1997).  LSTMs
addressed  the  vanishing  gradient  problem  by  incorporating  memory  cells  and  gating
mechanisms (input gate, forget gate, and output gate), which allowed the network to control the
flow of information and maintain long-term dependencies. The gating mechanisms enabled the
selective  updating  of  cell  states,  ensuring  that  important  information  could  be  retained  over
extended sequences while irrelevant information could be discarded.

https://iaeme.com/Home/journal/IJNNDL

3

editor@iaeme.com

The Evolution of Recurrent Neural Networks in Handling Long-Term Dependencies in
Sequential Data

Following the success of LSTMs, Gated Recurrent Units (GRUs) were introduced by Cho et al.
(2014) as a simpler alternative to LSTMs. GRUs combined the input and forget gates into a
single update gate, streamlining the architecture while retaining the ability to manage long-term
dependencies effectively. GRUs were shown to perform comparably to LSTMs in many tasks,
but with fewer parameters, making them computationally more efficient. These challenges led
to  further  innovations,  including  the  development  of  attention  mechanisms  and  transformer
models, which have since become the state-of-the-art for handling long-term dependencies in
sequential data (Vaswani et al., 2017).

3. CHALLENGES IN HANDLING LONG-TERM DEPENDENCIES

3.1 The Problem of Vanishing and Exploding Gradients

One of the most significant challenges in training Recurrent Neural Networks (RNNs) is the
problem of vanishing and exploding gradients. These issues arise during the backpropagation
process,  where  gradients  are  used  to  update  the  network's  weights  based  on  the  error  at  the
output. In RNNs, the gradients must be propagated back through many time steps, which can
lead to situations where the gradients either shrink to near zero (vanishing gradients) or grow
exponentially (exploding gradients). The vanishing gradient problem is particularly detrimental
because it causes the network to stop learning effectively. As the gradients diminish, the weights
of earlier layers are updated so minimally that the network essentially "forgets" the information
from earlier time steps. This makes it exceedingly difficult for the RNN to capture long-term
dependencies in the data, as the information required to make accurate predictions cannot be
retained over extended sequences.

On  the  other  hand,  the  exploding  gradient  problem,  although  less  common,  can  also  cause
severe  issues  during  training.  When  gradients  grow  too  large,  they  can  cause  the  model's
parameters to update too drastically, leading to instability in the learning process. This often
results in the model diverging rather than converging towards a solution. Techniques such as
gradient clipping have been developed to mitigate the exploding gradient problem by capping
the gradients at a maximum value. However, addressing the vanishing gradient problem has
proven more complex, necessitating the development of specialized RNN architectures such as
Long  Short-Term  Memory  (LSTM)  networks  and  Gated  Recurrent  Units  (GRUs)  that  are
designed to maintain gradient flow over long sequences.

3.2 Limitations of Traditional RNNs in Capturing Long-Term Dependencies

Traditional RNNs, often referred to as "vanilla" RNNs, are inherently limited in their ability to
capture long-term dependencies due to the aforementioned gradient issues. In vanilla RNNs,
each time step's hidden state is dependent on the previous hidden state and the current input.
While this recurrent structure theoretically allows the network to retain information over time,
in practice, the effectiveness of this memory is constrained by the network's ability to maintain
gradients over long sequences. As a result, vanilla RNNs tend to excel at modeling short-term
dependencies  but  struggle  with  tasks  that  require  the  integration  of  information  from  much
earlier in the sequence.

https://iaeme.com/Home/journal/IJNNDL

4

editor@iaeme.com

Dr. K K Ramachandran

The  limitations  of  vanilla  RNNs  become  particularly  evident  in  tasks  such  as  language
modeling, where the context provided by earlier words in a sentence is crucial for predicting
later words. For example, in a long sentence, a vanilla RNN might be able to remember the
immediate previous words, but it is likely to forget the subject of the sentence if it appeared
many words earlier. This leads to performance degradation as the network's predictions become
less accurate over longer sequences.

Graph 1: Performance Degradation in Vanilla RNNs Over Time Steps

Graph  1:  Shows  the  decline  in  accuracy  as  the  number  of  time  steps  increases.  The  graph
highlights the difficulty vanilla RNNs face in maintaining performance over longer sequences,
underscoring the challenges of capturing long-term dependencies in sequential data.

4. ADVANCED RNN ARCHITECTURES

4.1 Long Short-Term Memory (LSTM) Networks
Long  Short-Term  Memory  (LSTM)  networks  represent  a  significant  advancement  in  the
architecture  of  Recurrent  Neural  Networks  (RNNs),  specifically  designed  to  address  the
limitations  of  traditional  RNNs  in  handling  long-term  dependencies.  The  core  innovation  of
LSTMs lies in their use of memory cells and gating mechanisms, which allow them to maintain
information over extended periods. Each LSTM cell contains three gates: the input gate, the
forget gate, and the output gate. These gates regulate the flow of information into and out of the
cell, enabling the network to retain relevant information for as long as needed and discard what
is  unnecessary.  This  architecture  effectively  mitigates  the  vanishing  gradient  problem  that
plagues  vanilla  RNNs,  making  LSTMs  highly  effective  in  tasks  where  long-term  context  is

https://iaeme.com/Home/journal/IJNNDL

5

editor@iaeme.com

The Evolution of Recurrent Neural Networks in Handling Long-Term Dependencies in
Sequential Data

crucial, such as natural language processing, time-series forecasting, and speech recognition.
LSTMs can remember dependencies from much earlier in the sequence, which is essential for
understanding the context in applications like language translation or predicting future events
in a time series.

4.2 Gated Recurrent Units (GRUs)
Gated  Recurrent  Units  (GRUs)  were  introduced  as  a  simpler  alternative  to  LSTMs,  offering
comparable performance with a more streamlined architecture. GRUs combine the forget and
input gates into a single update gate, which simplifies the model by reducing  the number of
parameters that need to be learned during training. Additionally, GRUs have only two gates:
the update gate and the reset gate, which control the information flow similar to the mechanisms
in LSTMs. Despite being simpler, GRUs have been found to perform just as well as LSTMs on
many tasks, particularly when computational efficiency is a concern. The reduced complexity
of  GRUs  makes  them  faster  to  train  and  easier  to  implement  while  still  providing  strong
performance in capturing long-term dependencies. This makes GRUs particularly attractive in
scenarios  where  model  simplicity  and  training  speed  are  critical,  such  as  in  real-time
applications or when working with large datasets.

Table 1: Comparative Analysis of LSTM and GRU Architectures

Feature

Number of Gates
Memory Cells

Complexity
Training Time

Performance

LSTM

GRU

Three (Input, Forget, Output)  Two (Update, Reset)

Yes

Higher
Longer

High

No

Lower
Shorter
Comparable to
LSTM
High

Computational Efficiency

Moderate

4.3 Recent Innovations: Attention Mechanisms and Transformer Models
While LSTMs and GRUs have significantly advanced the ability of RNNs to handle long-term
dependencies,  recent  innovations  have  further  transformed  the  field.  Attention  mechanisms,
introduced  in  the  context  of  neural  machine  translation,  have  revolutionized  how  models
process  sequential  data.  Instead  of  relying  solely  on  the  hidden  state  of  the  last  time  step,
attention  mechanisms  allow  the  model  to  weigh  and  focus  on  different  parts  of  the  input
sequence  when  making  predictions.  This  approach  enhances  the  model's  ability  to  capture
relevant information from any part of the sequence, regardless of its distance from the current
time  step.  Attention  mechanisms  have  been  particularly  impactful  in  tasks  such  as  language
translation, where different words in a sentence can have varying importance depending on the
context.

Building on the success of attention mechanisms, transformer models have emerged as the state-
of-the-art architecture for handling sequential data. Transformers, unlike traditional RNNs, do
not  rely  on  a  recurrent  structure  but  instead  use  self-attention  mechanisms  to  process  all

https://iaeme.com/Home/journal/IJNNDL

6

editor@iaeme.com

Dr. K K Ramachandran

elements of a sequence in parallel. This not only allows transformers to handle much longer
sequences than RNNs but also makes them significantly faster to train. The parallelization of
computation  in  transformers  has  led  to  their  adoption  in  a  wide  range  of  applications,  from
natural language processing to image recognition, where they have consistently outperformed
previous models.

Chart 1: Performance Comparison of LSTM, GRU, and Transformer Models on Sequential
Data Tasks

Chart  1:  This  chart  would  visually  demonstrate  the  advantages  of  transformer  models  over
traditional  RNN-based  architectures,  particularly  in  tasks  that  require  processing  very  long
sequences of data.

Applications of RNNs in Long-Term Dependency Tasks
The  advancements  in  RNN  architectures,  from  LSTMs  and  GRUs  to  transformers,  have
expanded  the  range  of  applications  where  these  models  can  be  effectively  used.  In  natural
language processing, RNNs are foundational in tasks such as machine translation, sentiment
analysis, and text generation, where understanding context over long passages is crucial. Time-
series  forecasting  is  another  area  where  RNNs,  particularly  LSTMs  and  GRUs,  have  been
widely  adopted.  These  models  excel  in  predicting  future  values  in  a  sequence  based  on
historical  data,  making  them  invaluable  in  finance,  weather  forecasting,  and  inventory
management.

Speech recognition is yet another domain that benefits from advanced RNN architectures. The
ability  to  maintain  context  over  time  allows  these  models  to  accurately  transcribe  spoken
language, even when the sentence  structure is complex or when long-term dependencies are
present.  With  the  introduction  of  transformers,  the  potential  applications  of  sequential  data
models  have  expanded  even  further,  enabling  breakthroughs  in  areas  such  as  automated
question answering, document summarization, and beyond.

https://iaeme.com/Home/journal/IJNNDL

7

editor@iaeme.com

The Evolution of Recurrent Neural Networks in Handling Long-Term Dependencies in
Sequential Data

5. APPLICATIONS OF RNNS IN LONG-TERM DEPENDENCY TASKS

5.1 Natural Language Processing
Recurrent Neural Networks (RNNs), particularly advanced architectures like Long Short-Term
Memory (LSTM) networks and Gated Recurrent Units (GRUs), have become essential tools in
natural  language  processing  (NLP).  These  models  are  uniquely  suited  to  tasks  that  require
understanding and generating human language, as they can effectively manage the sequential
nature  of  text.  In  language  modeling,  RNNs  have  been  used  to  predict  the  next  word  in  a
sentence based on the context provided by preceding words. This ability to capture long-term
dependencies is critical in tasks such as machine translation, where the meaning of a word often
depends on the context provided by earlier words in the sentence. LSTMs and GRUs have also
been employed in sentiment analysis, where understanding the sentiment expressed in a text
requires tracking emotional cues across the entire passage. Additionally, RNNs are used in text
summarization,  where  the  model  generates  concise  summaries  of  longer  documents  by
identifying and retaining the most relevant information over extended text sequences. Overall,
the ability of RNNs to handle the intricacies of language and maintain contextual understanding
over long sequences has made them indispensable in NLP applications.

5.2 Time-Series Forecasting
Time-series forecasting is another domain where RNNs, particularly LSTMs and GRUs, have
shown  exceptional  performance. In  time-series  data,  the  future  values  of  a  sequence  depend
heavily on its historical values, making the ability to capture long-term dependencies crucial
for accurate predictions. RNNs are well-suited for this task because they can retain information
from  previous  time  steps  and  use  it  to  inform  predictions  at  future  time  steps.  In  financial
markets, for example, LSTMs are used to predict stock prices by analyzing historical trends and
patterns,  enabling  investors  to  make  more  informed  decisions.  Similarly,  in  energy
consumption  forecasting,  RNNs  can  predict  future  energy  demands  based  on  past  usage
patterns, which is critical for optimizing power grid operations. The healthcare industry also
benefits from RNNs in time-series forecasting, where models can predict disease outbreaks or
patient  health  metrics  based  on  historical  data,  allowing  for  proactive  intervention.  The
versatility of RNNs in capturing temporal dynamics makes them highly effective for a wide
range of time-series forecasting applications.

5.3 Speech Recognition
Speech recognition is a complex task that requires understanding spoken language in real-time
and  converting  it  into  text.  RNNs,  especially  LSTMs  and  GRUs,  have  been  instrumental  in
advancing the state of the art in this field. These models are capable of processing sequences of
audio data, where each time step corresponds to a fragment of the spoken input. RNNs can learn
to recognize patterns in speech that correspond to different phonemes, words, and phrases, even
when these patterns are spread out over long periods. This capability is particularly important
in continuous speech recognition, where the model must accurately transcribe spoken language
without the benefit of clearly defined word boundaries. LSTMs and GRUs excel in this domain
because they can maintain a memory of earlier parts of the audio sequence, allowing them to
understand and predict the next part of the speech based on the context provided by the entire

https://iaeme.com/Home/journal/IJNNDL

8

editor@iaeme.com

Dr. K K Ramachandran

sequence. This has led to significant improvements in the accuracy and reliability of speech
recognition  systems,  which  are  now  widely  used  in  applications  such  as  virtual  assistants,
transcription services, and voice-controlled devices. The ability of RNNs to handle the temporal
nature of speech makes them a powerful tool in the ongoing development of more advanced
and user-friendly speech recognition technologies.

6. CONCLUSION

6.1 Summary of Key Findings
This paper reviewed the evolution of Recurrent Neural Networks (RNNs) and their advanced
variants,  Long  Short-Term  Memory  (LSTM)  networks  and  Gated  Recurrent  Units  (GRUs),
highlighting their effectiveness in handling long-term dependencies in sequential data. These
architectures have significantly improved upon traditional RNNs by addressing challenges like
vanishing  and  exploding  gradients.  The  applications  of  these  models  in  natural  language
processing,  time-series  forecasting,  and  speech  recognition  demonstrate  their  crucial  role  in
modern AI.

6.2 Future Directions for RNN Research
Future  research  should  focus  on  enhancing  attention  mechanisms  and  transformer  models,
which have outperformed traditional RNNs in many tasks. Further exploration into integrating
RNNs  with  other  AI  techniques,  improving  efficiency  for  handling  long  sequences,  and
ensuring model transparency and fairness are also important. These advancements will expand
the capabilities and responsible use of RNNs in various applications.

REFERENCES
[1]

Bengio, Y., Simard, P., & Frasconi, P. (1994). Learning long-term dependencies with gradient

descent is difficult. IEEE Transactions on Neural Networks, 5(2), 157-166.

[2]

Cho, K., Van Merriënboer, B., Bahdanau, D., & Bengio, Y. (2014). On the properties of neural

[3]

[4]

machine translation: Encoder-decoder approaches. arXiv preprint arXiv:1409.1259.

Elman, J. L. (1990). Finding structure in time. Cognitive Science, 14(2), 179-211.

Vinay  SB  (2024)  Data  scientist  competencies  and  skill  assessment:  a  comprehensive

framework. Int J Data Sci Technol (IJDST) 1(1):1–10

[5]

Jegan  K,  Kannan  N  (2017)  Customer  expectation  and  perception  towards  organized  and

unorganized retail. Int J Manag (IJM) 8(3):159–168

[6]

Ramachandran KK (2023) Predicting supermarket sales with big data analytics: a comparative

study of machine learning techniques. Int J Data Anal (IJDA) 3(1):12–21

[7]

Sivakumar N, Sivaraman P, Tamilselvan N (2012) User expectations and requirements in the

knowledge society in digital era. Int J Comput Eng Technol (IJCET) 3(1):38–43

[8]

Hochreiter,  S.  (1991).  Untersuchungen  zu  dynamischen  neuronalen  Netzen.  [Doctoral

dissertation, TU München].

https://iaeme.com/Home/journal/IJNNDL

9

editor@iaeme.com

The Evolution of Recurrent Neural Networks in Handling Long-Term Dependencies in
Sequential Data

[9]

Hochreiter, S., & Schmidhuber, J. (1997). Long short-term memory. Neural Computation, 9(8),

1735-1780.

[10]  Rabiner, L. R. (1989). A tutorial on hidden Markov models and selected applications in speech

recognition. Proceedings of the IEEE, 77(2), 257-286.

[11]  Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A. N., ... & Polosukhin,

I. (2017). Attention is all you need. Advances in Neural Information Processing Systems, 30,

5998-6008.

[12]  Waibel, A., Hanazawa, T., Hinton, G., Shikano, K., & Lang, K. J. (1989). Phoneme recognition

using  time-delay  neural  networks.  IEEE  Transactions  on  Acoustics,  Speech,  and  Signal

Processing, 37(3), 328-339.

Citation:  Dr.  K  K  Ramachandran,  The  Evolution  of  Recurrent  Neural  Networks  in  Handling  Long-Term
Dependencies in Sequential Data. International Journal of Neural Networks and Deep Learning (IJNNDL), 1(1), 2024,
pp. 1-10.

Article Link:
https://iaeme.com/MasterAdmin/Journal_uploads/IJNNDL/VOLUME_1_ISSUE_1/IJNNDL_01_01_001.pdf
Abstract:
https://iaeme.com/Home/article_id/IJNNDL_01_01_001

Copyright: © 2024 Authors. This is an open-access article distributed under the terms of the Creative Commons
Attribution  License,  which  permits  unrestricted  use,  distribution,  and  reproduction  in  any  medium,  provided  the
original author and source are credited.

This  work  is  licensed  under  a  Creative  Commons  Attribution  4.0  International  License  (CC  BY  4.0).

✉ editor@iaeme.com

https://iaeme.com/Home/journal/IJNNDL

10

editor@iaeme.com

