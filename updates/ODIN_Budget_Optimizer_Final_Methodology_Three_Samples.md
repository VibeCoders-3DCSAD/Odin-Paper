# ODIN Budget Optimizer — Final Methodology and Three Worked Samples

**Method:** Strict feasibility assessment; lexicographic linear programming (LP) for hierarchical baseline funding; separate relaxed LP for infeasible budgets; deterministic proportional surplus allocation.  
**Solver:** SciPy `linprog(method="highs")` for LP stages.  
**Budgeting cycle:** One month. **Currency:** Philippine pesos (₱). **All data below are illustrative test data**, not empirical estimates or a claim that the chosen hierarchy is universally optimal.

## 1. Final design decisions

1. Priority: **Essentials → Emergency Fund → Debt Payments → Savings → Other Categories**. Essentials comprise individual categories; Emergency Fund, Debt Payments, and Savings are each **one aggregate LP envelope**, not individual debt accounts or savings goals.
2. A **minimum due** is a hard required amount for the current cycle. A **baseline** is the amount ODIN aims to fund. They are distinct; the baseline must not be below its minimum. A fixed item has an exact required amount. Protected items have hard minima.
3. Mandatory minimums and fixed obligations are protected **across all hierarchy levels**. The hierarchy determines how remaining funds are assigned, not whether lower-priority contractual minimums can be ignored.
4. Essentials must reach **100% of their baselines** for a recommendation to be labeled `FEASIBLE`. Other groups may be below baseline while their hard minimums are satisfied.
5. Flexible categories in the same partially funded priority group receive **proportional baseline funding**, after hard minima/fixed allocations are secured. Do not use arbitrary preference weights to break ties.
6. Baseline LP allocations are temporarily bounded above by their baselines. These are **not user maximums**. No historical maximum or other ceiling is invented when a user supplies none.
7. **Only when every baseline is funded**, distribute surplus proportionally by positive baseline among non-fixed Essentials, Emergency Fund, Debt Payments, and Savings. Other Categories and fixed items receive no surplus. If a category has a user-defined maximum, cap and redistribute excess; no maximums are used in the three samples here.
8. If there is no eligible positive-baseline recipient for remaining money, place it in **Unallocated Reserve**. Never silently invent a positive baseline to make a category eligible.
9. If the strict model is infeasible, a **separate, explicitly relaxed LP** may return a partial recommendation. Its status remains `INFEASIBLE`; disclose which requirements were relaxed and their shortfalls. The user may review, edit, accept, or reject the recommendation; acceptance does not change its feasibility classification.
10. If spendable money is omitted but adequate history/requirements exist, generate a **fully baseline-funded illustrative budget** with zero modeled shortfalls and status `AFFORDABILITY_UNKNOWN`. Its total is an *estimated funding requirement*, not verified cash or evidence of affordability.
11. If history is insufficient, block automatic historical baseline generation. Manual optimization is available when sufficient category inputs and requirements are provided.

## 2. Data ownership and preparation

| Input/output | Owner / handling |
|---|---|
| Spendable amount and eligible account balances | User supplies amount; Odin App/API validate eligibility, ownership, availability, and prevent double counting. Expected income and borrowing limits are not automatically available cash. |
| Historical transaction totals and recurring flags | Transaction/ledger module; reconcile recurring instances to avoid double counting. |
| Fixed/Protected/Free status and optional maxima | Categories and Restrictions module. |
| Emergency Fund current minimum | Agreed optimizer-facing integration contract (in the earlier Odin design, exposed by the Debt module); confirm actual module ownership at implementation. |
| Debt minimum and any separately evidenced target | Debt module; internally distributes the assigned aggregate envelope. |
| Savings minimum and any separately evidenced target | Savings module; internally distributes the assigned aggregate envelope. |
| Baselines, LP, partial allocations, surplus, explanations | Odin-ML optimizer and deterministic explanation layer. |
| Acceptance and budget activation | Odin App/API; no optimizer output automatically executes payments or transfers. |

### 2.1 Recurring-aware baseline

For category `i`, historical month `t`, let `T[i,t]` be the recorded monthly total and `R[i,t]` the recurring transactions **already included** in that total. Then:

