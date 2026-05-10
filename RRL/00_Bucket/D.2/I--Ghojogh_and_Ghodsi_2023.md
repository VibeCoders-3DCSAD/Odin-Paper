To appear as a part of an upcoming textbook on deep learning.

Recurrent Neural Networks and Long Short-Term Memory Networks:
Tutorial and Survey

3
2
0
2

r
p
A
2
2

]

G
L
.
s
c
[

1
v
1
6
4
1
1
.
4
0
3
2
:
v
i
X
r
a

Benyamin Ghojogh
Ali Ghodsi
Department of Statistics and Actuarial Science & David R. Cheriton School of Computer Science,
Data Analytics Laboratory, University of Waterloo, Waterloo, ON, Canada

BGHOJOGH@UWATERLOO.CA
ALI.GHODSI@UWATERLOO.CA

YouTube channel of Benyamin Ghojogh: https://www.youtube.com/@bghojogh
YouTube channel of Ali Ghodsi: https://www.youtube.com/@DataScienceCoursesUW

Abstract
This is a tutorial paper on Recurrent Neural Net-
work (RNN), Long Short-Term Memory Net-
work (LSTM), and their variants. We start with a
dynamical system and backpropagation through
time for RNN. Then, we discuss the problems
of gradient vanishing and explosion in long-
term dependencies. We explain close-to-identity
weight matrix, long delays, leaky units, and echo
state networks for solving this problem. Then,
we introduce LSTM gates and cells, history and
variants of LSTM, and Gated Recurrent Units
(GRU). Finally, we introduce bidirectional RNN,
bidirectional LSTM, and the Embeddings from
Language Model (ELMo) network, for process-
ing a sequence in both directions.

1. Introduction
Before the era of transformers in deep learning, regu-
lar neural networks could not process sequences, such
as sentences (sequence of words) or speech (sequence of
phonemes), properly without any recurrence. Recurrent
Neural Network (RNN), proposed in (Rumelhart et al.,
1986), is a dynamical system which considers recurrence.
In recurrence, the output of a model is fed as input to the
model again in the next time step. One of the main train-
ing algorithms for RNN is Backpropagation Through Time
(BPTT), developed by several works (Robinson & Fallside,
1987; Werbos, 1988; Williams, 1989; Williams & Zipser,
1995; Mozer, 1995), which is similar to the backpropaga-
tion algorithm (Rumelhart et al., 1986) but has also chain
rule through time. There were some problems with gra-

dient vanishing or explosion for long-term dependencies
in RNN (Bengio et al., 1993; 1994). Several solutions
were proposed for this issue, some of which are close-to-
identity weight matrix (Mikolov et al., 2015), long delays
(Lin et al., 1995), leaky units (Jaeger et al., 2007; Sutskever
& Hinton, 2010), and echo state networks (Jaeger & Haas,
2004; Jaeger, 2007).
Sequence modeling requires both short-term and long-term
dependencies. For example, consider the sentence “The
police is chasing the thief”.
In this sentence, the words
“police” and “thief” are related to each other with short-
term dependency because they are close to one another in
the sequence of words. Another example is the sentence “I
was born in France. My father was working there for many
years during my childhood. My family had a great time
there while my father was making money in his business
there. That is why I know how to speak French”. In this
second example, the words “France” and “French” are re-
lated to each other with long-term dependency because they
are far away from one another in the sequence of words.
That inspired researchers to propose the Long Short-Term
Memory (LSTM) network to handle both short-term and
long-tern dependencies (Hochreiter & Schmidhuber, 1995;
1997). Later, Grated Recurrent Unit (GRU) was proposed
(Cho et al., 2014) which simpliﬁed LSTM to reduce its un-
necessary complexity.
RNN and LSTM networks are causal models which con-
dition every sequence element on the previous elements
in the sequence. Later researches showed that process-
ing the sequence in both directions can perform better for
the sequences which can be processed ofﬂine; e.g., if the
chunks of sequence can be saved and processed and the
sequence elements should not be processed as a stream
(Graves & Schmidhuber, 2005a;b). Therefore, bidirec-
tional RNN (Schuster & Paliwal, 1997; Baldi et al., 1999)
and bidirectional LSTM (Graves & Schmidhuber, 2005a;b)

were proposed to process sequences in both directions. The
Embeddings from Language Model (ELMo) network (Pe-
ters et al., 2018) is a language model which makes use of
the bidirectional LSTM.
This is a tutorial on RNN, LSTM, and their variants. There
exist some other tutorials and surveys about this topic,
some of which are (Jaeger, 2002; Jozefowicz et al., 2015;
Lipton et al., 2015; Schmidhuber, 2015; Greff et al., 2016;
Salehinejad et al., 2017; Staudemeyer & Morris, 2019; Yu
et al., 2019; Smagulova & James, 2019). A very good sur-
vey on the variants of LSTM is (Greff et al., 2016).

2. Recurrent Neural Network
2.1. Dynamical System
A dynamical system is recursive and its classical form is as
follows:

ht = fθ(ht−1),

(1)

where t denotes the time step, ht is the state at time t, and
fθ(.) is a function ﬁxed between the states of all time steps.
Figure 1-a shows such a system. Dynamical systems are
widely used in chaos theory (Broer & Takens, 2011).
We can have a dynamical system with external input signal
where xt denotes the input signal at time t. This system is
modeled as:

2

Figure 1. The folded and unfolded structures of (a) a dynamic sys-
tem without input, (b) a dynamical system with input, and (c) an
RNN. Every square on an edge means connection from one time
slot before.

and by ∈ Rq, respectively. As shown in Fig. 1-c, we have:

Rp (cid:51) it = W ht−1 + U xt + bi,
[−1, 1]p (cid:51) ht = tanh(it)

(3)

(4)

(5)

ht = fθ(ht−1, xt).

(2)

= tanh(W ht−1 + U xt + bi),

Rq (cid:51) yt = V ht + by,

This system is depicted in Fig. 1-b.

2.2. Parameter Sharing
The state ht can be considered as a summary of the past
sequence of inputs and states. If a different function fθ is
deﬁned for each possible sequence length, the model will
not have generalization. If the same parameters are used
for any sequence length, the model will have generaliza-
tion properties. Therefore, the parameters are shared for
all lengths and between all states. Such a dynamical sys-
tem with parameter sharing can be implemented as a neural
network with weights. Such a network is called a Recurrent
Neural Network (RNN), which was proposed in (Rumel-
hart et al., 1986).
RNN is illustrated in Fig. 1-c, where the same weight ma-
trices are used for all time slots. RNN gets a sequence as
input and outputs a sequence as a decision for a task such
as regression or classiﬁcation. Suppose the input, output,
and state at time slot t are denoted by xt ∈ Rd, yt ∈ Rq,
and ht ∈ Rp, respectively. Let W ∈ Rp×p be the weight
matrix between states, U ∈ Rp×d be the weight matrix
between the inputs and the states, and V ∈ Rq×p denote
the weight matrix between the states and outputs. The bias
weights for the state and the output are denoted by bi ∈ Rp

where tanh(.) ∈ (−1, 1) denotes the hyperbolic tangent
function, which is used as an element-wise activation func-
tion for the states.
If there is an activation function, such as softmax, at the
output layer, we denote the output of activation function
by:

Rq (cid:51) (cid:98)yt = softmax(yt) =

exp(yt,1)
j=1 exp(yt,j)

(cid:80)q

,

(6)

where yt,j denotes the j-th component of yt.

2.3. Backpropagation Through Time (BPTT)
One of the methods for training RNN is Backpropagation
Through Time (BPTT), which is very similar to the back-
propagation algorithm (Rumelhart et al., 1986) because it
is based on gradient descent and chain rule (Ghojogh et al.,
2021), but it has also chain rule through time. BPTT was
developed by several works (Robinson & Fallside, 1987;
Werbos, 1988; Williams, 1989; Williams & Zipser, 1995;
Mozer, 1995). This algorithm is very solid in theory; how-
ever, it does not show the best performance in practice.
In BPTT, the loss is considered as a summation of loss
functions at the previous time steps until now. As it is im-

practical to consider all time steps from the start of train-
ing (especially after a long time of training), we only con-
sider the T previous time steps. In other words, we assume
that RNN has T -order Markov property (Ghojogh et al.,
2019b). Therefore, the loss function is:

According to Eqs. (3) and (4), we have:

it+1 = W ht + U xt+1 + bi,
(12)
ht+1 = tanh(it+1) = tanh(W ht + U xt+1 + bi). (13)

R (cid:51) L =

T
(cid:88)

t=1

Lt,

Therefore:

(7)

Rp×p (cid:51)

∂ht+1
∂ht

(a)

= (cid:0) ∂it+1
∂ht

(cid:1)(cid:62)

×

∂ht+1
∂it+1

3

where L1 is the loss function at the current time slot and Lt
denotes the loss function at the previous (t − 1) time slot.
This loss functions needs to be optimized using gradient
descent and chain rule. Therefore, we calculate its gradient
with respect to the parameters of RNN. These parameters
are yt, ht, V , W , U , bi, and by, based on Eqs. (3), (4),
and (5) and Fig. 1-c.

2.3.1. GRADIENT WITH RESPECT TO THE OUTPUT
If there is no activation function at the last layer, the gradi-
ent of the loss function of RNN with respect to the output
at time t is:

Rq (cid:51)

∂L
∂yt

(a)
=

∂L
∂Lt

×

∂Lt
∂yt

(7)
=

∂Lt
∂yt

,

(8)

where (a) is because of the chain rule.
The gradient of the loss function at time t with respect to
the output at time t, i.e., ∂Lt/∂yt, is calculated based on
the formula of the loss function. The loss function can
be any loss function for classiﬁcation, regression, or other
tasks.
If there is an activation function at the last layer (see Eq.
(6)), the gradient is:

Rq (cid:51)

∂L
∂yt

(a)
=

∂L
∂Lt

×

∂Lt
∂(cid:98)yt

×

∂(cid:98)yt
∂yt

(7)
=

∂Lt
∂(cid:98)yt

×

∂(cid:98)yt
∂yt

,

(9)

where (a) is because of the chain rule. The derivative
∂(cid:98)yt/∂yt is calculated based on the formula of the activa-
tion function. The other derivative, ∂Lt/∂(cid:98)yt, is calculated
based on the formula of the loss as a function of the output
of the activation function.

2.3.2. GRADIENT WITH RESPECT TO THE STATE
The gradient of the loss function of RNN with respect to
the state at time t is:

Rp (cid:51)

∂L
∂ht

(a)
=

(5)
=

(cid:16) ∂L
∂yt
(cid:16) ∂L
∂yt

×

× V

(cid:17)

∂yt
∂ht
(cid:17)

(cid:17)

+

(cid:16) ∂L

∂ht+1

+

(cid:16) ∂L

∂ht+1

×

×

∂ht+1
∂ht
(cid:17)
∂ht+1
∂ht

, (10)

where (a) is because changing ht affects both yt and ht+1.
We denote δt := ∂L/∂ht so Eq. (10) becomes:

δt =

(cid:16) ∂L
∂yt

(cid:17)

(cid:16)

+

× V

δt+1 ×

∂ht+1
∂ht

(cid:17)

.

(11)

(b)
= W (1 − h(cid:62)

t+1ht+1)I p×p,

(14)

where I p×p is the identity matrix of size (p × p), (a)
is because of the chain rule, and (b) is because Rp×p (cid:51)
∂it+1/∂ht = W (cid:62) for Eq. (12), and we have:

Rp×p (cid:51)

∂ht+1
∂it+1

= (1 − h(cid:62)

t+1ht+1)I p×p,

(15)

(13) and the formula for derivative of the
based on Eq.
hyperbolic tangent function, noticing that the state is mul-
tidimensional and not a scalar.
For the time slot t = T , the derivative ∂L/∂hT is much
simpler:

Rp (cid:51) δT =

∂L
∂hT

(a)
=

∂L
∂yT

×

∂yT
∂hT

(5)
=

∂L
∂yT

(8)
=

∂LT
∂yT

,

(16)

where (a) is because of the chain rule and the derivative
∂LT /∂yT is computed based on the formula of loss func-
tion.

2.3.3. GRADIENT WITH RESPECT TO V
The gradient of the loss function of RNN with respect to
the weight matrix V is:

Rq×p (cid:51)

∂L
∂V

(a)
=

T
(cid:88)

t=1

(cid:16) ∂L
∂yt

×

(cid:17) (b)
=

∂yt
∂V

T
(cid:88)

t=1

(cid:16) ∂Lt
∂yt

× h(cid:62)
t

(cid:17)

,

(17)

where (a) is because V exists in all time slots and changing
V affects the loss L in all time slots. The equation (b) is
because of Eqs. (8) and (5). The derivative ∂Lt/∂yt ∈ Rq
is calculated based on the formula of the loss function.

2.3.4. GRADIENT WITH RESPECT TO W
The gradient of the loss function of RNN with respect to
the weight matrix W is:

Rp×p (cid:51)

∂L
∂W

(a)
=

T
(cid:88)

t=1

vec−1
p×p

(cid:16)(cid:0) ∂ht
∂W

(cid:1)(cid:62)

×

(cid:17)

,

∂L
∂ht

(18)

where vec−1
p×p(.) de-vectorizes the vector of length p2 to a
matrix of size (p × p) and (a) is because W exists in all
time slots and changing W affects the loss L in all time

slots. The derivative ∂L/∂ht ∈ Rp in Eq. (18) was com-
puted in Section 2.3.2. The derivative ∂ht/∂W in Eq. (18)
is:

2.3.7. GRADIENT WITH RESPECT TO by
The gradient of the loss function of RNN with respect to
the bias by is:

4

Rp×p2

(cid:51)

∂ht
∂W

=

∂ht
∂it

×

∂it
∂W

,

because of the chain rule. The ﬁrst term is:

Rp×p (cid:51)

∂ht
∂it

= (1 − h(cid:62)

t ht)I p×p,

(19)

according to Eq. (15). Based on the Magnus-Neudecker
convention (Ghojogh et al., 2021), the second term is cal-
culated as:

Rp×p2

(cid:51)

∂it
∂W

= h(cid:62)

t−1 ⊗ I p×p,

where ⊗ denotes the Kronecker product.

2.3.5. GRADIENT WITH RESPECT TO U
The gradient of the loss function of RNN with respect to
the weight matrix U is:

Rp×d (cid:51)

∂L
∂U

(a)
=

T
(cid:88)

t=1

vec−1
p×d

(cid:16)(cid:0) ∂ht
∂U

(cid:1)(cid:62)

×

(cid:17)

,

∂L
∂ht

(20)

where (a) is because U exists in all time slots and chang-
ing U affects the loss L in all time slots. The derivative
∂L/∂ht ∈ Rp in Eq. (18) was computed in Section 2.3.2.
The derivative ∂ht/∂U in Eq. (18) is:

Rp×(pd) (cid:51)

∂ht
∂U

=

∂ht
∂it

×

∂it
∂U

,

because of the chain rule. The ﬁrst term is already calcu-
lated in Eq. (19). Based on the Magnus-Neudecker conven-
tion (Ghojogh et al., 2021), the second term is calculated
as:

Rp×(pd) (cid:51)

∂it
∂U

= x(cid:62)

t ⊗ I p×p.

2.3.6. GRADIENT WITH RESPECT TO bi
The gradient of the loss function of RNN with respect to
the bias bi is:

Rp (cid:51)

∂L
∂bi

(a)
=

T
(cid:88)

t=1

(cid:16)(cid:0) ∂ht
∂bi

(cid:1)(cid:62)

×

(cid:17)

,

∂L
∂ht

(21)

where (a) is because bi exists in all time slots and changing
b affects the loss L in all time slots. The derivative ∂L/∂ht
was already calculated in Section 2.3.2. The derivative
∂ht/∂bi is calculated as:

Rp×p (cid:51)

∂ht
∂bi

(a)
=

∂ht
∂it

×

∂it
∂bi

(3)
=

∂ht
∂it

,

Rq (cid:51)

∂L
∂by

(a)
=

T
(cid:88)

t=1

(cid:16) ∂L
∂yt

×

(cid:17) (b)
=

∂yt
∂by

T
(cid:88)

t=1

∂Lt
∂yt

,

(22)

where (a) is because by exists in all time slots and changing
by affects the loss L in all time slots. The equation (b) is
because of Eqs. (8) and (5). The derivative ∂Lt/∂yt ∈ Rq
is calculated based on the formula of the loss function.

2.3.8. UPDATES BY GRADIENT DESCENT
BPPT updates the parameters of RNN by gradient descent
(Ghojogh et al., 2021) using the calculated gradients:

ht := ht − η

,

∀t ∈ {1, . . . , T },

∂L
∂ht
∂L
∂V

,

,

∂L
∂U
∂L
∂bi
∂L
∂by

,

,

V := V − η

W := W − η

∂L
∂W

,

U := U − η

bi := bi − η

by := by − η

where η > 0 is the learning rate and the gradients are cal-
culated by Eqs. (10), (17), (18), (20), (21), and (22).

3. Gradient Vanishing or Explosion in

Long-term Dependencies

In recurrent neural networks, so as in deep neural networks,
the ﬁnal output is the composition of a large number of
non-linear transformations. This results in the problem of
either vanishing or exploding gradients in recurrent neural
networks, especially for capturing long-term dependencies
in sequence processing (Bengio et al., 1993; 1994). This
problem is explained in the following. Recall Eq. (2) for a
dynamical system:

ht = fθ(ht−1, xt).

By induction, the hidden state at time t, i.e., ht, can be writ-
ten as the previous T time steps. If the subscript t denotes
the previous t time steps, we have by induction (Hochreiter,
1998; Hochreiter et al., 2001):

where (a) is because of the chain rule and the derivative
∂ht/∂it was already calculated in Eq. (19).

(cid:16)

h1 = fθ

(cid:0) . . . fθ(hT , xT +1) . . . , x2

(cid:1), x1

fθ

(cid:17)

.

Then, by the chain rule in derivatives, the derivative loss at
time T , i.e., LT , is:

∂LT
∂θ

=

(cid:88)

t≤T

(cid:88)

(2)
=

t≤T

∂Lt
∂ht

∂ht
∂θ

(cid:88)

(a)
=

t≤T

∂Lt
∂hT

∂hT
∂ht

∂ht
∂θ

∂Lt
∂hT

∂hT
∂ht

∂fθ(ht−1, xt)
∂θ

,

(23)

where (a) is because of the chain rule. In this expression,
there is the derivative of hT with respect to ht which itself
can be calculated by the chain rule:

∂hT
∂ht

=

∂hT
∂hT −1

×

∂hT −1
∂hT −2

× · · · ×

∂ht+1
∂ht

.

(24)

for capturing long-term dependencies in the sequence, T
should be large. This means that in Eq. (24), and hence in
Eq. (23), the number of multiplicand terms becomes huge.
On the one hand, if each derivative is slightly smaller than
one, the entire derivative in the chain rule becomes very
small for multiplication of many terms smaller than one.
This problem is referred to as gradient vanishing. On the
other hand, if every derivative is slightly larger than one,
the entire derivative in the chain rule explodes, resulting in
the problem of exploding gradients. Note that gradient van-
ishing is more common than gradient explosion in recurrent
networks.
There exist various attempts for resolving the problem of
gradient vanishing or explosion (Hochreiter, 1998; Bengio
et al., 2013). In the following, some of these attempts are
introduced.

3.1. Close-to-identity Weight Matrix
As Eq. (4) shows, the state is multiplied by a weight ma-
trix W at every time step and if there is long-term depen-
dency, many of these W matrices are multiplied. Suppose
the eigenvalue decomposition (Ghojogh et al., 2019a) of
the matrix W is W = AΛA(cid:62) where A ∈ Rp×p and
Λ := diag([λ1, . . . , λp](cid:62)) contain the eigenvectors and
eigenvalues of W , respectively. Eq. (4) is restated as:

ht = tanh(AΛA(cid:62)ht−1 + U xt + bi).

(25)

If a change ε in some element of the state ht−1 is aligned
with an eigenvector of the weight matrix W , then the ef-
fect of this change in ht will be (λt ε) after t time steps,
according to Eq. (25). Two cases may happen:

• If the largest eigenvalue is less than one, i.e., λ < 1,
then the change (λt ε) is contrastive because λt (cid:28) 1
for long-term dependencies. In this case, gradient van-
ishing occurs in long-term dependency and the net-
work forgets very long time ago.

• If the largest eigenvalue is less than one, i.e., λ > 1,
then the change (λt ε) is diverging because λt (cid:29) 1

5

for long-term dependencies. In this case, the gradient
network forgets very long time ago. In this case, gra-
dient explosion occurs in long-term dependency and
remembering very long time ago dominates the short-
term memories.

As remembering short-term memories is usually more im-
portant than remembering very past time in different tasks,
it is recommended to use the weight matrix W whose
largest eigenvalue is less than one; this makes the RNN
have the Markovian property because it forgets very past
after some point. However, if the largest eigenvalue of W
is much less than one, i.e., λ (cid:28) 1, gradient vanishing hap-
pens very sooner than expected. Therefore, it is recom-
mended to use the weight matrix W whose largest eigen-
value is slightly less than one, i.e., λ (cid:46) 1. This makes the
RNN slightly contrastive. One way to have the weight ma-
trix W whose largest eigenvalue is slightly less than one is
to make this matrix close to the identity matrix (Mikolov
et al., 2015).
There exist some other ways to determine the weight ma-
trix W . For example, the wight matrix can be set to be
an orthogonal matrix (Arjovsky et al., 2016). Another ap-
proach is to copy the previous state exactly to the current
state. In this approach, the Eq. (4) is modiﬁed to (Hu et al.,
2018):

ht = tanh(W ht−1 + ht−1 + U xt + bi)
(cid:1),
= tanh (cid:0)(W + I)ht−1 + U xt + bi

(26)

where I is the identity matrix. This prevents gradient van-
ishing because it brings a copy of the previous step to the
current state. This can also be interpreted as strengthening
the diagonal of the weight matrix W ; hence, increasing the
largest eigenvalue of W for preventing gradient vanishing.

3.2. Long Delays
As Eq.
(4) and Fig. 1-c show, in the regular RNN, ev-
ery state ht is fed by its previous state ht−1 through the
weight matrix W . As discussed in Section 3.1, in the reg-
ular RNN, the effect of the change ε in a state results in
(λt ε) after t time steps, where λ is the largest eigenvalue
of W .
As shown in Fig. 1-c, the regular RNN has one-step con-
nections or delays between the states. It is possible to have
longer delays between the states in addition to the one-step
delays (Lin et al., 1995). In other words, it is possible to
have higher levels of Markov property in the network. Let
W k denote the weight matrix for k-step delays between
the states. Then, Eq. (4) can be modiﬁed to:

ht = tanh

(cid:16) (cid:88)

k

W kht−k + U xt + bi

(cid:17)

,

(27)

where the summation is over the k values for the existing

6

Figure 2. The (a) folded and (b) unfolded structures of an RNN
with long delays. Every square on an edge means connection from
one time slot before.

delays in the RNN structure. An example for an RNN net-
work with one-step and three-step delays is:

ht = tanh

(cid:16)

W 1ht−1 + W 3ht−3 + U xt + bi

(cid:17)

,

which is illustrated in Fig. 2.
Having long delays in RNN is one of the attempts for pre-
venting gradient vanishing (Lin et al., 1995). This is jus-
tiﬁed because every state is having impact not only from
the previous state but also from the more previous states.
Therefore, in backpropagation through time, there is some
skip in gradient ﬂow from a state to more previous states
without the need to go through the middle states in the
chain rule.

3.3. Leaky Units
Another way to resolve the problem of gradient vanish-
ing is leaky units (Jaeger et al., 2007; Sutskever & Hin-
ton, 2010). Let ht,j denote the j-th element of the state
ht ∈ [−1, 1]p. In leaky units, Eq. (4) is modiﬁed to the
following element-wise equation:

ht,j = (1 −

1
τj

) ht−1,j

+

1
τj

tanh(W j:ht−1 + U j:xt + bi,j),

(28)

where 1 ≤ τj < ∞ and W j: is the j-th row of W and
U j: is the j-th row of U and bi,j is the j-th element of bi.
When τi = 1, then Eq. (28) becomes:

ht,j =

1
τj

tanh(W j:ht−1 + U j:xt + bi,j),

which gives back Eq. (4) in the regular RNN. However,
when τi (cid:29) 1, then Eq. (28) becomes:

ht,j = ht−1,j,

which means that the previous state is copied to the current
state. The larger the τi, the easier the gradient propagates
for ht,i. Therefore, by tuning τi, it is possible to control
how much of the past should be directly copied and how

Figure 3. The echo state network.

much should be passed through the weight matrix. This can
control the amount of gradient vanishing. Note that leaky
units use different τi’s because there may be a need to keep
some of the directions of states (with τi = 1) or forget some
of the directions (with τi (cid:29) 1). In other words, it decides
about the p directions of states separately.

3.4. Echo State Networks
One of the approaches to handle the problem of gradient
vanishing in RNN is to use echo state networks (Jaeger
& Haas, 2004; Jaeger, 2007). These networks consider
the recurrent neural network as a black box having hidden
units with nonlinear activation functions and connections
between them. This black box of recurrent connections is
called the reservoir dynamical system which models the in-
ternal structure of a computer or brain. The connections in
the reservoir system are usually sparse and the weights of
these connections are considered to be ﬁxed. The output
of the reservoir system is connected to an additional linear
output layer whose weights are learnable. The echo state
network minimizes the mean squared error in the output
layer; hence, it performs linear regression in the last layer
(Jaeger & Haas, 2004). This network is shown in Fig. 3.
Because of not learning the recurrent weights in the reser-
voir system and sufﬁcing to learn the weights of the output
layer, the echo state network does not face the gradient van-
ishing problem. A tutorial on this topic is (Jaeger, 2002).

3.5. Other methods
There exist some other methods for not having gradient
vanishing in recurrent networks. For example, hierarchi-
cal RNN (Hihi & Bengio, 1995) and deep RNN (Graves,
2013) have been proposed which stack several recurrent
networks. Another related category of networks is the time-
delay neural networks (Lang et al., 1990; Peddinti et al.,
2015) which are used for shift-invariant sequence process-
ing, especially used in speech recognition (Sugiyama et al.,
1991).
In these networks, every neuron in a layer re-
ceives a contextual window of the neurons in the previous
layer as well as their delayed outputs in several time slots
ago. Moreover, these networks apply backpropagation on
several copies of the network shifted across the sequence

(time) so that the network becomes time-invariant.

4. Long Short-Term Memory Network
As the examples in Section 1 showed, we need short-term
relations in some cases and long-term relations in some
other cases. RNN learns the sequence based on one or sev-
eral previous states, depending on its structure and the level
of its Markov property (see Fig. 2). Therefore, we need to
decide on the structure of RNN to be able to handle short-
term or long-term dependencies in the sequence. Instead
of manual design of the RNN structure or deciding manu-
ally when to clear the state, we can let the neural network
learn by itself when to clear the state based on its input se-
quence. Long Short-Term Memory (LSTM), initially pro-
posed in (Hochreiter & Schmidhuber, 1995; 1997), is able
to do this; it learns from its input sequence when to use
short-term dependency (i.e., when to clear the state) and
when to use the long-term memory (i.e., when not to clear
the state).

4.1. LSTM Gates and Cells
LSTM consists of several cells, each of which corresponds
to a time slot (see Fig. 4). Every LSTM cell contains sev-
eral gates for learning different aspects of the input time
series (see Fig. 5). These gates are introduced in the fol-
lowing.

4.1.1. THE INPUT GATE
One of the gates in the LSTM cell is the input gate, ﬁrst
proposed in (Hochreiter & Schmidhuber, 1995; 1997). This
gate takes the input at the current time slot, xt ∈ Rd, and
the hidden state of the last time slot, ht−1 ∈ [−1, 1]p, and
outputs the signal it ∈ [0, 1]p:

it = sig(cid:0)W i ht−1 + U i xt + (pi (cid:12) ct−1) + bi

(cid:1),

(29)
where W i ∈ Rp×p, U i ∈ Rp×d, and the bias bi ∈ Rp
are the learnable weights for the input gate, (cid:12) denotes the
Hadamard (element-wise) product, ct−1 ∈ Rp is the ﬁ-
nal memory of the last time slot (which will be explained
in Section 4.1.5), and pi ∈ Rp is the learnable peephole
weight (Gers & Schmidhuber, 2000) letting a possible leak
of information from the previous ﬁnal memory. The func-
tion sig(.) ∈ (0, 1) is the sigmoid function which is applied
element-wise:

sig(x) =

1
1 + exp(−x)

.

(30)

7

4.1.2. THE FORGET GATE
Another gate in the LSTM cell is the forget gate, ﬁrst pro-
posed in (Gers et al., 2000). This gate also takes the input
at the current time slot, xt ∈ Rd, and the hidden state of
the last time slot, ht−1 ∈ [−1, 1]p, and outputs the signal
f t ∈ [0, 1]p:
f t = sig(cid:0)W f ht−1 + U f xt + (pf (cid:12) ct−1) + bf

(cid:1),

(31)
where W f ∈ Rp×p, U f ∈ Rp×d, and the bias bf ∈ Rp are
the learnable weights for the forget gate, and pf ∈ Rp is
the learnable peephole weight (Gers & Schmidhuber, 2000)
letting a possible leak of information from the previous ﬁ-
nal memory.
As Eq. (31) shows, the forget gate considers the effect of
the input and the previous hidden state, and perhaps a leak
of information from the previous memory. This gate con-
trols the amount of forgetting the previous information with
respect to the new-coming information. the forget gate is
illustrated in Fig. 5.

4.1.3. THE OUTPUT GATE
The next gate in the LSTM cell is the output gate ﬁrst pro-
posed in (Hochreiter & Schmidhuber, 1995; 1997). This
gate also takes the input at the current time slot, xt ∈ Rd,
and the hidden state of the last time slot, ht−1 ∈ [−1, 1]p,
and outputs the signal ot ∈ [0, 1]p:
ot = sig(cid:0)W o ht−1 + U o xt + (po (cid:12) ct) + bo

(32)

(cid:1),

where W o ∈ Rp×p, U o ∈ Rp×d, and the bias bo ∈ Rp are
the learnable weights for the output gate, and po ∈ Rp is
the learnable peephole weight (Gers & Schmidhuber, 2000)
letting a possible leak of information from the current ﬁnal
memory.
As shown in Eq. (32), the output gate considers the effect
of the input and the previous hidden state, and a possible
information leak from the current memory. The putput gate
is shown in Fig. 5.

4.1.4. THE NEW MEMORY CELL (BLOCK INPUT)
The LSTM cell includes a gate named the new memory cell.
This gate takes the input at the current time slot, xt ∈ Rd,
and the hidden state of the last time slot, ht−1 ∈ [−1, 1]p,
and outputs the signal (cid:101)ct ∈ [−1, 1]p. This gate considers
the effect of the input and the previous hidden state to rep-
resent the new information of current input. It is formulated
as:

As Eq. (29) demonstrates, the input gate considers the ef-
fect of the input and the previous hidden state.
It may
also use a leak of information from the previous memory
through the peephole. This gate carries the importance of
the information of the input at the current time slot. The
input gate is depicted in Fig. 5.

(cid:101)ct = tanh(W c ht−1 + U c xt + bc),
where W c ∈ Rp×p, U c ∈ Rp×d, and the bias bc are the
learnable weights for the new memory cell. The new mem-
ory cell is also referred to as the block input in the literature
(Greff et al., 2016). The signal (cid:101)ct is sometimes denoted by

(33)

8

Figure 4. A sequence of LSTM cells processing the input sequence.

Figure 5. The conveyor belt in the LSTM cell.

zt in the literature. The new memory cell is illustrated in
Fig. 5.

4.1.5. THE FINAL MEMORY CALCULATION
After computation of the outputs of the input gate it, the
forget gate f t, and the new memory cell (cid:101)ct, we calculate
the ﬁnal memory ct ∈ Rp:

(34)

ct = (f t (cid:12) ct−1) + (it (cid:12) (cid:101)ct),
where ct−1 ∈ Rp is the ﬁnal memory of the previous time
slot.
As Eq. (34) demonstrates, the ﬁnal memory considers the
effect of the forget gate, the previous memory, the input,
and the new memory. In the ﬁrst term, i.e., f t (cid:12) ct−1, the
forget gate f t ∈ [0, 1]p controls how much of the previous
memory ct−1 should be forgotten. The closer the f t is to
zero, the more the network forgets the previous memory

ct−1. In the second term, i.e., it (cid:12) (cid:101)ct, the input gate it ∈
[0, 1]p and the new memory cell (cid:101)ct ∈ [−1, 1]p both control
how much of the new input information should be used.
The closer the input gate it is to one and the closer the new
memory cell (cid:101)ct is to ±1, the more the input information is
used.
In other words, the ﬁrst and second terms in Eq. (34) deter-
mine the trade-off of usage of old versus new information
in the sequence. The weights of these gates are trained in
a way that they pass or block the input/previous informa-
tion based on the input sequence and the time step in the
sequence. The ﬁnal memory calculation is depicted in Fig.
5.

4.1.6. THE HIDDEN STATE (BLOCK OUTPUT)
After computation of the output of the output gate ot and
the ﬁnal memory ct, we calculate the hidden state ht ∈

[−1, 1]p:

ht = ot (cid:12) tanh(ct).

(35)

This hidden state is also considered as the block output of
the LSTM cell, depicted in Fig. 5.

4.1.7. THE OUTPUT
The output yt ∈ Rq of the LSTM cell is as follows:

(36)

yt = V ht + by,
where V ∈ Rq×p and the bias by ∈ Rq are the learnable
weights for the output. It is possible to use an activation
function, such as Eq. (6), after this output signal. Figure 5
shows the output signal in the LSTM cell.
Note that in the literature, the output is sometimes consid-
ered to be equal to the hidden state, i.e., yt = ht, by setting
V = I (the identity matrix) and by = 0 (the zero vector).

4.2. History and Variants of LSTM
LSTM has gone through various developments and im-
provements gradually (Greff et al., 2016). Some of the vari-
ants of LSTM do not have the peepholes. In this case, the
Eqs. (29), (31), and (32) are simpliﬁed to:

it = sig(cid:0)W i ht−1 + U i xt + bi
(cid:1),
(cid:1),
f t = sig(cid:0)W f ht−1 + U f xt + bf
(cid:1),
ot = sig(cid:0)W o ht−1 + U o xt + bo

(37)

(38)

(39)

respectively. In the following, we review a history of vari-
ants of the LSTM networks.

4.2.1. ORIGINAL LSTM
LSTM was originally proposed by Hochreiter and Schmid-
huber in years 1995 to 1997 (Hochreiter & Schmidhuber,
1995; 1997). We call it the original LSTM (Hochreiter &
Schmidhuber, 1997). The original LSTM had only the in-
put and output gates, introduced in Sections 4.1.1 and 4.1.3,
and it did not have a forget gate. It also did not contain
the peepholes; therefore, its gates were Eqs. (37) and (39).
The original LSTM trained the network using BPTT (intro-
duced in Section 2.3) and a mixture of real-time recurrent
learning (Robinson & Fallside, 1987; Williams, 1989).

4.2.2. VANILLA LSTM
Later, Gers et. al. (Gers et al., 2000; Gers & Schmidhuber,
2000) applied some changes to the original LSTM. The for-
get gate, introduced in Section 4.1.2, was proposed for the
ﬁrst time in (Gers et al., 2000) to let the network forget its
previous states either completely or partially. The peephole
connections, introduced in Sections 4.1.1, 4.1.2, and 4.1.3,
were ﬁrst proposed in (Gers & Schmidhuber, 2000). The
peepholes let a possible leak of information from the previ-
ous or current ﬁnal memory. This lets the memory control
the gates.

9

These two papers (Gers et al., 2000; Gers & Schmidhuber,
2000) also incorporated the full gate recurrence, in which
all gates receive additional recurrent inputs from all gates
at the previous time step. In full gate recurrence, the Eqs.
(29), (31), and (32) become:

it = sig(cid:0)W i ht−1 + U i xt + (pi (cid:12) ct−1) + bi
(cid:1).

+ Rii it−1 + Rif f t−1 + Rio ot−1

(40)

f t = sig(cid:0)W f ht−1 + U f xt + (pf (cid:12) ct−1) + bf
(cid:1).

+ Rf i it−1 + Rf f f t−1 + Rf o ot−1

(41)

ot = sig(cid:0)W o ht−1 + U o xt + (po (cid:12) ct) + bo
+ Roi it−1 + Rof f t−1 + Roo ot−1

(cid:1),

(42)

where Rii, Rif , Rio, Rf i, Rf f , Rf o, Roi, Rof , Roo ∈
Rp×p are the learnable recurrent weights. Note that the full
gate recurrence often disappeared in later papers on LSTM.
Later, Graves and Schmidhuber adapted the original LSTM
and proposed the vanilla LSTM in 2005 (Graves & Schmid-
huber, 2005a), which is one of the most common LSTMs
in the literature. The vanilla LSTM incorporated the struc-
tures of the original LSTM (Hochreiter & Schmidhuber,
1997) and the papers (Gers et al., 2000; Gers & Schmidhu-
ber, 2000). The full BPTT, introduced in Section 2.3, was
used for LSTM in the vanilla LSTM (Graves & Schmidhu-
ber, 2005a).

4.2.3. OTHER LSTM VARIANTS
There are other variants of LSTM (Greff et al., 2016;
Jozefowicz et al., 2015); although,
the most common
used LSTM is the vanilla LSTM (Graves & Schmidhuber,
2005a). BPTT was used for LSTM training in (Graves &
Schmidhuber, 2005a); however, Kalman ﬁltering was used
for its training (Gers et al., 2002) before that. Another train-
ing method for LSTM was evolutionary learning (Schmid-
huber et al., 2007). Context-sensitive evolutionary learning
was also used for LSTM training (Bayer et al., 2009).
Later works tried to improve the performance of LSTM.
For example, Sak et. al. added a linear layer which projects
the output of the LSTM to smaller number of parameters
before the recurrent connections (Sak et al., 2014). Doetsch
et. al. converted the slope of activation functions of the
LSTM gates to learnable parameters for performance im-
provement (Doetsch et al., 2014). Dynamic cortex memory
was another LSTM variant which added connections be-
tween the gates within every LSTM cell (Otte et al., 2014).
Finally in 2014, one the biggest improvements of LSTM
was proposed, which was named the Gated Recurrent Units
(GRU) (Cho et al., 2014). The philosophy of GRU was to
simplify the LSTM cell because we may no need to have a
very complicated cell to learn the sequence information. In

10

Figure 6. The conveyor belt in the GRU cell (the fully gated unit).

other words, GRU raised the question of whether we need
to be that ﬂexible like LSTM to learn the sequence. GRU is
less ﬂexible than LSTM but it is good enough for sequence
learning.
GRU redesigned the LSTM cell by introducing reset gate,
update gate, and new memory cell; therefore, the number
of gates were reduced from four to three. It was empiri-
cally shown in (Chung et al., 2014) that the performance
of LSTM improves by using GRU cells. Later in 2017, the
GRU was further simpliﬁed by merging the reset and up-
date gates into a forget gate (Heck & Salem, 2017). Nowa-
days, GRU is the most commonly used LSTM structure.
Section 4.3 introduces the details of the GRU cell.

4.3. Gated Recurrent Units (GRU)
GRU was ﬁrst proposed in (Cho et al., 2014). As was men-
tioned in Section 4.2.3, GRU simpliﬁed the LSTM cell in
order to make the ﬂexibility of LSTM.

4.3.1. FULLY GATED UNIT
The main GRU was the fully gated unit (Cho et al., 2014),
whose gates are introduced in the following. Its gates are
illustrated in Fig. 6.

– The Reset Gate: One of the gates in the GRU cell is
the reset gate. This gate takes the input at the current time
slot, xt ∈ Rd, and the hidden state of the last time slot,
ht−1 ∈ [−1, 1]p, and outputs the signal rt ∈ [0, 1]p:

rt = sig(W r ht−1 + U r xt + br),

(43)

where W r ∈ Rp×p, U r ∈ Rp×d, and the bias br ∈ Rp
are the learnable weights for the reset gate. The reset gate
considers the effect of the input and the previous hidden
state, and it controls the amount of forgetting/resetting the
previous information with respect to the new-coming in-
formation. Comparing Eqs. (38) and (43) shows that the
reset gate in the GRU cell is similar to the forget gate in the
LSTM cell. The reset gate is depicted in Fig. 6.

– The Update Gate: Another gate in the GRU cell is the
update gate. This gate also takes the input at the current
time slot, xt ∈ Rd, and the hidden state of the last time
slot, ht−1 ∈ [−1, 1]p, and outputs the signal zt ∈ [0, 1]p:

zt = sig(W z ht−1 + U z xt + bz),

(44)

where W z ∈ Rp×p, U z ∈ Rp×d, and the bias bz ∈ Rp
are the learnable weights for the update gate. The update
gate considers the effect of the input and the previous hid-
den state, and it controls the amount of using the new in-
put data for updating the cell by the coming information of
sequence. Comparing Eqs. (37) and (44) shows that the
update gate in the GRU cell is similar to the input gate in
the LSTM cell. Figure 6 shows the update gate in the GRU
cell.

– The New Memory Cell: The GRU cell includes a gate
named the new memory cell. This gate takes the input at
the current time slot, xt ∈ Rd, and the hidden state of
the last time slot, ht−1 ∈ [−1, 1]p, and outputs the signal

(cid:101)ht ∈ [−1, 1]p:
(cid:16)

(cid:101)ht = tanh

W c

(cid:0)rt (cid:12) ht−1)(cid:1) + U c xt + bc

