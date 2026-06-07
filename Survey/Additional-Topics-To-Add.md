## Additional Points To Consider in Preliminary Survey

These are the **open points** that cannot be answered by literature alone; they require input from target users (Filipino working young adults, aged 20–40, Metro Manila).

### Topic 1: Device Models for Testing
**Spec reference:** Article I, Section 1, NOTE  
**Question to include in survey:**  
> *What smartphone model are you currently using as your primary device?*  
> (Open text, but may also provide a list of common models: Samsung A series, Samsung S series, Xiaomi Redmi, Oppo A series, Realme, iPhone, etc.)

**Why needed:** To select at least one low‑end and one mid‑range device for system evaluation.

---

### Topic 2: Paluwagan (Informal Rotating Savings)
**Spec reference:** Article XV, Section 1.J (global comment #11)  
**Question to include in survey:**  
> *Do you currently participate in any "paluwagan" (group savings where members contribute regularly and take turns receiving the pot)?*  
> - Yes, I participate regularly  
> - Yes, occasionally  
> - No, but I know how it works  
> - No, and I’m not interested  

**Follow‑up (if Yes):**  
> *How would you prefer a finance app to handle your paluwagan contributions and payouts?*  
> - Track it completely separately from my budget (so receiving the pot does not affect my spending/savings reports)  
> - Treat contributions as expenses and the payout as a transfer (but I understand this may distort my reports)  
> - I don’t want the app to track paluwagan at all – I will track it manually outside  

**Why needed:** To decide whether to add a minimal dedicated module or explicitly exclude paluwagan as a limitation.

---

### Topic 3: Custom Category Mapping to Broad Groups (Essentials / Obligatory / Discretionary / Financial Allocation)
**Spec reference:** Article IV, Section 2, NOTE (and Section 3)  
**Question to include in survey (choose one format):**  

*Option A (rank‑order):*  
> *Listed below are expense types that may not fit clearly into standard categories. Please assign each to one of four groups:*  
> - **Essentials** (necessary for survival: food, health, basic utilities)  
> - **Obligatory** (contractual or unavoidable: rent, debt minimum payments, insurance)  
> - **Discretionary** (optional: entertainment, dining out, hobbies)  
> - **Financial Allocation** (savings, investments, extra debt payment)  

> Examples to show:  
> - Mobile data plan for work  
> - Haircut at a budget salon  
> - Online streaming subscription (Netflix, Spotify)  
> - Lalamove/Grab delivery fee for food  
> - Remittance to parents in province  

*Option B (agreement scale):*  
> *For each expense, please indicate whether you personally consider it "Essential" (cannot skip), "Obligatory" (contractually required), "Discretionary" (can reduce or skip), or "Financial Allocation" (saving/investing).*  
> (Same examples)

**Why needed:** To validate or adjust the default mapping used by the budget recommendation LP.

---

### Topic 4: UI Language Preference (English vs Taglish / Tagalog)
**Spec reference:** Article VI, Section 3, NOTE (budget strategy names)  
**Question to include in survey:**  
> *Which naming style do you prefer for budget strategy templates?*  
> - Full English (e.g., "Savings First", "Zero‑Based", "Fifty‑Thirty‑Twenty")  
> - Taglish / Tagalog (e.g., "Savings Muna", "Bawat Piso", "Limampu‑Tatlumpu‑Dalawampu")  
> - Mixed (English names but with Tagalog explanations)  

**Why needed:** To decide on localization for better user understanding and trust.

---

### Topic 5: Surplus Handling Preferences (What to do with unspent budget money)
**Spec reference:** Article VI, Section 5 (Rollover / Save / Reset)  
**Question to include in survey:**  
> *At the end of a budget period (e.g., end of month), if you have leftover money that was allocated but not spent, what would you prefer to happen by default?*  
> - **Rollover** – Add the leftover to next month’s budget (so you can spend more next month)  
> - **Save it** – Automatically move the leftover to your savings goal  
> - **Reset** – Return the leftover to your available cash, and start next month’s budget from zero  
> - I want to choose each time (no default)  

**Why needed:** To validate the spec’s proposed defaults (Rollover for stable profiles, Save for variable profiles) or adjust them.

---

### Topic 6: Sensitivity to Anomaly Alerts (Alert Fatigue)
**Spec reference:** Article VIII, Section 6, NOTE (and global comment on fatigue)  
**Question to include in survey:**  
> *If the app alerts you about an unusual transaction (e.g., a much larger than normal grocery expense), how many such alerts per week would you find acceptable before it becomes annoying?*  
> - 0–1 per week  
> - 2–3 per week  
> - 4–5 per week  
> - More than 5 per week  
> - I don’t want any anomaly alerts at all  

**Follow‑up (if alerts are acceptable):**  
> *Would you want to adjust the sensitivity (e.g., “Low / Medium / High”) yourself?*  
> - Yes, I want control  
> - No, let the app decide automatically  

**Why needed:** To decide whether to expose sensitivity adjustment and to calibrate the default alert cooldown/threshold.

---

### Topic 7: Whitelist Behavior (Expected Large Transactions)
**Spec reference:** Article VIII, Section 4  
**Question to include in survey:**  
> *If you make a large purchase that is unusual for you but expected (e.g., buying a laptop, paying tuition), what would you prefer the app to do after you mark it as “expected”?*  
> - Suppress future alerts from the same merchant for any amount  
> - Suppress alerts only for the same merchant AND similar amount (±25%)  
> - Do not suppress automatically – ask me again next time  

**Why needed:** To define the default whitelist behavior (spec currently says ±25% tolerance).

---

### Topic 8: Definition of “Working Young Adult” – Inactivity Limit
**Spec reference:** Global comment #10 (not explicitly in spec but raised by Claude)  
**Question to include in survey:**  
> *If you do not record any income for several months (e.g., between freelance projects, sabbatical, or job hunting), should the app still consider you an active user?*  
> - Yes, keep my data as is – I may still have expenses  
> - No, after ___ days of no income, treat me as inactive (archive my profile)  
> - I don’t know  

**Why needed:** To add a minimum income frequency rule (e.g., at least one income transaction every 90 days to remain in the target population).

---