\[
N_{i,t}=T_{i,t}-R_{i,t},\qquad
\overline N_i=\frac{1}{n}\sum_{t=1}^{n}N_{i,t},\qquad
\boxed{B_i=\overline N_i+C_{i,\mathrm{current}}}.
\]

`C[i,current]` is the sum of recurring instances due in the **new** budgeting cycle, using current amounts and frequencies. Subtract only recorded recurring amounts included in the historical totals; add each current commitment once. If the category is an exact fixed obligation (e.g., Rent), use its verified fixed current-cycle amount. For the three financial envelopes, use a separately supplied target if available; otherwise follow the **minimum-only rule in §2.2**.

**Utilities source records (used in all samples):**

| Historical month | Total | Recurring already included | Nonrecurring |
|---|---:|---:|---:|
| June | ₱2,200.00 | ₱1,500.00 | ₱700.00 |
| July | ₱2,500.00 | ₱1,500.00 | ₱1,000.00 |
| August | ₱2,100.00 | ₱1,500.00 | ₱600.00 |

The mean nonrecurring amount is `(700 + 1,000 + 600)/3 = ₱766.666…`. September's current recurring bills are Electricity ₱1,200 and Internet ₱800, so the Utilities baseline is `₱766.666… + ₱2,000 = ₱2,766.666…`, **₱2,766.67 after input rounding**. In this document, monetary inputs are rounded to centavos before solving; all later calculations use **₱2,766.67**.

### 2.2 Missing financial-envelope baselines: explicit minimum-only rule

When an Emergency Fund, Debt, or Savings envelope has a verified current-cycle minimum `m_i` **but no independently supplied target**, do **not** pretend that its baseline was predicted or historically estimated. For the current cycle, define an **operational funding target** `T_i := m_i`, tagged `target_source = MINIMUM_ONLY` and `baseline_available = false`. For an envelope with an evidenced baseline, use `T_i := B_i`, tagged `target_source = BASELINE`. Use `T_i` for the baseline-stage LP's upper bound and shortfall reporting; report **zero shortfall against the known minimum-only target**, not proof of a complete financial plan or of an unknown preferred baseline.

**Surplus eligibility policy for minimum-only envelopes:** Exclude them from proportional surplus until a separate positive baseline/target is supplied or the user explicitly changes the policy. Otherwise their surplus weight would be an invented baseline. In Sample 3, the remaining surplus is therefore distributed only to eligible Essentials with known baselines. This is an explicit implementation rule for the missing-target case, not a consequence of LP itself.

If `m_i > 0`, a missing baseline does **not** mean the envelope receives ₱0. Its minimum is funded as a hard requirement in a feasible plan.

## 3. Mathematical model

Let `I` be all elements, `G_1,...,G_5` the priority groups, `A` validated spendable money, `T_i` the operational target (`B_i` when available, otherwise `m_i` under §2.2), `m_i` minimum due, `f_i` exact fixed amount, `p_i` protected minimum, and `x_i` the baseline-stage allocation. Monetary amounts are nonnegative. For the strict model:

\[
\sum_{i\in I}x_i\le A,\quad 0\le x_i\le T_i,\quad
x_i\ge m_i\ \text{where applicable},\quad
x_i=f_i\ \text{if fixed},\quad
x_i\ge p_i\ \text{if protected}.
\]

For strict `FEASIBLE` status also require **each Essential** `x_i = B_i`. Where a user-defined maximum exists, it must be consistent with minimum/fixed requirements and respected in the relevant stage. No maximum is imposed in these examples. The strict model must flag contradictory inputs (e.g., a minimum greater than a claimed target or a fixed amount that disagrees with its target) for correction, rather than silently overriding them.

Define group target shortfalls:

\[
d_i=T_i-x_i\ge0,\qquad D_k=\sum_{i\in G_k}d_i,\qquad
\boxed{\operatorname{lexmin}(D_1,D_2,D_3,D_4,D_5)}.
\]

Implement this as **five sequential LPs**: minimize `D_1`; fix its optimum (within numerical tolerance); minimize `D_2`; preserve earlier optima; continue through `D_5`. All hard minima/fixed requirements remain enforced **in every stage**. A preliminary strict-feasibility solve can be performed first; a failure branches to §4.