(cid:17)

,

(45)

where W c ∈ Rp×p, U c ∈ Rp×d, and the bias bc are the
learnable weights for the new memory cell. This gate con-
siders the effect of the input and the previous hidden state to
represent the new information of current input. Comparing
Eqs. (33) and (45) shows that the new memory cell in the
GRU cell is similar to the new memory cell in the LSTM
cell. Note that, in the LSTM cell, the hidden state (see Eq.
(35)) and the new memory cell (see Eq.
(33)) were dif-
ferent; however, the hidden state of the GRU cell (see Eq.
(45)) replaces the new memory signal in the LSTM cell.
The new memory cell is shown in Fig. 6.

– The Final Memory (Hidden State): After computation
of the outputs of the update gate zt and the new memory
cell (cid:101)ht, we calculate the ﬁnal memory or the hidden state
ht ∈ Rp:

(cid:1) + (zt (cid:12) (cid:101)ht),

ht = (cid:0)(1 − zt) (cid:12) ht−1

(46)
where ht−1 ∈ Rp is the hidden state of the previous time
slot. The ﬁnal memory block is illustrated in Fig. 6.
As Eq. (46) demonstrates, the ﬁnal memory considers the
effect of the update gate, the previous memory, and the new
memory. In the ﬁrst term, i.e., (1 − zt) (cid:12) ht−1, the update
gate zt ∈ [0, 1]p controls how much of the previous state
ht−1 should be used based on the input data. The closer
the zt is to one (resp. zero), the more the network forgets
(resp. considers) the previous state ht−1. In the second
term, i.e., zt (cid:12) (cid:101)ht, the update gate zt ∈ [0, 1]p and the new
memory cell (cid:101)ht ∈ [−1, 1]p both control how much of the
new input information should be used. In other words, it
controls how much the information should be updated by
the new information. The closer the update gate zt is to
one and the closer the new memory cell (cid:101)ht is to ±1, the
more the input information is used.
Overall, the ﬁrst and second terms in Eq. (46) determine
the trade-off of usage of old versus new information in the
sequence. The weights of these gates are trained in a way
that they pass or block the input/previous information based
on the input sequence and the time step in the sequence.
Comparing Eqs. (34) and (46) shows that the ﬁnal memory
in the GRU cell is in the form of the ﬁnal memory in the
LSTM cell; however, they have somewhat different func-
tionality.

