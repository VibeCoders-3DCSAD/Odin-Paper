Proceeding Paper
Optimizing Fleet Composition for Electric Vehicle Integration:
A Case Study in the Philippines †

Lance Gabriel O. Ramos 1, Liam Alec M. Rapada 1, Dennis L. Umlas 1 and Yoshiki B. Kurata 1,2,3,*

1

The Graduate School, University of Santo Tomas, España Blvd, Manila 1015, Philippines;
lancegabriel.ramos.gs@ust.edu.ph (L.G.O.R.); liamalec.rapada.gs@ust.edu.ph (L.A.M.R.);
dennis.umlas.gs@ust.edu.ph (D.L.U.)

2 Department of Industrial Engineering, Faculty of Engineering, University of Santo Tomas, España Blvd,

Manila 1015, Philippines

3 Research Center for Engineering and Technological Sciences, University of Santo Tomas, España Blvd,

Manila 1015, Philippines

* Correspondence: ybkurata@ust.edu.ph; Tel.: +63-2-3406-1611 (ext. 8494)
†

Presented at 2025 IEEE International Conference on Computation, Big-Data and Engineering (ICCBE),
Penang, Malaysia, 27–29 June 2025.

Abstract

As the Philippines aims to electrify its vehicle fleet by 2030, it seeks to be a leading example
for other government agencies adopting electric and hybrid electric vehicles. This study
addresses the challenge of optimizing budget allocation to support this transition under
fiscal constraints. A hybrid decision-making approach is employed, integrating the analytic
hierarchy process (AHP) and linear programming (LP) to guide procurement strategy. AHP
is used to establish a hierarchy of decision criteria, and LP is used to translate these into
the most favorable outcome constrained by budget limitations. This framework supports
rational and criteria-driven decision-making for public fleet planning. The resulting model
enables the Philippines to maximize the impact of electrification while adhering to financial
and operational constraints. The findings contribute to policy-oriented planning models
that align sustainability goals with real-world budgetary conditions.

Keywords: fleet optimization; analytical hierarchy process; linear programming

1. Introduction

The decarbonization of government fleets has become a critical energy and envi-
ronmental policy goal in many developing countries. The Philippines’ energy plan for
2023–2050 sets ambitious targets for electrification by 2030. The directive pushes public
institutions toward electric vehicle (EV) adoption, supporting climate objectives and the
broader EV ecosystem [1].

EV adoption in the public sector faces non-negligible challenges, particularly in terms
of investment cost, maintenance needs, and readiness of supporting infrastructure. Con-
strained by rigid procurement processes and limited fiscal flexibility, public institutions
require rigorous planning tools to align long-term electrification goals with available bud-
gets. Traditional approaches often fail to integrate qualitative strategic criteria—such as
environmental impact or inter-agency replicability—into quantitative resource optimization
models [2].

In response to these complexities, we developed a hybrid decision-support frame-
work combining the analytic hierarchy process (AHP) with linear programming (LP) to

Academic Editors: Teen-Hang Meen,

Wei Chien and Cheng-Fu Yang

Published: 13 March 2026

Copyright: © 2026 by the authors.

Licensee MDPI, Basel, Switzerland.

This article is an open access article

distributed under the terms and

conditions of the Creative Commons

Attribution (CC BY) license.

Eng. Proc. 2026, 128, 29

https://doi.org/10.3390/engproc2026128029

Eng. Proc. 2026, 128, 29

2 of 6

evaluate and prioritize investment decisions for the country’s vehicle fleet moderniza-
tion. AHP is widely used for structuring multi-criteria problems and capturing expert
preferences through pairwise comparisons. At the same time, LP has proven effective in
optimizing discrete resource allocations under constraints such as cost, fleet mix, and policy
compliance [3,4].

The results of this study assist in determining the most cost-effective mix of EVs
and hybrid EVs, using a structured optimization model that integrates policy priorities
with fiscal realities. The framework applies to any global government agencies seeking to
balance sustainability, operational efficiency, and public accountability in their transition to
low-emission transport systems [5].

2. Materials and Methods

We applied to a hybrid decision-support framework integrating AHP and LP to deter-
mine the optimal composition of fuel technologies in the Philippines’ vehicle fleet, mandating
the gradual shift to cleaner vehicle technologies across the public sector. The model as-
sumes a fixed total fleet size of 135 vehicles, all internal combustion engine (ICE) units in the
2025 baseline. By 2030, at least 70% (≥95 units) must be converted to alternate fuel vehicles
(AFVs)—comprising battery electric vehicles (BEVs), hybrid electric vehicles (HEVs), and
plug-in hybrid electric vehicles (PHEVs)—without exceeding the original fleet size.