**Within-group proportionality:** Lexicographic minimization alone may admit multiple equally optimal allocations inside a group. Add a deterministic within-group tie-break/linear constraint. For an uncapped, minimum-free set of flexible elements, set `x_i = α_k T_i`, with common `0 ≤ α_k ≤ 1`. When fixed amounts or protected minima bind, first reserve their required funding; use a secondary proportional rule for the remaining *unmet* targets of flexible elements, capping each at its target and iterating as needed. In an LP implementation this can be expressed with group-specific linear constraints and/or additional lexicographic tie-break stages; do not claim the group shortfall objective by itself guarantees proportionality. Samples 1 and 3 have no partially funded group; Sample 2 applies the simple common-ratio case to Food and Utilities.

**Baseline vs feasibility:** A feasible plan can have nonzero shortfalls in Debt, Savings, or Other Categories **above their minima**. However, a plan with Essentials below baseline is `INFEASIBLE` under ODIN's selected feasibility definition even if all fixed and protected minima were funded.

## 4. Infeasible-case procedure

If the strict model cannot satisfy all hard requirements and full Essentials funding, **do not label its output feasible**. Run a separate partial-allocation LP. Introduce explicitly reported slack `q_i ≥ 0` for each requirement ODIN permits the partial model to relax: e.g., `x_i + q_i ≥ required_i`. Preserve `Σx_i ≤ A`, `x_i ≥ 0`, and non-negotiable technical constraints. Minimize mandatory/essential funding shortfalls according to the priority policy while recording every relaxed requirement and its exact gap. If fixed or protected amounts cannot be honored, they must be identified as unmet rather than silently treated as satisfied. This is a **recommendation for review**, not an executable claim that every obligation can be paid.

The separate relaxed LP can first reserve all simultaneously satisfiable hard minima, then distribute the remainder by hierarchy. If total mandatory minima exceed `A`, it must expose which minima are unpaid; a particular allocation across competing mandatory dues requires an explicit, tested relaxation policy and should not be presented as the unique financial answer.

## 5. Surplus allocation (after all operational targets are funded)

Only if `x_i = T_i` for **every** element, compute `S = A − Σ_i T_i`. Let `E` contain positive-**evidenced-baseline**, non-fixed Essentials, Emergency Fund, Debt, and Savings elements eligible under §2.2. Other Categories never receive surplus. With no user maximums and nonempty `E`:

\[
\boxed{s_i=S\frac{B_i}{\sum_{j\in E}B_j}},\qquad
x_i^{final}=T_i+s_i\ \text{for }i\in E.
\]

For ineligible elements `s_i = 0` and `x_i^{final}=T_i`. If `E` is empty, put `S` into Unallocated Reserve `R`. Otherwise use integer-centavo **largest-remainder rounding**: calculate exact centavo shares, floor each, then assign remaining centavos in descending fractional-remainder order with a stable category-ID tie-break. This preserves `Σs_i=S` exactly. The final conservation check is `Σ_i x_i^{final}+R=A`. If user maxima exist in future, cap and proportionally redistribute remaining surplus among eligible elements with capacity; **none are present in the following samples**.

---

# Sample 1 — No shortfalls; abundant spendable money

## 1A. Inputs and baseline construction

**Spendable money:** `A = ₱40,000.00`. No user-defined maxima. Utilities uses the recurring-aware calculation in §2.1; other ordinary category baselines use their historical averages; Rent is fixed. Financial modules supply evidenced baselines and separate minima.

| Priority | Element | Target/baseline | Minimum due | Status |
|---:|---|---:|---:|---|
| 1 | Food | ₱6,000.00 | ₱0.00 | Flexible |
| 1 | Rent | ₱8,000.00 | ₱8,000.00 | Fixed |
| 1 | Utilities | ₱2,766.67 | ₱0.00 | Flexible; recurring-aware |
| 2 | Emergency Fund | ₱2,000.00 | ₱2,000.00 | Protected |
| 3 | Debt Payments | ₱5,500.00 | ₱4,500.00 | Protected |
| 4 | Savings | ₱2,500.00 | ₱1,500.00 | Protected |
| 5 | Entertainment | ₱1,000.00 | ₱0.00 | Flexible |
| 5 | Dining Out | ₱1,000.00 | ₱0.00 | Flexible |
| | **Total** | **₱28,766.67** | **₱16,000.00** | |