4.3.2. MINIMAL GATED UNIT
Minimal gated unit (Heck & Salem, 2017) is another vari-
ant of GRU which has simpliﬁed the gate by merging the
reset and update gates into a forget gate. This merging is
possible because the forget gate can control both the previ-
ous and new information of the sequence.

11

– The Forget Gate: The forget gate takes the input at the
current time slot, xt ∈ Rd, and the hidden state of the last
time slot, ht−1 ∈ [−1, 1]p, and outputs the signal rt ∈
[0, 1]p:

f t = sig(W f ht−1 + U f xt + bf ),

(47)

where W f ∈ Rp×p, U f ∈ Rp×d, and the bias bf ∈ Rp are
the learnable weights for the forget gate. The forget gate
considers the effect of the input and the previous hidden
state, and it controls the amount of forgetting the previous
information with respect to the new-coming information.
Therefore, it controls both forgetting or using the previous
memory and using the new coming information.

– The New Memory Cell and the Final Memory: Be-
cause the forget gate replaces the reset and the update gate
in the minimal gate unit, Eqs. (45) and (46) are changed to:

(cid:16)

W c

(cid:101)ht = tanh
ht = (cid:0)(1 − f t) (cid:12) ht−1

(cid:0)f t (cid:12) ht−1)(cid:1) + U c xt + bc
(cid:1) + (f t (cid:12) (cid:101)ht),

