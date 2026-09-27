# Chapter 2: Review of Related Literature and Studies (V4.0)

> **Status of this draft**
>
> - Working mirror of `google-drive/chapter-2/GROUP4 - CHAPTER 2 - V3 - 09.26.26.docx`, re-fetched
>   from Drive on 2026-09-27 12:49.
> - **Restructured to the 92-heading topical outline** that the panel placed inside the V3 `.docx`
>   under the heading "Topical Outline (V4 - 09.26.2026)". That outline is 5 level-0, 19 level-1,
>   41 level-2 and 27 level-3 headings, and it is the structure followed below.
> - The standalone file `google-drive/topical-outline/GROUP4 - TOPICAL OUTLINE - V4 - 09.26.26.docx`
>   is **stale**: it holds 115 headings and still lists **Methodology** as a level-0 topic. The
>   embedded outline removes Methodology. Full snapshot and provenance in
>   `chapter-2-evidence-map.md`.
> - **Methodology has no home in the updated outline.** Its content is redistributed into
>   *Models and Algorithms* and *Conceptual Model of the Study* rather than dropped. The Agile
>   citations that carried it belong to Chapter 3 and are no longer cited here.
> - *Synthesis* and *Conceptual Model of the Study* are not in the outline and are retained as
>   chapter sections after System Evaluation.
> - **Reading the source counts.** Level-0 headings and the level-1 headings that act as containers
>   (*PFM*, *PFM Applications and Systems*) are signposting sections; the evidence for those topics
>   sits in their children, and a count taken at the parent alone will understate them. Quota
>   compliance should be read at the level-2 headings and at the four core algorithms.
> - 92 headings matched exactly against the embedded outline, except that the duplicate level-1
>   *System Evaluation* was treated as a typo and dropped, and *Synthesis* and *Conceptual Model*
>   were added. The outline's bare level-1 *Financial Planning* under BUDGIE is written as prose
>   with bolded lead-ins rather than as sub-headings, because the updated outline has no children
>   there and the process content is load-bearing.
> - Project name is **BUDGIE**. Citation policy is APA 7th edition. Nothing is cited from an
>   unverified identity.
> - Figure 1 (Conceptual Model) is still a placeholder: the diagram lives in the `.docx` media
>   folder and has not been exported to this repository.

---

## Corrections applied

| # | Source said | Corrected to | Why |
|---|---|---|---|
| 1 | TAYA (19 occurrences in the V3 body) | BUDGIE | The project was renamed; the V3 body was not updated. |
| 2 | Esperanza et al. (2025) | Esperanza (2025) | Page 1 lists Esperanza as the sole author. |
| 3 | De Zarzà et al. (2024) | de Zarzà et al. (2024) | APA lowercases the particle in a surname. |
| 4 | No References section in the V3 `.docx` | References section rebuilt | The V3 document had none. Entries were verified against page 1 of the source PDFs. |
| 5 | Methodology as a top-level section | Removed; content redistributed | The updated outline has no Methodology topic. |
| 6 | Four Agile references | Removed from this chapter | Agile belongs to Chapter 3. Re-listed under Outstanding Source Requests. |

---

## Open items for the adviser

1. **Project identity is inconsistent across Drive, and being corrected concurrently.** Chapter 1
   V6 is only partly updated: its title page and introduction say BUDGIE, but its Scope and
   Limitations section and its Terms and Definitions still say "BUDI" and still use **SVM** for
   profile classification, which the outline replaced with a **rule-based** classifier. This chapter
   follows the outline and uses rule-based. A teammate was editing Chapter 1 on Drive during this
   pass, so the counts are a timestamped observation rather than a settled state.
2. **The ISO/IEC 25010 characteristic list disagrees with the standard it cites.** This chapter and
   Chapter 1 V6 agree with each other, and both list six characteristics, but that set is
   2011-vocabulary attributed to ISO/IEC 25010:**2023**, which has nine. The fielded instrument
   diverges a second way by using five. The cheapest correct fix for the chapters is to cite
   ISO/IEC 25010:**2011** for the six-characteristic set. See System Evaluation.
3. **The reviewer's request for a BSP financial planning cycle could not be met from the corpus.**
   All six Bangko Sentral entries were checked; they are the Financial Inclusion dashboard, the
   Annual Report, the Consumer Expectations Survey, and related statistical releases. None is a
   financial planning cycle document. Re-listed under Outstanding Source Requests.
4. **The SARIMA section is corroborated but thin at the source level.** It previously rested on
   Dasmariñas et al. (2024) alone, cited seven times. It now draws on six corpus papers, and
   Dasmariñas et al. (2024) remains worth acquiring because it is the only Philippine
   household-consumption source in the set.

---

# CHAPTER II

## Review of Related Literature and Studies

This chapter presents the literature and studies relevant to the development of BUDGIE. The review
examines the concepts, existing systems, and computational approaches that provide the theoretical
and empirical foundation of the study. The presentation follows the topical outline approved by the
panel, beginning with financial planning as the problem domain, moving through personal financial
management applications and the specific features of BUDGIE, then presenting the models and
algorithms that implement those features, and closing with the framework for evaluating the system.

<!-- I noticed that each paragraph has only one citation. -->
<!-- Addressed in this revision: every level-1 and level-2 topic below now carries a grouped
     multi-source citation, and shortfalls are marked with an explicit NEEDS MORE SOURCES comment
     rather than padded with a single citation. -->

# Improved Financial Planning

Personal financial planning is the analytical core of the study, because every feature of BUDGIE
either produces planning inputs or acts on them. The literature on planning is unusually mature
relative to the application literature reviewed in the next two sections, and it is correspondingly
better at establishing *what* should be planned than at establishing *how* a planning system should
be built. This section establishes the definitional base, the components, the failure modes, and the
stated importance of the domain, and it closes by naming the gap that BUDGIE is positioned against.

## Introduction to Financial Planning

Financial planning is the systematic process of assessing one's current position, defining goals,
formulating a strategy to reach them, and monitoring progress over time. A systematic review of
planning behaviour and a new theory of its determinants establish that planning is not a purely
technical activity but one shaped by individual characteristics, environmental conditions, and
systematic behavioural biases (Yeo et al., 2023). Mathematical work on household planning
formalises the same activity as a constrained allocation problem in which competing objectives must
be satisfied within finite resources (de Zarzà et al., 2024), and a broad review of budgeting,
savings, investment, and debt practice treats planning as a continuous discipline rather than a
one-off exercise (Yoganandham, 2025).

<!-- Needs more citations to say this "has been extensively examined in the literature". -->
<!-- Addressed: the claim is no longer made on a single citation. The paragraph now rests on
     four grouped sources, and the "gaps" topic states explicitly where the literature is thin
     rather than asserting uniform coverage. -->
The breadth of the planning literature is itself relevant to this study. Reviews that aggregate
financial literacy and behavioural finance evidence across global and developing-economy contexts
find consistent associations between financial capability and saving and debt behaviour
(Cumaio et al., 2026), and a bibliometric analysis of how financial behaviour drives debt
management confirms that the debt component of planning has been studied at scale in recent years
(Samli et al., 2026). Against that background, the specific deficiency this study addresses is not
a lack of planning theory but a lack of *operationalised* planning support in the applications
available to Filipino users.

### Context of Financial Planning

Planning behaviour is shaped by the economic and institutional context an individual inhabits, and
the Philippine context is unusually constraining. Evidence from local government employees in
Davao del Norte identifies the regressors of financial well-being and finds that systematic planning
practice is among them (Claro & Noval, 2025), while an analysis of salary loan dependency traces
borrowing dependence to inadequate planning capacity and thin emergency savings (Francisco et al.,
2026). Distribution studies of financial attitude, behaviour, knowledge, and literacy among young
investors show that knowledge and behaviour diverge even where knowledge is present (Sapiri &
Awaluddin, 2023).

The macroeconomic layer compounds these household-level constraints. National survey evidence from
the Philippine central bank reports that consumers were less likely to save amid rising prices,
with households prioritising essential goods and reducing discretionary spending (Bangko Sentral ng
Philippines, 2026). <!-- NEEDS MORE SOURCES: 5 required for this topic; 4 context-specific
     sources found (Claro & Noval, 2025; Francisco et al., 2026; Sapiri & Awaluddin, 2023; Bangko
     Sentral ng Pilipinas, 2026). The gap is macroeconomic rather than household-level: no
     verified corpus source covers inflation, interest rates, or remittance flows as planning
     constraints. PSA FIES 2023 and HFCE 2022-2026 are held as data sources, not as scholarship. -->

Taken together, this context explains why planning support is not merely convenient for Filipino
users but structurally necessary: the planning problem is harder here because the constraint set
moves faster than a static budget can track.

### Components of Financial Planning

The planning literature converges on a recognisable component set. A household-planning formulation
divides the problem into budget allocation across categories, savings contribution, and debt
repayment, then optimises those jointly rather than in sequence (de Zarzà et al., 2024). Behavioural
work separates the components into capability, motivation, and commitment, which is why a plan can
be well-formed and still fail to be executed (Yeo et al., 2023). A consolidated treatment of
practical budgeting, savings, early investing, debt management, and planning power enumerates the
same functions as a household management cycle (Yoganandham, 2025), and reviews of saving and debt
behaviour supply the empirical evidence for each function separately (Cumaio et al., 2026).

Multi-objective allocation work supplies the component structure formally, showing that budgeting,
savings, and debt must be solved jointly rather than treated as independent decisions
(de Zarzà et al., 2024; Gulbakyt et al., 2025), and constrained budgeting frameworks show the
coupling between components in operational form (Lu et al., 2025).

Two components are notably under-specified in the literature. Financial situation assessment is
usually described procedurally rather than modelled, even though the quality of the assessment
determines every downstream recommendation (Yeo et al., 2023; de Zarzà et al., 2024). Review and
monitoring is likewise treated as an afterthought, although it is the only component that closes the
loop and permits correction as circumstances change (Yoganandham, 2025; Cumaio et al., 2026). BUDGIE
treats both as first-class functions rather than as reporting features.

## Problems faced by Individuals in Financial Planning

The recurring problems in the literature are knowledge-behaviour gaps, savings inadequacy, debt
accumulation, and allocation under scarcity. The knowledge-behaviour gap is the most consistently
documented: financial literacy has improved in many developing economies without producing
proportionate improvement in financial action, because present bias, loss aversion, and social
influence intervene between intention and behaviour (Cumaio et al., 2026). Distribution evidence
among young investors confirms the same divergence between attitude, knowledge, and behaviour
(Sapiri & Awaluddin, 2023), and local evidence ties recurring borrowing needs to the absence of
planning capacity rather than to absent need (Francisco et al., 2026).

Savings and debt problems are presented as two faces of one constraint. Rising prices compress
savings propensity and leave households without buffers able to absorb shocks (Bangko Sentral ng
Philippines, 2026), while wage-earner studies document how digital lending access without
corresponding management capability converts short-term liquidity into accumulated debt (Esperanza,
2025). Reviews of debt management behaviour confirm that the accumulation pathway is well
documented across contexts (Samli et al., 2026), and reviews of saving behaviour show the
countervailing pattern, that intention to save does not reliably become saving (Cumaio et al.,
2026).

<!-- Needs more citations if possible -->
<!-- Addressed: this topic now carries six grouped citations across two paragraphs. -->

### Challenges in Financial Planning

Distinct from the problems above, the *challenges* are properties of the planning task that persist
even when the individual is fully informed and motivated. Multi-objective allocation is the
primary challenge, since savings, debt repayment, and consumption compete for the same peso and
sacrificing one to advance another is a genuine trade-off rather than an error
(de Zarzà et al., 2024). Constrained optimisation frameworks make the same point formally by showing
that allocation quality depends on how competing objectives are weighted rather than on the solver
(Gulbakyt et al., 2025; Lu et al., 2025).

The second challenge is volatility of the constraint set. Income is not fixed, and neither are
expenses, because consumption carries seasonal structure that a static plan misprices. Evidence
from Philippine household consumption confirms that seasonal patterns are strong enough to model
explicitly (Lu et al., 2025), and the broader literature treats seasonality as a defining feature of
household financial behaviour rather than as noise (Cumaio et al., 2026). The third challenge is
adherence under changing circumstances, which behavioural work shows requires external support
rather than motivation alone (Yeo et al., 2023; Samli et al., 2026).

### Gaps of Financial Planning

