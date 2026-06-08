```yaml
paper_id: 10.1037/xge0001541
designation: international
title: How and when does a used (vs. unused) account affect consumption behavior?
authors: Yin, S.; Sharif, M. A.
year: 2024
venue: Journal of Experimental Psychology: General
odin_topics:
  - 5.A
  - 3.A
  - 7.A
shorthand_tags:
  - /financial-behavioral-profiles
  - /expense-categorization
  - /budgeting-strategies
tldr: Consumers are more likely to spend remaining resources from a used account than from an unused account with the same absolute amount because they value the resources less.
problem_and_motivation: No prior research has examined how the mere fact that an account has been used (vs. unused) influences future spending, holding absolute balance constant. Understanding this effect is important for predicting consumer behavior in gift cards, checking accounts, and reward programs. The gap is a lack of empirical evidence on within-account relative comparisons and their behavioral consequences.
approach:
  - Seven experimental studies (total N = 8,667) using MTurk and Prolific participants in the US.
  - Manipulated used accounts (e.g., $10 left from $100 gift card) versus unused accounts ($10 gift card) across gift cards, checking accounts, and credit card reward points.
  - Measured spending likelihood (0-100 scale) and perceived valuation (0-100 scale) as mediator.
  - Tested moderation by proportion remaining (60%, 40%, 20% left) and alternative explanations (external reference point).
  - Included incentive-compatible behavioral experiments (Studies 5 and 6) to confirm robustness.
findings:
  - "num: Participants were more likely to spend from a used vs. unused gift card (60.6 vs. 44.8, d = 0.44, p < .001)."
  - "num: Valuation significantly mediated the used vs. unused effect on spending (a´b = -0.91, 95% CI [-1.96, -0.025])."
  - "num: The effect strengthened as the proportion remaining decreased: spending likelihood dropped 7.99 points per 20% decrease in remaining proportion in used accounts (p < .001)."
  - When no original amount was specified, participants spent as if the account was used, not unused.
  - The effect held for endowed (gift cards, points) and earned resources (checking accounts) and extended from spending to charitable donation.
key_figures_tables:
  - "Figure 1: Spending likelihood by condition → Used account (60.6) higher than unused without reference (44.8) and with reference (49.5)."
  - "Figure 2: Used checking account leads to lower valuation and higher spending than unused account."
  - "Figure 3: Used reward points condition (63.98 spending) vs unused (58.26) and unused with external reference (57.83)."
  - "Figure 4: Linear decrease in spending as remaining proportion drops from 60% to 20% in used accounts, no trend in unused accounts."
key_equations:
  - equation: "None."
    explanation: ""
definitions:
  - term: Used account
    definition: An account from which some resources have already been spent, leaving a remaining balance smaller than the original amount.
  - term: Unused account
    definition: An account with the same absolute remaining balance but no prior spending (original amount equals current balance).
  - term: Within-account comparison
    definition: Comparing the current remaining amount to the original amount in the same account.
  - term: Valuation
    definition: Psychological perception of importance, worth, or usefulness of a resource.
critical_citations:
  - "[Thaler, 1985] — mental accounting foundation"
  - "[Morewedge et al., 2007] — relative comparison affects valuation"
  - "[Arkes et al., 1994] — lower valuation increases spending"
  - "[Heath & Soll, 1996] — earmarking and budgeting"
relevance:
  topics:
    - code: 5.A
      name: Financial Behavioral Profiles in Personal Finance
      justification: Identifies a systematic spending bias (used vs unused account) that can be used to profile users.
    - code: 3.A
      name: Expense Categorization Frameworks
      justification: Shows that the categorization of an account as used (vs unused) changes spending decisions, informing how expense categories should be designed.
    - code: 7.A
      name: Budgeting Strategies as Domain Knowledge
      justification: Provides evidence that framing an account as unused reduces spending, a strategy for budget recommendation.
  contribution: This paper informs Odin's spending forecasting module by demonstrating that account usage history (used vs unused) is a significant predictor of spending likelihood, beyond absolute balance. For budget recommendation, it suggests that presenting accounts as "unused" (e.g., fresh budget envelopes) can reduce unnecessary spending. The valuation mechanism can be integrated into Odin's behavioral profiling to better understand user sensitivity to account framing. Finally, the moderation by proportion remaining allows Odin to calibrate predictions dynamically as users spend down accounts.
  directly_justifies:
    - "Consumers value remaining resources less in a used account than in an unused account."
    - "Spending likelihood increases as the proportion remaining in a used account decreases."
    - "People spend from an unspecified checking account as if it were used, not unused."
  limits:
    - "All but one study used hypothetical scenarios, though the incentive-compatible study replicated the effect."
    - "Sample limited to US online participants, limiting cross-cultural generalizability."
  mapping_rationale: The paper directly addresses financial behavioral patterns (5.A) by revealing a robust bias in spending based on account usage history. It also falls under expense categorization (3.A) because the used/unused distinction is a categorical property of an account that influences consumption. Finally, it informs budgeting strategies (7.A) by showing how account framing can nudge spending. Codes related to prediction algorithms (6.A, 6.B) and anomaly detection (8.A) were rejected because the paper does not model or detect anomalies. Demographically specific codes (1.A-1.C) were rejected because the sample is not Filipino young professionals.
limitations:
  - "Results may not generalize to non-US cultures or languages. [unacknowledged]"
  - "The effect was not tested with very large account sizes (e.g., thousands of dollars). [unacknowledged]"
  - "Studies primarily used forced-choice spending scenarios; real-world longitudinal behavior not observed."
remember_this:
  - "Used accounts increase spending likelihood by 15-16 percentage points over unused accounts."
  - "Lower perceived valuation of remaining resources mediates the used-account effect."
  - "Spending rises as the remaining proportion drops from 60% to 20% in used accounts."
  - "Framing a checking account as unused can reduce spending."
```