(cid:17)
,

(48)

(49)

respectively, to be the new memory cell and the ﬁnal mem-
ory in the minimal gate unit.

5. Bidirectional RNN and LSTM
5.1. Justiﬁcation of Bidirectional Processing
A bidirectional RNN or LSTM network processes the se-
quence in both directions; left to right and right to left. In
the ﬁrst glance, online causal tasks such as reading a text
or listening to a speech do not have access to the future.
Therefore, bidirectional networks seem to violate causality
in them. However, in many of these tasks, it is possible
to wait for the completion of a part of the sequence such
as a sentence and then decide about it. For example, it is
normal to wait for the completion of sentence in speech
recognition and then recognize it (Graves & Schmidhuber,
2005a;b). In text processing, the text is usually available
except in a streaming text. Even in streaming text, it is
possible to wait for a sentence to complete. Therefore, it
makes sense to use bidirectional networks for processing
sequences because, sometimes, the important related word
comes after a word and not necessarily before it. An exam-
ple for such a case is the sentence “The police is chasing
the thief” where the word “thief” is a strongly related (op-
posite) word for the word “police”. In this sentence, both
the words “thief” and “police” are related and it is worth to
process the sentence in both directions.

5.2. Bidirectional RNN
The bidirectional RNN was ﬁrst proposed in (Schuster &
Paliwal, 1997) and further exploited in (Baldi et al., 1999).
It uses two sets of states each for one of the directions in

