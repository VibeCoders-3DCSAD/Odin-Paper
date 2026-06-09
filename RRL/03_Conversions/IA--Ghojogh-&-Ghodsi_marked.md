Toappearasapartofanupcomingtextbookondeeplearning.
Recurrent Neural Networks and Long Short-Term Memory Networks:
|                 |     |     |     |     | Tutorial |     | and Survey |     |                         |     |     |     |
| --------------- | --- | --- | --- | --- | -------- | --- | ---------- | --- | ----------------------- | --- | --- | --- |
| BenyaminGhojogh |     |     |     |     |          |     |            |     | BGHOJOGH@UWATERLOO.CA   |     |     |     |
| AliGhodsi       |     |     |     |     |          |     |            |     | ALI.GHODSI@UWATERLOO.CA |     |     |     |
DepartmentofStatisticsandActuarialScience&DavidR.CheritonSchoolofComputerScience,
DataAnalyticsLaboratory,UniversityofWaterloo,Waterloo,ON,Canada
3202 rpA 22  ]GL.sc[  1v16411.4032:viXra
YouTubechannelofBenyaminGhojogh: https://www.youtube.com/@bghojogh
https://www.youtube.com/@DataScienceCoursesUW
YouTubechannelofAliGhodsi:
Abstract
|     |     |     |     |     |     |     | dient vanishing | or explosion | for   | long-term | dependencies      |     |
| --- | --- | --- | --- | --- | --- | --- | --------------- | ------------ | ----- | --------- | ----------------- | --- |
|     |     |     |     |     |     |     | in RNN (Bengio  | et al.,      | 1993; | 1994).    | Several solutions |     |
ThisisatutorialpaperonRecurrentNeuralNet-
|      |        |      |            |        |     |      | were proposed | for this | issue, some | of which | are close-to- |     |
| ---- | ------ | ---- | ---------- | ------ | --- | ---- | ------------- | -------- | ----------- | -------- | ------------- | --- |
| work | (RNN), | Long | Short-Term | Memory |     | Net- |               |          |             |          |               |     |
work(LSTM),andtheirvariants. Westartwitha identity weight matrix (Mikolov et al., 2015), long delays
(Linetal.,1995),leakyunits(Jaegeretal.,2007;Sutskever
| dynamical |     | system | and backpropagation |     | through |     |     |     |     |     |     |     |
| --------- | --- | ------ | ------------------- | --- | ------- | --- | --- | --- | --- | --- | --- | --- |
time for RNN. Then, we discuss the problems &Hinton,2010),andechostatenetworks(Jaeger&Haas,
2004;Jaeger,2007).
| of  | gradient | vanishing |     | and explosion | in  | long- |     |     |     |     |     |     |
| --- | -------- | --------- | --- | ------------- | --- | ----- | --- | --- | --- | --- | --- | --- |
termdependencies. Weexplainclose-to-identity Sequencemodelingrequiresbothshort-termandlong-term
weightmatrix,longdelays,leakyunits,andecho dependencies. For example, consider the sentence “The
state networks for solving this problem. Then, police is chasing the thief”. In this sentence, the words
weintroduceLSTMgatesandcells, historyand “police” and “thief” are related to each other with short-
|          |     |       |     |                 |     |       | term dependency | because | they are | close | to one another | in  |
| -------- | --- | ----- | --- | --------------- | --- | ----- | --------------- | ------- | -------- | ----- | -------------- | --- |
| variants | of  | LSTM, | and | Gated Recurrent |     | Units |                 |         |          |       |                |     |
(GRU).Finally,weintroducebidirectionalRNN, thesequenceofwords. Anotherexampleisthesentence“I
bidirectional LSTM, and the Embeddings from wasborninFrance. Myfatherwasworkingthereformany
Language Model (ELMo) network, for process- years during my childhood. My family had a great time
ingasequenceinbothdirections. there while my father was making money in his business
|     |     |     |     |     |     |     | there. That    | is why I know                     | how | to speak | French”. | In this |
| --- | --- | --- | --- | --- | --- | --- | -------------- | --------------------------------- | --- | -------- | -------- | ------- |
|     |     |     |     |     |     |     | secondexample, | thewords“France”and“French”arere- |     |          |          |         |
1.Introduction latedtoeachotherwithlong-termdependencybecausethey
Before the era of transformers in deep learning, regu- are far away from one another in the sequence of words.
lar neural networks could not process sequences, such ThatinspiredresearcherstoproposetheLongShort-Term
|              |           |     |           |           |           |     | Memory (LSTM) | network | to handle | both | short-term | and |
| ------------ | --------- | --- | --------- | --------- | --------- | --- | ------------- | ------- | --------- | ---- | ---------- | --- |
| as sentences | (sequence |     | of words) | or speech | (sequence | of  |               |         |           |      |            |     |
phonemes), properly without any recurrence. Recurrent long-terndependencies(Hochreiter&Schmidhuber,1995;
|                |     |        |          |               |     |         | 1997). Later, | GratedRecurrentUnit(GRU)wasproposed |     |     |     |     |
| -------------- | --- | ------ | -------- | ------------- | --- | ------- | ------------- | ----------------------------------- | --- | --- | --- | --- |
| Neural Network |     | (RNN), | proposed | in (Rumelhart |     | et al., |               |                                     |     |     |     |     |
(Choetal.,2014)whichsimplifiedLSTMtoreduceitsun-
| 1986), is | a dynamical |     | system | which considers | recurrence. |     |     |     |     |     |     |     |
| --------- | ----------- | --- | ------ | --------------- | ----------- | --- | --- | --- | --- | --- | --- | --- |
In recurrence, the output of a model is fed as input to the necessarycomplexity.
model again in the next time step. One of the main train- RNN and LSTM networks are causal models which con-
ingalgorithmsforRNNisBackpropagationThroughTime dition every sequence element on the previous elements
|     |     |     |     |     |     |     | in the sequence. | Later | researches | showed | that | process- |
| --- | --- | --- | --- | --- | --- | --- | ---------------- | ----- | ---------- | ------ | ---- | -------- |
(BPTT),developedbyseveralworks(Robinson&Fallside,
1987; Werbos, 1988; Williams, 1989; Williams & Zipser, ing the sequence in both directions can perform better for
1995; Mozer, 1995), which is similar to the backpropaga- the sequences which can be processed offline; e.g., if the
tion algorithm (Rumelhart et al., 1986) but has also chain chunks of sequence can be saved and processed and the
rule through time. There were some problems with gra- sequence elements should not be processed as a stream
|     |     |     |     |     |     |     | (Graves & | Schmidhuber, | 2005a;b). | Therefore, |     | bidirec- |
| --- | --- | --- | --- | --- | --- | --- | --------- | ------------ | --------- | ---------- | --- | -------- |
tionalRNN(Schuster&Paliwal,1997;Baldietal.,1999)
andbidirectionalLSTM(Graves&Schmidhuber,2005a;b)

2
wereproposedtoprocesssequencesinbothdirections.The
EmbeddingsfromLanguageModel(ELMo)network(Pe-
| ters et al., | 2018) | is a | language | model | which | makes use of |     |     |     |     |     |     |     |
| ------------ | ----- | ---- | -------- | ----- | ----- | ------------ | --- | --- | --- | --- | --- | --- | --- |
thebidirectionalLSTM.
| ThisisatutorialonRNN,LSTM,andtheirvariants. |       |              |     |                  |       | There         |     |     |     |     |     |     |     |
| ------------------------------------------- | ----- | ------------ | --- | ---------------- | ----- | ------------- | --- | --- | --- | --- | --- | --- | --- |
| exist some                                  | other | tutorials    |     | and surveys      | about | this topic,   |     |     |     |     |     |     |     |
| some of                                     | which | are (Jaeger, |     | 2002; Jozefowicz |       | et al., 2015; |     |     |     |     |     |     |     |
Liptonetal.,2015;Schmidhuber,2015;Greffetal.,2016;
Salehinejadetal.,2017;Staudemeyer&Morris,2019;Yu
| etal.,2019;Smagulova&James,2019). |     |     |     |     | Averygoodsur- |     |     |     |     |     |     |     |     |
| --------------------------------- | --- | --- | --- | --- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- |
veyonthevariantsofLSTMis(Greffetal.,2016).
2.RecurrentNeuralNetwork
2.1.DynamicalSystem
Adynamicalsystemisrecursiveanditsclassicalformisas
follows:
|     |     |     | h =f | (h ), |     | (1) |     |     |     |     |     |     |     |
| --- | --- | --- | ---- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     | t    | θ t−1 |     |     |     |     |     |     |     |     |     |
Figure1.Thefoldedandunfoldedstructuresof(a)adynamicsys-
wheretdenotesthetimestep,h isthestateattimet,and temwithoutinput,(b)adynamicalsystemwithinput,and(c)an
t
RNN.Everysquareonanedgemeansconnectionfromonetime
f (.)isafunctionfixedbetweenthestatesofalltimesteps.
θ
| Figure 1-a | shows | such | a system. | Dynamical |     | systems are | slotbefore. |     |     |     |     |     |     |
| ---------- | ----- | ---- | --------- | --------- | --- | ----------- | ----------- | --- | --- | --- | --- | --- | --- |
widelyusedinchaostheory(Broer&Takens,2011).
∈Rq,respectively.
Wecanhaveadynamicalsystemwithexternalinputsignal andb AsshowninFig. 1-c,wehave:
y
| wherex | t denotestheinputsignalattimet. |     |     |     | Thissystemis |     |     | Rp  |                 |     |         |          |     |
| ------ | ------------------------------- | --- | --- | --- | ------------ | --- | --- | --- | --------------- | --- | ------- | -------- | --- |
|        |                                 |     |     |     |              |     |     |     | (cid:51)i t =Wh |     | t−1 +Ux | t +b i , | (3) |
modeledas:
[−1,1]p
|     |     |     |     |          |     |     |     |     | (cid:51)h | t =tanh(i |     | t )       |             |
| --- | --- | --- | --- | -------- | --- | --- | --- | --- | --------- | --------- | --- | --------- | ----------- |
|     |     | h   | =f  | (h ,x ). |     | (2) |     |     |           | =tanh(Wh  |     | t−1 +Ux t | +b i ), (4) |
|     |     |     | t θ | t−1 t    |     |     |     |     |           |           |     |           |             |
Rq
|     |     |     |     |     |     |     |     |     | (cid:51)y | =Vh | t +b y , |     | (5) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --------- | --- | -------- | --- | --- |
t
| ThissystemisdepictedinFig. |     |     |     | 1-b. |     |     |       |         |     |          |         |                |         |
| -------------------------- | --- | --- | --- | ---- | --- | --- | ----- | ------- | --- | -------- | ------- | -------------- | ------- |
|                            |     |     |     |      |     |     |       | tanh(.) |     | ∈ (−1,1) |         |                |         |
|                            |     |     |     |      |     |     | where |         |     |          | denotes | the hyperbolic | tangent |
2.2.ParameterSharing function,whichisusedasanelement-wiseactivationfunc-
tionforthestates.
| The state | h can | be  | considered | as a summary |     | of the past |     |     |     |     |     |     |     |
| --------- | ----- | --- | ---------- | ------------ | --- | ----------- | --- | --- | --- | --- | --- | --- | --- |
t
|                            |                 |          |          |                       |            |            | If     | there is | an activation |        | function, | such as softmax,     | at the   |
| -------------------------- | --------------- | -------- | -------- | --------------------- | ---------- | ---------- | ------ | -------- | ------------- | ------ | --------- | -------------------- | -------- |
| sequenceofinputsandstates. |                 |          |          | Ifadifferentfunctionf |            | θ is       |        |          |               |        |           |                      |          |
|                            |                 |          |          |                       |            |            | output | layer,   | we            | denote | the       | output of activation | function |
| defined                    | for each        | possible | sequence | length,               | the        | model will |        |          |               |        |           |                      |          |
| not have                   | generalization. |          | If       | the same              | parameters | are used   | by:    |          |               |        |           |                      |          |
for any sequence length, the model will have generaliza- exp(y )
|     |     |     |     |     |     |     |     | Rq  |     |     |     | t,  | 1   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
tion properties. Therefore, the parameters are shared for (cid:51)y (cid:98)t =softmax(y )= (cid:80)q , (6)
|             |     |         |     |              |             |      |     |     |     |     |     | t exp | ( y ) |
| ----------- | --- | ------- | --- | ------------ | ----------- | ---- | --- | --- | --- | --- | --- | ----- | ----- |
|             |     |         |     |              |             |      |     |     |     |     |     | j=1   | t,j   |
| all lengths | and | between | all | states. Such | a dynamical | sys- |     |     |     |     |     |       |       |
temwithparametersharingcanbeimplementedasaneural wherey denotesthej-thcomponentofy .
|     |     |     |     |     |     |     |     | t,j |     |     |     | t   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
networkwithweights.SuchanetworkiscalledaRecurrent
2.3.BackpropagationThroughTime(BPTT)
| Neural Network |     | (RNN), | which | was proposed |     | in (Rumel- |     |     |     |     |     |     |     |
| -------------- | --- | ------ | ----- | ------------ | --- | ---------- | --- | --- | --- | --- | --- | --- | --- |
hartetal.,1986). One of the methods for training RNN is Backpropagation
RNNisillustratedinFig. 1-c,wherethesameweightma- Through Time (BPTT), which is very similar to the back-
trices are used for all time slots. RNN gets a sequence as propagation algorithm (Rumelhart et al., 1986) because it
isbasedongradientdescentandchainrule(Ghojoghetal.,
inputandoutputsasequenceasadecisionforatasksuch
as regression or classification. Suppose the input, output, 2021), but it has also chain rule through time. BPTT was
andstateattimeslottaredenotedbyx ∈ Rd, y ∈ Rq, developed by several works (Robinson & Fallside, 1987;
|     |     |     |     |     | t   | t   |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Rp,respectively. Rp×p Werbos, 1988; Williams, 1989; Williams & Zipser, 1995;
| andh ∈ |     |     |     | LetW ∈ | betheweight |     |     |     |     |     |     |     |     |
| ------ | --- | --- | --- | ------ | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
t
matrix between states, U ∈ Rp×d be the weight matrix Mozer,1995). Thisalgorithmisverysolidintheory;how-
|         |            |     |     |             |     | Rq×p   | ever,itdoesnotshowthebestperformanceinpractice. |     |     |     |     |     |     |
| ------- | ---------- | --- | --- | ----------- | --- | ------ | ----------------------------------------------- | --- | --- | --- | --- | --- | --- |
| between | the inputs | and | the | states, and | V ∈ | denote |                                                 |     |     |     |     |     |     |
theweightmatrixbetweenthestatesandoutputs. Thebias In BPTT, the loss is considered as a summation of loss
weightsforthestateandtheoutputaredenotedbyb ∈Rp functionsattheprevioustimestepsuntilnow. Asitisim-
i

3
practical to consider all time steps from the start of train- AccordingtoEqs. (3)and(4),wehave:
ing(especiallyafteralongtimeoftraining),weonlycon-
sidertheT previoustimesteps. Inotherwords,weassume i t+1 =Wh t +Ux t+1 +b i , (12)
that RNN has T-order Markov property (Ghojogh et al., h =tanh(i )=tanh(Wh +Ux +b ). (13)
t+1 t+1 t t+1 i
2019b). Therefore,thelossfunctionis:
Therefore:
T
(cid:88)
R(cid:51)L= L t , (7) Rp×p (cid:51) ∂h t+1 ( = a)(cid:0)∂i t+1(cid:1)(cid:62) × ∂h t+1
t=1 ∂h t ∂h t ∂i t+1
whereL 1 isthelossfunctionatthecurrenttimeslotandL t ( = b) W(1−h(cid:62) h )I , (14)
t+1 t+1 p×p
denotesthelossfunctionattheprevious(t−1)timeslot.
This loss functions needs to be optimized using gradient where I is the identity matrix of size (p × p), (a)
p×p
descentandchainrule. Therefore,wecalculateitsgradient is because of the chain rule, and (b) is because Rp×p (cid:51)
with respect to the parameters of RNN. These parameters ∂i /∂h =W(cid:62)forEq. (12),andwehave:
t+1 t
are y , h , V, W, U, b , and b , based on Eqs. (3), (4),
t t i y ∂h
and(5)andFig. 1-c. Rp×p (cid:51) t+1 =(1−h(cid:62) h )I , (15)
∂i t+1 t+1 p×p
t+1
2.3.1.GRADIENTWITHRESPECTTOTHEOUTPUT
based on Eq. (13) and the formula for derivative of the
Ifthereisnoactivationfunctionatthelastlayer,thegradi-
hyperbolictangentfunction,noticingthatthestateismul-
entofthelossfunctionofRNNwithrespecttotheoutput
tidimensionalandnotascalar.
attimetis:
For the time slot t = T, the derivative ∂L/∂h is much
T
Rq (cid:51) ∂L ( = a) ∂L × ∂L t ( = 7) ∂L t, (8) simpler:
∂y ∂L ∂y ∂y
t t t t
where(a)isbecauseofthechainrule. Rp (cid:51)δ T = ∂ ∂ h L ( = a) ∂ ∂ y L × ∂ ∂ h y T ( = 5) ∂ ∂ y L ( = 8) ∂ ∂ L y T,
T T T T T
The gradient of the loss function at time t with respect to
(16)
the output at time t, i.e., ∂L /∂y , is calculated based on
t t
the formula of the loss function. The loss function can where (a) is because of the chain rule and the derivative
beanylossfunctionforclassification, regression, orother ∂L /∂y iscomputedbasedontheformulaoflossfunc-
T T
tasks. tion.
If there is an activation function at the last layer (see Eq.
2.3.3.GRADIENTWITHRESPECTTOV
(6)),thegradientis:
The gradient of the loss function of RNN with respect to
Rq (cid:51) ∂L ( = a) ∂L × ∂L t × ∂y (cid:98)t ( = 7) ∂L t × ∂y (cid:98)t, (9) theweightmatrixV is:
∂y ∂L ∂y ∂y ∂y ∂y
t t (cid:98)t t (cid:98)t t
T T
where (a) is because of the chain rule. The derivative Rq×p (cid:51) ∂L ( = a)(cid:88)(cid:16)∂L × ∂y t (cid:17)( = b)(cid:88)(cid:16)∂L t ×h(cid:62) (cid:17) ,
∂y (cid:98)t /∂y t is calculated based on the formula of the activa- ∂V t=1 ∂y t ∂V t=1 ∂y t t
tionfunction. Theotherderivative,∂L /∂y ,iscalculated (17)
t (cid:98)t
basedontheformulaofthelossasafunctionoftheoutput
oftheactivationfunction. where(a)isbecauseV existsinalltimeslotsandchanging
V affects the loss L in all time slots. The equation (b) is
2.3.2.GRADIENTWITHRESPECTTOTHESTATE becauseofEqs. (8)and(5). Thederivative∂L /∂y ∈Rq
t t
The gradient of the loss function of RNN with respect to iscalculatedbasedontheformulaofthelossfunction.
thestateattimetis:
2.3.4.GRADIENTWITHRESPECTTOW
Rp (cid:51) ∂L ( = a)(cid:16)∂L × ∂y t (cid:17) + (cid:16) ∂L × ∂h t+1 (cid:17) The gradient of the loss function of RNN with respect to
∂h ∂y ∂h ∂h ∂h
t t t t+1 t theweightmatrixW is:
( = 5)(cid:16)∂L ×V (cid:17) + (cid:16) ∂L × ∂h t+1 (cid:17) , (10)
∂y t ∂h t+1 ∂h t Rp×p (cid:51) ∂L ( = a)(cid:88) T vec−1 (cid:16)(cid:0)∂h t(cid:1)(cid:62) × ∂L(cid:17) , (18)
where(a)isbecausechangingh t affectsbothy t andh t+1 . ∂W t=1 p×p ∂W ∂h t
Wedenoteδ :=∂L/∂h soEq. (10)becomes:
t t
wherevec−1 (.)de-vectorizesthevectoroflengthp2 toa
(cid:16)∂L (cid:17) (cid:16) ∂h (cid:17) p×p
δ = ×V + δ × t+1 . (11) matrix of size (p×p) and (a) is because W exists in all
t ∂y t t+1 ∂h t time slots and changing W affects the loss L in all time

4
slots. Thederivative∂L/∂h
t
∈ Rp inEq. (18)wascom- 2.3.7.GRADIENTWITHRESPECTTOb
y
putedinSection2.3.2.Thederivative∂h t /∂W inEq.(18) The gradient of the loss function of RNN with respect to
is: thebiasb is:
y
∂h ∂h ∂i
Rp×p2 (cid:51) t = t × t ,
∂W ∂i t ∂W Rq (cid:51) ∂L ( = a)(cid:88) T (cid:16)∂L × ∂y t (cid:17)( = b)(cid:88) T ∂L t, (22)
becauseofthechainrule. Thefirsttermis: ∂b y t=1 ∂y t ∂b y t=1 ∂y t
∂h
Rp×p (cid:51) t =(1−h(cid:62)h )I , (19)
∂i t t t p×p where(a)isbecauseb y existsinalltimeslotsandchanging
b affects the loss L in all time slots. The equation (b) is
y
according to Eq. (15). Based on the Magnus-Neudecker becauseofEqs. (8)and(5). Thederivative∂L /∂y ∈Rq
convention (Ghojogh et al., 2021), the second term is cal- t t
iscalculatedbasedontheformulaofthelossfunction.
culatedas:
∂i
2.3.8.UPDATESBYGRADIENTDESCENT
Rp×p2 (cid:51) t =h(cid:62) ⊗I ,
∂W t−1 p×p BPPTupdatestheparametersofRNNbygradientdescent
(Ghojoghetal.,2021)usingthecalculatedgradients:
where⊗denotestheKroneckerproduct.
2.3.5.GRADIENTWITHRESPECTTOU ∂L
h :=h −η , ∀t∈{1,...,T},
The gradient of the loss function of RNN with respect to t t ∂h t
theweightmatrixU is: ∂L
V :=V −η ,
∂V
T
Rp×d (cid:51) ∂L ( = a)(cid:88) vec−1 (cid:16)(cid:0)∂h t(cid:1)(cid:62) × ∂L(cid:17) , (20) W :=W −η ∂L ,
∂U p×d ∂U ∂h ∂W
t
t=1
∂L
U :=U −η ,
where(a)isbecauseU existsinalltimeslotsandchang- ∂U
ing U affects the loss L in all time slots. The derivative ∂L
∂L/∂h t ∈ Rp inEq. (18)wascomputedinSection2.3.2. b i :=b i −η ∂b i ,
Thederivative∂h /∂U inEq. (18)is:
t ∂L
b :=b −η ,
Rp×(pd) (cid:51) ∂h t = ∂h t × ∂i t, y y ∂b y
∂U ∂i ∂U
t
whereη > 0isthelearningrateandthegradientsarecal-
because of the chain rule. The first term is already calcu-
culatedbyEqs. (10),(17),(18),(20),(21),and(22).
latedinEq.(19).BasedontheMagnus-Neudeckerconven-
tion (Ghojogh et al., 2021), the second term is calculated
3.GradientVanishingorExplosionin
as:
Long-termDependencies
∂i
Rp×(pd) (cid:51) t =x(cid:62)⊗I . Inrecurrentneuralnetworks,soasindeepneuralnetworks,
∂U t p×p
the final output is the composition of a large number of
2.3.6.GRADIENTWITHRESPECTTOb
i
non-linear transformations. This results in the problem of
eithervanishingorexplodinggradientsinrecurrentneural
The gradient of the loss function of RNN with respect to
thebiasb is: networks,especiallyforcapturinglong-termdependencies
i
in sequence processing (Bengio et al., 1993; 1994). This
Rp (cid:51) ∂L ( = a)(cid:88) T (cid:16)(cid:0)∂h t(cid:1)(cid:62) × ∂L(cid:17) , (21) problemisexplainedinthefollowing. RecallEq. (2)fora
∂b ∂b ∂h dynamicalsystem:
i i t
t=1
where(a)isbecauseb i existsinalltimeslotsandchanging h t =f θ (h t−1 ,x t ).
baffectsthelossLinalltimeslots.Thederivative∂L/∂h
t
was already calculated in Section 2.3.2. The derivative Byinduction,thehiddenstateattimet,i.e.,h ,canbewrit-
t
∂h t /∂b i iscalculatedas: tenasthepreviousT timesteps. Ifthesubscripttdenotes
Rp×p (cid:51) ∂h t ( = a) ∂h t × ∂i t ( = 3) ∂h t, t 1 h 9 e 9 p 8 r ; e H vi o o c u h s re t i t t i e m r e et st a e l p ., s 2 , 0 w 0 e 1 h ): avebyinduction(Hochreiter,
∂b ∂i ∂b ∂i
i t i t
where (a) is because of the chain rule and the derivative (cid:16) (cid:0) (cid:1) (cid:17)
h =f f ...f (h ,x )...,x ,x .
∂h /∂i wasalreadycalculatedinEq. (19). 1 θ θ θ T T+1 2 1
t t

5
Then,bythechainruleinderivatives,thederivativelossat forlong-termdependencies. Inthiscase,thegradient
timeT,i.e.,L ,is: networkforgetsverylongtimeago. Inthiscase,gra-
T
dient explosion occurs in long-term dependency and
∂L T = (cid:88) ∂L t ∂h t ( = a) (cid:88) ∂L t ∂h T ∂h t rememberingverylongtimeagodominatestheshort-
∂θ ∂h ∂θ ∂h ∂h ∂θ
t≤T t t≤T T t termmemories.
( = 2) (cid:88) ∂L t ∂h T ∂f θ (h t−1 ,x t ) , (23) Asrememberingshort-termmemoriesisusuallymoreim-
∂h ∂h ∂θ
t≤T T t portantthanrememberingverypasttimeindifferenttasks,
it is recommended to use the weight matrix W whose
where(a)isbecauseofthechainrule. Inthisexpression,
largest eigenvalue is less than one; this makes the RNN
thereisthederivativeofh withrespecttoh whichitself
T t have the Markovian property because it forgets very past
canbecalculatedbythechainrule:
aftersomepoint. However,ifthelargesteigenvalueofW
∂h ∂h ∂h ∂h ismuchlessthanone,i.e.,λ(cid:28)1,gradientvanishinghap-
T = T × T−1 ×···× t+1. (24)
∂h ∂h ∂h ∂h pens very sooner than expected. Therefore, it is recom-
t T−1 T−2 t
mendedtousetheweightmatrixW whoselargesteigen-
for capturing long-term dependencies in the sequence, T valueisslightlylessthanone,i.e.,λ (cid:46) 1. Thismakesthe
shouldbelarge. ThismeansthatinEq. (24),andhencein
RNNslightlycontrastive. Onewaytohavetheweightma-
Eq. (23),thenumberofmultiplicandtermsbecomeshuge. trixW whoselargesteigenvalueisslightlylessthanoneis
Ontheonehand,ifeachderivativeisslightlysmallerthan
to make this matrix close to the identity matrix (Mikolov
one, the entire derivative in the chain rule becomes very
etal.,2015).
small for multiplication of many terms smaller than one.
There exist some other ways to determine the weight ma-
This problem is referred to as gradient vanishing. On the
trix W. For example, the wight matrix can be set to be
other hand, if every derivative is slightly larger than one,
anorthogonalmatrix(Arjovskyetal.,2016). Anotherap-
theentirederivativeinthechainruleexplodes,resultingin
proach is to copy the previous state exactly to the current
theproblemofexplodinggradients.Notethatgradientvan-
state. Inthisapproach,theEq. (4)ismodifiedto(Huetal.,
ishingismorecommonthangradientexplosioninrecurrent
2018):
networks.
There exist various attempts for resolving the problem of h =tanh(Wh +h +Ux +b )
t t−1 t−1 t i
(26)
gradientvanishingorexplosion(Hochreiter,1998;Bengio (cid:0) (cid:1)
=tanh (W +I)h +Ux +b ,
t−1 t i
etal.,2013). Inthefollowing, someoftheseattemptsare
introduced. whereI istheidentitymatrix. Thispreventsgradientvan-
ishing because it brings a copy of the previous step to the
3.1.Close-to-identityWeightMatrix
currentstate. Thiscanalsobeinterpretedasstrengthening
As Eq. (4) shows, the state is multiplied by a weight ma- thediagonaloftheweightmatrixW;hence,increasingthe
trixW ateverytimestepandifthereislong-termdepen- largesteigenvalueofW forpreventinggradientvanishing.
dency,manyoftheseW matricesaremultiplied. Suppose
the eigenvalue decomposition (Ghojogh et al., 2019a) of 3.2.LongDelays
the matrix W is W = AΛA(cid:62) where A ∈ Rp×p and As Eq. (4) and Fig. 1-c show, in the regular RNN, ev-
Λ := diag([λ ,...,λ ](cid:62)) contain the eigenvectors and ery state h is fed by its previous state h through the
1 p t t−1
eigenvaluesofW,respectively. Eq. (4)isrestatedas: weightmatrixW. AsdiscussedinSection3.1,inthereg-
ular RNN, the effect of the change ε in a state results in
h t =tanh(AΛA(cid:62)h t−1 +Ux t +b i ). (25) (λtε) after t time steps, where λ is the largest eigenvalue
ofW.
Ifachangeεinsomeelementofthestateh isaligned
t−1
with an eigenvector of the weight matrix W, then the ef- As shown in Fig. 1-c, the regular RNN has one-step con-
fect of this change in h will be (λtε) after t time steps, nectionsordelaysbetweenthestates. Itispossibletohave
t
accordingtoEq. (25). Twocasesmayhappen: longerdelaysbetweenthestatesinadditiontotheone-step
delays (Lin et al., 1995). In other words, it is possible to
• If the largest eigenvalue is less than one, i.e., λ < 1, havehigherlevelsofMarkovpropertyinthenetwork. Let
thenthechange(λtε)iscontrastivebecauseλt (cid:28) 1 W denote the weight matrix for k-step delays between
k
forlong-termdependencies.Inthiscase,gradientvan- thestates. Then,Eq. (4)canbemodifiedto:
ishing occurs in long-term dependency and the net-
(cid:16)(cid:88) (cid:17)
workforgetsverylongtimeago. h =tanh W h +Ux +b , (27)
t k t−k t i
k
• If the largest eigenvalue is less than one, i.e., λ > 1,
then the change (λtε) is diverging because λt (cid:29) 1 where the summation is over the k values for the existing

6
Figure2.The (a) folded and (b) unfolded structures of an RNN
withlongdelays.Everysquareonanedgemeansconnectionfrom Figure3. Theechostatenetwork.
onetimeslotbefore.
muchshouldbepassedthroughtheweightmatrix.Thiscan
delaysintheRNNstructure. AnexampleforanRNNnet-
control the amount of gradient vanishing. Note that leaky
workwithone-stepandthree-stepdelaysis:
unitsusedifferentτ ’sbecausetheremaybeaneedtokeep
i
(cid:16) (cid:17)
someofthedirectionsofstates(withτ =1)orforgetsome
h =tanh W h +W h +Ux +b , i
t 1 t−1 3 t−3 t i
ofthedirections(withτ (cid:29) 1). Inotherwords,itdecides
i
aboutthepdirectionsofstatesseparately.
whichisillustratedinFig. 2.
HavinglongdelaysinRNNisoneoftheattemptsforpre-
3.4.EchoStateNetworks
venting gradient vanishing (Lin et al., 1995). This is jus-
One of the approaches to handle the problem of gradient
tified because every state is having impact not only from
vanishing in RNN is to use echo state networks (Jaeger
the previous state but also from the more previous states.
& Haas, 2004; Jaeger, 2007). These networks consider
Therefore,inbackpropagationthroughtime,thereissome
therecurrentneuralnetworkasablackboxhavinghidden
skip in gradient flow from a state to more previous states
units with nonlinear activation functions and connections
without the need to go through the middle states in the
between them. This black boxof recurrentconnections is
chainrule.
calledthereservoirdynamicalsystemwhichmodelsthein-
3.3.LeakyUnits ternalstructureofacomputerorbrain. Theconnectionsin
the reservoir system are usually sparse and the weights of
Another way to resolve the problem of gradient vanish-
these connections are considered to be fixed. The output
ing is leaky units (Jaeger et al., 2007; Sutskever & Hin-
ofthereservoirsystemisconnectedtoanadditionallinear
ton, 2010). Let h denote the j-th element of the state
t,j output layer whose weights are learnable. The echo state
h ∈ [−1,1]p. In leaky units, Eq. (4) is modified to the
t network minimizes the mean squared error in the output
followingelement-wiseequation:
layer; hence, itperformslinearregressioninthelastlayer
1 (Jaeger & Haas, 2004). This network is shown in Fig. 3.
h =(1− )h
t,j τ t−1,j Becauseofnotlearningtherecurrentweightsinthereser-
j
(28) voirsystemandsufficingtolearntheweightsoftheoutput
1
+ τ tanh(W j: h t−1 +U j: x t +b i,j ), layer,theechostatenetworkdoesnotfacethegradientvan-
j
ishingproblem. Atutorialonthistopicis(Jaeger,2002).
where 1 ≤ τ < ∞ and W is the j-th row of W and
j j:
3.5.Othermethods
U isthej-throwofU andb isthej-thelementofb .
j: i,j i
Whenτ =1,thenEq. (28)becomes: There exist some other methods for not having gradient
i
vanishing in recurrent networks. For example, hierarchi-
1
h = tanh(W h +U x +b ), cal RNN (Hihi & Bengio, 1995) and deep RNN (Graves,
t,j τ j j: t−1 j: t i,j 2013) have been proposed which stack several recurrent
networks.Anotherrelatedcategoryofnetworksisthetime-
which gives back Eq. (4) in the regular RNN. However,
delay neural networks (Lang et al., 1990; Peddinti et al.,
whenτ (cid:29)1,thenEq. (28)becomes:
i 2015)whichareusedforshift-invariantsequenceprocess-
h =h , ing,especiallyusedinspeechrecognition(Sugiyamaetal.,
t,j t−1,j
1991). In these networks, every neuron in a layer re-
whichmeansthatthepreviousstateiscopiedtothecurrent ceivesacontextualwindowoftheneuronsintheprevious
state. The larger the τ , the easier the gradient propagates layer as well as their delayed outputs in several time slots
i
for h . Therefore, by tuning τ , it is possible to control ago. Moreover, these networks apply backpropagation on
t,i i
how much of the past should be directly copied and how several copies of the network shifted across the sequence

7
(time)sothatthenetworkbecomestime-invariant. 4.1.2.THEFORGETGATE
AnothergateintheLSTMcellistheforgetgate,firstpro-
4.LongShort-TermMemoryNetwork
posedin(Gersetal.,2000). Thisgatealsotakestheinput
AstheexamplesinSection1showed,weneedshort-term at the current time slot, x t ∈ Rd, and the hidden state of
relations in some cases and long-term relations in some the last time slot, h t−1 ∈ [−1,1]p, and outputs the signal
othercases. RNNlearnsthesequencebasedononeorsev- f ∈[0,1]p:
t
eralpreviousstates,dependingonitsstructureandthelevel
(cid:0) (cid:1)
f =sig W h +U x +(p (cid:12)c )+b ,
ofitsMarkovproperty(seeFig. 2). Therefore,weneedto t f t−1 f t f t−1 f
(31)
decideonthestructureofRNNtobeabletohandleshort-
whereW ∈Rp×p,U ∈Rp×d,andthebiasb ∈Rpare
term or long-term dependencies in the sequence. Instead f f f
the learnable weights for the forget gate, and p ∈ Rp is
ofmanualdesignoftheRNNstructureordecidingmanu- f
thelearnablepeepholeweight(Gers&Schmidhuber,2000)
allywhentoclearthestate, wecanlettheneuralnetwork
lettingapossibleleakofinformationfromthepreviousfi-
learnbyitselfwhentoclearthestatebasedonitsinputse-
nalmemory.
quence. LongShort-TermMemory(LSTM),initiallypro-
posedin(Hochreiter&Schmidhuber,1995;1997),isable As Eq. (31) shows, the forget gate considers the effect of
to do this; it learns from its input sequence when to use theinputandtheprevioushiddenstate,andperhapsaleak
short-term dependency (i.e., when to clear the state) and of information from the previous memory. This gate con-
whentousethelong-termmemory(i.e.,whennottoclear trolstheamountofforgettingthepreviousinformationwith
thestate). respect to the new-coming information. the forget gate is
illustratedinFig. 5.
4.1.LSTMGatesandCells
4.1.3.THEOUTPUTGATE
LSTMconsistsofseveralcells,eachofwhichcorresponds
ThenextgateintheLSTMcellistheoutputgatefirstpro-
toatimeslot(seeFig. 4). EveryLSTMcellcontainssev-
posed in (Hochreiter & Schmidhuber, 1995; 1997). This
eral gates for learning different aspects of the input time
gatealsotakestheinputatthecurrenttimeslot,x ∈ Rd,
series (see Fig. 5). These gates are introduced in the fol- t
andthehiddenstateofthelasttimeslot,h ∈ [−1,1]p,
lowing. t−1
andoutputsthesignalo ∈[0,1]p:
t
4.1.1.THEINPUTGATE
(cid:0) (cid:1)
o =sig W h +U x +(p (cid:12)c )+b , (32)
One of the gates in the LSTM cell is the input gate, first t o t−1 o t o t o
proposedin(Hochreiter&Schmidhuber,1995;1997).This
whereW ∈Rp×p,U ∈Rp×d,andthebiasb ∈Rpare
gatetakestheinputatthecurrenttimeslot, x ∈ Rd, and o o o
t the learnable weights for the output gate, and p ∈ Rp is
thehiddenstateofthelasttimeslot,h ∈ [−1,1]p,and o
t−1 thelearnablepeepholeweight(Gers&Schmidhuber,2000)
outputsthesignali ∈[0,1]p:
t lettingapossibleleakofinformationfromthecurrentfinal
(cid:0) (cid:1) memory.
i =sig W h +U x +(p (cid:12)c )+b ,
t i t−1 i t i t−1 i
(29) AsshowninEq. (32),theoutputgateconsiderstheeffect
where W ∈ Rp×p, U ∈ Rp×d, and the bias b ∈ Rp of the input and the previous hidden state, and a possible
i i i
arethelearnableweightsfortheinputgate,(cid:12)denotesthe informationleakfromthecurrentmemory.Theputputgate
Hadamard (element-wise) product, c ∈ Rp is the fi- isshowninFig. 5.
t−1
nal memory of the last time slot (which will be explained
in Section 4.1.5), and p ∈ Rp is the learnable peephole
4.1.4.THENEWMEMORYCELL(BLOCKINPUT)
i
TheLSTMcellincludesagatenamedthenewmemorycell.
weight(Gers&Schmidhuber,2000)lettingapossibleleak
Thisgatetakestheinputatthecurrenttimeslot,x ∈ Rd,
ofinformationfromthepreviousfinalmemory. Thefunc- t
andthehiddenstateofthelasttimeslot,h ∈ [−1,1]p,
tionsig(.)∈(0,1)isthesigmoidfunctionwhichisapplied t−1
and outputs the signal c ∈ [−1,1]p. This gate considers
element-wise: (cid:101)t
theeffectoftheinputandtheprevioushiddenstatetorep-
1
sig(x)= . (30) resentthenewinformationofcurrentinput.Itisformulated
1+exp(−x) as:
AsEq. (29)demonstrates,theinputgateconsiderstheef- c =tanh(W h +U x +b ), (33)
(cid:101)t c t−1 c t c
fect of the input and the previous hidden state. It may
also use a leak of information from the previous memory where W ∈ Rp×p, U ∈ Rp×d, and the bias b are the
c c c
through the peephole. This gate carries the importance of learnableweightsforthenewmemorycell. Thenewmem-
the information of the input at the current time slot. The orycellisalsoreferredtoastheblockinputintheliterature
inputgateisdepictedinFig. 5. (Greffetal.,2016). Thesignalc issometimesdenotedby
(cid:101)t

8
|     |     |     | Figure4. | AsequenceofLSTMcellsprocessingtheinputsequence. |     |     |     |     |     |     |
| --- | --- | --- | -------- | ----------------------------------------------- | --- | --- | --- | --- | --- | --- |
Figure5. TheconveyorbeltintheLSTMcell.
z in the literature. The new memory cell is illustrated in c . Inthesecondterm, i.e., i (cid:12)c , theinputgatei ∈
| t       |     |     |     |     |     | t−1                        |                  | t (cid:101)t        |        | t        |
| ------- | --- | --- | --- | --- | --- | -------------------------- | ---------------- | ------------------- | ------ | -------- |
|         |     |     |     |     |     | [0,1]pandthenewmemorycellc |                  | ∈[−1,1]pbothcontrol |        |          |
| Fig. 5. |     |     |     |     |     |                            |                  | (cid:101)t          |        |          |
|         |     |     |     |     |     | how much                   | of the new input | information         | should | be used. |
4.1.5.THEFINALMEMORYCALCULATION Theclosertheinputgatei istooneandthecloserthenew
t
i
After computation of the outputs of the input gate t , the memorycell c isto±1,themoretheinputinformationis
(cid:101) t
| forget gate     | f , and | the new | memory | cell c      | , we calculate | used.                                    |     |     |            |     |
| --------------- | ------- | ------- | ------ | ----------- | -------------- | ---------------------------------------- | --- | --- | ---------- | --- |
|                 | t       |         |        | (cid:101) t |                |                                          |     |     |            |     |
| thefinalmemoryc |         | ∈Rp:    |        |             |                |                                          |     |     |            |     |
|                 |         | t       |        |             |                | Inotherwords,thefirstandsecondtermsinEq. |     |     | (34)deter- |     |
minethetrade-offofusageofoldversusnewinformation
|     | c =(f | (cid:12)c | )+(i  | (cid:12)c ), | (34) |                  |             |          |           |            |
| --- | ----- | --------- | ----- | ------------ | ---- | ---------------- | ----------- | -------- | --------- | ---------- |
|     | t     | t         | t−1 t | (cid:101)t   |      |                  |             |          |           |            |
|     |       |           |       |              |      | in the sequence. | The weights | of these | gates are | trained in |
wherec ∈ Rp isthefinalmemoryoftheprevioustime a way that they pass or block the input/previous informa-
t−1
slot. tion based on the input sequence and the time step in the
AsEq. (34)demonstrates, thefinalmemoryconsidersthe sequence. ThefinalmemorycalculationisdepictedinFig.
5.
| effect of        | the forget | gate,                 | the previous | memory, | the input,     |                                   |     |     |     |     |
| ---------------- | ---------- | --------------------- | ------------ | ------- | -------------- | --------------------------------- | --- | --- | --- | --- |
| andthenewmemory. |            | Inthefirstterm,i.e.,f |              |         | (cid:12)c ,the |                                   |     |     |     |     |
|                  |            |                       |              |         | t t−1          | 4.1.6.THEHIDDENSTATE(BLOCKOUTPUT) |     |     |     |     |
∈[0,1]p
| forgetgatef |                    | controlshowmuchoftheprevious |               |     |      |                   |        |               |             |       |
| ----------- | ------------------ | ---------------------------- | ------------- | --- | ---- | ----------------- | ------ | ------------- | ----------- | ----- |
|             | t                  |                              |               |     |      | After computation | of the | output of the | output gate | o and |
| memoryc     | shouldbeforgotten. |                              | Thecloserthef |     | isto |                   |        |               |             | t     |
|             | t−1                |                              |               |     | t    |                   |        |               |             |       |
zero, the more the network forgets the previous memory the final memory c t , we calculate the hidden state h t ∈

9
| [−1,1]p: |     |     |     |                |     |      | Thesetwopapers(Gersetal.,2000;Gers&Schmidhuber, |                   |     |     |                      |     |     |         |
| -------- | --- | --- | --- | -------------- | --- | ---- | ----------------------------------------------- | ----------------- | --- | --- | -------------------- | --- | --- | ------- |
|          |     |     |     |                |     |      | 2000)                                           | also incorporated |     | the | full gaterecurrence, |     |     | inwhich |
|          |     | h   | =o  | (cid:12)tanh(c | ).  | (35) |                                                 |                   |     |     |                      |     |     |         |
t t t all gates receive additional recurrent inputs from all gates
|                                                 |     |     |     |     |     |     | attheprevioustimestep. |     |     | Infullgaterecurrence, |     |     |     | theEqs. |
| ----------------------------------------------- | --- | --- | --- | --- | --- | --- | ---------------------- | --- | --- | --------------------- | --- | --- | --- | ------- |
| Thishiddenstateisalsoconsideredastheblockoutput |     |     |     |     |     | of  |                        |     |     |                       |     |     |     |         |
(29),(31),and(32)become:
| theLSTMcell,depictedinFig. |     |     |     | 5.  |     |     |     |     |     |     |     |     |     |     |
| -------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
(cid:0)
4.1.7.THEOUTPUT i t =sig W i h t−1 +U i x t +(p (cid:12)c t−1 )+b i
|     |     |     |     |     |     |     |     |     |     |     |     | i   |     | (40) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- |
(cid:1)
| Theoutputy |      | ∈Rq | oftheLSTMcellisasfollows: |        |       |               |     |              | +R i  | +R  | f     | +R        | o      | .       |
| ---------- | ---- | --- | ------------------------- | ------ | ----- | ------------- | --- | ------------ | ----- | --- | ----- | --------- | ------ | ------- |
|            | t    |     |                           |        |       |               |     |              | ii    | t−1 | if    | t−1       | io t−1 |         |
|            |      |     | y =Vh                     | +b     | ,     | (36)          |     |              |       |     |       |           |        |         |
|            |      |     | t                         | t      | y     |               |     |              |       |     |       |           |        |         |
|            |      |     |                           |        |       |               | f   | =sig (cid:0) | W h   | +U  | x +(p | (cid:12)c | )+b    |         |
|            | Rq×p |     |                           |        | Rq    |               | t   |              | f t−1 |     | f t   | f         | t−1    | f       |
| where      | V ∈  | and | the                       | bias b | ∈ are | the learnable |     |              |       |     |       |           |        | (41)    |
|            |      |     |                           | y      |       |               |     |              |       |     |       |           |        | (cid:1) |
weights for the output. It is possible to use an activation +R fi i t−1 +R ff f +R fo o t−1 .
t−1
| function,suchasEq. |     |     | (6),afterthisoutputsignal. |     |     | Figure5 |     |     |     |     |     |     |     |     |
| ------------------ | --- | --- | -------------------------- | --- | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
showstheoutputsignalintheLSTMcell.
|                                                     |     |     |     |     |     |     | o   | =sig (cid:0) | W h   | +U  | x +(p | (cid:12)c | )+b |      |
| --------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | ------------ | ----- | --- | ----- | --------- | --- | ---- |
|                                                     |     |     |     |     |     |     | t   |              | o t−1 |     | o t   | o         | t   | o    |
| Notethatintheliterature,theoutputissometimesconsid- |     |     |     |     |     |     |     |              |       |     |       |           |     | (42) |
(cid:1)
eredtobeequaltothehiddenstate,i.e.,y =h ,bysetting +R oi i t−1 +R of f +R oo o t−1 ,
|      |                         |     |     |     | t                  | t   |                                      |      |     |       |       | t−1 |                 |       |
| ---- | ----------------------- | --- | --- | --- | ------------------ | --- | ------------------------------------ | ---- | --- | ----- | ----- | --- | --------------- | ----- |
| V =I | (theidentitymatrix)andb |     |     | y   | =0(thezerovector). |     |                                      |      |     |       |       |     |                 |       |
|      |                         |     |     |     |                    |     | where                                | R ,R | ,R  | ,R    | ,R ,R | ,R  | ,R              | ,R ∈  |
|      |                         |     |     |     |                    |     |                                      | ii   | if  | io fi | ff    | fo  | oi              | of oo |
|      |                         |     |     |     |                    |     | Rp×parethelearnablerecurrentweights. |      |     |       |       |     | Notethatthefull |       |
4.2.HistoryandVariantsofLSTM
gaterecurrenceoftendisappearedinlaterpapersonLSTM.
| LSTM | has gone | through |     | various | developments | and im- |     |     |     |     |     |     |     |     |
| ---- | -------- | ------- | --- | ------- | ------------ | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
Later,GravesandSchmidhuberadaptedtheoriginalLSTM
provementsgradually(Greffetal.,2016).Someofthevari-
andproposedthevanillaLSTMin2005(Graves&Schmid-
| antsofLSTMdonothavethepeepholes. |     |     |     |     | Inthiscase,the |     |        |         |       |        |        |      |        |       |
| -------------------------------- | --- | --- | --- | --- | -------------- | --- | ------ | ------- | ----- | ------ | ------ | ---- | ------ | ----- |
|                                  |     |     |     |     |                |     | huber, | 2005a), | which | is one | of the | most | common | LSTMs |
Eqs. (29),(31),and(32)aresimplifiedto:
|     |     |         |     |     |         |     | intheliterature. |     | ThevanillaLSTMincorporatedthestruc- |     |     |     |     |     |
| --- | --- | ------- | --- | --- | ------- | --- | ---------------- | --- | ----------------------------------- | --- | --- | --- | --- | --- |
|     |     | (cid:0) |     |     | (cid:1) |     |                  |     |                                     |     |     |     |     |     |
i =sig W h +U x +b , (37) tures of the original LSTM (Hochreiter & Schmidhuber,
|     | t   |     | i t−1 | i   | t i |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
(cid:0) (cid:1) 1997)andthepapers(Gersetal.,2000;Gers&Schmidhu-
|     | f   | =sig | W h | +U  | x +b  | , (38) |     |     |     |     |     |     |     |     |
| --- | --- | ---- | --- | --- | ----- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
|     | t   |      | f   | t−1 | f t f |        |     |     |     |     |     |     |     |     |
(cid:0) (cid:1) ber,2000). ThefullBPTT,introducedinSection2.3,was
|               | o   | =sig                                   | W h   | +U  | x +b  | , (39) |                                              |     |     |     |     |     |     |     |
| ------------- | --- | -------------------------------------- | ----- | --- | ----- | ------ | -------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
|               | t   |                                        | o t−1 |     | o t o |        | usedforLSTMinthevanillaLSTM(Graves&Schmidhu- |     |     |     |     |     |     |     |
| respectively. |     | Inthefollowing,wereviewahistoryofvari- |       |     |       |        | ber,2005a).                                  |     |     |     |     |     |     |     |
antsoftheLSTMnetworks.
4.2.3.OTHERLSTMVARIANTS
|     |     |     |     |     |     |     | There | are other | variants |     | of LSTM | (Greff | et  | al., 2016; |
| --- | --- | --- | --- | --- | --- | --- | ----- | --------- | -------- | --- | ------- | ------ | --- | ---------- |
4.2.1.ORIGINALLSTM
|     |     |     |     |     |     |     | Jozefowicz |     | et al., | 2015); | although, | the | most | common |
| --- | --- | --- | --- | --- | --- | --- | ---------- | --- | ------- | ------ | --------- | --- | ---- | ------ |
LSTMwasoriginallyproposedbyHochreiterandSchmid-
usedLSTMisthevanillaLSTM(Graves&Schmidhuber,
| huber | in years | 1995 | to 1997 | (Hochreiter | & Schmidhuber, |     |     |     |     |     |     |     |     |     |
| ----- | -------- | ---- | ------- | ----------- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
1995; 1997). We call it the original LSTM (Hochreiter & 2005a). BPTT was used for LSTM training in (Graves &
Schmidhuber,2005a);however,Kalmanfilteringwasused
| Schmidhuber,1997). |     |     | TheoriginalLSTMhadonlythein- |     |     |     |     |     |     |     |     |     |     |     |
| ------------------ | --- | --- | ---------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
foritstraining(Gersetal.,2002)beforethat.Anothertrain-
putandoutputgates,introducedinSections4.1.1and4.1.3,
and it did not have a forget gate. It also did not contain ingmethodforLSTMwasevolutionarylearning(Schmid-
|                                         |     |     |     |     |              |     | huberetal.,2007). |     | Context-sensitiveevolutionarylearning |     |     |     |     |     |
| --------------------------------------- | --- | --- | --- | --- | ------------ | --- | ----------------- | --- | ------------------------------------- | --- | --- | --- | --- | --- |
| thepeepholes;therefore,itsgateswereEqs. |     |     |     |     | (37)and(39). |     |                   |     |                                       |     |     |     |     |     |
TheoriginalLSTMtrainedthenetworkusingBPTT(intro- wasalsousedforLSTMtraining(Bayeretal.,2009).
|     |     |     |     |     |     |     | Later | works | tried to | improve | the | performance |     | of LSTM. |
| --- | --- | --- | --- | --- | --- | --- | ----- | ----- | -------- | ------- | --- | ----------- | --- | -------- |
ducedinSection2.3)andamixtureofreal-timerecurrent
learning(Robinson&Fallside,1987;Williams,1989). Forexample,Saket.al.addedalinearlayerwhichprojects
|     |     |     |     |     |     |     | the output | of  | the LSTM | to  | smaller | number | of  | parameters |
| --- | --- | --- | --- | --- | --- | --- | ---------- | --- | -------- | --- | ------- | ------ | --- | ---------- |
4.2.2.VANILLALSTM
beforetherecurrentconnections(Saketal.,2014).Doetsch
Later,Gerset. al. (Gersetal.,2000;Gers&Schmidhuber, et. al. converted the slope of activation functions of the
2000)appliedsomechangestotheoriginalLSTM.Thefor- LSTM gates to learnable parameters for performance im-
getgate,introducedinSection4.1.2,wasproposedforthe provement(Doetschetal.,2014). Dynamiccortexmemory
firsttimein(Gersetal.,2000)toletthenetworkforgetits was another LSTM variant which added connections be-
previousstateseithercompletelyorpartially.Thepeephole tweenthegateswithineveryLSTMcell(Otteetal.,2014).
connections,introducedinSections4.1.1,4.1.2,and4.1.3, Finally in 2014, one the biggest improvements of LSTM
were first proposed in (Gers & Schmidhuber, 2000). The wasproposed,whichwasnamedtheGatedRecurrentUnits
peepholesletapossibleleakofinformationfromtheprevi- (GRU)(Choetal.,2014). ThephilosophyofGRUwasto
ousorcurrentfinalmemory. Thisletsthememorycontrol simplifytheLSTMcellbecausewemaynoneedtohavea
thegates. verycomplicatedcelltolearnthesequenceinformation. In

10
|     |     | Figure6. | TheconveyorbeltintheGRUcell(thefullygatedunit). |     |     |       |     |       |     |     |     |
| --- | --- | -------- | ----------------------------------------------- | --- | --- | ----- | --- | ----- | --- | --- | --- |
|     |     |          |                                                 |     |     | Rp×p, |     | Rp×d, |     |     | Rp  |
otherwords,GRUraisedthequestionofwhetherweneed where W r ∈ U r ∈ and the bias b r ∈
tobethatflexiblelikeLSTMtolearnthesequence.GRUis arethelearnableweightsfortheresetgate. Theresetgate
lessflexiblethanLSTMbutitisgoodenoughforsequence considers the effect of the input and the previous hidden
learning. state,anditcontrolstheamountofforgetting/resettingthe
|     |     |     |     | previous | information |     | with respect | to  | the | new-coming | in- |
| --- | --- | --- | --- | -------- | ----------- | --- | ------------ | --- | --- | ---------- | --- |
GRUredesignedtheLSTMcellbyintroducingresetgate,
update gate, and new memory cell; therefore, the number formation. Comparing Eqs. (38) and (43) shows that the
of gates were reduced from four to three. It was empiri- resetgateintheGRUcellissimilartotheforgetgateinthe
|                                |           |               |                      | LSTMcell. | TheresetgateisdepictedinFig. |     |     |     |     | 6.  |     |
| ------------------------------ | --------- | ------------- | -------------------- | --------- | ---------------------------- | --- | --- | --- | --- | --- | --- |
| cally shown                    | in (Chung | et al., 2014) | that the performance |           |                              |     |     |     |     |     |     |
| ofLSTMimprovesbyusingGRUcells. |           |               | Laterin2017,the      |           |                              |     |     |     |     |     |     |
GRU was further simplified by merging the reset and up- – The Update Gate: Another gate in the GRU cell is the
dategatesintoaforgetgate(Heck&Salem,2017). Nowa- update gate. This gate also takes the input at the current
days, GRU is the most commonly used LSTM structure. time slot, x ∈ Rd, and the hidden state of the last time
t
|                                             |     |     |           |        | ∈[−1,1]p,andoutputsthesignalz |        |       |     |      | ∈[0,1]p: |      |
| ------------------------------------------- | --- | --- | --------- | ------ | ----------------------------- | ------ | ----- | --- | ---- | -------- | ---- |
| Section4.3introducesthedetailsoftheGRUcell. |     |     |           | slot,h | t−1                           |        |       |     |      | t        |      |
| 4.3.GatedRecurrentUnits(GRU)                |     |     |           |        | z                             | =sig(W | h     | +U  | x +b | ),       | (44) |
|                                             |     |     |           |        |                               | t      | z t−1 |     | z t  | z        |      |
| GRUwasfirstproposedin(Choetal.,2014).       |     |     | Aswasmen- |        |                               |        |       |     |      |          |      |
tioned in Section 4.2.3, GRU simplified the LSTM cell in where W ∈ Rp×p, U ∈ Rp×d, and the bias b ∈ Rp
|     |     |     |     |         | z         |         | z   |            |       |     | z      |
| --- | --- | --- | --- | ------- | --------- | ------- | --- | ---------- | ----- | --- | ------ |
|     |     |     |     | are the | learnable | weights | for | the update | gate. | The | update |
ordertomaketheflexibilityofLSTM.
gateconsiderstheeffectoftheinputandtheprevioushid-
4.3.1.FULLYGATEDUNIT den state, and it controls the amount of using the new in-
ThemainGRUwasthefullygatedunit(Choetal.,2014),
putdataforupdatingthecellbythecominginformationof
whose gates are introduced in the following. Its gates are sequence. Comparing Eqs. (37) and (44) shows that the
illustratedinFig. 6. update gate in the GRU cell is similar to the input gate in
|               |                                       |              |            | theLSTMcell.  |     | Figure6showstheupdategateintheGRU |     |     |     |     |     |
| ------------- | ------------------------------------- | ------------ | ---------- | ------------- | --- | --------------------------------- | --- | --- | --- | --- | --- |
| – The Reset   | Gate: One                             | of the gates | in the GRU | cell is cell. |     |                                   |     |     |     |     |     |
| theresetgate. | Thisgatetakestheinputatthecurrenttime |              |            |               |     |                                   |     |     |     |     |     |
slot, x ∈ Rd, and the hidden state of the last time slot, – The New Memory Cell: The GRU cell includes a gate
t
| ∈[−1,1]p,andoutputsthesignalr |     |     | ∈[0,1]p: |     |     |     |     |     |     |     |     |
| ----------------------------- | --- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
h t−1 t named the new memory cell. This gate takes the input at
|     |     |     |     | the current | time | slot, | x ∈ | Rd, and | the | hidden | state of |
| --- | --- | --- | --- | ----------- | ---- | ----- | --- | ------- | --- | ------ | -------- |
t
r t =sig(W r h t−1 +U r x t +b r ), (43) the last time slot, h ∈ [−1,1]p, and outputs the signal
t−1

11
h(cid:101)t ∈[−1,1]p:
(cid:16) (cid:0) (cid:1) (cid:17) –TheForgetGate: Theforgetgatetakestheinputatthe
h(cid:101)t =tanh W c r t (cid:12)h t−1 ) +U c x t +b c , (45) currenttimeslot,x t ∈ Rd,andthehiddenstateofthelast
time slot, h ∈ [−1,1]p, and outputs the signal r ∈
where W ∈ Rp×p, U ∈ Rp×d, and the bias b are the t−1 t
c c c [0,1]p:
learnableweightsforthenewmemorycell. Thisgatecon-
siderstheeffectoftheinputandtheprevioushiddenstateto f =sig(W h +U x +b ), (47)
t f t−1 f t f
representthenewinformationofcurrentinput. Comparing
Eqs. (33)and(45)showsthatthenewmemorycellinthe whereW f ∈Rp×p,U f ∈Rp×d,andthebiasb f ∈Rpare
GRU cell is similar to the new memory cell in the LSTM the learnable weights for the forget gate. The forget gate
cell. Notethat,intheLSTMcell,thehiddenstate(seeEq. considers the effect of the input and the previous hidden
(35)) and the new memory cell (see Eq. (33)) were dif- state,anditcontrolstheamountofforgettingtheprevious
ferent; however, thehiddenstateoftheGRUcell(seeEq. information with respect to the new-coming information.
(45)) replaces the new memory signal in the LSTM cell. Therefore,itcontrolsbothforgettingorusingtheprevious
ThenewmemorycellisshowninFig. 6. memoryandusingthenewcominginformation.
–TheFinalMemory(HiddenState): Aftercomputation – The New Memory Cell and the Final Memory: Be-
of the outputs of the update gate z and the new memory causetheforgetgatereplacestheresetandtheupdategate
t
intheminimalgateunit,Eqs.(45)and(46)arechangedto:
cell h(cid:101)t , we calculate the final memory or the hidden state
h t ∈Rp: (cid:16) (cid:0) (cid:1) (cid:17)
(cid:0) (cid:1)
h(cid:101)t =tanh W
c
f
t
(cid:12)h
t−1
) +U
c
x
t
+b
c
, (48)
h
t
= (1−z
t
)(cid:12)h
t−1
+(z
t
(cid:12)h(cid:101)t ), (46)
(cid:0) (cid:1)
whereh ∈ Rp isthehiddenstateoftheprevious time
h
t
= (1−f
t
)(cid:12)h
t−1
+(f
t
(cid:12)h(cid:101)t ), (49)
t−1
slot. ThefinalmemoryblockisillustratedinFig. 6. respectively,tobethenewmemorycellandthefinalmem-
AsEq. (46)demonstrates, thefinalmemoryconsidersthe oryintheminimalgateunit.
effectoftheupdategate,thepreviousmemory,andthenew
5.BidirectionalRNNandLSTM
memory. Inthefirstterm,i.e.,(1−z )(cid:12)h ,theupdate
t t−1
gate z t ∈ [0,1]p controls how much of the previous state 5.1.JustificationofBidirectionalProcessing
h should be used based on the input data. The closer
t−1 A bidirectional RNN or LSTM network processes the se-
thez istoone(resp. zero),themorethenetworkforgets
t quenceinbothdirections; lefttorightandrighttoleft. In
(resp. considers) the previous state h . In the second
t−1 the first glance, online causal tasks such as reading a text
term,i.e.,z
t
(cid:12)h(cid:101)t ,theupdategatez
t
∈[0,1]pandthenew
or listening to a speech do not have access to the future.
memory cell h(cid:101)t ∈ [−1,1]p both control how much of the Therefore,bidirectionalnetworksseemtoviolatecausality
new input information should be used. In other words, it in them. However, in many of these tasks, it is possible
controls how much the information should be updated by to wait for the completion of a part of the sequence such
the new information. The closer the update gate z t is to as a sentence and then decide about it. For example, it is
one and the closer the new memory cell h(cid:101)t is to ±1, the normal to wait for the completion of sentence in speech
moretheinputinformationisused. recognitionandthenrecognizeit(Graves&Schmidhuber,
Overall, the first and second terms in Eq. (46) determine 2005a;b). In text processing, the text is usually available
thetrade-offofusageofoldversusnewinformationinthe except in a streaming text. Even in streaming text, it is
sequence. Theweightsofthesegatesaretrainedinaway possible to wait for a sentence to complete. Therefore, it
thattheypassorblocktheinput/previousinformationbased makes sense to use bidirectional networks for processing
on the input sequence and the time step in the sequence. sequencesbecause,sometimes,theimportantrelatedword
ComparingEqs. (34)and(46)showsthatthefinalmemory comesafterawordandnotnecessarilybeforeit. Anexam-
in the GRU cell is in the form of the final memory in the ple for such a case is the sentence “The police is chasing
LSTM cell; however, they have somewhat different func- thethief”wheretheword“thief”isastronglyrelated(op-
tionality. posite) word for the word “police”. In this sentence, both
thewords“thief”and“police”arerelatedanditisworthto
4.3.2.MINIMALGATEDUNIT processthesentenceinbothdirections.
Minimalgatedunit(Heck&Salem,2017)isanothervari-
ant of GRU which has simplified the gate by merging the 5.2.BidirectionalRNN
reset and update gates into a forget gate. This merging is The bidirectional RNN was first proposed in (Schuster &
possiblebecausetheforgetgatecancontrolboththeprevi- Paliwal,1997)andfurtherexploitedin(Baldietal.,1999).
ousandnewinformationofthesequence. It uses two sets of states each for one of the directions in

