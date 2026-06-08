# Making maps & visualizations for mobile devices: A research agenda for mobile-first and responsive cartographic design

## Metadata

```yaml
---
paper_id: "10.1080/17489725.2023.2251423"
designation: international
title: "Making maps & visualizations for mobile devices: A research agenda for mobile-first and responsive cartographic design"
authors: "Roth, R. E.; Çöltekin, A.; Delazari, L.; Denney, B.; Mendonça, A.; Ricker, B. A.; Shen, J.; Stachoň, Z.; Wu, M."
year: 2024
venue: "Journal of Location Based Services"
odin_topics: ["B.1"]
shorthand_tags: ["/mobile-first-def", "/mobile-ux-entry"]
member_checklist:
  - name: "Gabion, Stefanie S."
    status: "[ ]"
  - name: "Guevarra, Joaquin Luis T."
    status: "[x]"
  - name: "San Jose, Alexa Joanne Paula G."
    status: "[ ]"
  - name: "Togle, Charles Nathaniel B."
    status: "[ ]"
---
```

## TL;DR

Mobile-first cartographic design requires rethinking scale, projections, symbols, labels, and interaction — this paper lists 20 research challenges to adapt cartography for small screens, touch, and mobile contexts.

## Problem and Motivation

Most cartographic design principles were established for printed maps or desktop screens, not for mobile devices. Mobile constraints (small screens, limited bandwidth, battery life, touch interaction) and enablements (physical mobility, location services) are poorly addressed by existing guidelines. A comprehensive research agenda is needed to adapt cartographic design for mobile-first and responsive use cases.

## Approach

- Synthesized literature on mobile cartography, UX design, and related fields.
- Identified five dimensions of cartographic design requiring mobile adaptation: scale & generalization, projections, symbolization & visual hierarchy, toponymy & typography, user interaction.
- Derived 20 research challenges from a two-day workshop with 70 scholars from nine countries at the 2019 International Cartography Conference.
- Organized challenges within a partial design space that maps mobile constraints, enablements, and consequences to each dimension.

## Findings

- Screen size and bandwidth constraints force mobile maps to use fewer features, larger default scales, and off-screen caching, but empirical results on optimal level of detail are mixed (some studies show an inverted U‑shape).
- Egocentric oblique projections improve landmark association but may impede configural knowledge; their efficacy depends on task and user context.
- Energy-aware color schemes can reduce carbon footprint and preserve battery life, but conventional color schemes fail under dimming modes.
- Imagery basemaps are underused (only 25% of sampled apps offer dark mode) despite advantages for energy saving and landmark matching.
- **91% of sampled mobile maps have no legend**, indicating a shift toward glanceable visualizations viewed in under 500 ms.
- Gesture-based interaction operators (pan, zoom, rotate, tilt) are now conventional, but hover affordances are absent on multi‑touch screens.

## Key Figures and Tables

- Figure 1: Partial design space for mobile maps → shows five dimensions and places mobile constraints, enablements, consequences qualitatively.
- Figure 2: Mobile‑first vs. non‑mobile SDG map comparison → illustrates generalized basemap, hidden legend, thumb‑based UI, and audio search.
- Table 2: Design guidelines for mobile‑first and responsive cartography → summarizes evolving recommendations from literature.
- Figure 8: Energy‑aware color schemes under dimming → conventional schemes fail at 60% dimming; optimized schemes maintain legibility.
- Figure 13: Frequency of mobile interaction operators → pan/zoom implemented in >80% of apps; reexpress/resymbolize in <3%.

## Key Equations

None.

## Definitions

| Term / Acronym | Plain-English Definition |
| -------------- | ------------------------ |
| LOD | Level of detail — number and complexity of features on a map. |
| AR | Augmented reality — overlaying digital information onto the real world. |
| MR | Mixed reality — spatially registered virtual objects that interact with real objects. |
| VR | Virtual reality — fully immersive digital environment replacing the real world. |
| UX | User experience — overall quality of a person’s interaction with a system. |
| UI | User interface — the visual and interactive elements through which a user controls a system. |
| POI | Point of interest — a specific location marked on a map (e.g., restaurant, ATM). |
| XR | Extended reality — umbrella term for VR, AR, and MR. |
| WIMP | Windows, icons, menus, pointer — classic desktop GUI paradigm. |

## Critical Citations

- [Bertin, 1967] — Foundational visual variable syntactics that underpin all cartographic symbolization.
- [MacEachren, 1995] — Extended Bertin’s work to interactive and dynamic maps.
- [Imhof, 1975] — Classic guidelines for label placement on maps, largely untested for mobile.
- [Roth, 2013a] — Empirically derived taxonomy of interaction operators for cartography.

## Relevance to Odin

**Topics:**

B.1 — Mobile-First Design in Personal Finance Systems

**Contribution to Odin:**

This paper directly informs the mobile-first design of Odin’s interface. Odin is a mobile-FIRST personal budget management app targeting Filipino young professionals, and its usability depends on adapting cartographic principles to small screens, touch interaction, and variable environmental conditions. The paper’s synthesis of constraints (e.g., small screen, limited bandwidth, battery life) and enablements (e.g., location services, multimodal input) provides a checklist for Odin’s UI/UX planning. Although the paper focuses on maps, its findings on glanceable visualizations, energy-aware color schemes, and thumb‑based interaction layout are directly transferable to Odin’s budget dashboards and spending charts.

**Directly justifies:**

- “Mobile-first design constrains visual complexity: 91% of mobile map apps omit legends, requiring symbols that are immediately interpretable without external reference.”
- “Thumb‑based UI widgets (bottom navigation tabs, floating action buttons, pull‑up menus) improve interaction efficiency on handheld devices compared to top‑ or left‑aligned desktop layouts.”
- “Imagery basemaps and dark mode color schemes reduce energy consumption and preserve battery life, but only 25% of mobile apps offer a dark basemap option.”
- “Gaze‑contingent displays and multimodal (voice, haptic) feedback can reduce visual attention demands when users are moving—relevant to Odin’s use while commuting.”

**Limits of relevance:**

- The paper addresses cartographic maps, not financial dashboards; direct transfer of symbolization guidelines requires validation for bar charts and spending categories.
- Most empirical findings come from navigation and wayfinding tasks, not financial management.
- Energy‑aware design assumes OLED screens; Odin’s target device mix may include IPS LCD screens with different power profiles.
- The research agenda is conceptual; specific design recommendations are not yet empirically validated for personal finance apps.

## Limitations

- The paper is a research agenda, not an empirical study; no quantitative performance metrics are provided for mobile‑first designs. [unacknowledged]
- Focuses on cartographic maps; applicability to abstract data visualizations (e.g., spending trends) is assumed but not tested.
- Does not address cultural or regional differences in mobile use patterns, limiting direct generalization to Filipino young professionals. [unacknowledged]
- The literature review and workshop participants are predominantly from Global North institutions; local Filipino mobile behaviors are absent.
- Energy‑aware color guidelines are evaluated only for static maps, not for interactive dashboards with real‑time updates.

## Remember This

- 🔑 Mobile‑first means designing for the most constrained device first — small screen, touch, variable bandwidth.
- 📌 91% of mobile maps lack legends — symbols must be glanceable in under 500 ms.
- 💡 Thumb‑based UI (bottom menus, FABs) outperforms top‑left layouts on handhelds.
- ⚠️ Only 25% of mobile apps offer dark mode — a missed opportunity for battery life and energy savings.
- ✅ Gaze‑contingent and voice interfaces can reduce split attention when users are moving.
