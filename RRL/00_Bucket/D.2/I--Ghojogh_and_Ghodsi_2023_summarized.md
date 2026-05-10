# Recurrent Neural Networks and Long Short-Term Memory Networks: Tutorial and Survey

## Metadata

```yaml
---
paper_id: "8c3e8f2a-9d4c-5b7a-9f1e-3d4c5b6a7f8e"
designation: algorithm-specific
title: "Recurrent Neural Networks and Long Short-Term Memory Networks: Tutorial and Survey"
authors: "Ghojogh, B.; Ghodsi, A."
year: 2023
venue: "Unknown"
odin_topics: ["D.1", "D.2"]
shorthand_tags: ["/forecasting-methods", "/temporal-dependency", "/lstm-architecture", "/lstm-vs-alternatives", "/lstm-justification"]
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
```

## TL;DR

Mathematical derivation of RNN backpropagation through time, explanation of gradient vanishing/explosion, and introduction to LSTM gates, GRU, and bidirectional architectures.

## Problem and Motivation

Existing literature on RNN and LSTM is fragmented across many papers, lacking a comprehensive tutorial that covers both fundamentals and variants. Without a unified guide, researchers and practitioners struggle to implement and select appropriate recurrent architectures for sequence modeling tasks. Prior tutorials did not simultaneously cover BPTT, gradient issues, and modern variants like GRU and bidirectional LSTM in a single mathematical framework.

## Approach

- Derives RNN as a dynamical system with parameter sharing and backpropagation through time (BPTT).
- Computes gradients with respect to all RNN parameters: output, state, weight matrices V, W, U, and biases.
- Formalizes gradient vanishing and explosion via eigenvalue analysis of the state transition matrix.
- Reviews solutions: close-to-identity weight matrix, long delays, leaky units, and echo state networks.
- Introduces LSTM with input, forget, output gates, new memory cell, and peephole connections using sigmoid and tanh activations.
- Presents the final memory calculation: `c_t = f_t ⊙ c_{t-1} + i_t ⊙ ̃c_t`.
- Describes GRU with reset and update gates, simplified from LSTM.
- Covers bidirectional RNN/LSTM processing sequences forward and backward, concatenating hidden states.
- Explains ELMo network as stacked bidirectional LSTM with task-specific weighted combination of layers.

## Findings

- BPTT computes gradients by unrolling the network over T time steps, with loss summed over time.
- Gradient vanishing occurs when the largest eigenvalue of weight matrix W is <1; explosion when >1.
- **BPTT's chain rule over T time steps causes gradient vanishing when eigenvalues <1 and explosion when >1.**
- LSTM's forget gate (f_t) and input gate (i_t) create a trade-off between old and new memory, preventing vanishing gradients.
- GRU simplifies LSTM by merging forget and input gates into an update gate (z_t), with reset gate (r_t) controlling previous state influence.
- Bidirectional processing improves sequence tasks by accessing both past and future context, as demonstrated in phoneme classification.
- ELMo combines multiple layers of bidirectional LSTM with learned per-task weights to produce context-aware embeddings.

## Key Figures and Tables

- Figure 1: RNN folded/unfolded structure → shows parameter sharing across time steps.
- Figure 5: LSTM cell with gates (input, forget, output, new memory) → visualizes the conveyor belt of memory.
- Figure 6: GRU cell with reset and update gates → simplified LSTM with two gates.
- Figure 7: Bidirectional RNN → forward and backward states feed into output.
- Figure 9: ELMo network → stacked bidirectional LSTMs with weighted combination.

## Key Equations

$$h_t = \tanh(W h_{t-1} + U x_t + b_i)$$
*Core RNN recurrence: state from previous state and current input.*

$$c_t = f_t \odot c_{t-1} + i_t \odot \tilde{c}_t$$
*LSTM memory trade-off: forget old, add new gated information.*

$$h_t = o_t \odot \tanh(c_t)$$
*LSTM output gate modulates memory to produce hidden state.*

$$h_t = (1 - z_t) \odot h_{t-1} + z_t \odot \tilde{h}_t$$
*GRU update gate blends previous and new states.*

$$\frac{\partial h_T}{\partial h_t} = \prod_{k=t}^{T-1} \frac{\partial h_{k+1}}{\partial h_k}$$
*Product of Jacobians over time causes vanishing or exploding gradients.*

## Definitions

