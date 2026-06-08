# AI Wealth Navigator: An Integrated Platform for Smart Budgeting, Financial Learning, and Personalized Policy Guidance

## Metadata

```yaml
---
paper_id: "5e6f7a8b-9c0d-4e1f-9a2b-3c4d5e6f7a8b"
designation: international
title: "AI Wealth Navigator: An Integrated Platform for Smart Budgeting, Financial Learning, and Personalized Policy Guidance"
authors: "Yadav, A.; Prakash, R. S.; Iqubal, S. M.; Gebremicahea, M. G."
year: 2025
venue: "SSRN"
odin_topics: ["A.2", "C.1", "C.2", "G.1", "H.1", "J.1"]
shorthand_tags: ["/pfms-budget-rec", "/budget-rec-algorithms", "/western-cat-limitations", "/cat-approaches", "/security-standards", "/eval-pfms-applied"]
member_checklist:
  - name: "Gabion, Stefanie S."
    status: "[ ]"
  - name: "Guevarra, Joaquin Luis T."
    status: "[X]"
  - name: "San Jose, Alexa Joanne Paula G."
    status: "[ ]"
  - name: "Togle, Charles Nathaniel B."
    status: "[ ]"
---
```

## TL;DR

An integrated AI platform combining smart budgeting, adaptive financial learning, and policy recommendation achieved 94% receipt scan accuracy and user ratings above 4.6/5 across 50 users.

## Problem and Motivation

Existing personal finance apps treat budgeting, financial education, and policy navigation as separate silos, forcing users to juggle multiple tools. This fragmentation reduces financial literacy and prevents users from maximizing government benefits and savings. No prior system unified all three domains with AI-driven personalization in a single platform.

## Approach

- Frontend: Next.js with Tailwind CSS for responsive dashboards, spending visualizations, and dark/light mode.
- Backend: Supabase (database) + Prisma (ORM) + Inngest (automated tasks like budget resets and learning updates).
- AI insights: Gemini LLM generates tailored savings advice, investment plans, and budgeting tips based on spending patterns and goals.
- Policy engine: Hybrid data APIs + Gemini recommend government schemes, tax breaks, and subsidies using user location, income, and demographic profile.
- Receipt scanner: OCR powered by AI (not Gemini alone) converts paper and digital receipts into structured logs; reported 94% accuracy.
- Security: Arcjet provides rate limiting, threat prevention, and end-to-end encryption.
- Evaluation: 50-user survey measured personalization, relevance, and empathy; plus simulated security tests.

## Findings

1. Receipt scanner achieved **94% accuracy** on both physical and digital receipts (GPay, paper bills), drastically reducing manual entry errors.
2. User ratings: budgeting insights 4.8/5, policy recommendations 4.7/5, learning roadmap 4.6/5 — all above 4.6.
3. Over 70% of users discovered previously unknown government programs tailored to their profiles.

- Arcjet blocked all simulated security threats; Inngest handled automated tasks without performance degradation.
- Users valued the elimination of multiple apps and the cultural relevance of actionable suggestions.

## Key Figures and Tables

- Figure 1.1: System layered architecture → three core modules (budgeting, learning, policy) on a common AI+web stack.
- Figure 1.2: Architecture diagram → frontend, backend, AI layer, and security components interact via APIs.
- Figure 1.4: Dashboard → real‑time spending analytics and budget tracking in one view.
- Figure 1.5: Transaction page with scanner → OCR receipt upload plus manual entry option.
- Figure 1.6: Learning modules → adaptive roadmap with gamified progress tracking.

## Key Equations

None.

## Definitions

