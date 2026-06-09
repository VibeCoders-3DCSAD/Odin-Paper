```yaml
paper_id: a3b7c9d1-4e5f-4a6b-8c7d-9e0f1a2b3c4d
designation: international
title: Optimizing Banking Application Interfaces: A User-Centric Perspective on Consent Management in Digital Banking Environments
authors: Pakarinen, O.
year: 2025
venue: Jyväskylä University of Applied Sciences
odin_topics:
  - 9.A
  - 9.B
  - 10.A
  - 10.B
shorthand_tags:
  - /mobile-design-principles
  - /mobile-ux
  - /data-privacy
  - /user-trust
tldr: A two-level consent management prototype with category-based overview and granular controls improved user understanding and confidence in digital banking interfaces.
problem_and_motivation: Existing consent screens in banking apps use lengthy legal text and complex layouts, causing users to skim and feel unsure about their decisions. There is a gap between regulatory compliance and usable consent interfaces that support informed choice. A user-centric design is needed to make consent transparent, accessible, and controllable.
approach:
  - Mixed-methods approach including an exploratory survey (n=6), two rounds of usability testing, and semi-structured interviews.
  - Prototype designed with two layers: category-based consent overview and detailed granular consent view with tooltips.
  - Full-stack implementation using MEAN stack (MongoDB, Express.js, Angular, Node.js) with auditable consent records.
  - Iterative improvements based on user feedback: shortened text, added icons, simplified labels, and adjusted tooltip placement.
  - Evaluation focused on task completion time, hesitation, error rate, and user confidence in consent decisions.
findings:
  - Lengthy, complex consent language impairs users’ understanding and leads to disengagement.
  - Concise, clear steps and explicit labels improve users’ perception of control and confidence when giving consent.
  - Category-based overview with visible consent state (green/yellow badges) helps users orient faster.
  - Tooltips with brief explanations reduce confusion about technical terms.
  - Participants preferred progressive disclosure over dense text blocks.
key_figures_tables:
  - Figure 6.1: Revolut privacy settings showing category-based controls → Categories improve scanability.
  - Figure 6.2: ING Spain consent page via Didomi CMP → Standardized consent reduces cognitive load.
  - Figure 6.3: Nordea open banking authorization flow → In-app authorization enhances control.
  - Figure A1.1: Category-based consent overview → High-level structure aids navigation.
  - Figure A2.1: Detailed consent settings within category → Granular toggles support informed choice.
key_equations:
  - equation: None.
    explanation: ""
definitions:
  - term: GDPR
    definition: General Data Protection Regulation, EU law on data protection and privacy.
  - term: CCPA
    definition: California Consumer Privacy Act, US state law for consumer data privacy.
  - term: Consent management
    definition: Process of obtaining, recording, and managing user permissions for data processing.
  - term: User-centered design
    definition: Design philosophy that prioritizes end-user needs and feedback throughout development.
critical_citations:
  - "[Nouwens et al., 2020] — Dark patterns after GDPR affect consent decisions."
  - "[EDPB, 2020] — Guidelines on consent under GDPR require clarity and accessibility."
  - "[Kyi et al., 2024] — Long consent text leads to confusion and disengagement."
relevance:
  topics:
    - code: 9.A
      name: Mobile-First Design Principles and Rationale
      justification: Paper designs and tests a consent interface specifically for mobile banking apps.
    - code: 9.B
      name: Mobile UX Design for Personal Finance
      justification: Usability testing and iterative improvements focus on touch-friendly navigation and clarity.
    - code: 10.A
      name: Data Privacy and Security in Personal Finance Systems
      justification: Core topic is consent management for personal financial data under GDPR/CCPA.
    - code: 10.B
      name: User Trust in Personal Finance Systems
      justification: Findings show transparent consent flows improve user confidence and perceived control.
  contribution: "This paper directly informs Odin's data privacy module by demonstrating a two-level consent interface that balances transparency and usability. It provides empirical evidence that category-based overviews with visible consent states reduce cognitive load and improve decision confidence. The usability testing methodology offers a template for evaluating consent flows in PFMS. The design recommendations (progressive disclosure, reversible consent, explicit labeling) can be integrated into Odin's mobile UX. Finally, the AI-supported summary concept suggests a path for enhancing user understanding without overwhelming detail."
  directly_justifies:
    - "Concise, clear steps and explicit labels improve users' perception of control when giving consent."
    - "Category-based consent overview with visible status badges helps users orient faster than dense text blocks."
    - "Reversible consent decisions and tooltips reduce hesitation and support informed choice."
    - "Long, complex consent language impairs understanding and leads to disengagement in banking apps."
  limits:
    - "Small sample size (survey n=6, usability tests small) limits generalizability."
    - "Controlled environment not a real banking system, prototype simplified."
    - "No longitudinal measurement of trust or retention effects."
  mapping_rationale: "The paper focuses exclusively on consent management in digital banking, addressing data privacy (10.A) and user trust (10.B) as core themes. The design and testing of a mobile consent interface directly map to mobile-first principles (9.A) and mobile UX (9.B). The paper does not address behavioral profiling, spending forecasting, budget recommendation, anomaly detection, expense categorization (beyond consent), savings/debt management, or retention mechanisms beyond trust. Borderline case: evaluation methodology (12.A) is present but not the primary contribution; thus excluded. No Filipino context, so topics 1.A-1.C, 2.A-2.C are irrelevant. Algorithm-specific claims absent, so no 5.C,6.B,7.C,8.B."
limitations:
  - "Limited user group and small sample size reduce generalizability of findings."
  - "Controlled environment testing, not integrated into a live banking system."
  - "Prototype simplified; real-world technical integration challenges not fully addressed."
  - "AI-supported summary feature was a design idea, not fully implemented or tested."
remember_this:
  - Two-level consent structure (category overview + granular view) reduces cognitive load.
  - Visible consent state badges improve user orientation and decision confidence.
  - Progressive disclosure and tooltips outperform dense legal text blocks.
  - Reversible consent choices support long-term trust and user control.
```