12

Figure 8. The bidirectional LSTM.

has shown its merit (Graves et al., 2005). Another example
is the hybrid of bidirectional LSTM and Conditional Ran-
dom Fields (CRF) (Lafferty et al., 2001) for the sequence
tagging task (Huang et al., 2015). Other extensions of bidi-
rectional LSTM networks exist such as (Peters et al., 2017).

5.4. Embeddings from Language Model (ELMo)
The Embeddings from Language Model (ELMo) network,
ﬁrst proposed in (Peters et al., 2018), is a language model
which makes use of bidirectional LSTM networks. It is one
of the successful context-aware language modeling net-
works.
It has been widely used in various applications
such as in medical interview processing (Sarzynska-Wawer
et al., 2021).
The structure of ELMo is illustrated in Fig. 9. As shown in
this ﬁgure, ELMo contains L layers of bidirectional LSTM
networks where the output of each bidirectional LSTM is
fed to the next bidirectional LSTM. in The bidirectional
LSTM networks of ELMo, V = I is set so that the outputs
y becomes equal to the hidden states h. At time slot t and
layer l, the outputs (or hidden states) of the two directions
of LSTM are concatenated together to make h(l)
t

:

h(l)
t

:= [

−→
h (l)(cid:62)
t

←−
h (l)(cid:62)
t

,

](cid:62).