| Term / Acronym | Plain-English Definition |
| -------------- | ------------------------ |
| Gemini LLM | Google's large language model powering personalized financial advice. |
| OCR | Optical Character Recognition — scans text from receipts. |
| Supabase | Open-source Firebase alternative; handles database and authentication. |
| Prisma | Database toolkit that maps code to SQL queries. |
| Inngest | Background job queue for scheduled tasks (e.g., monthly budget reset). |
| Arcjet | API security layer with rate limiting and threat detection. |
| Next.js | React framework for server‑rendered web apps. |
| Policy recommendation engine | Suggests government schemes and subsidies based on user profile. |
| Adaptive financial learning roadmap | A learning path that changes difficulty and content based on user's knowledge level. |

## Critical Citations

- [Patel et al., 2023] — Established that AI can deliver personalized financial literacy paths, grounding the learning module.
- [Kumar et al., 2023] — Demonstrated dynamic budgeting with real‑time data, directly informing the budget tracker design.
- [Lee et al., 2023] — Showed AI can recommend social benefits using user financial profiles, justifying the policy engine.

## Relevance to Odin

**Topics:**

A.2 — Existing Personal Finance and Budget Management Systems

C.1 — Budgeting Strategies and Budget Recommendation

C.2 — Budget Recommendation Algorithm

G.1 — Expense Categorization in Filipino Personal Finance Contexts

H.1 — Data Privacy, Security, and User Trust in Personal Finance Systems

J.1 — System Evaluation

**Contribution to Odin:**

This paper directly supports Odin’s expense categorization module by demonstrating that AI‑powered OCR receipt scanning achieves 94% accuracy, justifying a move away from purely manual entry. The budgeting module’s use of LLMs to generate personalized savings alerts and spending insights provides a benchmark for Odin’s budget recommendation algorithm, even though Odin does not use LLMs. The human evaluation with 50 users offers a low‑cost, feasible evaluation template for Odin’s ISO 25010 and SUS testing, particularly the use of 5‑point ratings for perceived relevance and empathy.

**Directly justifies:**

- “OCR‑based receipt scanning achieved 94% accuracy on both digital and physical receipts, reducing manual categorization errors and user entry friction.”
- “Personalized budgeting insights powered by an LLM received a 4.8/5 user rating, indicating that AI‑driven, context‑aware advice improves perceived financial control.”
- “A policy recommendation engine that matches user profiles (income, location, demographics) to government schemes uncovered previously unknown benefits for over 70% of users, demonstrating the value of profile‑driven suggestions.”
- “A 50‑user survey using simple Likert scales (1–5) can effectively measure platform relevance and empathy, offering a lightweight evaluation method for early‑stage personal finance systems.”

**Limits of relevance:**

- The study was conducted in India and Ethiopia, not the Philippines; cultural spending norms and government scheme structures differ.
- Odin relies on manual transaction input, while this paper emphasizes automated receipt scanning — the accuracy claim may not transfer to a fully manual workflow.
- Evaluation used only 50 users and asked about empathy and relevance, not ISO 25010 or SUS; direct comparability to Odin’s evaluation framework is limited.
- The platform uses Gemini LLM, a large model with infrastructure demands (API cost, latency) that Odin’s mobile‑first, offline‑capable design may not support.

## Limitations

- Small sample size (50 users) limits statistical power and generalizability. [unacknowledged]
- No long‑term retention data; the evaluation measured only immediate user ratings. [unacknowledged]
- Paper acknowledges sporadic OCR errors and reliance on full user profiles for policy matching.
- No baseline comparison against non‑AI or single‑module apps; the reported benefits are absolute, not relative. [unacknowledged]
- Performance metrics (response time 2‑3 seconds, token efficiency) are reported without standard deviations or statistical tests.

## Remember This

- 🔑 **94% receipt scan accuracy** — OCR reduces manual entry, a key input for expense categorization.
- 📌 User ratings 4.6‑4.8/5 — high perceived value across budgeting, learning, and policy modules.
- 💡 Policy engine found unknown schemes for 70% — profile‑driven suggestions drive user discovery.
- ⚠️ Only 50 users, no SUS/ISO — evaluation is lightweight and not directly comparable to Odin’s required framework.