## 1B. Strict feasibility

Essentials full target: `₱6,000 + ₱8,000 + ₱2,766.67 = ₱16,766.67`. Other envelope minima: `₱2,000 + ₱4,500 + ₱1,500 = ₱8,000`. The combined **mandatory feasibility requirement** is **₱24,766.67 ≤ ₱40,000**, with no conflicting restrictions; the strict model is **FEASIBLE**. The remaining `₱15,233.33` after mandatory funding is **not yet surplus**, since some nonessential targets remain.

## 1C. Hierarchical LP

The solver minimizes `D_1` through `D_5` sequentially. The budget covers all targets, so `D_1*=D_2*=D_3*=D_4*=D_5*=0`. Baseline-stage allocations equal the target column, totaling **₱28,766.67**. No proportional *underfunding* tie-break is needed because all targets are met.

## 1D. Surplus allocation

`S = ₱40,000 − ₱28,766.67 = ₱11,233.33`. Eligible baselines: Food ₱6,000; Utilities ₱2,766.67; Emergency Fund ₱2,000; Debt Payments ₱5,500; Savings ₱2,500. Denominator: **₱18,766.67**. Rent is fixed; Entertainment and Dining Out are Other Categories.

For each eligible element, `s_i = ₱11,233.33 × B_i / ₱18,766.67`. Apply largest-remainder centavo reconciliation:

| Element | LP target allocation | Surplus | Final allocation | Target shortfall |
|---|---:|---:|---:|---:|
| Food | ₱6,000.00 | ₱3,591.47 | ₱9,591.47 | ₱0.00 |
| Rent | ₱8,000.00 | ₱0.00 | ₱8,000.00 | ₱0.00 |
| Utilities | ₱2,766.67 | ₱1,656.07 | ₱4,422.74 | ₱0.00 |
| Emergency Fund | ₱2,000.00 | ₱1,197.16 | ₱3,197.16 | ₱0.00 |
| Debt Payments | ₱5,500.00 | ₱3,292.18 | ₱8,792.18 | ₱0.00 |
| Savings | ₱2,500.00 | ₱1,496.45 | ₱3,996.45 | ₱0.00 |
| Entertainment | ₱1,000.00 | ₱0.00 | ₱1,000.00 | ₱0.00 |
| Dining Out | ₱1,000.00 | ₱0.00 | ₱1,000.00 | ₱0.00 |
| **Total** | **₱28,766.67** | **₱11,233.33** | **₱40,000.00** | **₱0.00** |

**Output:** `FEASIBLE`; all minima and baselines funded; surplus ₱11,233.33 allocated; reserve **₱0.00**. The user reviews the proposal before activation.

---

# Sample 2 — Shortfalls; insufficient spendable money

## 2A. Inputs

Use **exactly the same baseline dataset and restrictions as Sample 1**, including Utilities ₱2,766.67, but change only spendable money to **`A = ₱23,000.00`**. No user-defined maxima.

Full Essentials plus other envelope minima require **₱24,766.67**, exceeding available money by **₱1,766.67**. Therefore the **strict ODIN model is INFEASIBLE** even though all fixed/protected minima alone total only ₱16,000.

## 2B. Separate relaxed LP and priority funding

For this illustrative partial recommendation, preserve the jointly affordable fixed/protected minimums first: Rent ₱8,000; Emergency Fund ₱2,000; Debt Payments ₱4,500; Savings ₱1,500. These sum to **₱16,000**, leaving **₱7,000** for flexible Essentials. The full flexible Essentials targets are Food ₱6,000 and Utilities ₱2,766.67, totaling **₱8,766.67**. Since neither has a positive minimum in this example, use one common ratio:

\[
\alpha=\frac{7,000}{8,766.67}\approx0.79847878,\quad
x_{Food}=6,000\alpha\approx ₱4,790.87,\quad
x_{Utilities}=2,766.67\alpha\approx ₱2,209.13.
\]