Then, a linear combination of these hidden states of layers
is considered to be the embedding vector of ELMo network
at time t (Peters et al., 2018):

yELMo
t

:= γ

L
(cid:88)

l=1

sl h(l)
t

,

(53)

where γ and {sl}L
l=1 are the hyperparameter scalar weights
which are determined according to the speciﬁc task (e.g.,

Figure 7. The bidirectional RNN.

the sequence. Let the states for left-to-right and right-to-
←−
h t, respectively. In
left processing be denoted by
the bidirectional RNN, Eq. (4) is replaced by two equations
(Graves et al., 2013):

−→
h t and

−→
h t = tanh(
←−
h t = tanh(

−→
W
←−
W

−→
h t−1 +
←−
h t+1 +

−→
U xt +
←−
U xt +

−→
b i),
←−
b i),

and Eq. (5) is replaced by:

−→
V

−→
h t +

←−
V

←−
h t + by,

yt =

(50)

(51)

(52)

where the arrows show the parameters for each direction of
processing. The unfolding schematic of the bidirectional
RNN is illustrated in Fig. 7. As this ﬁgure shows, the out-
puts of both directions are connected to an output layer.
In some cases, this output layer may be replaced by a third
multi-layer neural network. All weights of the bidirectional
RNN are trained using backpropagation through time simi-
larly to what was explained in Section 2.3. It is noteworthy
that the deep variant of bidirectional RNN has been pro-
posed in (Graves et al., 2013).

5.3. Bidirectional LSTM
Bidirectional LSTM was ﬁrst proposed in (Graves &
Schmidhuber, 2005a;b). As obvious from its name, the
bidirectional LSTM includes two LSTM networks each of
which processes the sequence from one direction. In other
words, there are two LSTM networks which are fed with
the sequence in opposite orders. This structure is depicted
in Fig. 8. Experiments have shown that the bidirectional
LSTM outperforms the unidirectional LSTM (Graves &
Schmidhuber, 2005a; Graves et al., 2005). This is expected
according to the justiﬁcation in Section 5.1. Because of its
advantages, various methods have combined the bidirec-
tional LSTM with other methods. For example, a hybrid of
the bidirectional LSTM and HMM (Ghojogh et al., 2019b)

13

Bengio, Yoshua, Simard, Patrice, and Frasconi, Paolo.
Learning long-term dependencies with gradient descent
is difﬁcult. IEEE transactions on neural networks, 5(2):
157–166, 1994.

Bengio, Yoshua, Boulanger-Lewandowski, Nicolas, and
Pascanu, Razvan. Advances in optimizing recurrent
In 2013 IEEE international conference on
networks.
acoustics, speech and signal processing, pp. 8624–8628.
IEEE, 2013.

Broer, Hendrik Wolter and Takens, Floris. Dynamical sys-

tems and chaos, volume 172. Springer, 2011.

Cho, Kyunghyun, Van Merri¨enboer, Bart, Bahdanau,
Dzmitry, and Bengio, Yoshua. On the properties of neu-
ral machine translation: Encoder-decoder approaches. In
Eighth Workshop on Syntax, Semantics and Structure in
Statistical Translation (SSST-8), 2014.

Chung, Junyoung, Gulcehre, Caglar, Cho, KyungHyun,
and Bengio, Yoshua. Empirical evaluation of gated re-
current neural networks on sequence modeling. arXiv
preprint arXiv:1412.3555, 2014.

Doetsch, Patrick, Kozielski, Michal, and Ney, Hermann.
Fast and robust training of recurrent neural networks for
In 2014 14th interna-
ofﬂine handwriting recognition.
tional conference on frontiers in handwriting recogni-
tion, pp. 279–284. IEEE, 2014.

Gers, Felix A and Schmidhuber, J¨urgen. Recurrent nets
that time and count. In Proceedings of the IEEE-INNS-
ENNS International Joint Conference on Neural Net-
works. IJCNN 2000. Neural Computing: New Chal-
lenges and Perspectives for the New Millennium, vol-
ume 3, pp. 189–194. IEEE, 2000.

Gers, Felix A, Schmidhuber, J¨urgen, and Cummins, Fred.
Learning to forget: Continual prediction with LSTM.
Neural computation, 12(10):2451–2471, 2000.

Gers, Felix A, P´erez-Ortiz, Juan Antonio, Eck, Dou-
glas, and Schmidhuber, J¨urgen. DEKF-LSTM.
In
10th European Symposium on Artiﬁcial Neural Networks
(ESANN), 2002.

Ghojogh, Benyamin, Karray, Fakhri, and Crowley, Mark.
Eigenvalue and generalized eigenvalue problems: Tuto-
rial. arXiv preprint arXiv:1903.11240, 2019a.

Ghojogh, Benyamin, Karray, Fakhri, and Crowley, Mark.
Hidden Markov model: Tutorial. Engineering Archive,
2019b.

Figure 9. The ELMo network.

question answering, translation, etc) in natural language
processing.

