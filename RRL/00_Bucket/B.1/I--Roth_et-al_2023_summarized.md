---
name: paper-summary
paper_id: "10.1080/17489725.2023.2251423"
source_document: "I--Roth_et-al_2023.md"
designation: international
title: "Making maps & visualizations for mobile devices: A research agenda for mobile-first and responsive cartographic design"
authors: "Roth, R. E.; Cöltekin, A.; Delazari, L.; Denney, B.; Mendonça, A.; Ricker, B. A.; Shen, J.; Stachoň, Z.; Wu, M."
year: 2024
venue: "Journal of Location Based Services"
odin_topics: ["B.1"]
shorthand_tags: ["/mobile-first-def", "/mobile-dominance", "/mobile-constraints", "/mobile-ux-entry"]
summary_date: 2026-05-08
version: "1.0"
member_checklist:
  - name: "Gabion, Stefanie S."
    status: "[ ]"
  - name: "Guevarra, Joaquin Luis T."
    status: "[ ]"
  - name: "San Jose, Alexa Joanne Paula G."
    status: "[ ]"
  - name: "Togle, Charles Nathaniel B."
    status: "[ ]"
---

# Making maps & visualizations for mobile devices: A research agenda for mobile-first and responsive cartographic design

## TL;DR
Mobile-first design prioritizes constrained devices first, then adapts to non-mobile, requiring fundamental rethinking of cartography’s scale, projections, symbols, labels, and interaction rules.

## Problem and Motivation
Most cartographic design rules were built for printed maps, not small, touch-based mobile screens with limited battery and bandwidth. Mobile-first design — optimizing for the most constrained user experience first — remains understudied in mapping. The paper asks: how must cartographic design adapt when mobile is the primary platform?

## Approach
- Defines a five‑dimension design space: scale/generalization, projections, symbolization/visual hierarchy, toponymy/typography, and user interaction.
- Reviews constraints (small screen, variable lighting, battery, data costs) and enablements (touch, GPS, sensors, multimodal output).
- Derives 20 research challenges from a 70‑scholar, 9‑country 2019 ICA workshop.
- Proposes empirical experiments and design case studies as validation methods.

## Findings
1. Mobile generalization should be **speed‑ or cost‑dependent**, not scale‑dependent — travel mode (walking vs. driving) changes feature salience.
2. Oblique, egocentric projections improve place attachment but risk reducing configural spatial knowledge.
3. **89%** of sampled mobile maps are legendless, shifting toward glanceable “maps to see” over “maps to read.”
4. Dark imagery basemaps use less energy but only appear in **25%** of sampled apps, despite most (91%) offering a light basemap.
5. Energy‑aware color schemes can reduce carbon footprint — Google Maps’ annual display energy equals the electricity use of ~255,000 people.

## Key Figures and Tables
- Figure 1: Five dimensions of mobile map design space → organizes all 20 research challenges.
- Figure 2: Mobile vs. non‑mobile map of UN mobile coverage → illustrates egocentric centering, bottom thumb menus, hidden legends.
- Figure 13: Frequency of mobile interaction operators → shows reproject (47%) and rotate (61%) more common on mobile than desktop.

## Key Equations
None. (Paper is a qualitative research agenda.)

## Definitions

| Term / Acronym | Plain-English Definition |
| -------------- | ------------------------ |
| Mobile-first design | Build for the smallest, weakest device first, then scale up. |
| Responsive design | Interface adapts content/layout to screen size and device capabilities. |
| LOD (Level of Detail) | How many and how complex features appear on the map. |
| Egocentrism | Map centered on user’s location, with “forward” as “up.” |
| Glanceable visualization | Understood in ≤500 ms without reading a legend. |
| Focus+context | Shows local detail and distant overview simultaneously (e.g., fisheye lens). |

## Critical Citations
- [Abraham, 2019] — Comprehensive survey of 36 mobile maps; provides many baseline statistics cited throughout.
- [Kraak et al., 2020] — UN sustainable development mapping framework; source for mobile‑responsive Figure 2.
- [Roth et al., 2018] — Global Madison case study; illustrates mobile‑first UX design in practice.

## Relevance to Odin

**Topics:**
B.1 — Mobile-First Design in Personal Finance Systems

**Contribution to Odin:**
This paper provides the foundational design philosophy and empirical justification for building Odin as a mobile‑first system. It establishes that mobile is now the dominant map viewing platform (more maps viewed on mobile than any other medium), and that mobile‑first is an inclusive design strategy — prioritizing the most constrained experience first benefits all users. The paper’s 20 research challenges directly inform Odin’s approach to mobile‑first interaction, energy‑aware color schemes, and glanceable visualizations for budget tracking.

**Directly justifies:**
- Odin’s mobile‑first design philosophy is a deliberate inclusive design strategy, not a afterthought.
- Small screen, touch‑based interaction, and variable lighting are the primary constraints Odin must solve.
- Legendless, glanceable visualizations are appropriate for mobile finance apps when designed as “maps to see.”
- Bottom‑mounted thumb‑based UI (bottom navigation, floating action buttons) improves efficiency on mobile devices.

**Limits of relevance:**
- Domain is cartography and geovisualization, not personal finance — design principles transfer, but transaction data differs from map data.
- Filipino cultural or behavioral context is not addressed.
- Focus is on mobile map UX, not algorithmic design (forecasting, anomaly detection, classification).

## Limitations
- Paper is a research agenda, not a controlled experiment — claims are proposals, not validated findings.
- Most mobile usage statistics come from a 2019 survey; device capabilities have improved since.
- “Denominator” for the 89% legendless figure is unclear across 36 sampled apps.
- No user‑in‑the‑loop testing of the proposed design strategies.

## Remember This
- 💡 **Mobile‑first means design for the smallest screen first** — not a port of desktop features to mobile.
- 🔑 **89% of mobile maps are legendless** — glanceable “maps to see” dominate over “maps to read.”
- 📌 **Speed matters more than scale** — generalization should depend on walking vs. driving, not zoom level.