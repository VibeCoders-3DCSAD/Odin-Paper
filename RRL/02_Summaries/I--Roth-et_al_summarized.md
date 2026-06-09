```yaml
paper_id: 10.1080/17489725.2023.2251423
designation: international
title: Making maps & visualizations for mobile devices: A research agenda for mobile-first and responsive cartographic design
authors: Roth, R. E.; Çöltekin, A.; Delazari, L.; Denney, B.; Mendonça, A.; Ricker, B. A.; Shen, J.; Stachoň, Z.; Wu, M.
year: 2024
venue: Journal of Location Based Services
odin_topics:
  - 9.A
  - 9.B
shorthand_tags:
  - /mobile-first-design
  - /responsive-design
  - /ux-design
  - /cartographic-design
tldr: A research agenda for mobile-first and responsive cartographic design presents 20 challenges across scale, projections, symbolization, toponymy, and user interaction to adapt cartographic canon for mobile devices.
problem_and_motivation: Most maps are viewed on mobile devices, yet cartographic design principles were established for print maps and rarely consider mobile constraints. Mobile devices impose small screens, limited bandwidth, battery life, and touch interaction, but also enable new possibilities like location-based services and egocentric views. A comprehensive reevaluation of the cartographic design space is needed to support mobile-first and responsive maps.
approach:
  - Conducted a two-day workshop with 70 scholars from nine countries to identify research challenges.
  - Reviewed existing literature on mobile cartography constraints, enablements, and consequences.
  - Organized challenges into five design dimensions: scale/generalization, projections, symbolization/visual hierarchy, toponymy/typography, and user interaction.
  - Proposed 20 specific research questions and potential avenues for future empirical research.
findings:
  - Mobile generalization should consider speed or cost rather than scale alone.
  - Egocentric oblique projections require renewed research on pitch, bearing, and depth cues.
  - Energy-aware color schemes can reduce carbon footprint but conventional schemes fail under dimming.
  - Gaze-contingent displays offer potential for adaptive labeling on mobile devices.
  - Emerging mobile platforms like wearables and AR/VR introduce new design constraints and enablements.
key_figures_tables:
  - Table 1: 20 research challenges for mobile-first and responsive cartographic design → Organized by five dimensions.
  - Figure 1: Partial design space with five dimensions and mobile constraints/enablements → Framework for research agenda.
  - Figure 2: Illustration of mobile-first responsive design using SDG map → Shows application of recommendations.
key_equations:
  - equation: None.
    explanation: ""
definitions:
  - term: Mobile-first design
    definition: Design philosophy optimized for the most constrained mobile user experience first.
  - term: Responsive design
    definition: Dynamic adaptation of content and styling from mobile to non-mobile contexts.
  - term: Egocentrism
    definition: Map view centered on user's location with forward-up orientation.
  - term: Focus+context visualization
    definition: Techniques providing simultaneous overview and local detail on small screens.
  - term: Energy-aware design
    definition: Balancing user experience with energy consumption to reduce carbon footprint.
  - term: Glanceable visualization
    definition: Visualization understood within 500ms to 5 seconds for peripheral attention.
critical_citations:
  - "[Meng, 2005] — Established egocentric design for map-based mobile services."
  - "[Bertin, 1967/1983] — Semiology of graphics and visual variables foundation."
  - "[Imhof, 1975] — Canonical labeling guidelines needing mobile update."
relevance:
  topics:
    - code: 9.A
      name: Mobile-First Design Principles and Rationale
      justification: Defines mobile-first design and provides research agenda for adapting cartographic design to mobile constraints.
    - code: 9.B
      name: Mobile UX Design for Personal Finance
      justification: Discusses touch interaction, energy-aware design, and glanceable visualizations applicable to PFMS mobile UX.
  contribution: This paper provides a comprehensive research agenda for mobile-first cartographic design that directly informs Odin's mobile interface design. It identifies specific challenges in scale adaptation, symbolization, and user interaction that Odin can address to improve usability on small screens. The focus on energy-aware color schemes and glanceable visualizations supports Odin's need for battery-efficient and quick-access financial data displays. The discussion of inclusive design and cross-cultural iconography guides Odin's design for Filipino young professionals.
  directly_justifies:
    - Mobile maps should use speed-dependent generalization rather than scale-dependent.
    - Energy-aware color schemes require redesign for OLED screens and dimming modes.
    - Gaze-contingent labeling can reduce visual clutter on small displays.
    - Bottom navigation and pull-up menus improve thumb-based interaction on mobile.
  limits:
    - Most recommendations are conceptual and lack empirical testing in financial contexts.
    - Focuses on cartographic maps, not specifically personal finance data visualizations.
  mapping_rationale: This paper primarily addresses mobile-first and responsive design principles (domains 9.A and 9.B). It provides a research agenda for adapting cartographic design to mobile constraints such as small screens, touch interaction, and variable connectivity. While it touches on data privacy and user trust (10.A, 10.B) regarding location services, these are not central. No direct relevance to expense categorization, spending forecasting, or behavioral profiling. The paper was selected for Odin because its UX design insights directly inform the mobile interface of a PFMS.
limitations:
  - The research agenda is conceptual and lacks empirical validation of specific design recommendations.
  - Focuses on cartographic maps rather than financial data visualizations common in PFMS. [unacknowledged]
  - Does not consider low-end mobile devices prevalent in developing economies. [unacknowledged]
remember_this:
  - Annual global energy for Google Maps is 820.9 million kWh.
  - Mobile-first design prioritizes most constrained user experience first.
  - Generalization should depend on travel speed not just scale.
  - Gaze-contingent displays can reduce map clutter.
  - Energy-aware color schemes save battery and carbon.
```