2.1. AHP

AHP, developed by Saaty [4], was used to quantify the relative importance of three
decision criteria: emission, range, and technology maturity. Expert input was gathered
through pairwise comparisons using a 1–9 scale, which captures the relative importance of
each criterion. The structure of the AHP decision process is illustrated in Figure 1.

Figure 1. AHP priorities.

The criteria were compared in pairs, and a normalized matrix was constructed. The
weight vector was derived from this matrix using the principal eigenvector method. The
process included consistency verification using the consistency ratio (CR). A resulting CR
of 0.0564 confirmed that the judgments were consistent. These weights were then used to
score the decision alternatives—HEV, BEV, and PHEV—under each criterion, and a final
utility score for each alternative was calculated through weighted summation. These utility
scores were used as coefficients in the LP objective function [2,4].

2.2. LP

The linear programming model was formulated to maximize objective value using
the AHP-derived weights while satisfying operational, financial, and policy constraints.

https://doi.org/10.3390/engproc2026128029

 Eng. Proc. 2026, 128, 29

3 of 6

Let xi ∈ Z+ represent the number of vehicles of fuel type i ∈ {HEV, BEV, PHEV, BEV}. The
model does not classify vehicles by size or type (e.g., MPV, pickup), focusing instead on
optimizing the fuel technology mix.

2.2.1. Objective Function

The objective function is used to maximize the objective value and is calculated as the

weighted sum of selected units for each fuel type.

Maximize Z = 0.2922 X1HEV + 0.5507 X2BEV + 0.1572 X3PHEV

(1)

such that X1 denotes the number of HEVs, X2 denotes the number of BEVs, and X3 denotes
the number of PHEVs.

2.2.2. Constraints

To ensure feasibility, the following constraints were applied.

•

Fleet size constraint: The total number of vehicles remains fixed at 135.

∑

i Xi = 135

(2)

• AFV share constraint: At least 95 (70.00%) vehicles out of the 135 from the baseline

must be HEV, PHEV, or BEV.

•

•

XHEV + XBEV + XPHEV ≥ 95

(3)

BEV lower bound constraint: BEV count must be equal or greater than the existing
charging stations.

XBEV ≥ 9

(4)

BEV upper bound constraint: An existing charger can accommodate up to only 2 BEVs;
each vehicle charges every 3 days.

XBEV ≤ 54

• Annual fuel budget constraint: PhP. 8.20 million (USD 140,000).

30, 370XHEV + 10, 123.46XPHEV ≤ PhP. 8, 200, 000

•

Procurement budget constraint: PhP. 273.30 million (USD 4.70 million).

(5)

(6)

2, 333, 000XHEV + 1, 925, 000XPHEV + 2, 869, 000XBEV ≤ PhP. 273, 300, 000

(7)

• Annual repair and maintenance constraint:

30, 000XHEV + 30, 000XPHEV + 15, 000XBEV ≤ PhP. 6, 000, 000

(8)

• Diversity constraint: No fuel type can comprise more than 70% of the required

95 AFVs.

Xi ≤ 0.70 × 95 ∀i ∈ {HEV, PHEV, BEV}

• Non-negativity and integer constraint:

Xi,j ∈ Z +

(9)

(10)

https://doi.org/10.3390/engproc2026128029

Eng. Proc. 2026, 128, 29

4 of 6

The integer linear programming model was solved using the branch and bound
method to guarantee whole-number solutions and ensure compliance with the country’s
fleet transition guidelines.

2.3. Assumptions and Cost Estimation

The Philippines’ 2025 baseline consists of 135 ICE vehicles. The optimization does not
classify vehicles by type but focuses on the technology mix. The final fleet will combine
HEV, BEV, PHEV, and ICE units. The number of BEVs ranges from 9, matching the number
of charging stations available, to 54, assuming each station serves 2 BEVs per day and that
each vehicle charges every 3 days without exceeding service limits. Annual fuel cost and
repair and maintenance (R&M) budget caps are USD 140,000 and USD 103,000, respectively.
The total procurement budget is USD 4.6 million. Table 1 summarizes each fuel type’s
assumed unit costs, fuel consumption, and R&M values.