| Term / Acronym | Plain-English Definition |
| -------------- | ------------------------ |
| RNN | Recurrent Neural Network — a network with loops that processes sequences step by step. |
| BPTT | Backpropagation Through Time [think: unroll RNN over time and backpropagate] — training algorithm that unrolls the network across time steps. |
| LSTM | Long Short-Term Memory [think: memory cell that can keep information for long or short periods] — gated RNN that avoids vanishing gradients. |
| GRU | Gated Recurrent Unit [think: simpler version of LSTM with two gates] — simplified LSTM with reset and update gates. |
| ELMo | Embeddings from Language Model [think: deep bidirectional LSTM for word context] — stacked bidirectional LSTM producing context-aware word vectors. |
| Vanishing gradient | Gradients shrink to near zero over many time steps, preventing learning of long-term dependencies. |
| Exploding gradient | Gradients grow exponentially over time, causing unstable training. |
| Peephole | Connection allowing the memory cell to directly influence gates. |
| Forget gate | LSTM gate (f_t) controlling how much of previous memory to discard. |
| Input gate | LSTM gate (i_t) controlling how much new input to write to memory. |
| Output gate | LSTM gate (o_t) controlling how much memory is exposed as hidden state. |
| Reset gate | GRU gate (r_t) controlling how much previous state to ignore. |
| Update gate | GRU gate (z_t) controlling blend of previous and new states. |
| Dynamical system | System where current state depends only on previous state (and input). |

## Critical Citations

- [Hochreiter & Schmidhuber, 1997] — Original LSTM paper; defines core architecture with input and output gates.
- [Rumelhart et al., 1986] — Introduced RNN and backpropagation, foundation of recurrent networks.
- [Bengio et al., 1994] — Formalized gradient vanishing/explosion problem in long-term dependencies.
- [Cho et al., 2014] — Proposed GRU as a simplified LSTM with competitive performance.
- [Graves & Schmidhuber, 2005a] — Vanilla LSTM and bidirectional LSTM for phoneme classification.

## Relevance to Odin

**Topics:**

D.1 — Predictive Modeling in Personal Finance Systems

D.2 — LSTM as the Spending Forecasting Algorithm

**Contribution to Odin:**

This paper provides the mathematical foundation for Odin's spending forecasting module, which uses LSTM. It explains why LSTM addresses gradient vanishing—critical for learning long-term spending patterns (e.g., monthly rent or quarterly bills). The comparison between LSTM and GRU informs algorithm selection; GRU's reduced complexity may be advantageous for mobile deployment with limited compute resources. The discussion of bidirectional LSTM, while not directly applicable to causal forecasting, is relevant to offline profiling or anomaly detection that could look at historical windows both directions.

**Directly justifies:**

- "Vanilla RNNs suffer from gradient vanishing when the largest eigenvalue of the state transition matrix is less than 1, making them unable to learn long-term dependencies (e.g., monthly spending cycles over 12+ months)."
- "LSTM's forget gate (f_t) and input gate (i_t) create a weighted trade-off between old and new memory, mathematically expressed as c_t = f_t ⊙ c_{t-1} + i_t ⊙ ̃c_t, which preserves gradients over long sequences."
- "GRU simplifies LSTM by merging forget and input gates into a single update gate, reducing parameter count and computational cost while maintaining competitive performance on sequence tasks."
- "Backpropagation through time (BPTT) unrolls the RNN over T time steps; the chain rule results in a product of Jacobians, causing gradients to vanish or explode unless gating mechanisms like LSTM are used."
- "Bidirectional LSTM concatenates forward and backward hidden states, providing richer context but violating causality—only applicable when the entire sequence is available offline."

**Limits of relevance:**

- Paper is a tutorial, not an empirical study; provides no performance benchmarks on financial data or comparisons specific to spending forecasting.
- Domain is general sequence modeling (text, speech), not personal finance; applicability to spending patterns requires validation on transaction data.
- No discussion of mobile-specific constraints (memory, inference speed) or cold-start scenarios for new users without spending history.
- Bidirectional LSTM is not suitable for real-time forecasting where future data is unavailable; Odin's forecasting module uses unidirectional LSTM.

## Limitations

- No empirical evaluation of any model on real-world data; all claims are theoretical or architectural. [unacknowledged]
- Does not cover implementation details or hyperparameter tuning for LSTM in practice.
- Assumes familiarity with linear algebra and calculus; may not be accessible to all readers.
- Focuses on mathematical derivations but omits discussion of modern transformer-based alternatives (e.g., attention) that have largely replaced RNN/LSTM in many NLP tasks. [unacknowledged]
- No guidance on selecting between LSTM and GRU for a specific task beyond complexity trade-off.

## Remember This

- 🔑 Gradient vanishes when largest eigenvalue <1; explodes when >1 — chain rule over time.
- 💡 LSTM's memory cell: `c_t = forget_gate * old + input_gate * new` — preserves long-term info.
- 📌 GRU uses two gates (reset, update) vs LSTM's four — simpler, often matches performance.
- 🧠 BPTT unrolls RNN; product of Jacobians causes vanishing/explosion — fixed by gating.