12
|     | Figure7. |     | ThebidirectionalRNN. |     |     |     |     |     |     |     |     |     |
| --- | -------- | --- | -------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
the sequence. Let the states for left-to-right and right-to- Figure8. ThebidirectionalLSTM.
|                           |     |     | →−  | ←−    |                |     |     |     |     |     |     |     |
| ------------------------- | --- | --- | --- | ----- | -------------- | --- | --- | --- | --- | --- | --- | --- |
| leftprocessingbedenotedby |     |     | h   | and h | ,respectively. | In  |     |     |     |     |     |     |
|                           |     |     |     | t     | t              |     |     |     |     |     |     |     |
thebidirectionalRNN,Eq.(4)isreplacedbytwoequations
|     |     |     |     |     |     |     | hasshownitsmerit(Gravesetal.,2005). |     |     |     | Anotherexample |     |
| --- | --- | --- | --- | --- | --- | --- | ----------------------------------- | --- | --- | --- | -------------- | --- |
(Gravesetal.,2013): isthehybridofbidirectionalLSTMandConditionalRan-
→− −→→− →− →− dom Fields (CRF) (Lafferty et al., 2001) for the sequence
|     | h =tanh(W |     | h   | +Ux | + b ), | (50) |     |     |     |     |     |     |
| --- | --------- | --- | --- | --- | ------ | ---- | --- | --- | --- | --- | --- | --- |
t t−1 t i taggingtask(Huangetal.,2015). Otherextensionsofbidi-
|     | ←−  |     | ←−←− | ←−  | ←−  |     |     |     |     |     |     |     |
| --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
h =tanh(W h +Ux + b ), (51) rectionalLSTMnetworksexistsuchas(Petersetal.,2017).
|     | t   |     | t+1 |     | t i |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
andEq. (5)isreplacedby: 5.4.EmbeddingsfromLanguageModel(ELMo)
|     |     | →−→− | ←−←− |     |     |     | TheEmbeddingsfromLanguageModel(ELMo)network, |     |     |     |     |     |
| --- | --- | ---- | ---- | --- | --- | --- | -------------------------------------------- | --- | --- | --- | --- | --- |
y = V h +V h +b , (52) firstproposedin(Petersetal.,2018), isalanguagemodel
|     |     | t   | t   | t   | y   |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
whichmakesuseofbidirectionalLSTMnetworks.Itisone
wherethearrowsshowtheparametersforeachdirectionof
|                        |     |           |                              |     |                      |     | of the successful | context-aware |        | language        | modeling     | net- |
| ---------------------- | --- | --------- | ---------------------------- | --- | -------------------- | --- | ----------------- | ------------- | ------ | --------------- | ------------ | ---- |
| processing.            | The | unfolding | schematic                    |     | of the bidirectional |     |                   |               |        |                 |              |      |
|                        |     |           |                              |     |                      |     | works. It         | has been      | widely | used in various | applications |      |
| RNNisillustratedinFig. |     |           | 7. Asthisfigureshows,theout- |     |                      |     |                   |               |        |                 |              |      |
suchasinmedicalinterviewprocessing(Sarzynska-Wawer
| puts of | both directions |     | are connected |     | to an output | layer. |     |     |     |     |     |     |
| ------- | --------------- | --- | ------------- | --- | ------------ | ------ | --- | --- | --- | --- | --- | --- |
etal.,2021).
Insomecases,thisoutputlayermaybereplacedbyathird
|     |     |     |     |     |     |     | ThestructureofELMoisillustratedinFig. |     |     |     | 9. Asshownin |     |
| --- | --- | --- | --- | --- | --- | --- | ------------------------------------- | --- | --- | --- | ------------ | --- |
multi-layerneuralnetwork.Allweightsofthebidirectional
thisfigure,ELMocontainsLlayersofbidirectionalLSTM
RNNaretrainedusingbackpropagationthroughtimesimi-
|                                      |              |     |               |     |                |      | networks where       | the                | output of | each bidirectional       | LSTM              | is  |
| ------------------------------------ | ------------ | --- | ------------- | --- | -------------- | ---- | -------------------- | ------------------ | --------- | ------------------------ | ----------------- | --- |
| larlytowhatwasexplainedinSection2.3. |              |     |               |     | Itisnoteworthy |      |                      |                    |           |                          |                   |     |
|                                      |              |     |               |     |                |      | fed to the           | next bidirectional |           | LSTM. in                 | The bidirectional |     |
| that the                             | deep variant | of  | bidirectional | RNN | has been       | pro- |                      |                    |           |                          |                   |     |
|                                      |              |     |               |     |                |      | LSTMnetworksofELMo,V |                    |           | =I issetsothattheoutputs |                   |     |
posedin(Gravesetal.,2013).
|     |     |     |     |     |     |     | y becomesequaltothehiddenstatesh. |     |     | Attimeslottand |     |     |
| --- | --- | --- | --- | --- | --- | --- | --------------------------------- | --- | --- | -------------- | --- | --- |
layerl,theoutputs(orhiddenstates)ofthetwodirections
5.3.BidirectionalLSTM
ofLSTMareconcatenatedtogethertomakeh(l):
| Bidirectional                                  | LSTM      | was | first      | proposed | in (Graves     | &       |     |      |                  |                        | t   |     |
| ---------------------------------------------- | --------- | --- | ---------- | -------- | -------------- | ------- | --- | ---- | ---------------- | ---------------------- | --- | --- |
| Schmidhuber,                                   | 2005a;b). |     | As obvious |          | from its name, | the     |     |      | →−               | ←−                     |     |     |
|                                                |           |     |            |          |                |         |     | h(l) | :=[h(l)(cid:62), | h(l)(cid:62)](cid:62). |     |     |
| bidirectionalLSTMincludestwoLSTMnetworkseachof |           |     |            |          |                |         |     | t    | t                | t                      |     |     |
| whichprocessesthesequencefromonedirection.     |           |     |            |          |                | Inother |     |      |                  |                        |     |     |
Then,alinearcombinationofthesehiddenstatesoflayers
| words, | there are | two LSTM | networks |     | which are | fed with |     |     |     |     |     |     |
| ------ | --------- | -------- | -------- | --- | --------- | -------- | --- | --- | --- | --- | --- | --- |
isconsideredtobetheembeddingvectorofELMonetwork
| thesequenceinoppositeorders. |     |     |     | Thisstructureisdepicted |     |     |     |     |     |     |     |     |
| ---------------------------- | --- | --- | --- | ----------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
attimet(Petersetal.,2018):
| in Fig. | 8. Experiments |     | have shown     | that | the bidirectional |     |     |     |     |     |     |     |
| ------- | -------------- | --- | -------------- | ---- | ----------------- | --- | --- | --- | --- | --- | --- | --- |
| LSTM    | outperforms    | the | unidirectional |      | LSTM (Graves      | &   |     |     |     |     |     |     |
L
(cid:88)
Schmidhuber,2005a;Gravesetal.,2005).Thisisexpected yELMo :=γ s h(l), (53)
|                                          |     |     |     |     |              |     |     | t   |     | l t |     |     |
| ---------------------------------------- | --- | --- | --- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- |
| accordingtothejustificationinSection5.1. |     |     |     |     | Becauseofits |     |     |     |     |     |     |     |
l=1
| advantages, | various | methods | have | combined | the | bidirec- |     |     |     |     |     |     |
| ----------- | ------- | ------- | ---- | -------- | --- | -------- | --- | --- | --- | --- | --- | --- |
tionalLSTMwithothermethods. Forexample,ahybridof whereγand{s }L arethehyperparameterscalarweights
l l=1
thebidirectionalLSTMandHMM(Ghojoghetal.,2019b) which are determined according to the specific task (e.g.,

13
|     |     |     |     |     |     |     | Bengio, Yoshua, |     | Simard, | Patrice, | and | Frasconi, | Paolo. |
| --- | --- | --- | --- | --- | --- | --- | --------------- | --- | ------- | -------- | --- | --------- | ------ |
Learninglong-termdependencieswithgradientdescent
|     |     |     |     |     |     |     | isdifficult. | IEEEtransactionsonneuralnetworks,5(2): |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------------ | -------------------------------------- | --- | --- | --- | --- | --- |
157–166,1994.
|     |     |     |     |     |     |     | Bengio, Yoshua, |         | Boulanger-Lewandowski, |               |               | Nicolas,   | and       |
| --- | --- | --- | --- | --- | --- | --- | --------------- | ------- | ---------------------- | ------------- | ------------- | ---------- | --------- |
|     |     |     |     |     |     |     | Pascanu,        | Razvan. | Advances               |               | in optimizing |            | recurrent |
|     |     |     |     |     |     |     | networks.       | In 2013 | IEEE                   | international |               | conference | on        |
acoustics,speechandsignalprocessing,pp.8624–8628.
IEEE,2013.
|     |     |     |     |     |     |     | Broer,HendrikWolterandTakens,Floris. |     |     |     |     | Dynamicalsys- |     |
| --- | --- | --- | --- | --- | --- | --- | ------------------------------------ | --- | --- | --- | --- | ------------- | --- |
temsandchaos,volume172.
Springer,2011.
|     |     |     |     |     |     |     | Cho, Kyunghyun,           |     | Van | Merrie¨nboer, |                       | Bart, | Bahdanau, |
| --- | --- | --- | --- | --- | --- | --- | ------------------------- | --- | --- | ------------- | --------------------- | ----- | --------- |
|     |     |     |     |     |     |     | Dzmitry,andBengio,Yoshua. |     |     |               | Onthepropertiesofneu- |       |           |
ralmachinetranslation:Encoder-decoderapproaches.In
EighthWorkshoponSyntax,SemanticsandStructurein
StatisticalTranslation(SSST-8),2014.
|     |     |     |     |     |     |     | Chung, Junyoung, |                 | Gulcehre, | Caglar,     |            | Cho,      | KyungHyun,   |
| --- | --- | --- | --- | --- | --- | --- | ---------------- | --------------- | --------- | ----------- | ---------- | --------- | ------------ |
|     |     |     |     |     |     |     | and Bengio,      | Yoshua.         | Empirical |             | evaluation |           | of gated re- |
|     |     |     |     |     |     |     | current          | neural networks |           | on sequence |            | modeling. | arXiv        |
preprintarXiv:1412.3555,2014.
|     | Figure9. | TheELMonetwork. |     |     |     |     |                   |     |            |         |     |      |          |
| --- | -------- | --------------- | --- | --- | --- | --- | ----------------- | --- | ---------- | ------- | --- | ---- | -------- |
|     |          |                 |     |     |     |     | Doetsch, Patrick, |     | Kozielski, | Michal, | and | Ney, | Hermann. |
Fastandrobusttrainingofrecurrentneuralnetworksfor
|          |            |              |     |         |         |          | offline handwriting |     | recognition. |     | In  | 2014 14th | interna- |
| -------- | ---------- | ------------ | --- | ------- | ------- | -------- | ------------------- | --- | ------------ | --- | --- | --------- | -------- |
| question | answering, | translation, |     | etc) in | natural | language |                     |     |              |     |     |           |          |
processing. tional conference on frontiers in handwriting recogni-
tion,pp.279–284.IEEE,2014.
6.Conclusion
|     |     |     |     |     |     |     | Gers, Felix | A and | Schmidhuber, |     | Ju¨rgen. | Recurrent | nets |
| --- | --- | --- | --- | --- | --- | --- | ----------- | ----- | ------------ | --- | -------- | --------- | ---- |
ThiswasatutorialpaperonRNN,LSTM,anditsvariants. thattimeandcount. InProceedingsoftheIEEE-INNS-
| We covered | dynamical | system, | backpropagation |     |     | through |                    |     |       |            |     |     |             |
| ---------- | --------- | ------- | --------------- | --- | --- | ------- | ------------------ | --- | ----- | ---------- | --- | --- | ----------- |
|            |           |         |                 |     |     |         | ENNS International |     | Joint | Conference |     | on  | Neural Net- |
time,LSTMgatesandcells,historyandvariantsofLSTM, works. IJCNN 2000. Neural Computing: New Chal-
theGRUcell,bidirectionalRNN,bidirectionalLSTM,and lenges and Perspectives for the New Millennium, vol-
ELMonetwork.
ume3,pp.189–194.IEEE,2000.
References Gers, Felix A, Schmidhuber, Ju¨rgen, and Cummins, Fred.
|           |              |                 |     |     |         |      | Learning | to forget: | Continual |     | prediction |     | with LSTM. |
| --------- | ------------ | --------------- | --- | --- | ------- | ---- | -------- | ---------- | --------- | --- | ---------- | --- | ---------- |
| Arjovsky, | Martin,Shah, | Amar,andBengio, |     |     | Yoshua. | Uni- |          |            |           |     |            |     |            |
Neuralcomputation,12(10):2451–2471,2000.
| tary evolution |     | recurrent | neural | networks. | In  | Interna- |     |     |     |     |     |     |     |
| -------------- | --- | --------- | ------ | --------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- |
tionalconferenceonmachinelearning, pp.1120–1128. Gers, Felix A, Pe´rez-Ortiz, Juan Antonio, Eck, Dou-
PMLR,2016.
|     |     |     |     |     |     |     | glas, and | Schmidhuber, |     | Ju¨rgen. | DEKF-LSTM. |     | In  |
| --- | --- | --- | --- | --- | --- | --- | --------- | ------------ | --- | -------- | ---------- | --- | --- |
10thEuropeanSymposiumonArtificialNeuralNetworks
| Baldi, Pierre, | Brunak, | Søren, | Frasconi, |     | Paolo, Soda, | Gio- |     |     |     |     |     |     |     |
| -------------- | ------- | ------ | --------- | --- | ------------ | ---- | --- | --- | --- | --- | --- | --- | --- |
(ESANN),2002.
| vanni, | and Pollastri, |     | Gianluca. | Exploiting |     | the past |     |     |     |     |     |     |     |
| ------ | -------------- | --- | --------- | ---------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- |
andthefutureinproteinsecondarystructureprediction. Ghojogh, Benyamin, Karray, Fakhri, and Crowley, Mark.
Bioinformatics,15(11):937–946,1999.
|     |     |     |     |     |     |     | Eigenvalueandgeneralizedeigenvalueproblems: |     |     |     |     |     | Tuto- |
| --- | --- | --- | --- | --- | --- | --- | ------------------------------------------- | --- | --- | --- | --- | --- | ----- |
rial. arXivpreprintarXiv:1903.11240,2019a.
| Bayer, | Justin, | Wierstra, | Daan, | Togelius, | Julian, | and |     |     |     |     |     |     |     |
| ------ | ------- | --------- | ----- | --------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
Schmidhuber, Ju¨rgen. Evolvingmemorycellstructures Ghojogh, Benyamin, Karray, Fakhri, and Crowley, Mark.
for sequence learning. In International conference on Hidden Markov model: Tutorial. Engineering Archive,
artificialneuralnetworks,pp.755–764.Springer,2009.
2019b.
Bengio,Yoshua,Frasconi,Paolo,andSimard,Patrice. The Ghojogh, Benyamin, Ghodsi, Ali, Karray, Fakhri, and
problemoflearninglong-termdependenciesinrecurrent Crowley,Mark. KKTconditions,first-orderandsecond-
networks. In IEEE international conference on neural order optimization, and distributed optimization: Tuto-
networks,pp.1183–1188.IEEE,1993. rialandsurvey. arXivpreprintarXiv:2110.01858,2021.