This is the **partial-allocation** solve, not a strict feasible solution. All available money is consumed by mandatory minima and partially funded Essentials; there is nothing left to fund the optional portions of Debt/Savings or Other Categories.

## 2C. Result

| Element | Target | Partial allocation | Target shortfall | Mandatory requirement met? |
|---|---:|---:|---:|---|
| Food | ₱6,000.00 | ₱4,790.87 | ₱1,209.13 | Essential baseline **not met** |
| Rent | ₱8,000.00 | ₱8,000.00 | ₱0.00 | Yes; fixed |
| Utilities | ₱2,766.67 | ₱2,209.13 | ₱557.54 | Essential baseline **not met** |
| Emergency Fund | ₱2,000.00 | ₱2,000.00 | ₱0.00 | Yes; minimum met |
| Debt Payments | ₱5,500.00 | ₱4,500.00 | ₱1,000.00 | Yes; ₱4,500 minimum met |
| Savings | ₱2,500.00 | ₱1,500.00 | ₱1,000.00 | Yes; ₱1,500 minimum met |
| Entertainment | ₱1,000.00 | ₱0.00 | ₱1,000.00 | No mandatory minimum |
| Dining Out | ₱1,000.00 | ₱0.00 | ₱1,000.00 | No mandatory minimum |
| **Total** | **₱28,766.67** | **₱23,000.00** | **₱5,766.67** | |

Group shortfalls: Essentials **₱1,766.67**; Emergency Fund **₱0**; Debt Payments **₱1,000** (above-minimum target); Savings **₱1,000** (above-minimum target); Other Categories **₱2,000**. Total **₱5,766.67**.

**Output:** `INFEASIBLE — PARTIAL_RECOMMENDATION`; mandatory fixed/protected minima are satisfied, **but Essentials are below their required full baselines**. Surplus **₱0**, reserve **₱0**. Show the essential shortfall and other target gaps; allow user review/modification/acceptance without changing the `INFEASIBLE` classification. No payment is executed automatically.

---

# Sample 3 — No financial-envelope baselines; minimum dues available

## 3A. Inputs and missing-target handling

Keep the **same ordinary spending categories and recurring-aware Utilities calculation** as Samples 1–2. For this variant, the Emergency Fund, Debt Payments, and Savings modules supply **only current-cycle minimum dues** and **no independent baseline targets**. To illustrate the missing-target behavior with a small surplus, set **`A = ₱28,000.00`**. No user-defined maxima.

| Priority | Element | Evidenced baseline | Minimum due | Operational target `T_i` | Source/status |
|---:|---|---:|---:|---:|---|
| 1 | Food | ₱6,000.00 | ₱0.00 | ₱6,000.00 | Historical baseline |
| 1 | Rent | ₱8,000.00 | ₱8,000.00 | ₱8,000.00 | Fixed commitment |
| 1 | Utilities | ₱2,766.67 | ₱0.00 | ₱2,766.67 | Recurring-aware baseline |
| 2 | Emergency Fund | **Unknown** | ₱2,000.00 | ₱2,000.00 | `MINIMUM_ONLY` |
| 3 | Debt Payments | **Unknown** | ₱4,500.00 | ₱4,500.00 | `MINIMUM_ONLY` |
| 4 | Savings | **Unknown** | ₱1,500.00 | ₱1,500.00 | `MINIMUM_ONLY` |
| 5 | Entertainment | ₱1,000.00 | ₱0.00 | ₱1,000.00 | Historical baseline |
| 5 | Dining Out | ₱1,000.00 | ₱0.00 | ₱1,000.00 | Historical baseline |
| | **Total** | **Not fully known** | **₱16,000.00** | **₱26,766.67** | Operational target total, **not** a fully evidenced baseline total |

**Do not claim the unknown Emergency/Debt/Savings baselines are ₱2,000/₱4,500/₱1,500.** Those are only known current-cycle minimums, used as operational targets so the solver can make a defensible allocation without inventing additional needs.

## 3B. Strict feasibility and LP

Full Essentials = **₱16,766.67**. Add the known envelope minimums `₱2,000 + ₱4,500 + ₱1,500 = ₱8,000`: mandatory funding **₱24,766.67 ≤ ₱28,000**. The strict model is **FEASIBLE against all known requirements**. All operational targets can also be funded: `ΣT_i = ₱26,766.67`; sequential group target shortfalls are all **₱0**. This means **no shortfall against known targets**, not that unknown preferred financial-envelope baselines have been assessed.

