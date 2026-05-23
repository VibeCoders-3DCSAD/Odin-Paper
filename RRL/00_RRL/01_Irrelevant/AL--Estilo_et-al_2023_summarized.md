# Destamp: A Mobile Application for Generating Budget-Based Itineraries to Enhance Travel Planning

## Metadata

```yaml
---
paper_id: "f47ac10b-58cc-4372-a567-0e02b2c3d479"
designation: local
title: "Destamp: A Mobile Application for Generating Budget-Based Itineraries to Enhance Travel Planning"
authors: "Estilo, C.; Jondanero, S.; Lajo, J."
year: 2023
venue: "Unknown"
odin_topics: []
shorthand_tags: []
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

A mobile app using genetic algorithms and content-based filtering generates budget-constrained travel itineraries for Iloilo City, with 84% of surveyed Filipinos prioritizing budget in travel planning.

## Problem and Motivation

Manual travel planning is time‑consuming (31% spend a day or more) and overwhelming due to fragmented online research. Budget management during trips remains challenging, with 76% of travelers saying staying within budget is very important. Existing travel guides and apps lack personalized, budget‑aware itinerary generation that optimizes routes and tracks spending.

## Approach

- Survey of 319 Filipinos aged 18–60 to identify planning pain points and budget priorities.
- Genetic algorithm (GA) with initialization, fitness scoring, selection, crossover, and mutation to optimize Points of Interest (POI) sequences under budget and time constraints.
- Content‑based filtering to rank POIs by similarity to user preferences (accommodation type, activities, cuisine, dining style).
- Dijkstra’s algorithm on a distance matrix for route optimization (fastest path by distance).
- Budget tracking using CRUD operations on Supabase backend; Mapbox for geocoding and matrix APIs.
- React Native frontend with Expo; tested with 10 travelers and 5 business operators.

## Findings

1. **100% of 10 test users agreed** the GA significantly improved travel recommendations (rejected null hypothesis).
2. **100% agreed** the content‑based recommender aligned itineraries with their interests.
3. Budget tracking was effective for **80% of users** (8/10) in allocating trip budgets.
4. Route optimization achieved significantly better routes for **60% of users** (6/10).
5. Survey (n=319): **84%** considered budget a significant factor in itinerary planning; 76% rated staying on budget as “very important”.

- 47% of respondents lacked knowledge to create their own itinerary; 54% relied on self‑research and booking.
- 68% research travel routes before departure; 80% struggle to find affordable attractions.

## Key Figures and Tables

- Figure 1.1: Genetic Algorithm flow diagram → initialization → fitness → selection → crossover → mutation.
- Figure 3.17: Importance of staying within budget → 76% say “very important”.
- Table 5.4: Traveler objective completion → GA 100%, recommender 100%, budget tracking 80%, route optimization 60%.
- Table 5.2: Traveler test participant demographics → ages 20–49, budgets from 1k–9k+ PHP.

## Key Equations

None.

## Definitions

| Term / Acronym | Plain-English Definition |
| -------------- | ------------------------ |
| GA | Genetic Algorithm — optimization method mimicking natural selection (survival of fittest). |
| POI | Point of Interest — a destination, attraction, restaurant, or accommodation. |
| Content‑based filtering | Recommends items similar to a user’s past preferences (e.g., same cuisine or activity type). |
| CRUD | Create, Read, Update, Delete — basic database operations. |
| SDLC | Software Development Life Cycle — structured process for building software. |

## Critical Citations

- [Yochum et al., 2021] — Defined Mandatory Tour problem and proposed GAM genetic algorithm for POI sequences with time/budget constraints.
- [Handayani, 2018] — Applied GA to travel itinerary with restaurant selection and time windows.
- [Ho & Amin, 2019] — Showed personalized itineraries increase user sense of ownership and app acceptance.
- [Sia et al., 2022] — Identified itinerary generators and real‑time personalization as major mobile travel app features.

## Relevance to Odin

**Topics:**

None — contextual only.

**Contribution to Odin:**

Although Destamp addresses travel planning rather than personal budget management, its methods offer transferable insights. The genetic algorithm’s success in optimizing allocations under hard budget constraints (100% user agreement) provides a precedent for using evolutionary algorithms in Odin’s budget recommendation module. The content‑based filtering approach demonstrates how user preference vectors can drive personalized suggestions, relevant to Odin’s expense categorization and profile classification. The survey data (84% of Filipinos consider budget significant) reinforces the user need for budget‑aware tools in the Philippine context, supporting Odin’s core value proposition.

**Directly justifies:**

- “Genetic algorithms can optimize activity sequences under budget and time constraints, achieving 100% user‑perceived improvement in recommendation quality (n=10).”
- “Content‑based filtering using user preference tags (accommodation type, cuisine, activities) successfully aligns generated plans with individual interests, with all test users confirming relevance.”
- “84% of Filipino survey respondents (n=319) rated budget as a significant factor in planning decisions, and 76% said staying within budget is ‘very important’.”
- “Dijkstra’s algorithm on a distance matrix produces the fastest route between POIs, used by 60% of test users who rated routes as significantly better than unoptimized sequences.”

**Limits of relevance:**

- Domain is travel itinerary planning, not recurring personal expense management (daily/monthly budgeting).
- Algorithm evaluation based on small sample (10 users) without statistical significance testing.
- Geographic scope limited to Iloilo City; findings may not generalize to other Philippine regions or daily spending contexts.
- No comparison against alternative optimization methods (e.g., integer programming, simulated annealing).

## Limitations

- Algorithm performance tested with only 10 users — insufficient for generalizable claims. [unacknowledged]
- Route optimization success rate of 60% indicates room for improvement; users requested real‑time routing and better map alignment.
- Budget tracking module tested for trip expenses only; no validation for ongoing budget adherence over time.
- App relies on internet connectivity and Google Maps data; offline functionality not supported.
- No formal usability evaluation using standardized instruments (e.g., SUS, ISO 25010).

## Remember This

- 🔑 **84% of Filipinos** prioritize budget in planning — survey evidence for Odin’s user need.
- 💡 GA and content‑based filtering both achieved **100% user agreement** — strong signals for personalized optimization.
- 📌 Route optimization lagged at **60%** — user‑requested real‑time routing highlights a feature gap.
- ⚠️ Small test sample (n=10) — findings are directional, not statistically robust.