14
Graves,Alex. Generatingsequenceswithrecurrentneural Hu, Yuhuang, Huber, Adrian, Anumula, Jithendar, and
networks. arXivpreprintarXiv:1308.0850,2013. Liu, Shih-Chii. Overcoming the vanishing gradient
|         |      |     |              |          |     |           | problem | in plain | recurrent | networks. |     | arXiv | preprint |
| ------- | ---- | --- | ------------ | -------- | --- | --------- | ------- | -------- | --------- | --------- | --- | ----- | -------- |
| Graves, | Alex | and | Schmidhuber, | Ju¨rgen. |     | Framewise |         |          |           |           |     |       |          |
arXiv:1801.06105,2018.
| phoneme | classification |     | with | bidirectional |     | LSTM and |     |     |     |     |     |     |     |
| ------- | -------------- | --- | ---- | ------------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- |
otherneuralnetworkarchitectures. Neuralnetworks,18 Huang, Zhiheng, Xu, Wei, and Yu, Kai. Bidirec-
(5-6):602–610,2005a.
|     |     |     |     |     |     |     | tional | LSTM-CRF | models | for | sequence | tagging. | arXiv |
| --- | --- | --- | --- | --- | --- | --- | ------ | -------- | ------ | --- | -------- | -------- | ----- |
preprintarXiv:1508.01991,2015.
| Graves, | Alex | and | Schmidhuber, | Ju¨rgen. |     | Framewise |     |     |     |     |     |     |     |
| ------- | ---- | --- | ------------ | -------- | --- | --------- | --- | --- | --- | --- | --- | --- | --- |
phonemeclassificationwithbidirectionallstmnetworks.
|                 |     |      |      |               |     |               | Jaeger, Herbert. |     | Tutorial | on training | recurrent | neural | net- |
| --------------- | --- | ---- | ---- | ------------- | --- | ------------- | ---------------- | --- | -------- | ----------- | --------- | ------ | ---- |
| In Proceedings. |     | 2005 | IEEE | International |     | Joint Confer- |                  |     |          |             |           |        |      |
works,coveringBPPT,RTRL,EKFandthe”echostate
| ence | on Neural | Networks, |     | 2005., | volume | 4, pp. 2047– |                   |     |       |     |     |     |     |
| ---- | --------- | --------- | --- | ------ | ------ | ------------ | ----------------- | --- | ----- | --- | --- | --- | --- |
|      |           |           |     |        |        |              | network”approach. |     | 2002. |     |     |     |     |
2052.IEEE,2005b.
|         |       |             |           |     |     |              | Jaeger, Herbert. |     | Echo state | network. | Scholarpedia, |     | 2(9): |
| ------- | ----- | ----------- | --------- | --- | --- | ------------ | ---------------- | --- | ---------- | -------- | ------------- | --- | ----- |
| Graves, | Alex, | Ferna´ndez, | Santiago, |     | and | Schmidhuber, |                  |     |            |          |               |     |       |
2330,2007.
| Ju¨rgen.                             | Bidirectional |     | LSTM | networks |                 | for improved |     |     |     |     |     |     |     |
| ------------------------------------ | ------------- | --- | ---- | -------- | --------------- | ------------ | --- | --- | --- | --- | --- | --- | --- |
| phonemeclassificationandrecognition. |               |     |      |          | InInternational |              |     |     |     |     |     |     |     |
Jaeger,HerbertandHaas,Harald.Harnessingnonlinearity:
| conference |     | on artificial | neural | networks, |     | pp. 799–804. |     |     |     |     |     |     |     |
| ---------- | --- | ------------- | ------ | --------- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- |
Predictingchaoticsystemsandsavingenergyinwireless
Springer,2005.
|         |       |          |               |     |     |             | communication. |     | Science,304(5667):78–80,2004. |     |     |     |     |
| ------- | ----- | -------- | ------------- | --- | --- | ----------- | -------------- | --- | ----------------------------- | --- | --- | --- | --- |
| Graves, | Alex, | Mohamed, | Abdel-rahman, |     | and | Hinton, Ge- |                |     |                               |     |     |     |     |
Jaeger,Herbert,Lukosˇevicˇius,Mantas,Popovici,Dan,and
| offrey.   | Speech | recognition |      | with deep     | recurrent | neural        |                |      |                       |     |                  |          |         |
| --------- | ------ | ----------- | ---- | ------------- | --------- | ------------- | -------------- | ---- | --------------------- | --- | ---------------- | -------- | ------- |
|           |        |             |      |               |           |               | Siewert,       | Udo. | Optimization          |     | and applications |          | of echo |
| networks. |        | In 2013     | IEEE | international |           | conference on |                |      |                       |     |                  |          |         |
|           |        |             |      |               |           |               | state networks |      | with leaky-integrator |     |                  | neurons. | Neural  |
acoustics,speechandsignalprocessing,pp.6645–6649.
networks,20(3):335–352,2007.
IEEE,2013.
|                          |     |     |                   |     |     |             | Jozefowicz, | Rafal, | Zaremba, | Wojciech, |     | and Sutskever, |     |
| ------------------------ | --- | --- | ----------------- | --- | --- | ----------- | ----------- | ------ | -------- | --------- | --- | -------------- | --- |
| Greff, Klaus,Srivastava, |     |     | RupeshK,Koutn´ık, |     |     | Jan,Steune- |             |        |          |           |     |                |     |
brink,BasR,andSchmidhuber,Ju¨rgen.LSTM:Asearch Ilya. An empirical exploration of recurrent network
|       |          |      |              |     |           |          | architectures. |     | In International |     | conference | on  | machine |
| ----- | -------- | ---- | ------------ | --- | --------- | -------- | -------------- | --- | ---------------- | --- | ---------- | --- | ------- |
| space | odyssey. | IEEE | transactions |     | on neural | networks |                |     |                  |     |            |     |         |
andlearningsystems,28(10):2222–2232,2016. learning,pp.2342–2350.PMLR,2015.
Heck, Joel C and Salem, Fathi M. Simplified minimal Lafferty, John, McCallum, Andrew, and Pereira, Fer-
gated unit variations for recurrent neural networks. In nando CN. Conditional random fields: Probabilis-
2017 IEEE 60th International Midwest Symposium on tic models for segmenting and labeling sequence data.
| CircuitsandSystems(MWSCAS),pp.1593–1596.IEEE, |     |     |     |     |     |     | 2001. |     |     |     |     |     |     |
| --------------------------------------------- | --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- |
2017.
|             |     |         |         |              |     |           | Lang,KevinJ,Waibel,AlexH,andHinton,GeoffreyE. |     |     |     |     |     | A   |
| ----------- | --- | ------- | ------- | ------------ | --- | --------- | --------------------------------------------- | --- | --- | --- | --- | --- | --- |
| Hihi, Salah | and | Bengio, | Yoshua. | Hierarchical |     | recurrent |                                               |     |     |     |     |     |     |
time-delayneuralnetworkarchitectureforisolatedword
neural networks for long-term dependencies. Advances recognition. Neuralnetworks,3(1):23–43,1990.
inneuralinformationprocessingsystems,8,1995.
|              |               |           |           |                 |     |               | Lin, Tsungnan,                         |          | Horne,    | Bill G.,     | Tino, | Peter, and | Giles,  |
| ------------ | ------------- | --------- | --------- | --------------- | --- | ------------- | -------------------------------------- | -------- | --------- | ------------ | ----- | ---------- | ------- |
| Hochreiter,  | Sepp.         | The       | vanishing | gradient        |     | problem dur-  |                                        |          |           |              |       |            |         |
|              |               |           |           |                 |     |               | C. Lee.                                | Learning | long-term | dependencies |       | is not     | as dif- |
| ing learning |               | recurrent | neural    | nets            | and | problem solu- |                                        |          |           |              |       |            |         |
|              |               |           |           |                 |     |               | ficultwithnarxrecurrentneuralnetworks. |          |           |              |       | Advancesin |         |
| tions.       | International |           | Journal   | of Uncertainty, |     | Fuzziness     |                                        |          |           |              |       |            |         |
neuralinformationprocessingsystems,1995.
andKnowledge-BasedSystems,6(02):107–116,1998.
Lipton,ZacharyC,Berkowitz,John,andElkan,Charles.A
| Hochreiter, | Sepp | and | Schmidhuber, |     | Ju¨rgen. | Long short- |     |     |     |     |     |     |     |
| ----------- | ---- | --- | ------------ | --- | -------- | ----------- | --- | --- | --- | --- | --- | --- | --- |
criticalreviewofrecurrentneuralnetworksforsequence
| term | memory. | Technical |     | report, | FKI-207-95, | Depart- |           |                                     |     |     |     |     |     |
| ---- | ------- | --------- | --- | ------- | ----------- | ------- | --------- | ----------------------------------- | --- | --- | --- | --- | --- |
|      |         |           |     |         |             |         | learning. | arXivpreprintarXiv:1506.00019,2015. |     |     |     |     |     |
mentofFakulta¨tfu¨rInformatik,TechnicalUniversityof
Munich,Munich,Germany,1995.
Mikolov,Tomas,Joulin,Armand,Chopra,Sumit,Mathieu,
|             |      |     |              |     |          |             | Michael, | and | Ranzato, | Marc’Aurelio. |     | Learning | longer |
| ----------- | ---- | --- | ------------ | --- | -------- | ----------- | -------- | --- | -------- | ------------- | --- | -------- | ------ |
| Hochreiter, | Sepp | and | Schmidhuber, |     | Ju¨rgen. | Long short- |          |     |          |               |     |          |        |
term memory. Neural computation, 9(8):1735–1780, memory in recurrent neural networks. Workshop at the
|     |     |     |     |     |     |     | International |     | Conference | on Learning |     | Representations, |     |
| --- | --- | --- | --- | --- | --- | --- | ------------- | --- | ---------- | ----------- | --- | ---------------- | --- |
1997.
2015.
| Hochreiter, | Sepp, |     | Bengio, | Yoshua, | Frasconi, | Paolo, |     |     |     |     |     |     |     |
| ----------- | ----- | --- | ------- | ------- | --------- | ------ | --- | --- | --- | --- | --- | --- | --- |
Schmidhuber, Ju¨rgen, et al. Gradient flow in recurrent Mozer, Michael C. A focused backpropagation algorithm
nets: the difficulty of learning long-term dependencies, fortemporalpatternrecognition.Backpropagation:The-
| 2001. |     |     |     |     |     |     | ory,architectures,andapplications,137,1995. |     |     |     |     |     |     |
| ----- | --- | --- | --- | --- | --- | --- | ------------------------------------------- | --- | --- | --- | --- | --- | --- |

