## Technical Advisor (Sir Mansueto)

> For advice about the system.

1. We plan to set the following system modules as the primary modules:
    A. Financial behavioral profile classification module
        - Is this name okay? It's properly descriptive but may be too long.
        - This module implements a classification algorithm, as requested by Panel Member Ma'am Plan, hence why it's designated as a primary module.
            - Top candidate for the algorithm is Decision Tree.
                - Validity of this candidate depends `Ma'am Cervantes`'s verdict on if thresholds can be defined, and if it is to be defined by the researchers based on sources.
    B. Spending forecasting module
        - Before this is proposed, confirm with Dr. Go first whether `spending` is an appropriate term that encompasses all outflows, including savings, funds, and investments.
        - This module implements LSTM as the forecast algorithm.
    C. Budget recommendation module
        - This module implements a rule-based algorithm.
    D. Anomalous spending detection module
        - `Anomaly detection` was changed to `anomalous spending detection` for clarification.
        - This module implements Isolation Forest as the anomaly detection algorithm.
2. Regarding the aforementioned plan:
    - Is it okay to proceed with these model/algorithm preconceptions right now? For example, if the researchers can do research now to define by themselves the thresholds for profile classification.
        - If so, should we update Chapter I to mention the four new models/algorithms?

## Course Advisor (Ma'am Cervantes)

> For advice about the research.

1. Is it correct that during our experimental phase in the thesis, we will be able to answer a portion of SO1 (Examine and understand Filipino behavioral profiles) via experimentation, i.e., using RRL and survey results to define the thresholds (CV, pay period) for profile classification?
2. Can we give viewer-level access to our thesis documents to our Subject Matter Expert?

## Subject Matter Expert (Dr. Go)

> For advice about the business logic.

1. How can we exactly determine the thresholds of the two financial behavioral profile classifications?
    - How can we determine someone is Stable or Variable? 
        - What is the variance range?
        - What is the income horizon length?
    - How can we determine someone is Flexible or Obligated?
        - What are the dimensions?
2. Is it correct that one of the goals of the system is to balance cash inflow and outflow?
3. Is there an official or proper term for inflows and outflows in personal finance? E.g., income and expenditure?
4. Do savings, funds, and investments fall under cash inflow, outflow, or a separate distinction?
    - Important for naming the forecasting module (is it expense forecasting, expenditure forecasting, spending forecasting, or some other?).