6. Conclusion
This was a tutorial paper on RNN, LSTM, and its variants.
We covered dynamical system, backpropagation through
time, LSTM gates and cells, history and variants of LSTM,
the GRU cell, bidirectional RNN, bidirectional LSTM, and
ELMo network.

References
Arjovsky, Martin, Shah, Amar, and Bengio, Yoshua. Uni-
In Interna-
tary evolution recurrent neural networks.
tional conference on machine learning, pp. 1120–1128.
PMLR, 2016.

Baldi, Pierre, Brunak, Søren, Frasconi, Paolo, Soda, Gio-
Exploiting the past
vanni, and Pollastri, Gianluca.
and the future in protein secondary structure prediction.
Bioinformatics, 15(11):937–946, 1999.

Bayer, Justin, Wierstra, Daan, Togelius, Julian, and
Schmidhuber, J¨urgen. Evolving memory cell structures
In International conference on
for sequence learning.
artiﬁcial neural networks, pp. 755–764. Springer, 2009.

Bengio, Yoshua, Frasconi, Paolo, and Simard, Patrice. The
problem of learning long-term dependencies in recurrent
In IEEE international conference on neural
networks.
networks, pp. 1183–1188. IEEE, 1993.

Ghojogh, Benyamin, Ghodsi, Ali, Karray, Fakhri, and
Crowley, Mark. KKT conditions, ﬁrst-order and second-
order optimization, and distributed optimization: Tuto-
rial and survey. arXiv preprint arXiv:2110.01858, 2021.

Graves, Alex. Generating sequences with recurrent neural

networks. arXiv preprint arXiv:1308.0850, 2013.

Graves, Alex and Schmidhuber, J¨urgen.

Framewise
phoneme classiﬁcation with bidirectional LSTM and
other neural network architectures. Neural networks, 18
(5-6):602–610, 2005a.

Graves, Alex and Schmidhuber, J¨urgen.

Framewise
phoneme classiﬁcation with bidirectional lstm networks.
In Proceedings. 2005 IEEE International Joint Confer-
ence on Neural Networks, 2005., volume 4, pp. 2047–
2052. IEEE, 2005b.

Graves, Alex, Fern´andez, Santiago, and Schmidhuber,
J¨urgen. Bidirectional LSTM networks for improved
phoneme classiﬁcation and recognition. In International
conference on artiﬁcial neural networks, pp. 799–804.
Springer, 2005.

Graves, Alex, Mohamed, Abdel-rahman, and Hinton, Ge-
offrey. Speech recognition with deep recurrent neural
In 2013 IEEE international conference on
networks.
acoustics, speech and signal processing, pp. 6645–6649.
IEEE, 2013.

14

Hu, Yuhuang, Huber, Adrian, Anumula, Jithendar, and
Liu, Shih-Chii. Overcoming the vanishing gradient
arXiv preprint
problem in plain recurrent networks.
arXiv:1801.06105, 2018.