Table 1. Summary of input values by fuel type.

Capital
(USD)

39,788.52
32,830.22
48,776.33

Annual Fuel Cost
(USD)

Annual R&M Cost
(USD)

517.95
172.65
-

511.64
511.64
255.82

Fuel Type

HEV
PHEV
BEV

3. Results

AHP was used to evaluate three AFV technologies: HEV, BEV, and PHEV. Expert
judgments were elicited using a structured pairwise comparison matrix across three criteria:
emission, range, and technology maturity. The resulting criteria weights were emission
(0.6434), range (0.2828), and technology maturity (0.0738). Each alternative was then rated
under these criteria. The resulting local priorities and weighted aggregation yielded the
following overall scores: BEV = 0.5507, HEV = 0.2933, and PHEV = 0.1572.

This indicates that experts preferred BEVs due to their strong performance in emission
reduction, while HEVs ranked second mainly due to their superior range. Though offering
dual-fuel flexibility, PHEVs ranked lowest among the three alternatives due to a limited
advantage in any criterion. This prioritization reflects similar applications of AHP in sus-
tainable fleet planning, where emissions and operational reliability have been emphasized
over cost in public sector decision frameworks [2,4].

Using the AHP-derived priority weights, an integer LP model was solved using the
branch and bound method to determine the optimal number of HEVs, BEVs, PHEVs, and
remaining ICE units. The objective was to maximize the objective value of the fleet while
satisfying constraints on fleet size (135 vehicles), minimum AFV share (≥95), BEV limit
(9 < BEV ≤ 54), and budget ceilings for fuel, procurement, and maintenance. The resulting
objective value was 44.5050 with an optimal fleet mix consisting of the following: (1) BEVs:
54 units; (2) HEVs: 50 units; (3) PHEVs: 1 unit; and (4) ICEs: 30 units.

This configuration satisfies all policy and technical requirements. It achieves 77.78%
AFV penetration, well above the 70% minimum threshold. The BEV count reached the
upper bound limit of 54 units under a charging station’s capability assumption. Moreover,
it can reach up to 70 units if the upper bound limit is removed. Each AFV technology
was capped at 70% to retain diversity, leading to a balanced mix; BEVs were selected
more frequently due to high AHP overall weight and compatibility with existing fuel
infrastructure. This result supports earlier findings that hybrid decision models combining
AHP and LP can balance qualitative sustainability criteria with quantitative operational
constraints in fleet decision-making [2].

https://doi.org/10.3390/engproc2026128029

Eng. Proc. 2026, 128, 29

5 of 6

4. Discussion
4.1. Preference Structure

The prioritization of emission reduction within the AHP framework reinforced align-
ment with the Philippines’ sustainability goals. The high weight assigned to the emission
criteria ensured that technologies with lower environmental impact were structurally pre-
ferred, even when their costs or range performance were inferior. This mirrors global
fleet decarbonization priorities and emphasizes the utility of integrating policy values into
multi-criteria models. References [2,4] support this methodology, showing that decision-
makers can rationalize technology selection beyond mere cost comparison when explicit
environmental and operational priorities are made.

4.2. Strategic Role of Constraints

Accounting for the operational realities in the Philippines, the constraints were care-
fully chosen to represent these factors in the integer linear programming model. For
instance, the BEV charger cap (a minimum of 9 units, which can go up to 54 units) greatly
affected its deployment. If paired with expanded charging availability, a relaxed infras-
tructure constraint could theoretically yield a higher objective value—potentially raising it
by 6.5%, based on a scenario with unrestricted BEV allocation. These trade-offs reflect the
importance of infrastructure-readiness pacing policy ambition.

4.3. Utility and Replicability of AHP–LP

The integration of AHP and LP provided both methodological rigor and policy practi-
cality. AHP reflected the nuanced judgments of experts in the industry, while LP translated
those preferences into effective decisions under actual resource constraints. Moreover,
each allocation decision could be correlated to explicit preferences and constraints. Also,
the modular structure of the framework facilitates straightforward updating in the face
of costs and technological or infrastructure changes. As a result, it is equally well-suited
to strategic, long-term fleet planning and short-term budgeting. It can be modified by
other public agencies seeking to introduce structured electrification plans. Additionally, the
framework promotes policy feedback mechanisms. Its open design enhances continuous
improvement through stakeholder feedback to provide a firm analytical foundation for
institutional decision-making.