## 3C. Surplus with missing envelope baselines

`S = ₱28,000 − ₱26,766.67 = ₱1,233.33`. Under the explicit missing-target rule (§2.2), the three `MINIMUM_ONLY` envelopes **do not participate** in proportional surplus, because they have no evidenced baseline weight. Rent is fixed; Other Categories are excluded. Thus the eligible set contains only Food (`₱6,000`) and Utilities (`₱2,766.67`), denominator **₱8,766.67**.

\[
s_{Food}=1,233.33\frac{6,000}{8,766.67}\approx ₱844.07,\qquad
s_{Utilities}=1,233.33\frac{2,766.67}{8,766.67}\approx ₱389.26.
\]

## 3D. Final result

| Element | Operational target | Surplus | Final allocation | Known-target shortfall |
|---|---:|---:|---:|---:|
| Food | ₱6,000.00 | ₱844.07 | ₱6,844.07 | ₱0.00 |
| Rent | ₱8,000.00 | ₱0.00 | ₱8,000.00 | ₱0.00 |
| Utilities | ₱2,766.67 | ₱389.26 | ₱3,155.93 | ₱0.00 |
| Emergency Fund (`MINIMUM_ONLY`) | ₱2,000.00 | ₱0.00 | ₱2,000.00 | ₱0.00 against minimum |
| Debt Payments (`MINIMUM_ONLY`) | ₱4,500.00 | ₱0.00 | ₱4,500.00 | ₱0.00 against minimum |
| Savings (`MINIMUM_ONLY`) | ₱1,500.00 | ₱0.00 | ₱1,500.00 | ₱0.00 against minimum |
| Entertainment | ₱1,000.00 | ₱0.00 | ₱1,000.00 | ₱0.00 |
| Dining Out | ₱1,000.00 | ₱0.00 | ₱1,000.00 | ₱0.00 |
| **Total** | **₱26,766.67** | **₱1,233.33** | **₱28,000.00** | **₱0.00 against known targets** |

**Output:** `FEASIBLE` **with `BASELINES_INCOMPLETE` flag**; all known minimum dues and Essentials are satisfied, and all operational targets are funded. The three financial envelopes' preferred baselines are **unknown**, so ODIN must not claim that their broader savings/debt goals have been fully funded. Reserve **₱0**. The UI should explicitly say: “Emergency Fund, Debt Payments, and Savings were funded to their current minimum requirements; no additional targets were available.” The user may edit the proposed allocations before approval.

---

## 6. Final output contract and checks

Return: budgeting period, validated spendable amount, each element's `baseline_available`, `target_source`, baseline or `null`, current-cycle minimum, operational target, baseline-stage allocation, surplus, final allocation, mandatory shortfall, known-target shortfall, group priority, fixed/protected status, feasibility status, optional `BASELINES_INCOMPLETE` / `BASELINE_UNAFFORDABLE` flags, Unallocated Reserve, and deterministic explanation/reason codes. Never label a minimum-only target as a historical or module-evidenced baseline.

**Automated checks:** (1) every final allocation is nonnegative; (2) `Σfinal + reserve = spendable` to the centavo; (3) fixed items remain exact; (4) in a `FEASIBLE` result all known mandatory minima and full Essentials are satisfied; (5) baseline LP allocations never exceed their operational targets; (6) surplus occurs only after all known operational targets are funded; (7) Other Categories and fixed items receive no surplus; (8) missing baselines are not silently fabricated; (9) infeasible partial recommendations retain `INFEASIBLE`; (10) explanations reproduce authoritative computed amounts and status.

**Evaluation:** Test strict-feasibility classification, constraint satisfaction (separately for strict and relaxed results), funding-shortfall accuracy, proportional within-group funding, proportional surplus/centavo conservation, budget utilization, and explanation consistency. A user study would be required before claiming improved real-world financial outcomes. The exact hierarchy, missing-target surplus policy, and acceptance workflow are **ODIN design decisions**, not outcomes established by the illustrative arithmetic.