Huang, Zhiheng, Xu, Wei, and Yu, Kai.

Bidirec-
tional LSTM-CRF models for sequence tagging. arXiv
preprint arXiv:1508.01991, 2015.

Jaeger, Herbert. Tutorial on training recurrent neural net-
works, covering BPPT, RTRL, EKF and the ”echo state
network” approach. 2002.

Jaeger, Herbert. Echo state network. Scholarpedia, 2(9):

2330, 2007.

Jaeger, Herbert and Haas, Harald. Harnessing nonlinearity:
Predicting chaotic systems and saving energy in wireless
communication. Science, 304(5667):78–80, 2004.

Jaeger, Herbert, Lukoˇseviˇcius, Mantas, Popovici, Dan, and
Siewert, Udo. Optimization and applications of echo
state networks with leaky-integrator neurons. Neural
networks, 20(3):335–352, 2007.

Greff, Klaus, Srivastava, Rupesh K, Koutn´ık, Jan, Steune-
brink, Bas R, and Schmidhuber, J¨urgen. LSTM: A search
IEEE transactions on neural networks
space odyssey.
and learning systems, 28(10):2222–2232, 2016.

Jozefowicz, Rafal, Zaremba, Wojciech, and Sutskever,
Ilya. An empirical exploration of recurrent network
In International conference on machine
architectures.
learning, pp. 2342–2350. PMLR, 2015.

Heck, Joel C and Salem, Fathi M. Simpliﬁed minimal
In
gated unit variations for recurrent neural networks.
2017 IEEE 60th International Midwest Symposium on
Circuits and Systems (MWSCAS), pp. 1593–1596. IEEE,
2017.

Hihi, Salah and Bengio, Yoshua. Hierarchical recurrent
neural networks for long-term dependencies. Advances
in neural information processing systems, 8, 1995.

Hochreiter, Sepp. The vanishing gradient problem dur-
ing learning recurrent neural nets and problem solu-
International Journal of Uncertainty, Fuzziness
tions.
and Knowledge-Based Systems, 6(02):107–116, 1998.

Hochreiter, Sepp and Schmidhuber, J¨urgen. Long short-
term memory. Technical report, FKI-207-95, Depart-
ment of Fakult¨at f¨ur Informatik, Technical University of
Munich, Munich, Germany, 1995.

Hochreiter, Sepp and Schmidhuber, J¨urgen. Long short-
term memory. Neural computation, 9(8):1735–1780,
1997.

Hochreiter, Sepp, Bengio, Yoshua, Frasconi, Paolo,
Schmidhuber, J¨urgen, et al. Gradient ﬂow in recurrent
nets: the difﬁculty of learning long-term dependencies,
2001.

Lafferty, John, McCallum, Andrew, and Pereira, Fer-
nando CN. Conditional random ﬁelds: Probabilis-
tic models for segmenting and labeling sequence data.
2001.

Lang, Kevin J, Waibel, Alex H, and Hinton, Geoffrey E. A
time-delay neural network architecture for isolated word
recognition. Neural networks, 3(1):23–43, 1990.

Lin, Tsungnan, Horne, Bill G., Tino, Peter, and Giles,
C. Lee. Learning long-term dependencies is not as dif-
ﬁcult with narx recurrent neural networks. Advances in
neural information processing systems, 1995.

Lipton, Zachary C, Berkowitz, John, and Elkan, Charles. A
critical review of recurrent neural networks for sequence
learning. arXiv preprint arXiv:1506.00019, 2015.

Mikolov, Tomas, Joulin, Armand, Chopra, Sumit, Mathieu,
Michael, and Ranzato, Marc’Aurelio. Learning longer
memory in recurrent neural networks. Workshop at the
International Conference on Learning Representations,
2015.

Mozer, Michael C. A focused backpropagation algorithm
for temporal pattern recognition. Backpropagation: The-
ory, architectures, and applications, 137, 1995.

15

Smagulova, Kamilya and James, Alex Pappachen. A sur-
vey on LSTM memristive neural network architectures
and applications. The European Physical Journal Spe-
cial Topics, 228(10):2313–2324, 2019.

Staudemeyer, Ralf C and Morris, Eric Rothstein. Un-
into long short-term
arXiv preprint

derstanding LSTM–a tutorial
memory recurrent neural networks.
arXiv:1909.09586, 2019.

Sugiyama, Masahide, Sawai, Hidehumi, and Waibel,
Alexander H. Review of tdnn (time delay neural net-
In 1991
work) architectures for speech recognition.
IEEE International Symposium on Circuits and Systems
(ISCAS), pp. 582–585. IEEE, 1991.

Sutskever, Ilya and Hinton, Geoffrey. Temporal-kernel re-
current neural networks. Neural Networks, 23(2):239–
243, 2010.

Werbos, Paul J. Generalization of backpropagation with
application to a recurrent gas market model. Neural net-
works, 1(4):339–356, 1988.

Williams, Ronald J. Complexity of exact gradient computa-
tion algorithms for recurrent neural networks. Technical
report, NU-CCS-89-27, Northeastern University, 1989.

Williams, Ronald J and Zipser, David. Gradient-based
learning algorithms for recurrent networks and their
computational complexity. Backpropagation: Theory,
architectures, and applications, 433:17, 1995.

Yu, Yong, Si, Xiaosheng, Hu, Changhua, and Zhang,
Jianxun. A review of recurrent neural networks: LSTM
cells and network architectures. Neural computation, 31
(7):1235–1270, 2019.

Otte, Sebastian, Liwicki, Marcus, and Zell, Andreas. Dy-
namic cortex memory: Enhancing recurrent neural net-
In Inter-
works for gradient-based sequence learning.
national Conference on Artiﬁcial Neural Networks, pp.
1–8. Springer, 2014.

Peddinti, Vijayaditya, Povey, Daniel, and Khudanpur, San-
jeev. A time delay neural network architecture for efﬁ-
cient modeling of long temporal contexts. In Sixteenth
annual conference of the international speech communi-
cation association, 2015.

Peters, Matthew E, Ammar, Waleed, Bhagavatula, Chan-
dra, and Power, Russell. Semi-supervised sequence tag-
ging with bidirectional language models. In Association
for Computational Linguistics (ACL), 2017.

Peters, Matthew E., Neumann, Mark, Iyyer, Mohit, Gard-
ner, Matt, Clark, Christopher, Lee, Kenton, and Zettle-
moyer, Luke. Deep contextualized word representations.
In North American Chapter of the Association for Com-
putational Linguistics (NAACL), 2018.

Robinson, AJ and Fallside, Frank. The utility driven
dynamic error propagation network. Technical report,
Department of Engineering, University of Cambridge,
1987.

Rumelhart, David E, Hinton, Geoffrey E, and Williams,
Ronald J. Learning representations by back-propagating
errors. Nature, 323(6088):533–536, 1986.

Sak, Hasim, Senior, Andrew W, and Beaufays, Franc¸oise.
Long short-term memory recurrent neural network archi-
In INTER-
tectures for large scale acoustic modeling.
SPEECH, 2014.

Salehinejad, Hojjat, Sankar, Sharan, Barfett, Joseph,
Recent ad-
arXiv preprint

Colak, Errol, and Valaee, Shahrokh.
vances in recurrent neural networks.
arXiv:1801.01078, 2017.

Sarzynska-Wawer, Justyna, Wawer, Aleksander, Pawlak,
Aleksandra, Szymanowska, Julia, Stefaniak, Izabela,
Jarkiewicz, Michal, and Okruszek, Lukasz. Detect-
ing formal
thought disorder by deep contextualized
word representations. Psychiatry Research, 304:114135,
2021.

Schmidhuber, J¨urgen. Deep learning in neural networks:

An overview. Neural networks, 61:85–117, 2015.

Schmidhuber, J¨urgen, Wierstra, Daan, Gagliolo, Matteo,
and Gomez, Faustino. Training recurrent networks by
Evolino. Neural computation, 19(3):757–779, 2007.

Schuster, Mike and Paliwal, Kuldip K. Bidirectional re-
IEEE transactions on Signal

current neural networks.
Processing, 45(11):2673–2681, 1997.