15
Otte, Sebastian, Liwicki, Marcus, andZell, Andreas. Dy- Smagulova, Kamilya and James, Alex Pappachen. A sur-
namic cortex memory: Enhancing recurrent neural net- vey on LSTM memristive neural network architectures
works for gradient-based sequence learning. In Inter- and applications. The European Physical Journal Spe-
national Conference on Artificial Neural Networks, pp. cialTopics,228(10):2313–2324,2019.
1–8.Springer,2014.
|     |     |     |     |     |     |     | Staudemeyer, | Ralf | C and | Morris, Eric | Rothstein. | Un- |
| --- | --- | --- | --- | --- | --- | --- | ------------ | ---- | ----- | ------------ | ---------- | --- |
Peddinti,Vijayaditya,Povey,Daniel,andKhudanpur,San- derstanding LSTM–a tutorial into long short-term
jeev. A time delay neural network architecture for effi- memory recurrent neural networks. arXiv preprint
cient modeling of long temporal contexts. In Sixteenth arXiv:1909.09586,2019.
annualconferenceoftheinternationalspeechcommuni-
|     |     |     |     |     |     |     | Sugiyama, | Masahide, | Sawai, | Hidehumi, | and | Waibel, |
| --- | --- | --- | --- | --- | --- | --- | --------- | --------- | ------ | --------- | --- | ------- |
cationassociation,2015.
|     |     |     |     |     |     |     | Alexander | H. Review |     | of tdnn (time | delay | neural net- |
| --- | --- | --- | --- | --- | --- | --- | --------- | --------- | --- | ------------- | ----- | ----------- |
Peters, Matthew E, Ammar, Waleed, Bhagavatula, Chan- work) architectures for speech recognition. In 1991
dra,andPower,Russell. Semi-supervisedsequencetag- IEEEInternationalSymposiumonCircuitsandSystems
| gingwithbidirectionallanguagemodels. |     |     |     |     | InAssociation |     |     |     |     |     |     |     |
| ------------------------------------ | --- | --- | --- | --- | ------------- | --- | --- | --- | --- | --- | --- | --- |
(ISCAS),pp.582–585.IEEE,1991.
forComputationalLinguistics(ACL),2017.
|                 |        |              |     |              |        |             | Sutskever,IlyaandHinton,Geoffrey. |                  |     |                  | Temporal-kernelre- |            |
| --------------- | ------ | ------------ | --- | ------------ | ------ | ----------- | --------------------------------- | ---------------- | --- | ---------------- | ------------------ | ---------- |
| Peters, Matthew |        | E., Neumann, |     | Mark, Iyyer, | Mohit, | Gard-       |                                   |                  |     |                  |                    |            |
|                 |        |              |     |              |        |             | current                           | neural networks. |     | Neural Networks, |                    | 23(2):239– |
| ner, Matt,      | Clark, | Christopher, |     | Lee, Kenton, |        | and Zettle- | 243,2010.                         |                  |     |                  |                    |            |
moyer,Luke.Deepcontextualizedwordrepresentations.
|     |     |     |     |     |     |     | Werbos, Paul | J. Generalization |     | of backpropagation |     | with |
| --- | --- | --- | --- | --- | --- | --- | ------------ | ----------------- | --- | ------------------ | --- | ---- |
InNorthAmericanChapteroftheAssociationforCom-
putationalLinguistics(NAACL),2018. applicationtoarecurrentgasmarketmodel. Neuralnet-
works,1(4):339–356,1988.
| Robinson, | AJ  | and Fallside, | Frank. |     | The utility | driven |     |     |     |     |     |     |
| --------- | --- | ------------- | ------ | --- | ----------- | ------ | --- | --- | --- | --- | --- | --- |
dynamic error propagation network. Technical report, Williams,RonaldJ.Complexityofexactgradientcomputa-
Department of Engineering, University of Cambridge, tionalgorithmsforrecurrentneuralnetworks. Technical
| 1987. |     |     |     |     |     |     | report,NU-CCS-89-27,NortheasternUniversity,1989. |     |     |     |     |     |
| ----- | --- | --- | --- | --- | --- | --- | ------------------------------------------------ | --- | --- | --- | --- | --- |
Rumelhart, David E, Hinton, Geoffrey E, and Williams, Williams, Ronald J and Zipser, David. Gradient-based
RonaldJ. Learningrepresentationsbyback-propagating learning algorithms for recurrent networks and their
Nature,323(6088):533–536,1986.
| errors. |     |     |     |     |     |     | computational | complexity. |     | Backpropagation: |     | Theory, |
| ------- | --- | --- | --- | --- | --- | --- | ------------- | ----------- | --- | ---------------- | --- | ------- |
architectures,andapplications,433:17,1995.
| Sak, Hasim, | Senior, | Andrew | W,  | and Beaufays, |     | Franc¸oise. |     |     |     |     |     |     |
| ----------- | ------- | ------ | --- | ------------- | --- | ----------- | --- | --- | --- | --- | --- | --- |
Longshort-termmemoryrecurrentneuralnetworkarchi- Yu, Yong, Si, Xiaosheng, Hu, Changhua, and Zhang,
| tectures | for | large scale | acoustic | modeling. |     | In INTER- |          |                                   |     |     |     |      |
| -------- | --- | ----------- | -------- | --------- | --- | --------- | -------- | --------------------------------- | --- | --- | --- | ---- |
|          |     |             |          |           |     |           | Jianxun. | Areviewofrecurrentneuralnetworks: |     |     |     | LSTM |
SPEECH,2014.
|     |     |     |     |     |     |     | cellsandnetworkarchitectures. |     |     | Neuralcomputation,31 |     |     |
| --- | --- | --- | --- | --- | --- | --- | ----------------------------- | --- | --- | -------------------- | --- | --- |
(7):1235–1270,2019.
| Salehinejad, | Hojjat,      | Sankar,     |     | Sharan,   | Barfett, | Joseph,    |     |     |     |     |     |     |
| ------------ | ------------ | ----------- | --- | --------- | -------- | ---------- | --- | --- | --- | --- | --- | --- |
| Colak,       | Errol,       | and Valaee, |     | Shahrokh. |          | Recent ad- |     |     |     |     |     |     |
| vances       | in recurrent | neural      |     | networks. | arXiv    | preprint   |     |     |     |     |     |     |
arXiv:1801.01078,2017.
| Sarzynska-Wawer, |     | Justyna,     | Wawer,        | Aleksander, |                | Pawlak,  |     |     |     |     |     |     |
| ---------------- | --- | ------------ | ------------- | ----------- | -------------- | -------- | --- | --- | --- | --- | --- | --- |
| Aleksandra,      |     | Szymanowska, |               | Julia,      | Stefaniak,     | Izabela, |     |     |     |     |     |     |
| Jarkiewicz,      |     | Michal,      | and Okruszek, |             | Lukasz.        | Detect-  |     |     |     |     |     |     |
| ing formal       |     | thought      | disorder      | by deep     | contextualized |          |     |     |     |     |     |     |
wordrepresentations.PsychiatryResearch,304:114135,
2021.
| Schmidhuber, |                                       | Ju¨rgen. Deep                  | learning |              | in neural     | networks:   |     |     |     |     |     |     |
| ------------ | ------------------------------------- | ------------------------------ | -------- | ------------ | ------------- | ----------- | --- | --- | --- | --- | --- | --- |
| Anoverview.  |                                       | Neuralnetworks,61:85–117,2015. |          |              |               |             |     |     |     |     |     |     |
| Schmidhuber, |                                       | Ju¨rgen, Wierstra,             |          | Daan,        | Gagliolo,     | Matteo,     |     |     |     |     |     |     |
| and Gomez,   |                                       | Faustino.                      | Training | recurrent    |               | networks by |     |     |     |     |     |     |
| Evolino.     | Neuralcomputation,19(3):757–779,2007. |                                |          |              |               |             |     |     |     |     |     |     |
| Schuster,    | Mike                                  | and Paliwal,                   | Kuldip   | K.           | Bidirectional | re-         |     |     |     |     |     |     |
| current      | neural                                | networks.                      | IEEE     | transactions |               | on Signal   |     |     |     |     |     |     |
Processing,45(11):2673–2681,1997.