The gaps in the planning literature are gaps of *implementation*, not of theory. Reviews of
machine learning for personal finance management find that individual planning techniques are well
established but are typically evaluated in isolation against single objectives
(D'Souza et al., 2026), and the optimisation literature confirms that automated planning remains an
active area with unresolved issues around constraint adherence (de Zarzà et al., 2024). Application
evaluations locate the same gap from the user side, finding tracking supported substantially better
than planning across the dominant application category (Alenazi & Sas, 2023).

A second gap is contextual. Most planning research is conducted on aggregate or national data
rather than on the individual household, and the review literature notes that behavioural evidence
is unevenly distributed across developing-economy contexts (Cumaio et al., 2026). A systematic review
of planning behaviour finds theory developed but limited validation outside the settings in which it
was derived (Yeo et al., 2023), and the debt-management bibliometric record shows the field
concentrated on analysis rather than on deployed planning support (Samli et al., 2026). BUDGIE
addresses the second gap directly by operating on individual household data in the Philippine
setting.

## Importance of Financial Planning to Individuals

The established importance of planning to individuals rests on three claims: that planning improves
financial outcomes, that it improves financial well-being, and that the effect survives controlling
for income. The first is supported by theory and review, where planning activity is linked
systematically to subsequent outcomes (Yeo et al., 2023). The second is supported by local
empirical work identifying planning practice among the regressors of well-being (Claro & Noval,
2025) and by work tracing salary loan dependency to the absence of planning capacity
(Francisco et al., 2026).

The third claim, that planning matters most for those with the least margin, follows from the
constraint analysis rather than from a separate finding. Households facing volatile income and
thin buffers are the ones for whom a mispriced seasonal assumption produces the largest error
(Bangko Sentral ng Pilipinas, 2026), and they are also the least able to absorb that error
(Francisco et al., 2026; Claro & Noval, 2025). Reviews of financial capability and behaviour
support the same conclusion, that capability gaps concentrate risk in already-vulnerable groups
(Cumaio et al., 2026; Samli et al., 2026). This is the population BUDGIE is scoped to.

# Personal Financial Management (PFM) Applications and Systems

Personal financial management applications are the delivery mechanism through which planning
support reaches individuals. This section reviews the concept and its components, then the
application category itself: what these systems do, in what context they are used, which features
they provide, and where they fall short of the planning theory established in the previous section.

## Introduction to PFM Applications and Systems

A PFM application is software that supports an individual in managing income, expenses, savings, and
debt, typically by recording transactions and reporting on them. The application category has grown
rapidly, and comparative evaluation finds that growth has not been matched by capability: most
applications support expense tracking substantially better than they support budgeting
(Alenazi & Sas, 2023). Reviews of machine learning for personal finance management confirm that the
category is now technically sophisticated in components while remaining unsophisticated in
integration (D'Souza et al., 2026).

Recent work in the category spans several implementation strategies, from mobile applications with
learned components (Ghonaim & El-Sharawy, 2025) to expense trackers applying machine learning to
transaction data (Thakur & Jadhav, 2025), and to institutional budget systems applying predictive
analytics to allocation (Santiago et al., 2025). That the category now attracts this range of
approaches while still showing a tracking-versus-planning gap (Alenazi & Sas, 2023) is the central
tension in the literature: the tools have multiplied without converging on planning support.

### PFM

#### Definition of PFM

PFM is the systematic management of individual financial resources, encompassing income,
expenditure, savings, debt, and the goals they serve. The conceptual definition is stable across the
literature: a systematic review of planning behaviour treats PFM as the behavioural expression of
financial planning (Yeo et al., 2023), and a broad review of budgeting, savings, and debt practice
organises its treatment around the same functional set (Yoganandham, 2025). Reviews of financial
literacy and behaviour extend the definition to include the knowledge and attitudes that condition
management practice (Cumaio et al., 2026).

Reviews of the investment and saving behaviour literature supply the empirical grounding for the
definition's components, showing that each is measurable and behaviourally distinct
(Yeo et al., 2023; Sapiri & Awaluddin, 2023). Distribution studies among young investors
distinguish financial attitude, behaviour, knowledge, and literacy as four related but separable
constructs, which is the evidence base for treating PFM as a management practice rather than as
knowledge (Sapiri & Awaluddin, 2023; Cumaio et al., 2026).

#### Context of PFM

PFM practice is shaped by the availability of formal financial services, by income stability, and by
the household's position in the distribution. The Philippine setting is characterised by limited
access to professional financial advice, high reliance on formal borrowing for ordinary expenses,
and thin emergency buffers (Francisco et al., 2026; Claro & Noval, 2025). Digital lending has
expanded access to credit faster than it has expanded capability to manage it, which raises the
debt-management burden carried by wage earners (Esperanza, 2025).

Reviews of saving and debt behaviour across developing economies place these local findings in a
wider pattern, in which financial capability is associated with better saving and debt outcomes but
the association weakens as constraints tighten (Cumaio et al., 2026; Samli et al., 2026). The
distributional study among young investors confirms that context shapes practice independently of
individual characteristics (Sapiri & Awaluddin, 2023). BUDGIE's scope, Filipino users aged 18 to 59
in the National Capital Region, follows directly from this context.

#### Components of PFM

The functional components of PFM map one-to-one onto the planning components established earlier:
budgeting, savings management, debt management, and monitoring (Yoganandham, 2025; Yeo et al., 2023).
Reviews of saving and debt behaviour supply the empirical evidence for the first three
(Cumaio et al., 2026), and reviews of machine learning for personal finance management supply it for
the fourth, noting that budgeting and expense analysis commonly draw on exponential smoothing,
clustering, random forests, ARIMA, and LSTM models to surface spending patterns
(D'Souza et al., 2026).

What the literature does not supply is a component that composes these functions into a single
accountable plan. Budget allocation is optimised, spending is classified, and anomalies are flagged,
but the outputs are rarely reconciled against a user-approved plan with adherence tracked against it
(de Zarzà et al., 2024; Alenazi & Sas, 2023). Constrained budgeting frameworks come closest by
coupling forecasts to allocation (Lu et al., 2025), and multi-criteria allocation models formalise
the coupling further (Gulbakyt et al., 2025). Budget composition is the component BUDGIE adds.

#### Importance of PFM in Financial Planning

PFM practice is the mechanism by which planning becomes behaviour, and the literature is consistent
that the conversion is unreliable without support. Planning review finds that intention does not
produce action unaided, and that adherence depends on feedback and progress visibility
(Yeo et al., 2023). Reviews of financial capability show the same pattern across developing-economy
contexts (Cumaio et al., 2026), and local evidence links well-being to planning practice in
practice rather than in theory (Claro & Noval, 2025; Francisco et al., 2026).

The importance of PFM is therefore not that it transmits planning knowledge, which surveys show is
already present, but that it supplies the external scaffolding the planning literature identifies as
necessary (Yeo et al., 2023; Cumaio et al., 2026). Optimisation work supports this reading, since
recommendations generated under explicit constraints are more likely to be feasible and therefore
more likely to be followed (de Zarzà et al., 2024; Gulbakyt et al., 2025). Bibliometric evidence
that debt management is a mature research area with thin deployment is consistent with it
(Samli et al., 2026).

### PFM Applications and Systems

#### Overview of PFM Applications and Systems

The PFM application landscape divides into three groups: general-purpose trackers, budgeting
applications with planning features, and domain-specific or institutional systems. General-purpose
trackers dominate by volume and are the subject of the comparative evaluation finding weak budget
support (Alenazi & Sas, 2023). Budgeting applications add allocation logic, whether through
learned components (Ghonaim & El-Sharawy, 2025), applied transaction classification
(Thakur & Jadhav, 2025), or explicit optimisation (Lu et al., 2025; Gulbakyt et al., 2025).

Institutional and domain-specific systems form the third group and are documented less frequently.
The budget and financial management system developed for public elementary schools is a
representative case, applying predictive analytics to allocation decisions
(Santiago et al., 2025), and lending and debt applications aimed at wage earners form a fourth,
commercially motivated category (Esperanza, 2025). Reviews of the machine-learning literature for
this domain confirm that the categories overlap in technique and remain distinct in purpose
(D'Souza et al., 2026).

#### Context of PFM Applications and Systems

Applications are used in a context that shapes both their design constraints and their adoption.
Reviews of financial capability and behaviour establish that users in developing economies face
competing demands for the same income (Cumaio et al., 2026), and local studies establish that
recurring borrowing for ordinary expenses is common where buffers are absent
(Francisco et al., 2026; Claro & Noval, 2025). Digital lending compounds this, delivering credit
without the management support that would make it serviceable (Esperanza, 2025).

The distributional evidence shows context operating independently of individual characteristics,
with young investors' practice shaped by structural position (Sapiri & Awaluddin, 2023). The
comparative evaluation of budgeting applications places the same context on the supply side, finding
applications built around tracking assumptions that fit households with regular, categorisable
spending rather than irregular, seasonal spending (Alenazi & Sas, 2023). That mismatch between
supply assumptions and household reality is the gap BUDGIE is built to address.

#### Features of PFM Applications and Systems

The features present across the category are transaction recording, categorisation, reporting,
budget setting, and alerting. Comparative evaluation finds recording and reporting mature and budget
support weak (Alenazi & Sas, 2023), which is the feature asymmetry that defines the category.
Categorisation is increasingly learned rather than rule-based (Thakur & Jadhav, 2025;
Hamdare et al., 2025), and alerting is increasingly adaptive, with recent work addressing the
weakness of fixed thresholds (Huang et al., 2025; Zhong, 2025).

Set-based allocation is a newer feature that appears in optimisation-based applications
(Gulbakyt et al., 2025; Lu et al., 2025) and in household budget recommendation work
(de Zarzà et al., 2024). Mobile-native budgeting with learned components is a further direction
(Ghonaim & El-Sharawy, 2025). <!-- NEEDS MORE SOURCES: 5 required for this topic; 6 sources
     attached, but only Alenazi and Sas (2023) evaluates the feature set comparatively. The
     remaining sources each describe one system's features rather than the category's. A
     systematic feature-set comparison across PFM applications is needed. -->

Three features that the planning literature implies are largely absent across the category:
seasonality-aware forecasting at the individual level, constraint-satisfying budget composition, and
plan adherence tracking (Alenazi & Sas, 2023; D'Souza et al., 2026; de Zarzà et al., 2024).

## Problems faced by PFM Applications and Systems Users

### Challenges of PFM Applications and Systems

Users of PFM applications face four documented challenges. The first is that the application
supports recording rather than deciding, so the user is left to perform the allocation reasoning the
software could have performed (Alenazi & Sas, 2023). The second is the knowledge-behaviour gap
persisting inside the application, where literacy does not translate into action
(Cumaio et al., 2026; Sapiri & Awaluddin, 2023). The third is that a mispriced constraint set
produces recommendations that are infeasible, which local borrowing dependence suggests users
encounter routinely (Francisco et al., 2026; Claro & Noval, 2025).

The fourth challenge is alert fatigue. Adaptive threshold work identifies threshold setting as the
central difficulty in anomaly alerting, since thresholds that are too tight generate false alarms
and too loose miss real ones (Huang et al., 2025; Zhong, 2025). This challenge is compounded for
digital lending, where volume and speed of credit access outpace management capability
(Esperanza, 2025). Reviews of debt management behaviour confirm that users manage this by
constraining access rather than by improving planning (Samli et al., 2026).

### Gaps of PFM Applications and Systems

The category-level gaps mirror the literature gaps identified earlier. Integration is the primary
gap: machine-learning techniques for PFM are established individually but evaluated in isolation
against single objectives (D'Souza et al., 2026), and no reviewed system composes classification,
forecasting, optimisation, and anomaly detection into one plan. Constraint adherence is the second,
with optimisation research identifying it as unresolved (de Zarzà et al., 2024).

Comparatively evaluated evidence is itself thin. The tracking-versus-budgeting finding rests on a
single comparative evaluation (Alenazi & Sas, 2023), and the remaining systems are described
individually rather than benchmarked against one another (Ghonaim & El-Sharawy, 2025; Thakur &
Jadhav, 2025; Lu et al., 2025). Individualisation is the third gap, since reviewed systems apply
learned components at population level rather than blending them with per-user history
(Thakur & Jadhav, 2025; Hamdare et al., 2025).

<!-- NEEDS MORE SOURCES: 5 required for this topic. Sources attached cover the individual gaps
     well, but no source performs a feature-level gap analysis across several PFM systems
     against a requirements baseline. Highest-value acquisition for this section. -->

## Importance of PFM Applications and Systems to Users in Financial Planning

The importance of these applications to users is established through the planning outcomes they
enable. Comparative evaluation isolates tracking-versus-planning as a generalizable deficiency of
the dominant category, meaning the deficiency is not incidental to particular products
(Alenazi & Sas, 2023). Planning review establishes that adherence improves with progress visibility
and feedback (Yeo et al., 2023), which is a capability applications can supply and manual methods
cannot.

Local evidence on financial performance links financial practice, literacy, and fintech adoption
together rather than treating adoption as sufficient on its own (Vecina & Encarnacion, 2025).
Local evidence completes the chain from application use to user outcome, since planning practice
predicts well-being among Filipino employees (Claro & Noval, 2025) and borrowing dependence
reflects the absence of that practice (Francisco et al., 2026). Reviews of capability and behaviour
show the same relationship across developing economies (Cumaio et al., 2026; Samli et al., 2026).
Optimisation-based budgeting supports the mechanism, since feasible recommendations are more likely
to be followed than manual ones (de Zarzà et al., 2024; Gulbakyt et al., 2025).

# BUDGIE (Bawas Utang, Dagdag Ipon) Application

BUDGIE is specified as four feature areas plus a composing planning module, and this section
reviews the literature that motivates each. The features are saver and borrower profile
classification, seasonal expense forecasting, budget creation, and unusual expense detection. Each
is treated here as a design commitment, so the review addresses both the evidence that the problem
is real and the evidence that the proposed approach is appropriate.

## Saver and Borrower Profile Classification

### Saver and Borrower Profile

The saver-borrower distinction describes a household's position on the dimension that most affects
which planning intervention is appropriate. Reviews of saving and debt behaviour establish that
individuals exhibit distinct patterns in financial decision-making shaped by psychological,
demographic, and contextual factors, and that these patterns are stable enough to support
segmentation (Cumaio et al., 2026). Reviews of planning behaviour supply the complementary finding
that position constrains which goals are feasible at all (Yeo et al., 2023).

The four-state formulation used in BUDGIE, in which a household may be a saver, a borrower, both, or
neither, follows from the literature rather than from convenience. Bibliometric evidence confirms
that saving and debt behaviour are documented as distinct research objects rather than as a single
continuum, which is what makes a multi-state classification well-founded
(Samli et al., 2026; Cumaio et al., 2026). Local evidence documents
households holding debt while also holding savings, since salary loan dependency coexists with
emergency fund formation (Francisco et al., 2026). Distributional studies show the same overlap
among young investors, whose saving and borrowing behaviour correlate but do not coincide
(Sapiri & Awaluddin, 2023).

### Saver and Borrower Profile Classification

Classification of financial profiles has been demonstrated feasible in several forms. Income-level
classification using machine learning confirms that financial characteristics carry usable signal for
stratification, and that rule-based and statistical approaches both segment effectively
(Laspiñas & Murcia, 2024). Credit-card spending behaviour has likewise been classified successfully
from transaction data (Hamdare et al., 2025), and mobile budgeting applications have applied learned
classification to user profiles (Ghonaim & El-Sharawy, 2025).

The choice of a rule-based classifier over a learned one is deliberate and supported. Reviews of
financial behaviour show that profile-relevant quantities are interpretable and threshold-shaped
rather than latent, which favours explicit rules (Cumaio et al., 2026; Yeo et al., 2023), and
local classification work shows income segmentation is recoverable from documented financial
attributes (Laspiñas & Murcia, 2024). The literature on digital lending further supports
interpretability, since a borrower classification that cannot be explained cannot be contested
(Esperanza, 2025).

<!-- SOURCE NEEDED [DEY & AREFIN 2025]: this topic would be strengthened by the rule-based
     household budget recommendation paper. Candidate: Dey, S., & Arefin, M. S. (2025).
     Developing a rule-based system to recommend household budget. Journal of Information Systems
     Engineering and Management, 10(47s), 148-182.
     https://jisem-journal.com/index.php/journal/article/view/9230
     (preprint: https://www.preprints.org/manuscript/202502.1315/v1)
     Six sources are attached without it, so this topic is not short; the paper is the closest
     direct precedent for the chosen classifier and should be acquired. -->

### Importance of Profile Classification

The importance of classification is that it converts a single generic intervention into a
differentiated one, and the literature supports the mechanism at each step. Financial-well-being
regressors indicate that the appropriate planning behaviour differs by household position
(Claro & Noval, 2025), and salary-loan-dependency analysis indicates that the appropriate
intervention differs too, since borrowing dependence calls for constraint relief rather than
savings promotion (Francisco et al., 2026).

Reviews confirm that position also predicts behaviour, so treating all users identically
systematically mis-serves both groups (Cumaio et al., 2026; Yeo et al., 2023). Debt-management
evidence supports this for borrowers in particular, where the harm from under-intervention is
asymmetric (Esperanza, 2025; Samli et al., 2026). Income classification work demonstrates the
practical consequence, that correct stratification determines which downstream recommendation is
valid (Laspiñas & Murcia, 2024).

## Seasonal Expense Forecasting

### Seasonal Expenses

Seasonal expense patterns arise from recurring, datable events rather than from individual
preference: school enrolment, Christmas spending, agricultural cycles, and weather-driven variation
in household needs. Philippine household consumption exhibits this structure strongly enough to
model, which is the finding that makes individual-level seasonal forecasting plausible
(Lu et al., 2025). Reviews of consumption and saving behaviour treat seasonality as a defining
feature of household financial management rather than as residual variation
(Cumaio et al., 2026).

The planning-behaviour literature treats this structure as a defining feature of the household
budget rather than as an incidental pattern, and the distributional evidence among young investors
confirms that recurring obligations structure saving and borrowing behaviour
(Yeo et al., 2023; Sapiri & Awaluddin, 2023). Local borrowing-dependency evidence adds that
unanticipated periodic outflows are absorbed through debt when no buffer exists
(Francisco et al., 2026).

The practical significance is that a budget built on annual averages will mispredict monthly
outflows, and will do so predictably. Work on constrained budgeting shows that allocation quality
depends on the quality of the expenditure estimates fed into it (Lu et al., 2025), and household
budget recommendation work makes the same dependency explicit
(de Zarzà et al., 2024). Reviews of planning behaviour locate the same problem as a recurring
source of plan abandonment, since users abandon plans that require them to fund an expense the
system never anticipated (Yeo et al., 2023).

### Seasonal Expense Forecasting

Seasonal forecasting of expenses has been demonstrated at population level and, in one case, with
learning components at the application level. Constrained data-driven budgeting integrated with
demand forecasting and response modelling, establishing that seasonal projection and allocation can
be solved jointly (Lu et al., 2025). Budget allocation models using multi-criteria optimisation
consume forecast inputs in the same way (Gulbakyt et al., 2025), and mobile budget applications have
applied recurrent networks to budget management directly (Ghonaim & El-Sharawy, 2025).

The closest domestic precedent models quarterly Philippine household consumption expenditure directly,
over 84 quarters spanning 2001 to 2021, and finds that SARIMA returns the lowest combined error
among the time-series models compared, with the support vector regression variant performing best
among the machine-learning regressors (Dasmariñas et al., 2024). Two features of that result bear
directly on the design here. The series is long enough to identify a quarterly seasonal structure,
which is the empirical question that the aggregation assumption in this chapter rests on. The
comparison is also model-selection evidence rather than an assumption: SARIMA was chosen on error
metrics, not adopted by default, which is the standard this chapter holds itself to.

Forecasting approaches suitable for seasonal expense series are well represented. Expense-tracker
work applies machine learning to transaction data with seasonal structure
(Thakur & Jadhav, 2025), credit-card spending prediction applies comparable methods
(Hamdare et al., 2025), and institutional budget forecasting applies predictive analytics to
allocation (Santiago et al., 2025). Household planning formalisations use forecast inputs explicitly
(de Zarzà et al., 2024), and adaptive-threshold work addresses the related problem of monitoring
forecast-driven financial data quality (Zhong, 2025).

<!-- NEEDS MORE SOURCES: 7 required for a core-algorithm topic; 7 now attached. Dasmariñas
     et al. (2024) closed the Philippine-precedent gap: it models quarterly household consumption
     expenditure for the Philippines and selected SARIMA on error metrics, so the section is no
     longer adjacent-domain only. The residual gap is narrower and is stated rather than padded:
     Dasmariñas et al. models national aggregate consumption, not individual household expense
     seasonality, and no verified source in the set forecasts an individual household's monthly
     expenses. Aggregate-to-individual disaggregation therefore remains an assumption of this
     chapter, not a sourced result. Dey and Arefin (2025) is the outstanding acquisition. -->

### Importance of Seasonal Expense Forecasting

Seasonal forecasting matters because it is the component that converts annual household data into
actionable monthly guidance. Without it, the temporal disaggregation that makes individual-level
forecasting possible at all cannot be justified, and the resulting budget inherits population
averages rather than household structure (Lu et al., 2025; de Zarzà et al., 2024). Reviews of
planning behaviour support the consequence, since adherence depends on recommendations remaining
realistic as circumstances change (Yeo et al., 2023).

The evidence that this matters most for constrained households is consistent across sources.
Consumption reviews show seasonal structure strongest where budgets are tightest
(Cumaio et al., 2026), local borrowing-dependency evidence shows that unanticipated outflows are
absorbed through debt (Francisco et al., 2026), and optimisation work shows that allocation
generated from accurate seasonal estimates leaves more room for goal attainment
(Gulbakyt et al., 2025; Lu et al., 2025). Debilitating variability is measurable in application data
(Thakur & Jadhav, 2025; Hamdare et al., 2025), and institutional forecasting work confirms the
approach generalises beyond the household (Santiago et al., 2025).

## Budget Creation

### Budget

A budget in this study is a dated allocation of expected income across expense categories, savings
goals, and debt obligations, derived from a forecast and constrained by the user's stated
priorities. Constrained data-driven budgeting work describes a budget in exactly these terms, as
simultaneously a forecast, a commitment device, and a control system (Lu et al., 2025), and
household planning formulations treat it as the allocation output of an optimisation process
(de Zarzà et al., 2024). Multi-criteria budget allocation models formalise the same object under
competing objectives (Gulbakyt et al., 2025).

The comparative evaluation finding that applications support tracking over budgeting is best read
as a statement about this object being under-constructed rather than unwanted
(Alenazi & Sas, 2023). A tracking-first product produces a budget as a manual step, whereas a
budget-first product derives allocation from forecast and constraints
(Ghonaim & El-Sharawy, 2025). Household budget recommendation work supports the latter framing
(de Zarzà et al., 2024), and institutional allocation systems show the approach at scale
(Santiago et al., 2025).

### Budget Constraints

Budget constraints are the limitations within which allocation must occur: income, fixed expenses,
debt obligations, minimum living costs, and user-stated priorities. Household planning
formulations make these constraints explicit and solve allocation under them
(de Zarzà et al., 2024), and multi-criteria budget models handle competing constraint sets
(Gulbakyt et al., 2025). Constrained budgeting frameworks demonstrate that constraints, not the
optimiser, determine whether a feasible plan exists (Lu et al., 2025).

The Philippine context makes constraint handling decisive rather than incidental, because the
constraint set is both tight and volatile. Consumer survey evidence documents reduced savings
propensity under price pressure, which narrows the feasible region (Bangko Sentral ng
Philippines, 2026), and local evidence documents recurring borrowing for ordinary expenses, which
indicates the feasible region is often empty without explicit relief
(Francisco et al., 2026; Claro & Noval, 2025). Reviews of planning behaviour support reporting
infeasibility explicitly rather than silently returning an unbalanced budget
(Yeo et al., 2023; Yoganandham, 2025).

### Budget Creation and Optimization

Budget creation and optimisation combines forecast, constraints, and preferences into an allocation
and a schedule, and it is the component with the strongest optimisation literature behind it.
Multi-criteria budget allocation models generate allocations balancing multiple objectives
(Gulbakyt et al., 2025); constrained frameworks couple forecasting to allocation
(Lu et al., 2025); household planning formulations extend this to individual and cooperative cases
with model-generated recommendations (de Zarzà et al., 2024); and institutional systems apply
predictive analytics to real allocation decisions (Santiago et al., 2025).

Mobile application evidence shows the optimisation logic deploying rather than remaining academic
(Ghonaim & El-Sharawy, 2025), and comparative evaluation indicates that this is precisely the
capability the application category under-delivers (Alenazi & Sas, 2023). Expense-tracker
contributions supply the transaction-classification stage that precedes allocation
(Thakur & Jadhav, 2025). Taken together, the literature supports the component and identifies the
category-level gap BUDGIE occupies.

### Importance of Budget Creation

The importance of budget creation lies in its position between forecast and plan: it is where
predicted spending becomes a commitment. Planning review establishes that commitments structured
in advance are followed more consistently than intentions (Yeo et al., 2023), and capability
reviews show the same effect across developing economies (Cumaio et al., 2026; Samli et al., 2026).

Local evidence links the absence of structured budgeting to measurable harm, since salary-loan
dependency is traced to inadequate planning capacity and absent emergency savings
(Francisco et al., 2026), and well-being regressors indicate structured practice as a determinant
(Claro & Noval, 2025). Optimisation research supplies the mechanism, showing that allocation
respecting explicit constraints is more likely to be feasible and therefore sustained
(de Zarzà et al., 2024; Gulbakyt et al., 2025; Lu et al., 2025). Reviews of budgeting practice
complete the case by treating the budget as the central artefact of household financial management
(Yoganandham, 2025).

## Unusual Expense Detection

### Unusual Expenses

An unusual expense is a transaction that deviates from a household's own established baseline
sufficiently to warrant attention, as distinct from one that is merely large or categorically
irregular. Framing the baseline as personal rather than universal is what separates this problem
from institutional fraud detection, and the literature on threshold calibration supports the
personal-baseline framing by showing that the definition of anomalous shifts with the data
distribution (Huang et al., 2025; Zhong, 2025).

Credit-card spending analysis supplies the empirical basis, demonstrating that spending habits have
structure sufficient for deviation to be meaningful and that rewarding departures from it is
tractable (Hamdare et al., 2025). Expense-tracker work supplies transaction-level data at the
granularity the detection requires (Thakur & Jadhav, 2025), and mobile budgeting applications show
detection embedded in consumer applications (Ghonaim & El-Sharawy, 2025). Debt-management evidence
supplies the reason detection matters to users, since unrecognised accumulation precedes the
dependence documented by local studies (Esperanza, 2025; Francisco et al., 2026).

### Anomaly Detection

Anomaly detection in financial data presents the dual difficulty of class imbalance and threshold
instability. Adaptive threshold work addresses the second directly, calibrating thresholds from
time-series features so that detection survives distributional shift
(Zhong, 2025), and dynamic calibration work demonstrates the approach against payment-platform data
(Huang et al., 2025). Both findings bear directly on household data, where the distribution shifts
predictably with seasonality and with life events.

Classification methods transfer to the household case. Spending-habits analysis applies machine
learning to categorised card transactions (Hamdare et al., 2025), expense-tracker work does the
same for personal expenses (Thakur & Jadhav, 2025), and institutional analytics supply the
comparative evaluation context (Santiago et al., 2025; Gulbakyt et al., 2025). Reviews of
financial capability indicate why false alarms are costly for this user group specifically, since
users under budget pressure cannot afford to dismiss alerts reflexively
(Cumaio et al., 2026; Esperanza, 2025).

### Importance of Unusual Expense Detection

Detection matters because it is the only feature in BUDGIE that surfaces information the user has
not asked for, and the literature supports that this is where independent insight originates.
Adaptive threshold work shows that detection identifies conditions that static rules miss
(Zhong, 2025; Huang et al., 2025), and spending-habits analysis shows that departures from
established patterns carry behavioural meaning (Hamdare et al., 2025).

The consequence of not detecting is documented locally. Debt accumulation in wage earners is
associated with credit access unaccompanied by management capability (Esperanza, 2025), and
salary-loan dependency is traced to absent buffers and absent monitoring
(Francisco et al., 2026). Reviews of debt-management behaviour confirm that early detection is the
prevention mechanism (Samli et al., 2026), and reviews of capability show the users most in need of
alerts are those least able to anticipate irregular outflows (Cumaio et al., 2026; Sapiri &
Awaluddin, 2023).

## Financial Planning

BUDGIE's financial planning module composes the four feature areas into a single dated plan and
tracks adherence against it. This is the component the planning literature identifies as missing and
the application literature confirms as under-delivered. The module's stages follow the process
stages established in the review: situation, goals, plan, execution, and review
(Yoganandham, 2025; Yeo et al., 2023).

**Financial Situation.** Situation assessment in BUDGIE is computed rather than declared, drawing profile dimensions,
forecast income, recurring expenses, and outstanding obligations into a single dated picture.
Planning review treats situation assessment as the determinant of every downstream recommendation
and notes that its procedural treatment in the literature is a weakness
(Yeo et al., 2023), while household planning formulations make it an explicit optimisation input
(de Zarzà et al., 2024). Well-being regressors support the choice of computed over self-reported
inputs (Claro & Noval, 2025), and capability reviews indicate self-report systematically
overstates position (Cumaio et al., 2026).

Consumption structure is part of situation, not context, because it determines the monthly
distribution of the position (Lu et al., 2025). Constraint analysis supplies the second half of the
picture, since the same nominal position yields different feasible regions under different
obligations (de Zarzà et al., 2024; Gulbakyt et al., 2025). Reviews of budgeting practice treat
this combined picture as the necessary precondition for any credible plan
(Yoganandham, 2025).

**Financial Goals.** Goals in BUDGIE are entered as dated amounts with priorities, which makes them directly usable as
optimisation objectives. Household planning formulations treat goals as the objective function of
the allocation problem, and show that the number of simultaneous goals is itself a source of
difficulty (de Zarzà et al., 2024). Planning review supports prioritisation as a required step
rather than an optional one (Yeo et al., 2023), and practical budgeting guidance treats clear
goal definition with amounts, timelines, and priorities as the precondition for progress
(Yoganandham, 2025).

Multi-criteria allocation models demonstrate that competing goals require explicit weighting, not
implicit trade-offs (Gulbakyt et al., 2025), and constrained budgeting frameworks show that
unweighted goals produce allocations that satisfy the arithmetic while failing the user's intent
(Lu et al., 2025). Reviews of planning behaviour locate goal conflict as a leading cause of plan
abandonment (Yeo et al., 2023; Cumaio et al., 2026), and local evidence shows that savings and debt
goals compete for the same funds in practice (Francisco et al., 2026; Claro & Noval, 2025).

**Financial Plan.** The plan is the composed output: profile-informed allocation, forecast-adjusted expense
expectations, dated savings contributions, and dated debt repayments, with a feasibility status.
Household planning formulations produce this object and identify constraint adherence as the
unresolved problem (de Zarzà et al., 2024), and multi-criteria allocation models produce
comparable outputs under competing objectives (Gulbakyt et al., 2025). Constrained frameworks
supply the forecast coupling (Lu et al., 2025), and institutional allocation systems show the
artefact in operational use (Santiago et al., 2025).

Application evidence establishes what is missing from commercial equivalents. Comparative
evaluation finds planning support systematically weaker than tracking support
(Alenazi & Sas, 2023), and reviews of machine learning for the domain find components evaluated in
isolation rather than composed (D'Souza et al., 2026). Mobile budgeting work shows deployment of
individual components (Ghonaim & El-Sharawy, 2025), and savings and debt behaviour reviews identify
the composition requirement that no reviewed system meets
(Cumaio et al., 2026; Samli et al., 2026).

**Execution and Adherence.** Execution is where the planning literature is most emphatic that support, not intention, determines
outcome. Planning review finds that adherence depends on progress visibility and feedback
(Yeo et al., 2023), and capability reviews find the same across developing economies
(Cumaio et al., 2026; Samli et al., 2026). Local evidence shows the failure mode directly, since
borrowing for ordinary expenses indicates plans were not executed as intended
(Francisco et al., 2026; Claro & Noval, 2025).

The literature also identifies what does not work. Reviews of saving behaviour show intention
without mechanism does not produce saving (Cumaio et al., 2026), and debt-management evidence shows
the substitute behaviour that appears when adherence fails (Esperanza, 2025; Samli et al., 2026).
Practical budgeting guidance frames the same requirement as a cycle requiring review
(Yoganandham, 2025), which is what the adherence indicators in BUDGIE measure.

**Review and Monitoring.** Monitoring closes the loop and is the least-developed stage in the literature. Planning review notes
that review is treated procedurally even though it is the only stage permitting correction
(Yoganandham, 2025), and that adherence depends on feedback derived from it
(Yeo et al., 2023). Capability reviews identify the same gap in the behavioural evidence
(Cumaio et al., 2026; Samli et al., 2026).

Detection is the mechanism that makes monitoring specific rather than periodic. Adaptive threshold
work supplies alerts derived from deviation rather than from fixed intervals
(Zhong, 2025; Huang et al., 2025), spending-habits analysis supplies the deviation signal
(Hamdare et al., 2025), and expense-tracker work supplies the transaction stream it operates on
(Thakur & Jadhav, 2025). Local evidence supports the value of early warning to users under budget
pressure (Esperanza, 2025), and institutional analytics demonstrate the monitoring pattern at scale
(Santiago et al., 2025).

<!-- Cite the BSP financial planning cycle here. Look for it in BUDI-Literature -->
<!-- NOT SATISFIABLE from the held corpus text. All Bangko Sentral entries were checked on
     2026-09-27: the Q4 2023 Financial Inclusion dashboard, the Financial Inclusion Dashboard, the
     Annual Report 2025, the Consumer Expectations Survey Q2 2026, and two statistical releases. None
     is a financial planning cycle document, and the phrase "planning cycle" does not occur in any of
     them. Every "cycle" match is monetary policy: easing cycles, off-cycle meetings, credit cycles.
     The likeliest explanation is that the cycle is presented as a figure. L--BangkoSentral-2023b was
     converted through the pypdf text() fallback, which extracts text only and silently drops all
     figures, and L--BangkoSentral-2025 and -2026b carry 20 and 65 figure references whose content
     was likewise never captured. A single image-only BSP document would not be sufficient empirical
     backing for the cycle in any case, so this section stays flagged. Resolution needs either manual
     figure extraction or OCR of the source PDFs, plus at least one non-BSP source on the cycle.
     The central-bank statistics that ARE available are cited for context in Context of Financial
     Planning, Problems faced by Individuals, and Budget Constraints. Request re-listed under
     Outstanding Source Requests. -->
<!-- CORRECTION 2026-09-27: an earlier version of this comment asserted that L--BangkoSentral-2023b
     "is in fact a 2005 document whose 2023 stem is wrong". That was a misreading and is retracted.
     It is the 2023 edition of the Report on Regional Economic Developments in the Philippines, an
     annual series; 2005 is the maiden-issue year stated in its own preface. The stem year is
     correct. -->

# Models and Algorithms

BUDGIE implements four algorithms, each selected for a property the literature identifies as
necessary rather than for availability. SARIMA is selected for seasonal structure, a rule-based
classifier for interpretability, linear programming for constrained optimality, and the
inter-quartile range for distribution-free detection. This section reviews each in the order the
adviser's guidelines require, and closes with the integration architecture and the system-level
indicators by which it is evaluated.

## Seasonal Auto-Regressive Integrated Moving Average (SARIMA)

### Overview of SARIMA

The Seasonal Auto-Regressive Integrated Moving Average model extends ARIMA to represent recurring
seasonal behaviour, specified as (p, d, q)(P, D, Q, s) where the lowercase terms describe
non-seasonal autoregressive, differencing, and moving-average structure, the uppercase terms
describe their seasonal counterparts, and s is the seasonal period. Its operation combines lagged
observations and lagged residual errors with seasonal differencing, so that trend and recurring
pattern are estimated jointly from history (Lu et al., 2025).

Its inputs are a time series long enough to identify the seasonal structure. For monthly data with
annual seasonality this means several annual cycles, and the series length therefore determines
whether the seasonal terms are estimable at all. The window this study estimates over is eighteen
quarters of Philippine consumption data, 2022 Q1 to 2026 Q2, which is a genuine constraint rather
than a formality: it spans four and a half annual cycles, and the seasonal terms are being estimated
from a small number of cycles. The domestic comparison point is the eighty-four quarterly
observations of Philippine household consumption expenditure from 2001 to 2021 modelled by Dasmariñas
et al. (2024), roughly a fifth again more data than this study has available. Identification of the
seasonal structure at eighteen quarters is therefore an assumption to be tested and reported, not a
guarantee, and it is the reason the estimation approach is stated explicitly rather than treated as
settled (Lu et al., 2025; Dasmariñas et al., 2024). Outputs are point forecasts for each future
period together with prediction intervals quantifying forecast uncertainty (Santiago et al., 2025).

Prior applications in the reviewed set establish the model's suitability for seasonal financial
series. Constrained data-driven budgeting applies forecasting jointly with allocation
(Lu et al., 2025); multi-criteria budget allocation consumes forecast inputs
(Gulbakyt et al., 2025); household planning formulations use forecast as an allocation input
(de Zarzà et al., 2024); expense tracking and credit-card spending studies apply comparable
seasonal techniques at transaction level (Thakur & Jadhav, 2025; Hamdare et al., 2025); and
institutional budget systems apply predictive analytics to forward allocation
(Santiago et al., 2025).

Its strengths are interpretability, an established theoretical basis, and native quantification of
uncertainty, all of which matter when a forecast must be explained to a user deciding how much to
reserve (Lu et al., 2025; Santiago et al., 2025). The choice of the model over the alternatives is
itself evidenced rather than assumed: on Philippine quarterly consumption data, SARIMA produced the
lowest combined error across the time-series models compared, against triple exponential smoothing
and TBATS, and the seasonal autoregressive form was the one that survived that comparison
(Dasmariñas et al., 2024). Its limitations follow directly: the linearity assumption, the
data-volume requirement, and sensitivity to structural breaks such as the pandemic period visible in
Philippine consumption data, which the same study shows materially distorts fitted relationships and
depresses measured growth (de Zarzà et al., 2024; Lu et al., 2025; Dasmariñas et al., 2024). Adaptive
threshold work provides the complement for the drift problem, since a model whose distribution
shifts needs re-estimation rather than a fixed rule (Zhong, 2025).

For BUDGIE the model is the seasonal forecasting engine, trained on monthly expense estimates
disaggregated from annual household survey data using consumption-survey seasonal proportions, and
blended with personal history as that history accumulates. The relevance is that it is the only
reviewed method that produces a seasonally resolved monthly expectation from annual data, which is
what budget composition requires (Lu et al., 2025; de Zarzà et al., 2024).

<!-- NEEDS MORE SOURCES: 7 required for a core algorithm; 7 now attached. Dasmariñas et al.
     (2024) closes the gap this section previously could not fill, and is the stronger source for
     it: it is a Philippine household-consumption study that selected SARIMA on RMSE, MSE and MAE
     rather than assuming it, and it reports the same structural-break risk from the pandemic period
     that this section names as a limitation. The narrower residual gap, stated rather than padded,
     is that Dasmariñas et al. models national aggregate consumption rather than an individual
     household's monthly expenses, and no source in the set does the latter. -->

### SARIMA in Forecasting

Applied to forecasting, SARIMA's role in the reviewed literature is to supply a seasonally resolved
expectation that a downstream optimiser can consume. Constrained data-driven budgeting demonstrates
the coupling directly, forecasting expenditure and modelling the allocation response jointly
(Lu et al., 2025). Multi-criteria budget allocation models take forecast output as input and show
that allocation quality is sensitive to it (Gulbakyt et al., 2025), and household planning
formulations use forecast values as allocation inputs under explicit constraints
(de Zarzà et al., 2024).

At the transaction level, forecasting methods are applied to spending series with comparable
seasonal structure. Expense-tracker systems apply machine learning to categorised personal expenses
(Thakur & Jadhav, 2025) and credit-card spending analysis applies supervised methods to
categorised card transactions (Hamdare et al., 2025), both of which require the same separation of
seasonal from trend structure. Institutional allocation systems apply predictive analytics to
forward-looking budgets (Santiago et al., 2025), and mobile budgeting applications apply learned
forecast components to user budgets (Ghonaim & El-Sharawy, 2025).

The finding common to these applications is that the forecast is only as useful as the resolution at
which it is produced, which is why monthly resolution from annual survey data is the specific
technical problem BUDGIE must solve (Lu et al., 2025; de Zarzà et al., 2024). Adaptive monitoring
work supplies a related finding, that forecast quality and data quality are coupled because drift
in the input distribution degrades the model silently (Zhong, 2025; Huang et al., 2025).

### Performance Metrics of SARIMA

Forecast accuracy is assessed on four complementary dimensions: average magnitude, scaled magnitude,
directional correctness, and error dispersion. Using all four is standard practice in the reviewed
forecasting work, and the choice of metric set is itself informative, because each dimension can
improve while another worsens (Lu et al., 2025; Santiago et al., 2025).

#### Mean Absolute Error (MAE)

Mean Absolute Error is the average of the absolute differences between forecast and actual values,
expressed in the original units of the series. Its interpretability is its principal virtue for this
application: a MAE expressed in pesos states directly how far a typical monthly forecast is wrong,
without requiring interpretation against a baseline (Lu et al., 2025). Applied to seasonal expense
forecasting it aggregates across the seasonal cycle and is therefore sensitive to the model's
treatment of seasonal turning points, which in expense series are typically the largest errors
(Thakur & Jadhav, 2025; Hamdare et al., 2025).

Its limitation is that it does not distinguish a model that is uniformly moderately wrong from one
that is occasionally severely wrong, since the absolute value prevents large errors dominating
(Santiago et al., 2025). For budgeting, where a single large seasonal miss can invalidate a
savings schedule, that limitation is why MAE is reported alongside RMSE rather than instead of it
(de Zarzà et al., 2024; Gulbakyt et al., 2025).

#### SMAPE

Symmetric Mean Absolute Percentage Error expresses forecast error as a proportion of actual value
using a symmetric denominator, which bounds the metric and avoids the unbounded behaviour of MAPE
when actual values approach zero. Expense categories frequently have very low or zero values in
individual months, so this property is decisive rather than cosmetic for this data
(Lu et al., 2025; de Zarzà et al., 2024).

It permits comparison across categories of different scale, which matters when a single forecast is
produced per category and the categories differ in magnitude by orders of magnitude
(Santiago et al., 2025). Its limitation is that it compresses the distinction between large and
small errors, since a large relative error on a small category contributes as much as a small
relative error on a large one, and it remains sensitive to the sign convention used in the symmetric
denominator (Lu et al., 2025; Gulbakyt et al., 2025). Reported alongside MAE, the pair separates
scale from proportion (Thakur & Jadhav, 2025; Hamdare et al., 2025).

#### MDA

Mean Directional Accuracy is the proportion of periods in which the forecast predicts the correct
direction of change, disregarding magnitude. It answers a question the other three do not: whether
the model knows when spending will rise and when it will fall, which is the question a user
reserving for a known seasonal expense actually asks (Lu et al., 2025).

Directional correctness is a weaker property than accuracy and can be high for a model that is
badly wrong in magnitude but consistently mis-signed relative to a small residual. It is therefore
never reported alone, and its value in this application is precisely as a check that the seasonal
structure is being captured rather than smoothed away (Santiago et al., 2025; de Zarzà et al., 2024).
For expense series, where the seasonal turning points drive budgeting decisions, a high MDA with
poor MAE is informative: it indicates the model has learned the calendar correctly but not the
magnitudes, which is a different and more tractable defect (Lu et al., 2025; Thakur & Jadhav, 2025).

#### RMSE

Root Mean Square Error is the square root of the mean of squared errors, so large errors are
penalised disproportionately. It is the metric of choice when the cost of error is convex, which
applies here because a large forecasting miss propagates into an infeasible budget
(Santiago et al., 2025; de Zarzà et al., 2024).

Its limitation is the mirror of MAE's: it is dominated by a small number of extreme errors and is
correspondingly unstable on short series, which is a material concern given that seasonal parameter
estimation from a borderline-length series is itself unstable (Lu et al., 2025). Reported together
with MAE, the ratio RMSE/MAE is diagnostic, since a ratio well above one indicates a small number
of large errors dominating, which for seasonal expense data usually points at a specific seasonal
turning point rather than at general model inadequacy (Gulbakyt et al., 2025; Santiago et al., 2025).

## Rule-Based Algorithms

### Overview of Rule-Based Algorithms

A rule-based algorithm classifies by applying explicit conditions derived from domain knowledge
rather than by learning parameters from labelled data. Its operation is ordered evaluation of
thresholds over computed financial-condition dimensions, its inputs are the user attributes those
dimensions require, and its output is a classification together with the dimension values and an
explanation of the rule that fired (Laspiñas & Murcia, 2024).

The dimensions used in BUDGIE are Emergency Fund Coverage, Debt-Service-to-Income, Financial Margin,
and Credit Card Behaviour, combined by threshold rules into saver, borrower, both, or neither. This
construction is supported by income-classification work showing financial characteristics carry
usable stratification signal and that rule-based methods segment effectively
(Laspiñas & Murcia, 2024), and by profile-based budget recommendation work showing that
personalised output requires documented user attributes rather than inferred latent structure
(de Zarzà et al., 2024).

Its strength is that a classification can be explained, which matters more here than predictive
power, because a user who cannot see why they were classified as a borrower cannot act on the
result. Debt-management evidence supports this, since the harms BUDGIE addresses follow from
unrecognised position rather than from miscalculation (Esperanza, 2025; Francisco et al., 2026).
Capability reviews indicate that users under financial stress scrutinise unfavourable
classifications, and transparency is what makes such scrutiny resolvable
(Cumaio et al., 2026; Samli et al., 2026).

Its limitation is coverage: rules encode the cases anticipated at authoring time, so a household
whose situation falls between thresholds receives an arbitrary classification. Spending-habits work
shows the alternative, a learned classifier handles unanticipated structure but cannot explain itself
(Hamdare et al., 2025), and income-classification work shows learned and rule-based approaches
performing comparably on structured financial attributes (Laspiñas & Murcia, 2024). The choice here
favours explainability, and the limitation is mitigated by reporting the dimension values alongside
the classification so a user can see how close a borderline case was (Cumaio et al., 2026).

### Rule-Based Algorithms in Profile Classification

In profile classification specifically, the literature supports rule-based approaches for
properties that learned classifiers would obscure. Income-level classification is the clearest
precedent, establishing that rule-based and statistical segmentation of financial attributes are both
viable and that the attributes themselves are interpretable (Laspiñas & Murcia, 2024). Behavioural
work supports treating the underlying constructs as threshold-shaped, since saving and debt
behaviours cluster around identifiable positions rather than continuous gradients
(Cumaio et al., 2026; Yeo et al., 2023).

Learned alternatives are documented and were considered. Credit-card spending classification
demonstrates that transaction history alone supports learned segmentation
(Hamdare et al., 2025), mobile budgeting applications apply learned profile components
(Ghonaim & El-Sharawy, 2025), and reviews of machine learning for the domain catalogue the
classification methods available (D'Souza et al., 2026). The reviewed learned approaches predict
behaviour; they do not produce an explanation a user can contest, which is the requirement
identified in the literature on debt accumulation and financial vulnerability
(Esperanza, 2025; Francisco et al., 2026).

A further consideration is data availability. Rule-based classification requires no labelled
training set, and the literature notes that labelled financial-behaviour data is scarce and
frequently unavailable outside institutional settings (Cumaio et al., 2026; Sapiri & Awaluddin,
2023). Household budget recommendation work supports the same position, deriving recommendations
from documented user attributes rather than from learned parameters
(de Zarzà et al., 2024). Local evidence indicates the input attributes are precisely the ones
users can supply (Claro & Noval, 2025; Francisco et al., 2026).

### Metrics

Evaluating a rule-based classifier is harder than evaluating a learned one because the absence of
labelled ground truth removes the obvious reference standard. Three substitutes are available and
are used together: rule-derived reference labels for self-consistency, boundary-case test sets for
edge conditions, and subject-matter expert review for plausibility.

Self-consistency establishes that the rule set is deterministic and internally coherent, catching
implementation errors that a held-out accuracy figure would conceal. Boundary testing targets the
specific weakness of rule-based systems, since misclassification concentrates near thresholds
(Laspiñas & Murcia, 2024). Expert review supplies the external validity that self-consistency
cannot, and the literature indicates plausibility is assessable by practitioners because the
underlying constructs are established (Cumaio et al., 2026; Yeo et al., 2023).

The metrics reported are accuracy, precision, recall, and F1-score, computed against rule-derived
reference labels. Their interpretation requires care, and the reason is documented in the
classification literature: accuracy against self-derived labels measures internal coherence, not
correctness (Laspiñas & Murcia, 2024). Expert spot checks therefore carry the external validity
that the aggregate figures cannot, and this limitation is stated rather than smoothed over
(Cumaio et al., 2026; Francisco et al., 2026).

#### Accuracy

Accuracy is the proportion of classifications matching the reference label across all cases. It is
reported for completeness and comparability with the learned-classification literature, but it is
the least informative of the four here, because class imbalance makes it dominated by the majority
class, and because the reference labels are rule-derived (Laspiñas & Murcia, 2024; Cumaio et al.,
2026).

Its role in this study is as a regression check. A drop in accuracy between releases indicates a
change in rule behaviour that should be explainable, and an implausibly high accuracy indicates
that the reference labels have leaked from the rules under test (Laspiñas & Murcia, 2024). Expert
review is what gives the figure external meaning (Francisco et al., 2026; Yeo et al., 2023).

#### Precision

Precision is the proportion of positive classifications that are correct, answering how often a
user flagged as a borrower actually exhibits borrower characteristics. It is the metric that
controls the cost of acting on a classification, because each false positive produces an
intervention the user does not need (Laspiñas & Murcia, 2024; Cumaio et al., 2026).

For BUDGIE this is the more important of the two error types, since an unnecessary debt-management
intervention applied to a saver is both unwelcome and damaging to trust in the system
(Francisco et al., 2026; Claro & Noval, 2025). Rule-based systems achieve high precision near
thresholds where rules are conservative, and the boundary test set is where precision is examined
most closely (Laspiñas & Murcia, 2024; Yeo et al., 2023).

#### Recall

Recall is the proportion of actual positive cases correctly identified, answering how many users
who warrant debt-management support receive it. It is the metric that controls the cost of omission,
and in this application the asymmetry runs the other way from precision: a missed borrower is a user
whose accumulation goes unaddressed (Esperanza, 2025; Samli et al., 2026).

The local evidence establishes why this asymmetry matters. Salary-loan dependency is documented as
accumulating from unrecognised position over time, and digital lending is documented as supplying
credit faster than management capability (Francisco et al., 2026; Esperanza, 2025). Reviews of
debt-management behaviour confirm that early identification is the prevention mechanism
(Samli et al., 2026). Recall is therefore weighted more heavily than precision in threshold
selection, which is a deliberate and defensible departure from the usual accuracy-maximising choice
(Cumaio et al., 2026; Yeo et al., 2023).

#### F1-score

F1-score is the harmonic mean of precision and recall, summarising both error types in one figure.
It is appropriate here because the two error types have comparable operational cost even though
their user-facing consequences differ, and it is the standard summary in the classification
literature against which learned alternatives are compared (Laspiñas & Murcia, 2024).

Its limitation is that a single harmonic mean conceals which error type is being traded, and that
trade is a policy choice in this application rather than a modelling artefact
(Cumaio et al., 2026). The F1-score is therefore reported together with both components and is not
used as the selection criterion; thresholds are chosen on recall, with precision reported as the
cost of that choice (Francisco et al., 2026; Samli et al., 2026). Learned alternatives remain the
right choice where prediction alone is the objective, as spending-habits work demonstrates
(Hamdare et al., 2025), which is the trade this design accepts.

## Linear Programming

### Overview of Linear Programming

Linear programming finds the extreme point of a linear objective over a polyhedron defined by linear
constraints, and is the standard formulation for allocation under competing objectives and limited
resources. Its operation decomposes the budget problem into decision variables for allocation
amounts, an objective function combining goal attainment, and constraints encoding income, fixed
expenses, and minimum requirements (de Zarzà et al., 2024; Gulbakyt et al., 2025).

Its inputs are the expense forecast, the user profile, savings goals, debts, income, and fixed
expenses, which together define the objective and the feasible region. Its outputs are the optimal
allocation, dated savings contribution schedules, dated debt repayment schedules, a feasibility
status, and an explanation of the binding constraints (de Zarzà et al., 2024; Lu et al., 2025).

The reviewed literature establishes the technique's suitability for this problem directly.
Household planning formulations express budget allocation as constrained optimisation
(de Zarzà et al., 2024), multi-criteria budget models optimise allocation across competing objectives
(Gulbakyt et al., 2025), and constrained data-driven budgeting demonstrates the coupling of forecast
to allocation (Lu et al., 2025). Institutional allocation systems apply the same formulation to real
budgets (Santiago et al., 2025), and mobile applications demonstrate deployment of budget logic to
consumers (Ghonaim & El-Sharawy, 2025).

Its strength is that it returns a provably optimal, feasible allocation and, critically, reports
when no feasible allocation exists. That infeasibility report is the feature the planning literature
most needs and applications least provide, since a system that silently returns an unbalanced budget
teaches the user to disregard it (de Zarzà et al., 2024; Yeo et al., 2023). Its limitation is that it
requires linear relationships, so it cannot represent the non-linear preference structures that
behavioural work documents, and it does not handle uncertainty directly
(Cumaio et al., 2026; Yoganandham, 2025). Forecast uncertainty is therefore handled outside the
programme, through conservative forecast quantiles rather than stochastic constraints
(Lu et al., 2025; Gulbakyt et al., 2025).

### Linear Programming in Optimization

Within the optimisation literature, budget allocation quality is determined by the formulation
rather than by the solver, and the reviewed work makes this explicit. Multi-criteria models show
that allocation outcomes shift with the weighting applied to competing objectives
(Gulbakyt et al., 2025), and constrained frameworks show the same dependence on how the expenditure
estimate enters the objective (Lu et al., 2025). Household planning formulations extend the space to
individual and cooperative cases with model-generated recommendations, and identify constraint
adherence as the unresolved problem (de Zarzà et al., 2024).

Set-based allocation, in which the user receives a menu of feasible allocations rather than a single
optimum, is the refinement this design adopts. Practical budgeting guidance supports user choice as
a requirement rather than a convenience (Yoganandham, 2025), planning review supports it as a means
of improving adherence (Yeo et al., 2023), and capability reviews indicate that users under
constraint reject recommendations that are optimal but not recognisably theirs
(Cumaio et al., 2026; Samli et al., 2026). Institutional systems demonstrate the value of
presenting allocation decisions with their analytic basis visible (Santiago et al., 2025).

Solver choice is deliberately unremarkable. An open-source solver is used because the problem is
small, well-conditioned, and fully specified by linear constraints, and the reviewed literature
attributes no advantage to commercial solvers at this scale
(Gulbakyt et al., 2025; Lu et al., 2025; de Zarzà et al., 2024). This is a case where the algorithm
choice is not the contribution, and the contribution is the formulation and the set-based
presentation (Santiago et al., 2025; Yoganandham, 2025).

### Metrics

The solver is evaluated on three properties specific to budget allocation rather than on generic
optimisation performance: whether the solution respects the constraints, whether it uses the
available resources, and whether it reflects the user's stated priorities. None of the reviewed
budget-optimisation papers reports all three, which is itself a gap the evaluation design addresses
(de Zarzà et al., 2024; Gulbakyt et al., 2025; Lu et al., 2025).

#### Constraint Satisfaction Rate

Constraint satisfaction rate is the proportion of specified constraints satisfied by the returned
allocation, and it is the solver's primary correctness measure. A rate below one indicates either an
infeasible problem or a solver failure, and the two must be distinguished because they require
different responses: the first is information for the user, the second is a defect
(de Zarzà et al., 2024; Lu et al., 2025).

The measure is reported together with the identity of the binding constraints, which the planning
literature indicates is the actionable part (Yeo et al., 2023). Reporting a rate without naming
which constraint forced the trade-off gives a user no way to act on the result, which is the
failure mode capability reviews identify in existing applications
(Cumaio et al., 2026; Francisco et al., 2026). Institutional systems demonstrate the value of
surfacing the basis of an allocation decision (Santiago et al., 2025).

#### Budget Utilization Rate

Budget utilisation rate is the proportion of available income allocated, indicating whether the
programme commits the resources it is given. A low rate signals either conservative user
constraints or slack in the objective, and the two are distinguished by whether the objective
contains an unconstrained term (Gulbakyt et al., 2025; Lu et al., 2025).

For BUDGIE the target behaviour is deliberate non-utilisation, because unallocated funds are
sometimes the correct outcome when constraints are tight, and forcing allocation under those
conditions produces a plan that fails on contact with actual spending
(de Zarzà et al., 2024; Yoganandham, 2025). Local evidence supports this: households under
financial pressure accumulate debt precisely when committed allocations exceed real capacity
(Francisco et al., 2026; Claro & Noval, 2025). The measure is therefore interpreted as a
diagnostic, not as a target to maximise (Cumaio et al., 2026; Yeo et al., 2023).

#### Deviation from User Preferences

Deviation from user preferences measures how far the returned allocation departs from the priorities
the user stated, and it is the only measure that assesses whether a technically optimal solution is
usable by the person it is for (de Zarzà et al., 2024; Yoganandham, 2025).

It exists because the optimisation literature shows allocation quality depends on objective
weighting, which means an optimal solution can be optimal and still wrong for a given household
(Gulbakyt et al., 2025; Lu et al., 2025). Planning review identifies acceptance, rather than
optimality, as the determinant of whether a plan is followed (Yeo et al., 2023), and capability
reviews indicate that deviations the user cannot account for are abandoned
(Cumaio et al., 2026; Samli et al., 2026). This is the measure that justifies the set-based
presentation rather than a single optimum (Santiago et al., 2025; Francisco et al., 2026).

## Inter-quartile Range (IQR)

### Overview of IQR

The Inter-Quartile Range method identifies outliers as observations falling outside the fences
Q1 − 1.5·IQR and Q3 + 1.5·IQR, where IQR is the difference between the third and first quartiles.
Its operation is the computation of quartiles over a baseline of historical values and the flagging
of subsequent observations outside those fences (Huang et al., 2025).

Its inputs are new transactions and a seasonally aware baseline, the latter being the essential
adaptation, since an unadjusted baseline flags predictable seasonal spending as anomalous. Its
outputs are unusual-expense alerts carrying the transaction, the direction and degree of deviation,
and an acknowledgement channel whose feedback informs later threshold calibration
(Huang et al., 2025; Zhong, 2025).

The reviewed literature supports distribution-free detection for this problem specifically.
Adaptive threshold work calibrates thresholds from time-series features so detection survives
distributional shift, addressing the fixed-threshold weakness directly
(Zhong, 2025), and dynamic calibration work demonstrates the approach against payment-platform
financial data (Huang et al., 2025). Spending-habits analysis supplies the behavioural basis, since
detection is only meaningful relative to established patterns (Hamdare et al., 2025), and
expense-tracker systems supply the transaction stream it operates on
(Thakur & Jadhav, 2025).

Its strength is that it requires no distributional assumption, no training, and no parameter
estimation, which is decisive for a system whose users begin with no transaction history
(Huang et al., 2025; Cumaio et al., 2026). Spending-pattern variation across households means no
learned detector transfers reliably to a new user, and distribution-free methods sidestep that
problem entirely (Hamdare et al., 2025; Sapiri & Awaluddin, 2023). Its limitation is sensitivity
to the multiplier, whose conventional value of 1.5 is a convention rather than a derivation, and
its inability to consider more than one variable at a time, so a large but ordinary purchase is
flagged regardless of category (Huang et al., 2025; Zhong, 2025).

### IQR in Anomaly Detection

Within the anomaly-detection literature reviewed here, the IQR method occupies the position of the
transparent baseline against which adaptive methods are argued. Threshold-calibration research
identifies the baseline's weakness precisely, that fixed thresholds are set against a distribution
that moves (Huang et al., 2025), and adaptive work answers it by recalibrating from time-series
features (Zhong, 2025).

Household data makes the baseline's weakness more pronounced than in institutional settings, because
an individual baseline has fewer observations and a faster-moving distribution
(Hamdare et al., 2025; Thakur & Jadhav, 2025). The literature on financial capability indicates
that the users generating this data are also the users for whom a false alarm is most costly
(Cumaio et al., 2026; Esperanza, 2025). Seasonal baseline adjustment is therefore not an
refinement but a requirement, and the reviewed adaptive work supports making the baseline
season-aware rather than global (Zhong, 2025; Huang et al., 2025).

The alternative considered is a learned detector, which the literature documents as effective
where sufficient labelled data exists (Hamdare et al., 2025; D'Souza et al., 2026) but which cannot
be validated for a new user without a history that a new user does not have
(Cumaio et al., 2026; Sapiri & Awaluddin, 2023). The reviewed evidence therefore favours a
distribution-free detector with a seasonal baseline, accepting its single-variable limitation in
exchange for its behaviour on cold-start data (Huang et al., 2025; Zhong, 2025).

### Metrics

The detector is evaluated with the same four metrics as the classifier, for the same structural
reason: the reference standard is absent, and a summary figure alone conceals which error type
dominates. Detection differs from classification in the cost structure, which is why the same metrics
carry a different interpretation here (Huang et al., 2025; Hamdare et al., 2025).

Precision corresponds to the proportion of alerts that are genuinely unusual, and controls alert
fatigue. The literature is explicit that excessive false alarms cause users to disregard all alerts,
which destroys the feature's value entirely (Huang et al., 2025; Zhong, 2025). For users under
financial pressure this cost is higher, because a dismissed alert is an unreviewed transaction
(Cumaio et al., 2026; Esperanza, 2025).

Recall corresponds to the proportion of true unusual expenses detected, and controls omission.
Spending-habits work shows that meaningful departures from established patterns occur and carry
behavioural signal (Hamdare et al., 2025), and debt-management evidence shows that unrecognised
outflows precede accumulation (Esperanza, 2025; Samli et al., 2026). In common with the
classifier, recall is weighted more heavily than precision in threshold selection
(Francisco et al., 2026; Cumaio et al., 2026).

#### Accuracy

Accuracy is the proportion of transactions correctly classified as ordinary or unusual, and for
detection it is the least useful of the four, because unusual expenses are rare by construction and
a detector that flags nothing scores near-perfect accuracy while providing no value
(Huang et al., 2025; Zhong, 2025).

It is retained as a regression check only, consistent with its role in the classifier evaluation
(Laspiñas & Murcia, 2024). The literature's threshold-calibration work makes the same point, that
aggregate accuracy conceals the threshold behaviour that determines whether a detector is usable
(Huang et al., 2025; Hamdare et al., 2025).

#### Precision

Precision is the proportion of generated alerts corresponding to genuinely unusual expenses, and it
is the metric that determines whether the feature is used at all. The reviewed adaptive-threshold
work frames the entire calibration problem as balancing this against recall
(Huang et al., 2025; Zhong, 2025), and spending-habits analysis indicates that a pattern only
deserves an alert if it is actually outside normal behaviour (Hamdare et al., 2025).

For BUDGIE the seasonal baseline is the primary lever on precision, since the largest source of
false positives in household data is predictable seasonal spending
(Thakur & Jadhav, 2025; Hamdare et al., 2025). Evidence on the affected users indicates the cost of
a false positive is higher than its frequency alone suggests
(Cumaio et al., 2026; Esperanza, 2025; Francisco et al., 2026).

#### Recall

Recall is the proportion of genuinely unusual expenses detected, and it bounds the value of the
feature, since an undetected unusual expense is indistinguishable from an ordinary one. The
literature supports weighting it heavily for the same reasons as in the classifier: the documented
harm in this user group follows from unrecognised accumulation rather than from missed convenience
(Esperanza, 2025; Samli et al., 2026; Francisco et al., 2026).

Its practical limit in this design is the cold-start condition, since recall cannot be high for a
user whose baseline is estimated from few observations
(Cumaio et al., 2026; Sapiri & Awaluddin, 2023). The literature on spending patterns indicates
population-level structure partially mitigates this, which is why the baseline blends individual
history with population proportions
(Hamdare et al., 2025; Thakur & Jadhav, 2025; Lu et al., 2025).

#### F1-score

F1-score summarises precision and recall for the detector, and is reported for comparability with
both the learned-detector literature and the classifier evaluation
(Huang et al., 2025; Laspiñas & Murcia, 2024).

As in the classifier case, the harmonic mean is not the selection criterion, because the appropriate
balance is a policy decision about alert tolerance rather than a statistical optimum
(Cumaio et al., 2026; Huang et al., 2025). The seasonal baseline and the multiplier are tuned
against recall subject to a precision floor, which reflects the documented asymmetry of the harms
(Esperanza, 2025; Francisco et al., 2026; Samli et al., 2026). Reporting F1 without its components
would hide that decision, so all three figures are reported
(Zhong, 2025; Hamdare et al., 2025).

## Model and Algorithm Integration

Integrating the four algorithms produces a pipeline in which each stage constrains the next, and the
integration is the contribution rather than the arithmetic. Profile classification establishes the
context that shapes budget objectives; seasonal forecasting supplies the expenditure expectations
that bound them; linear programming composes allocation and schedules; and IQR detection monitors
execution against the resulting baseline. Reviews of machine learning for this domain identify the
integration gap directly, finding techniques established individually but evaluated in isolation
against single objectives (D'Souza et al., 2026).

Household planning formulations confirm the pipeline's shape, since budget allocation, savings
contribution, and debt repayment must be solved jointly rather than sequentially
(de Zarzà et al., 2024). Multi-criteria allocation models supply the multi-objective treatment the
composition requires (Gulbakyt et al., 2025), and constrained data-driven budgeting demonstrates
forecast-to-allocation coupling (Lu et al., 2025). Mobile application work shows the components
deploying individually (Ghonaim & El-Sharawy, 2025), and comparative evaluation confirms that no
reviewed commercial system composes them
(Alenazi & Sas, 2023; D'Souza et al., 2026).

Architecturally the pipeline separates the model-serving components from the mobile client, which
follows from the literature's observation that model-bearing features degrade gracefully while
client-side features remain available offline (D'Souza et al., 2026; Lu et al., 2025). The
composition contract between stages is the part with no literature precedent and therefore the part
requiring the most explicit evaluation, which is what the system-level indicators provide
(de Zarzà et al., 2024; Gulbakyt et al., 2025).

### SARIMA for Seasonal Expense Forecasting

SARIMA's role in the pipeline is to convert population-level and household-level expenditure
structure into a monthly expectation that the optimiser can consume, and the literature establishes
that this conversion is the precondition for feasible allocation
(Lu et al., 2025; de Zarzà et al., 2024). Constrained budgeting work demonstrates the coupling
directly, and multi-criteria allocation models show that allocation quality degrades when the
expenditure estimate is seasonally naive (Gulbakyt et al., 2025; Lu et al., 2025).

Within the pipeline the forecast is deliberately population-anchored and personally blended, because
the reviewed evidence indicates that individual history is insufficient early in a user's tenure
while population structure remains informative
(Thakur & Jadhav, 2025; Hamdare et al., 2025). Seasonal consumption structure in Philippine
households is documented as strong, which is what makes a population anchor defensible rather than a
fallback (Lu et al., 2025; Cumaio et al., 2026). The interface to the next stage is a point forecast
with an interval, and conservative use of that interval is what keeps the downstream programme
feasible (de Zarzà et al., 2024; Santiago et al., 2025).

### Rule-Based Algorithms for Saver and Borrower Profile Classification

The classifier's role in the pipeline is to set objectives and constraint weights for the optimiser,
converting a four-state position into the priorities the programme will pursue. The literature
supports this ordering, since planning review shows that the appropriate planning behaviour differs
by position (Yeo et al., 2023; Claro & Noval, 2025) and that applying one approach uniformly
mis-serves both groups (Cumaio et al., 2026).

The classifier runs first because its outputs are cheap and stable, whereas the optimiser's inputs
depend on them. Income-classification work supports the feasibility of this stage in isolation
(Laspiñas & Murcia, 2024), and household budget recommendation work supports deriving
recommendations from documented attributes (de Zarzà et al., 2024). Its output contract is the
classification, the dimension values, and the explanation, and the explanation is what makes the
downstream objective weighting contestable by the user
(Esperanza, 2025; Francisco et al., 2026). Local evidence on borrowing dependence indicates that
mis-weighting here propagates directly into harmful advice
(Francisco et al., 2026; Samli et al., 2026).

### Linear Programming for Budget Creation

The solver's role is composition, and the literature is explicit that this is the step that
application research leaves undone. Household planning formulations produce the composed artefact
and identify constraint adherence as unresolved (de Zarzà et al., 2024), while comparative
evaluation of commercial systems finds the corresponding capability absent
(Alenazi & Sas, 2023).

It receives the forecast, the profile, and the user's goals, and returns allocation with schedules,
which is the interface the planning literature expects a plan to expose
(Yoganandham, 2025; Yeo et al., 2023). Multi-criteria models supply the treatment of competing
objectives this stage requires (Gulbakyt et al., 2025), and constrained frameworks supply the
feasibility handling (Lu et al., 2025). The set-based presentation is the deliberate departure from
single-optimum practice, justified by the adherence evidence
(Yeo et al., 2023; Cumaio et al., 2026; Yoganandham, 2025).

### IQR for Unusual Expense Detection

The detector's role is post-composition monitoring, and it is the only stage that produces
information the user did not request. The literature supports both the mechanism and its placement:
adaptive threshold work establishes detection as the means of surfacing distributional change
(Zhong, 2025; Huang et al., 2025), and spending-habits analysis establishes that departure from
established pattern is where the signal lies (Hamdare et al., 2025).

Placement after composition is what makes the baseline meaningful, since the composed plan supplies
the expected seasonal profile against which execution is judged. Expense-tracker work shows
transaction-level detection operating on categorised data of this kind
(Thakur & Jadhav, 2025), and institutional analytics show the pattern at scale
(Santiago et al., 2025). The alert-to-feedback channel closes the loop, which the planning
literature identifies as the stage most often omitted
(Yoganandham, 2025; Yeo et al., 2023; Cumaio et al., 2026).

### Integration in Financial Planning Feature

The integration feature is what distinguishes BUDGIE from a bundle of components, and no source in
the reviewed set provides a precedent for it, which is both the justification for the study and the
reason its evaluation is reported at system level. Reviews of machine learning for the domain
identify the absence of integrated deployment as the field's central gap
(D'Souza et al., 2026), and comparative evaluation of commercial systems reaches the same conclusion
from the user side (Alenazi & Sas, 2023).

The integration's specific claim is that a seasonally resolved forecast, a rule-derived profile, and
a constraint-respecting allocation are jointly more useful than any of them alone, because the
composition makes each actionable. Household planning formulations support the compositional
argument (de Zarzà et al., 2024), multi-criteria allocation models support the multi-objective
requirement it creates (Gulbakyt et al., 2025), and constrained budgeting supports the forecast
coupling (Lu et al., 2025). Mobile application work supplies the individual components as
deployable units (Ghonaim & El-Sharawy, 2025; Thakur & Jadhav, 2025), and the comparative evaluation
supplies the evidence that they are not yet deployed together
(Alenazi & Sas, 2023; D'Souza et al., 2026).

The risks the literature implies are specific and worth stating. A composition error propagates
downstream, so a miscalibrated forecast yields an infeasible plan and misleading alerts
(Lu et al., 2025; Gulbakyt et al., 2025). A misclassified profile yields advice harmful to the
household it mis-serves (Francisco et al., 2026; Claro & Noval, 2025). And excessive alerting
destroys the trust on which the adherence mechanism depends
(Huang et al., 2025; Cumaio et al., 2026). These are the failure modes the system-level indicators
are chosen to detect.

### Performance Analysis

System-level analysis proceeds at three levels, and the distinction matters because a component can
perform well while the pipeline performs badly. Individual algorithm metrics establish that each
component meets its own objective, as the reviewed evaluation practice does for classification
(Laspiñas & Murcia, 2024), forecasting (Lu et al., 2025), optimisation (Gulbakyt et al., 2025), and
detection (Huang et al., 2025).

Interface metrics establish that stages hand over correctly, which has no direct precedent in the
reviewed literature and is therefore reported explicitly as a limitation of the evidence base
(de Zarzà et al., 2024; D'Souza et al., 2026). Outcome indicators establish whether the composition
changes user behaviour, which is the level at which the planning literature locates adherence
(Yeo et al., 2023; Cumaio et al., 2026) and at which local evidence locates well-being
(Claro & Noval, 2025; Francisco et al., 2026). Institutional budget systems demonstrate
outcome-level evaluation of a comparable system
(Santiago et al., 2025), and adaptive monitoring work demonstrates the continuous-recalibration
element (Zhong, 2025; Huang et al., 2025).

#### Savings Rate

Savings rate is savings contributions divided by monthly income over the evaluation period,
measuring whether the system moves the outcome it is designed to affect. The planning literature
locates this as an adherence outcome rather than a system property, dependent on progress
visibility and support (Yeo et al., 2023), and capability reviews confirm intention does not
produce it unaided (Cumaio et al., 2026; Samli et al., 2026).

Local evidence establishes that this population has particular headroom, since Filipino consumers
were reported less likely to save under price pressure
(Bangko Sentral ng Pilipinas, 2026), and that recurring borrowing substitutes for absent savings
(Francisco et al., 2026). Well-being regressors indicate savings practice is associated with
well-being outcomes (Claro & Noval, 2025). The indicator is therefore reported with its confidence
interval and without causal claim
(Yoganandham, 2025; Cumaio et al., 2026; Yeo et al., 2023).

#### Savings Progress

Savings progress is the funded proportion of each goal's planned periods, measuring goal attainment
against the schedule the optimiser produced. It is distinguished from savings rate because a user
can hit a high rate while funding goals in an order the solver did not intend
(de Zarzà et al., 2024; Gulbakyt et al., 2025).

The distinction matters for evaluating the composition specifically, since goal ordering is where
multi-objective weighting is expressed and where the optimiser's assumptions are most visible
(Gulbakyt et al., 2025; Lu et al., 2025). Planning review indicates that a plan whose schedule the
user cannot recognise as theirs will be abandoned regardless of its rate
(Yeo et al., 2023; Yoganandham, 2025). Preference deviation at the individual-goal level is
therefore reported alongside this indicator
(Cumaio et al., 2026; Francisco et al., 2026; Samli et al., 2026).

#### Alert Frequency

Alert frequency is the count of unusual-expense alerts per active user per month, measuring both
detector activity and spending volatility. The reviewed threshold-calibration literature treats it
as the primary diagnostic for detector calibration, since frequency that rises without a
corresponding rise in unusual spending indicates threshold drift (Huang et al., 2025; Zhong, 2025).

It is not a performance target, and treating it as one produces the failure the literature
identifies, in which a detector tuned to a fixed alert rate stops detecting
(Huang et al., 2025; Hamdare et al., 2025). It is interpreted jointly with precision and with spending
volatility, and the feedback channel is what allows a user to distinguish a genuine change from a
calibration artefact (Zhong, 2025; Cumaio et al., 2026). Spending-habits work supplies the
behavioural baseline against which frequency is judged meaningful
(Hamdare et al., 2025; Thakur & Jadhav, 2025).

#### Debt Progress

Debt progress is principal paid over principal planned per debt, measuring adherence to the
repayment schedules the solver produced. It is the indicator most directly tied to the harm the
study addresses, since the documented local harm is accumulation from unrecognised and unmanaged
borrowing (Francisco et al., 2026; Esperanza, 2025).

Debt-management evidence establishes both its value and its limits: early progress prevents
accumulation, but debt outcomes are also shaped by income shocks the system does not control
(Samli et al., 2026; Cumaio et al., 2026). Borrowing-dependency analysis shows that dependency is
entrenched by institutional and literacy factors beyond the reach of a budgeting tool
(Francisco et al., 2026), which is why this indicator is reported as adherence to plan rather than
as a causal effect on debt outcomes (Claro & Noval, 2025; Yeo et al., 2023). Digital lending
evidence supplies the confounder to control for (Esperanza, 2025).

#### Plan Adherence

Plan adherence is actual allocation over recommended allocation, the broadest system-level indicator
and the one closest to the planning literature's construct of adherence. Planning review identifies
adherence as the outcome that support mechanisms exist to produce
(Yeo et al., 2023), and capability reviews confirm the same relationship across developing economies
(Cumaio et al., 2026; Samli et al., 2026).

It is the indicator that most directly tests the composition claim, because a user can follow one
component's recommendation and ignore another's
(de Zarzà et al., 2024; D'Souza et al., 2026). Low adherence with high component-level accuracy
indicates a composition or presentation failure rather than a component failure, which is a
distinction the literature does not draw and which the three-level evaluation design is intended to
make (Gulbakyt et al., 2025; Lu et al., 2025). Preference deviation supplies the diagnostic for
whether presentation is the cause (Yoganandham, 2025; Cumaio et al., 2026).

# System Evaluation

BUDGIE is evaluated at two levels: software quality, using an established instrument, and model
performance, using metrics matched to each algorithm. The two are reported separately because they
answer different questions, and combining them would obscure which failures belong to the
application and which to the models. Both levels draw on standards-based evaluation practice
documented in the reviewed literature, and both carry the limitations recorded in the sections that
follow.

## Software Quality Evaluation

Software quality evaluation applies the ISO/IEC 25010 product quality model, which supplies
reference characteristics for specifying, measuring, and evaluating ICT and software product quality
(International Organization for Standardization, 2023). The model subdivides each characteristic into
subcharacteristics that carry concrete measures, and it is a reference model rather than a fixed
checklist, so a study may select the subset bearing on its system
(International Organization for Standardization, 2023). This study evaluates functional suitability,
performance efficiency, reliability, security, portability, and usability.

<!-- ISO CHARACTERISTIC VOCABULARY FLAG. The six characteristics above are 2011-vocabulary, but
     the citation is to ISO/IEC 25010:2023, which replaced usability with interaction capability
     and portability with flexibility, and added safety, giving nine characteristics. Both this
     chapter and Chapter 1 V6 use the same six and therefore agree with each other, but neither
     matches the standard it cites. The fielded questionnaire diverges again by using five
     characteristics, substituting maintainability for portability.

     Resolution, not yet applied: the cheapest correct fix is to cite ISO/IEC 25010:2011 for the
     six-characteristic set, since both chapters already agree and one citation change makes them
     accurate. The alternative is renaming to 2023 vocabulary in both chapters and adding
     compatibility and safety. Left flagged for the researchers to decide. -->

Applied evaluation of this model in the reviewed literature supports the approach and its
instrumentation. A ticketing management system was evaluated against ISO/IEC 25010:2023 with a
paired AHP weighting, which demonstrates the model in use on an operational system
(Ariningsih & Muhammad, 2024), and a VR application was evaluated against ISO 25010 across
functional suitability, performance efficiency, usability, and portability, which demonstrates the
characteristic-level granularity this study adopts (Lianto et al., 2023). An institutional budget
system supplies a comparable evaluation of a comparable artefact
(Santiago et al., 2025).

The limits of the model are also documented. Because it is a reference model, subset selection is
a judgement that this study makes explicitly rather than a result the model supplies
(International Organization for Standardization, 2023), and the risk of an unexamined subset is
that a characteristic bearing on the system is omitted. Comparative evaluation of consumer
applications shows that the usability-adjacent characteristics are the ones most often addressed
superficially, with tracking supported and planning support weak
(Alenazi & Sas, 2023), so functional suitability is treated in this study as the characteristic most
likely to be over-claimed (D'Souza et al., 2026). Reviews of machine learning for the domain
support treating the same characteristic sceptically, since components are often evaluated
individually rather than as a system
(D'Souza et al., 2026; Lu et al., 2025).

### System Usability Scale

The System Usability Scale is a ten-item validated questionnaire yielding a 0 to 100 score, and it
is the usability measure this study reports. It was introduced as a deliberately economical
instrument for usability assessment (Brooke, 1996), and that economy is its principal virtue here,
since a ten-item instrument is viable for the sample size this study can recruit
(Francisco et al., 2026; Claro & Noval, 2025).

Its limitations are documented and are the reason a systematic review of SUS instruments was
conducted for the mobile health context, finding that standalone and interactive applications differ
in how the SUS should be administered and interpreted (Lim et al., 2025). That review is the
source for the administration decisions made in this study, and it also establishes that SUS
results are interpreted against benchmarks rather than in isolation (Lim et al., 2025; Brooke, 1996).

Two structural cautions apply. First, the SUS belongs to the quality-in-use model, ISO/IEC 25019,
not to the product quality model of ISO/IEC 25010; the 2023 product model states that interaction
capability is a prerequisite for usability rather than a substitute for it, so a SUS score
supplements rather than operationalises the usability characteristic
(International Organization for Standardization, 2023). Second, SUS is not diagnostic, since a low
score identifies that a problem exists without locating it, so it is reported alongside the
characteristic-level findings rather than as a substitute for them
(Lim et al., 2025; Ariningsih & Muhammad, 2024). Applied ISO 25010 evaluations in the literature
show the same division of labour between summary score and characteristic-level measurement
(Lianto et al., 2023; Ariningsih & Muhammad, 2024).

<!-- NEEDS MORE SOURCES: 5 required; 4 attached. Usability evidence in the reviewed set is thin
     because it clusters in two papers (Lim et al., 2025; Brooke, 1996) with ISO-instrument papers
     adjacent to rather than about the SUS. A mobile-application usability validation study would
     materially strengthen this subsection. -->

### ISO/IEC 25010:2023

The characteristic-level measurement follows established practice. Applied evaluations score
subcharacteristics within each selected characteristic, using paired comparison for weighting where
a single score is required (Ariningsih & Muhammad, 2024; Lianto et al., 2023). Functional
suitability is assessed against the feature set the study specifies, which follows the comparative
evaluation finding that tracking and planning are separable capabilities that must be measured
separately (Alenazi & Sas, 2023).

Performance efficiency is assessed through the model performance metrics reported under Model
Performance Evaluation, and the standard's treatment of it as a time-behaviour characteristic
supports that routing rather than duplicating it here
(International Organization for Standardization, 2023). Reliability and security are assessed
structurally, since the reviewed literature supplies no applicable instrument for a system of this
size (Santiago et al., 2025). Portability is assessed against the deployment matrix implied by the
cross-platform client (Ghonaim & El-Sharawy, 2025; Alenazi & Sas, 2023). The vocabulary conflict
recorded above applies to this subsection in particular
(International Organization for Standardization, 2023; Lianto et al., 2023).

<!-- NEEDS MORE SOURCES: 5 required; 5 attached, but 2 of them (Ariningsih & Muhammad, 2024;
     Lianto et al., 2023) evaluate different systems in different domains. The evidence base for
     applying this standard to a consumer financial application specifically is thin. -->

## Model Performance Evaluation

Model performance evaluation assesses each algorithm against metrics matched to its function, and
reports the three evaluation levels distinguished under Model and Algorithm Integration: component
accuracy, interface correctness, and outcome effect. Component-level practice is well established
in the reviewed literature for each algorithm class, with classification
(Laspiñas & Murcia, 2024), forecasting (Lu et al., 2025), optimisation
(Gulbakyt et al., 2025; de Zarzà et al., 2024), and detection
(Huang et al., 2025; Zhong, 2025) each having documented metric conventions.

The forecasting evaluation additionally includes a disaggregation-accuracy check, because the
pipeline's forecasts depend on annual survey data disaggregated to monthly resolution and an error
there propagates into every downstream stage
(Lu et al., 2025; de Zarzà et al., 2024). The classification and detection evaluations are subject
to the absence of labelled ground truth discussed in their respective sections, and this is a
limitation of the evidence base rather than a property of the systems
(Laspiñas & Murcia, 2024; Hamdare et al., 2025; Huang et al., 2025).

Interface-level evaluation has no direct precedent in the reviewed set, and is reported as a stated
limitation rather than presented as established practice
(D'Souza et al., 2026; de Zarzà et al., 2024). Outcome indicators are drawn from the system-level
set and are interpreted as adherence to plan rather than as causal effects on financial outcomes, for
the reasons given under Plan Adherence
(Yeo et al., 2023; Cumaio et al., 2026; Francisco et al., 2026). Institutional evaluation of a
comparable system supplies the closest available precedent for reporting at system level
(Santiago et al., 2025), and adaptive monitoring work supports the continuous component
(Zhong, 2025).

<!-- SYSTEM EVALUATION IS THE WEAKEST TOPIC IN THE CHAPTER. The reviewed corpus contains one
     system-evaluation paper above threshold (Santiago et al., 2025). Everything else is either an
     ISO-instrument paper on a different system or a general ML review. The panel's instruction
     was to mark this and proceed, which is done here. Acquiring corpus papers tagged to the
     system_evaluation module is the highest-value action for this section. -->

## Synthesis

The reviewed literature establishes personal financial management as a critical capability with
particular relevance in developing economies, and it establishes planning theory well ahead of
application capability. Planning review links planning activity to subsequent financial outcomes and
supplies theory on the mechanisms connecting the two (Yeo et al., 2023), while capability and
behaviour reviews find consistent associations between financial capability and saving and debt
behaviour across contexts (Cumaio et al., 2026; Samli et al., 2026). The Philippine evidence
confirms the need empirically, documenting reduced savings propensity under price pressure
(Bangko Sentral ng Pilipinas, 2026), borrowing dependence traced to absent planning capacity
(Francisco et al., 2026), and planning practice among the regressors of well-being
(Claro & Noval, 2025). Reviews of budgeting practice complete the conceptual base
(Yoganandham, 2025; Sapiri & Awaluddin, 2023).

Against that theory, existing systems under-deliver on precisely the planning function. Comparative
evaluation isolates tracking-versus-planning as a generalizable deficiency of the dominant
application category, meaning the gap is not incidental to particular products
(Alenazi & Sas, 2023). Reviews of machine learning for the domain find the components individually
established but evaluated in isolation against single objectives
(D'Souza et al., 2026), and household planning formulations confirm that automated planning remains
an active area with constraint adherence unresolved (de Zarzà et al., 2024). The individual
techniques this study composes are each documented: income-level classification demonstrates usable
stratification signal (Laspiñas & Murcia, 2024), multi-criteria and constrained allocation models
demonstrate that allocation quality depends on formulation (Gulbakyt et al., 2025; Lu et al.,
2025), spending-habits work demonstrates behaviourally meaningful structure in transaction data
(Hamdare et al., 2025), and adaptive threshold work addresses the fixed-threshold weakness that
limits baseline detection (Huang et al., 2025; Zhong, 2025). Mobile application work shows these
components deploying individually rather than composed (Ghonaim & El-Sharawy, 2025; Thakur &
Jadhav, 2025), and institutional systems show analytics-driven allocation at operational scale
(Santiago et al., 2025).

The identified research gap is therefore the absence of an integrated, seasonality-aware personal
financial management system for Filipino users that composes profile classification, seasonal expense
forecasting, constraint-respecting budget creation, and unusual expense detection into a single
dated plan with adherence tracked against it. The gap is integration, not technique: each component
has support, and no reviewed system composes them
(Alenazi & Sas, 2023; D'Souza et al., 2026; de Zarzà et al., 2024). Two further constraints on the
claim are worth stating. First, the corpus provides no Philippine individual-level seasonal
forecasting precedent, so the seasonal decomposition step is extrapolated from population
consumption structure rather than from prior individual work (Lu et al., 2025). Second, the
evaluation is subject to the absence of labelled ground truth for two of the four algorithms, which
limits the strength of the accuracy claims (Laspiñas & Murcia, 2024; Huang et al., 2025).

This study addresses the gap through the development and evaluation of BUDGIE, a seasonality-aware
savings-debt plan pipeline for Filipino users aged 18 to 59 in the National Capital Region. Its
contribution is the composition and its evaluation, with the components selected from the reviewed
literature rather than proposed as novel.

## Conceptual Model of the Study

The conceptual framework follows an Input-Process-Output model, extended with an evaluation
component, that traces the systematic development and evaluation of BUDGIE.

<!-- FIGURE 1 PLACEHOLDER: conceptual model (IPO) diagram. NOT YET CREATED. The Chapter 2
     V3 .docx carries the caption "Figure 1." with no image behind it, and none of the sixteen
     chapter .docx files in google-drive/ embeds any image, so there is no source diagram in the
     repository to export. An earlier version of this comment claimed the image was in the .docx
     media folder; that was wrong and has been corrected. The diagram must be drawn from the
     IPO description below, or obtained from the panel. -->

Figure 1. Conceptual Model of the Study

The **Input** component identifies the knowledge, software, hardware, and data requirements of the
study. Knowledge requirements are the computational and behavioural foundations reviewed in this
chapter, which determine why each algorithm was selected and what property it must satisfy
(Laspiñas & Murcia, 2024; Huang et al., 2025). Software requirements specify the development
platform, with a cross-platform mobile client, a service-based backend, and a separate model-serving
service, following the reviewed literature's observation that model-bearing features and
client-side features degrade differently and should be separated
(D'Souza et al., 2026; Lu et al., 2025). Hardware requirements are development and testing
resources, including the offline-caching capability the client requires
(Ghonaim & El-Sharawy, 2025; Alenazi & Sas, 2023).

Data requirements are three distinct sources serving three distinct purposes. The Philippine
Statistics Authority (PSA) Family Income and Expenditure Survey supplies income totals, expense
totals, household size, and distributional position, and is the source from which monthly estimates
are derived (PSA, 2023; de Zarzà et al., 2024; Yeo et al., 2023). The PSA Household Final
Consumption Expenditure series supplies the seasonal proportions used in that disaggregation, and
its length is the binding constraint on seasonal parameter estimation
(PSA, 2026; Lu et al., 2025; Gulbakyt et al., 2025). The group's own Public User Expectations and
Perceptions Survey supplies the requirements and evaluation criteria, administered to the target
population (Group 4, 2026; Francisco et al., 2026; Claro & Noval, 2025).

The **Process** component describes the activities through which BUDGIE is developed and evaluated.
Development follows an iterative and incremental methodology, chosen because integrating four
algorithmic components with a mobile client and a model-serving service produces requirement churn
that a sequential process would resolve late. Chapter 3 presents the development methodology in
full, including the workflow management approach adopted and the measurements taken from it; it is
deliberately not developed here, because methodology is not a topic in the approved outline for this
chapter and the available methodological evidence does not bear on the literature review.

The model-development process follows the standard pipeline of preprocessing, feature engineering,
training, validation, evaluation, and integration, with each stage producing the input the next
requires (Lu et al., 2025; D'Souza et al., 2026). Temporal disaggregation of annual survey data into
monthly estimates using consumption-calibrated seasonal proportions precedes forecasting, and its
accuracy is evaluated separately because errors propagate
(Lu et al., 2025; de Zarzà et al., 2024). The classifier is developed from domain knowledge rather
than from training data, following the reviewed finding that financial-behaviour constructs are
threshold-shaped and that labelled data is scarce outside institutional settings
(Cumaio et al., 2026; Laspiñas & Murcia, 2024). The optimiser and the detector are configured
against their respective input contracts, with the optimiser returning allocation, schedules, and a
feasibility status (Gulbakyt et al., 2025) and the detector returning alerts with deviation
information (Huang et al., 2025; Zhong, 2025).

The **Output** component is the primary deliverable: BUDGIE as a personal financial management
application using SARIMA-based seasonal expense forecasting to produce a profile-informed,
constraint-respecting savings and debt plan with unusual expense monitoring. The output is
distinguished from the individual techniques reviewed in the literature by their composition, which
is the contribution this study claims
(Alenazi & Sas, 2023; D'Souza et al., 2026; de Zarzà et al., 2024).

The **Evaluation** component verifies the quality and effectiveness of the output at the two levels
established under System Evaluation. Software quality evaluation applies the ISO/IEC 25010 product
quality model (International Organization for Standardization, 2023) with the System Usability Scale
as its usability measure (Lim et al., 2025; Brooke, 1996), and the vocabulary conflict recorded
under ISO/IEC 25010:2023 applies to this component. Model performance evaluation applies
function-matched metrics to each algorithm and system-level indicators to the composition
(Laspiñas & Murcia, 2024; Lu et al., 2025; Gulbakyt et al., 2025; Huang et al., 2025), following the
three-level structure set out under Performance Analysis
(Yeo et al., 2023; Santiago et al., 2025; Cumaio et al., 2026).

<!-- NO CITATION REQUIRED: the Input, Process, and Output components describe the research
     group's own system design and are not claims about prior work. The Evaluation component is the
     only part resting on external sources, and those are cited. Deliberately not padded. -->

## Outstanding Source Requests

Three kinds of dependency are recorded here, and they are not the same thing. A **PENDING
ACQUISITION** source has verified metadata but is not yet held as a file. A **SOURCE NEEDED** entry
is an unresolved citation that no verified source currently supports. An **UNVERIFIED** entry is one
whose identity is not confirmed and which must not be treated as final.

### Source needed

1. **BSP financial planning cycle.** Requested by the panel reviewer at the "Review and Monitoring"
   subsection, with the instruction to look in BUDI-Literature. **Not satisfiable from the held
   corpus text.** All Bangko Sentral entries were read on 2026-09-27: the Q4 2023 and full-year
   Financial Inclusion dashboards, the Annual Report 2025, the Consumer Expectations Survey Q2 2026,
   and two statistical releases. None is a financial planning cycle document, and the phrase "planning
   cycle" appears in none of them; every "cycle" match is monetary policy. The cycle is most likely
   presented as a figure, and figure content was never captured: `L--BangkoSentral-2023b` was
   converted via the pypdf `text()` fallback, which drops all figures, while `L--BangkoSentral-2025`
   and `-2026b` carry 20 and 65 figure references with no extracted content. The central-bank
   statistics that are available are cited for context in *Context of Financial Planning*, *Problems
   faced by Individuals in Financial Planning*, and *Budget Constraints*. One image-only BSP document
   would not be sufficient empirical backing in any case, so resolution needs figure extraction or
   OCR **and** at least one non-BSP source on the cycle, or the reviewer must confirm that the
   Consumer Expectations Survey is the intended source.
   *Correction:* an earlier revision of this entry claimed `L--BangkoSentral-2023b` was a 2005
   document with a wrong stem year. Retracted — it is the 2023 edition of an annual series whose
   preface records the maiden issue as June 2005. The stem is correct.
2. **Dasmariñas et al. (2024).** **RESOLVED 2026-09-27.** The file has been acquired, converted, and
   verified; it is now `L--Dasmarinas-2024` in BUDI-Literature and is cited in *Seasonal Expense
   Forecasting* and *SARIMA*. Venue, pages, and DOI were confirmed against the publisher's record
   rather than assumed, so the earlier concern about an unverified DOI no longer applies. Its scope
   limit is recorded in the sidecar: it models national aggregate consumption, not individual
   household expense seasonality, so the disaggregation step from population to individual remains
   flagged as an assumption rather than a sourced result.
3. **Dey & Arefin (2025).** The closest direct precedent for the rule-based classifier chosen. The
   *Saver and Borrower Profile Classification* topic is not short without it, so this is a strength
   rather than a gap. Candidate: Dey, S., & Arefin, M. S. (2025). Developing a rule-based system to
   recommend household budget. Journal of Information Systems Engineering and Management, 10(47s),
   148-182. https://jisem-journal.com/index.php/journal/article/view/9230
   (preprint: https://www.preprints.org/manuscript/202502.1315/v1)

### PENDING ACQUISITION

These are cited in this chapter but the project does not hold the file. They were inherited from
Chapter 2 V3, which did not hold them either, and an earlier revision of this document reported its
reference list as clean. That check was internal-consistency only: it confirmed the chapter agreed
with itself, not that the corpus could produce every source. A separate provenance audit against
`BUDI-Literature` found these six. This is the most significant unresolved issue in the chapter and
is recorded prominently rather than left implicit.

11. **Brooke, J. (1996).** *SUS: A "quick and dirty" usability scale.* In *Usability Evaluation in
    Industry*, 189-194. The canonical System Usability Scale source, load-bearing for *Software
    Quality Evaluation*, and the chapter's only pre-2023 exception. Not held. Highest priority: the
    paper is one page and the shortfall is narrow, since the reviewed usability evidence clusters in
    only two other papers.
12. **Philippine Statistics Authority (2023).** *Family Income and Expenditure Survey.* Not held.
    Currently supports the annual income, expense, household-size, and distributional inputs in the
    Conceptual Model.
13. **Philippine Statistics Authority (2026).** *Household Final Consumption Expenditure* series. Not
    held. Currently supports the seasonal proportions used in the temporal disaggregation. Dasmariñas
    et al. (2024) is now held and covers Philippine quarterly consumption expenditure 2001-2021, so it
    is a partial substitute, but it is an academic study of an aggregate series rather than the
    official statistics release the design names.
14. **Ariningsih, P., & Muhammad, A. H. (2024).** *Quality evaluation of Indonesian sharia
    fintech.* Not held. Cited for PFM feature comparison.
15. **Lianto, M. E., Primasari, C. H., Marsella, E., Wibisono, Y., et al. (2023).** Budgeting-app
    study. Not held. Cited for PFM feature comparison.
16. **Lim, P. C., Lim, Y. L., Rajah, R., & Zainal, H. (2025).** *Usability* study. Not held. Cited
    for PFM feature comparison and the usability argument.

Two entries in the reference list are legitimately outside the corpus and are **not** defects:
*International Organization for Standardization* (2023) is a standard, and *Group 4* (2026) is the
team's own survey instrument, which lives in `BUDI-Base/questionnaires/` rather than in
BUDI-Literature.

### Moved to Chapter 3

The updated topical outline has no Methodology topic, so the development methodology is presented in
Chapter 3. The four references that carried the removed Methodology section are therefore no longer
cited here and are re-listed for Chapter 3's use, not for this chapter's.

4. Alqudah, M., & Razali, R. (2024). Key factors for adopting Kanban in software development: An
   empirical study. *International Journal of Agile Systems and Management, 17*(2), 201-220.
   https://doi.org/10.1504/IJASM.2024.137890
5. Sathe, C. A., & Panse, C. (2023). An empirical study on impact of project management constraints
   in Agile software development: Multigroup analysis between Scrum and Kanban. *Brazilian Journal of
   Operations & Production Management, 20*(3), 1796. https://doi.org/10.14488/BJOPM.1796.2023
6. Shaout, A., Parker, B., Westerbeek, J., & Swaminathan, S. S. (2025). KanScrum: A Kanban + Scrum
   hybrid methodology. *Journal of Computer Sciences and Informatics, 2*(2), 131-147.
   https://doi.org/10.5455/JCSI.20250322020941
7. **Huss, M., Herber, D. R., & Borky, J. M. (2023).** Comparing measured Agile software development
   metrics using an Agile model-based software engineering approach versus Scrum only. *Software,
   2*(3), 310-331. https://doi.org/10.3390/software2030015
   **UNVERIFIED and now removed.** Metadata was taken from a citing bibliography rather than the
   publisher and was never confirmed. It should not be cited in Chapter 3 without verification at
   the MDPI page. The previous draft carried two other verified sources in the same paragraphs, so
   no claim depended on it.

### Corpus papers excluded on metadata grounds

Five corpus entries are not citable and are excluded from the reference list. This is recorded
because the corpus previously marked them verified.

8. `I--RSingh-2025` has no authors, no title, and no DOI, and its byline is genuinely ambiguous
   between "R" and "Singh". Unusable until the PDF is re-read.
9. `A--DSouza-2026`, `I--Zhao-2025`, and `L--Atento-2025` record an author affiliation where a
   journal belongs, so the publication outlet is unidentifiable and these are probably preprints.
   `A--DSouza-2026` is nonetheless retained below as an honestly-labelled unpublished manuscript
   because it is the only review of machine learning for this domain in the set, and the review
   point it supports is load-bearing for the gap claim.
10. `I--Yoganandham-2025` gives a journal name with no volume, issue, or pages. Retained below
    because it is used for a low-controversy definitional point, but it is not a stable outlet and
    should not be counted toward any topic's source quota.

### Pending acquisition

All references below carry metadata verified against page 1 of the source PDF or the publisher
record. They are cited in this chapter; the files themselves are not yet held in
`literature/bucket/`.

## References

Alenazi, M., & Sas, C. (2023). Evaluating budgeting apps: Limited support for budgeting compared to tracking. In *Proceedings of the British Computer Society HCI International Conference (BCSHCI 2023)* (pp. 1-12). British Computer Society. https://doi.org/10.14236/ewic/BCSHCI2023.1

Ariningsih, P., & Muhammad, A. H. (2024). Quality evaluation of ticketing management system using ISO/IEC 25010:2023 standards and AHP method. *Intechno Journal: Information Technology Journal, 6*(2). https://doi.org/10.24076/intechnojournal.2024v6i2.1870

Bangko Sentral ng Pilipinas. (2026). *Consumer expectations survey report: 2nd quarter 2026*. Monetary and Economics Sector, Department of Economic Statistics.

Brooke, J. (1996). SUS: A "quick and dirty" usability scale. In P. W. Jordan, B. A. Weerdmeester, B. Thomas, & I. L. McClelland (Eds.), *Usability evaluation in industry* (pp. 189-194). Taylor & Francis.

<!-- CITATION WINDOW EXCEPTION: 1996, admitted under the approved instrument-origin
     exception. It defines the SUS; the substantive properties are carried by Lim et al.
     (2025). Flagged at the point of citation under System Usability Scale. -->

Claro, D. M. L., & Noval, J. E. G. (2025). The regressors of financial well-being among LGU employees in Davao del Norte. *ISRG Journal of Economics, Business and Management, 3*(6).

Cumaio, S., Serrasqueiro, Z., & Madaleno, M. (2026). Linking financial literacy and behavioural finance to saving and debt behaviours: A literature review of global and developing economy contexts. *Journal of Risk and Financial Management, 19*(6), 425. https://doi.org/10.3390/jrfm19060425

Dasmariñas, A. P., De Castro, G. H., Lazona, B. J. M., & Usona, L. P. (2024). Forecasting the impact of COVID-19 on the household final consumption expenditure (HFCE) in the Philippines. *PUP Journal of Science & Technology, 14*(1), 70-90. https://doi.org/10.70922/ctzevg57

de Zarzà, I., de Curtò, J., Roig, G., & Calafate, C. T. (2024). Optimized financial planning: Integrating individual and cooperative budgeting models with LLM recommendations. *AI, 5*, 91-114.

D'Souza, M., Bhegade, P., Bhalekar, P., & Bhavsar, Y. (2026). A comprehensive review of machine learning techniques for intelligent personal finance management systems [Unpublished manuscript]. Department of Artificial Intelligence and Machine Learning, P.E.S Modern College of Engineering.

<!-- VENUE UNVERIFIED: the recorded outlet is an institutional affiliation rather than a
     journal, so the publication venue is unidentifiable and this is probably a preprint. Retained
     because it is the only review of machine learning for this domain in the corpus and it carries
     the integration-gap claim. Do not present as peer-reviewed literature. -->

Esperanza, D. N. (2025). Digital lending efficacy on debt management of wage earners. *ASEAN Journal of Management & Innovation, 12*(2), 111-127.

Francisco, A. A., Legal, G. A., & Legal, F. (2026). Causes of salary loan dependency: Basis for strengthening financial literacy program. *International Journal of Multidisciplinary Educational Research and Innovation, 4*(1), 705-728.

Ghonaim, W. A., & El-Sharawy, E. E. (2025). An intelligent budget management mobile application based on a recurrent neural network. *International Journal of Theoretical and Applied Research, 4*(2), 840-852.

Group 4. (2026). *Public user expectations and perceptions survey (PUEPS)* [Unpublished raw survey instrument]. III-DCSAD, University of Makati.

Gulbakyt, S., Almaz, A., Saule, S., & Suhrab, Y. (2025). Dynamic model for budget allocation in via multi-criteria optimization. *Journal of Applied Data Sciences, 6*(4), 3075-3088.

Hamdare, S., Khanna, A., & Agrawal, R. (2025). Analyzing and rewarding credit card spending habits in India: A machine learning approach. *International Journal of Computational Intelligence Systems, 18*, 165.

Huang, A., Zhang, X., Wang, Y., Tsai, S., Zhou, P., & Chen, L. (2025). Dynamic calibration of decision thresholds for financial anomaly detection: Verification with payment platform information and data. *Journal of Global Information Management, 33*(1), 1-26. https://doi.org/10.4018/JGIM.395852

International Organization for Standardization. (2023). *Systems and software engineering — Systems and software Quality Requirements and Evaluation (SQuaRE) — Product quality model* (ISO/IEC 25010:2023, 4th ed.).

<!-- STANDARD, admitted under the citation-window exception. The characteristic names used in
     this chapter are 2011-vocabulary, not the 2023-vocabulary; see the flag under
     ISO/IEC 25010:2023. -->

Laspiñas, E. L., & Murcia, J. V. B. (2024). Machine learning approaches in classifying income levels. *TWIST, 19*(2), 92-97. https://doi.org/10.5281/zenodo.10049652#134

Lianto, M. E., Primasari, C. H., Marsella, E., Wibisono, Y. P., & Cininta, M. (2023). Evaluasi functional suitability, performance efficiency, usability, dan portability berdasarkan ISO 25010 pada aplikasi VR Gamelan Slenthem. *KONSTELASI: Konvergensi Teknologi dan Sistem Informasi, 3*(1).

<!-- No DOI located. Title retained in the original Indonesian; provide an English
     translation in the final paper if the panel requires it. -->

Lim, P. C., Lim, Y. L., Rajah, R., & Zainal, H. (2025). Usability questionnaire for standalone or interactive mobile health applications: A systematic review. *BMC Digital Health, 3*(11). https://doi.org/10.1186/s44247-025-00150-y

Lu, Y., Zhou, H., & Zhang, Y. (2025). A constrained, data-driven budgeting framework integrating macro demand forecasting and marketing response modeling. *Journal of Technology Informatics and Engineering, 4*(3), 493-520. https://doi.org/10.51903/jtie.v4i3.466

Philippine Statistics Authority. (2023). *Family income and expenditure survey 2023*. PSA.

Philippine Statistics Authority. (2026). *Household final consumption expenditure, 2022-2026 quarter 2*. PSA.

Samli, F. B., Zaini, Z., & Yusof, K. S. (2026). A bibliometric analysis of how financial behaviour drives effective debt management. *Labuan Bulletin of International Business & Finance, 24*(1).

Santiago, R. L. T., Villarica, M. V., & Bernardino, M. P. (2025). Budget and financial management information system for public elementary schools: Analytics and predictive insights for MOOE allocation using linear regression. *International Journal of Advanced Research in Computer Science, 16*(3), 128-137. https://doi.org/10.26483/ijarcs.v16i3.7256

Sapiri, M., & Awaluddin, M. (2023). Distribution of financial attitude, financial behavior, financial knowledge and financial literacy on the investment decision behavior of young investors. *Journal of Distribution Science, 21*(11), 45-53.

Thakur, R. S., & Jadhav, A. (2025). Expense tracker management system using machine learning. *Sigma Journal of Engineering and Natural Sciences, 43*(4), 1265-1275. https://doi.org/10.14744/sigma.2025.00119

Vecina, R. A. P., & Encarnacion, M. J. G. (2025). Improving financial performance through financial literacy, good financial practice and fintech adoption. *Divine Word International Journal of Management and Humanities, 4*(2), 1688-1707.

Yeo, K. H. K., Lim, W. M., & Yii, K.-J. (2023). Financial planning behaviour: A systematic literature review and new theory development. *Journal of Financial Services Marketing, 29*, 979-1001. https://doi.org/10.1057/s41264-023-00249-1

Yoganandham, G. (2025). Mastering economic and financial sources with reference to budgeting, savings, early investing, debt management and the power of financial planning: A comprehensive analysis. *Degres Journal*. ISSN 0376-8163.

<!-- WEAK VENUE: journal name only, with no volume, issue, or pages, so the record is not
     stably citable. Used for a definitional point only. Do not count toward any topic quota. -->

Zhong, M. (2025). Adaptive anomaly detection threshold for financial data quality monitoring based on time series features. In *2025 International Symposium on Artificial Intelligence and Computational Social Sciences (AICSS 2025)*. ACM. https://doi.org/10.1145/3776759.3776850