4.4. Limitations

While the model effectively determines a high-level technology mix, it does not disaggre-
gate vehicles by class (e.g., sedan, multi-purpose vehicles, van, pickup). This limits its ability
to inform logistics-specific planning or infrastructure deployment strategies. Additionally, the
model uses static assumptions for cost, operation and management, and infrastructure, subject
to fluctuations. Finally, AHP reflects a fixed stakeholder perspective; outcomes may shift with
the participation of top management, domain experts, or other relevant decision-makers, as
well as with changing priorities. Given these limitations, the framework still offers a valid
and well-structured approach to optimizing fleet transitions under multiple constraints while
also serving as a replicable tool for policy-aligned decision-making.

5. Conclusions

We developed the AHP–LP hybrid method to guide the Philippines’ transition toward
a strategically optimized vehicle fleet. AHP was used to capture expert-based preferences
across emissions, range, and technology maturity, producing a structured utility ranking
of AFV technologies. These preferences were then operationalized through LP, which
identified an objective value-maximizing mix of HEVs, BEVs, and PHEVs under budgetary,

https://doi.org/10.3390/engproc2026128029

Eng. Proc. 2026, 128, 29

6 of 6

infrastructure, and policy constraints. The final fleet allocation surpassed the 70% AFV
target while remaining fully compliant with resource and diversity limits.

The developed method’s advantage is its ability to link institutional objectives to quan-
titative planning mechanisms in a clear and defendable way. It is modular, flexible, and
responsive to changing planning environments. The model provides a replicable decision-
making aid for public agencies seeking greener initiatives by codifying value decisions and
operating compromises. Future improvements may include a more detailed criteria eval-
uation, vehicle class type breakdown, and employing scenario and sensitivity analysis to
improve the framework’s flexibility to changes in policy, costs, and infrastructure landscape.

Author Contributions: Conceptualization, methodology, validation, L.G.O.R., L.A.M.R., D.L.U. and Y.B.K.;
formal analysis, L.G.O.R., D.L.U. and Y.B.K.; investigation, L.A.M.R. and D.L.U.; resources, L.A.M.R. and
D.L.U.; writing—original draft preparation, L.G.O.R., L.A.M.R. and D.L.U.; writing—review and editing,
L.G.O.R., L.A.M.R., D.L.U. and Y.B.K.; visualization, L.G.O.R.; supervision, Y.B.K.; project administration,
Y.B.K. All authors have read and agreed to the published version of the manuscript.

Funding: This research received no external funding.

Institutional Review Board Statement: Not applicable.

Informed Consent Statement: Not applicable.

Data Availability Statement: The data used in this study are not publicly available due to limited
access. Interested parties may obtain the data by contacting the corresponding author upon request
and appropriate confirmation.

Conflicts of Interest: The authors declare no conflicts of interest.

References

1.

2.

3.

4.
5.

Varghese, A.M.; Pradhan, R.P. Roadmap for transitioning India’s privately owned bus fleets to electric fleets. Transp. Res. Part D
Transp. Environ. 2025, 140, 104623. [CrossRef]
Bai, C.; Fahimnia, B.; Sarkis, J. Sustainable transport fleet appraisal using a hybrid multi-objective decision-making approach.
Ann. Oper. Res. 2016, 358, 691–715. [CrossRef]
Cinar, A.P.; Eren, T. A large-scale integer linear programming to the daily fleet assignment problem: A case study in Turkey. In
Proceedings of the 2019 International Conference Industrial Engineering and Operations Management, Bangkok, Thailand, 5–7
March 2019.
Saaty, T.L. Decision making with the analytic hierarchy process. Int. J. Serv. Sci. 2008, 1, 83–98. [CrossRef]
Behdani, B.; Mahdavi, M.R.; Cinar, A.P. Strategic public transport planning using multi-objective optimization: Application to a
mixed-fleet scenario. In Proceedings of the IEEE International Conference Industrial Engineering and Engineering Management
(IEEM), Singapore, 10–13 December 2017.

Disclaimer/Publisher’s Note: The statements, opinions and data contained in all publications are solely those of the individual
author(s) and contributor(s) and not of MDPI and/or the editor(s). MDPI and/or the editor(s) disclaim responsibility for any injury to
people or property resulting from any ideas, methods, instructions or products referred to in the content.

https://doi.org/10.3390/engproc2026128029

