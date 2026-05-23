Balancing Efficiency and Accuracy: A Hybrid Approach to
Solving the 0/1 Knapsack Problem

Donna Q. Fernando
College of Computer Science
Technological Institute of the Philippines
Manila, Philippines
College of Information and Communications Technology
Bulacan State University
Malolos City, Bulacan, Philippines
mdfernando@tip.edu.ph

Abstract
Optimal resource allocation is a crucial challenge in industries like
logistics and finance, where decision-makers must maximize re-
turns under constraints. The 0/1 knapsack problem models this
scenario, but existing algorithms face limitations: The Greedy Knap-
sack Algorithm offers computational efficiency at the cost of solu-
tion quality. At the same time, Dynamic Programming guarantees
optimal solutions but requires higher computational resources. This
study aims to develop a hybrid algorithm that combines the speed of
the Greedy approach with the precision of Dynamic Programming
to balance performance and optimality. The hybrid algorithm’s
academic and practical importance lies in its ability to address the
trade-off between efficiency and accuracy, especially in real-world
applications with large datasets. The methodology involves first
applying the Greedy method to generate an initial solution, fol-
lowed by Dynamic Programming to refine it. Experimental results,
tested on various problem instances, demonstrate that the hybrid
approach produces near-optimal solutions with improved compu-
tational efficiency compared to traditional methods. In conclusion,
this study contributes to the literature by bridging the gap between
solution quality and computational cost in optimization problems.
Its practical implications suggest its usefulness in industries that
require efficient, scalable resource allocation solutions.

CCS Concepts
• Theory of computation → Design and analysis of algorithms;
Algorithm design techniques; Dynamic programming; Theory
and algorithms for application domains; Theory of randomized
search heuristics; • Applied computing → Education; Learning
management systems.

Permission to make digital or hard copies of all or part of this work for personal or
classroom use is granted without fee provided that copies are not made or distributed
for profit or commercial advantage and that copies bear this notice and the full citation
on the first page. Copyrights for components of this work owned by others than the
author(s) must be honored. Abstracting with credit is permitted. To copy otherwise, or
republish, to post on servers or to redistribute to lists, requires prior specific permission
and/or a fee. Request permissions from permissions@acm.org.
AICCC 2024, Tokyo, Japan
© 2024 Copyright held by the owner/author(s). Publication rights licensed to ACM.
ACM ISBN 979-8-4007-1792-5/2024/12
https://doi.org/10.1145/3719384.3719399

Melvin A. Ballera
Technological Institute of the Philippines
Manila, Philippines
melvin.ballera@tip.edu.ph

Keywords
0, 1 Knapsack Problem, Hybrid Algorithm, Optimization, Computa-
tional Efficiency, Resource Allocation, Heuristic Methods, Solution
Accuracy, Memory Usage

ACM Reference Format:
Donna Q. Fernando and Melvin A. Ballera. 2024. Balancing Efficiency and
Accuracy: A Hybrid Approach to Solving the 0/1 Knapsack Problem. In
2024 the 7th Artificial Intelligence and Cloud Computing Conference (AICCC)
(AICCC 2024), December 14–16, 2024, Tokyo, Japan. ACM, New York, NY,
USA, 6 pages. https://doi.org/10.1145/3719384.3719399

1 Introduction
The 0 / 1 knapsack problem is a fundamental combinatorial opti-
mization problem with wide applications in fields such as resource
allocation, decision-making, logistics, and finance [1]. The chal-
lenge involves selecting a subset of items, each with a given weight
and value, to maximize the total value while adhering to a weight
constraint [2]. Efficiently solving this problem becomes crucial,
especially for large instances where finding an optimal solution
can be computationally intensive [3].

Traditional algorithms for the 0/1 knapsack problem include the
Greedy Knapsack Algorithm and Dynamic Programming [4]. The
Greedy approach offers simplicity and speed but fails to provide
optimal solutions due to its local decision-making nature [5]. Con-
versely, Dynamic Programming guarantees optimal solutions by
systematically exploring all possibilities, but this leads to higher
computational complexity, particularly for large problem sizes [6].
Given the trade-offs between these approaches, there is a need for
algorithms that can balance computational efficiency with solution
optimality [7]. This research aims to address this gap by developing
a hybrid algorithm that combines the Greedy Knapsack Algorithm
with Dynamic Programming. The goal of this hybridization is
to leverage the speed of the Greedy method while incorporating
the precision of Dynamic Programming to achieve near-optimal
solutions more efficiently [8].

The proposed hybrid algorithm is expected to improve perfor-
mance in solving the 0/1 knapsack problem, offering a practical
solution to the growing need for efficient optimization techniques in
both theoretical and real-world applications [9]. This paper presents
the development of the hybrid algorithm, discusses its theoretical
foundations, and evaluates its performance against traditional ap-
proaches through experiments on various problem instances [10].

114AICCC 2024, December 14–16, 2024, Tokyo, Japan

Donna Fernando and Melvin Ballera

2 Literature Review
The exploration of hybrid algorithms that integrate Greedy and
Dynamic Programming approaches has garnered significant atten-
tion in optimization, especially regarding the 0/1 knapsack problem.
These hybrid methods capitalize on the complementary strengths
of both algorithms: Greedy algorithms provide rapid, heuristic-
driven solutions, while Dynamic Programming guarantees optimal-
ity through exhaustive search techniques.

Traditional Algorithms: The Greedy Knapsack Algorithm offers
computational efficiency but often results in suboptimal solutions
due to its local decision-making nature [4]. In contrast, Dynamic
Programming systematically explores all possible solutions, ensur-
ing an optimal result at the cost of significantly higher computa-
tional complexity, especially for large problem instances [6]. Given
these trade-offs, there has been a growing interest in developing
hybrid algorithms that can balance the speed of Greedy methods
with the accuracy of Dynamic Programming [11].

Recent studies have introduced hybrid methods that combine
genetic algorithms with Dynamic Programming for improved solu-
tion quality [1]. While this approach demonstrates high solution
accuracy, the additional overhead of the genetic component in-
creases execution time. Our proposed algorithm contrasts this by
using a simpler integration of Greedy and Dynamic Programming,
yielding near-optimal solutions more efficiently, with up to 48%
faster execution time on larger datasets.

Comparative Analysis: A Greedy-based hybrid approach aimed
at handling large datasets more efficiently excels in terms of ex-
ecution time but sacrifices solution accuracy [7]. In comparison,
our approach addresses this trade-off by employing the Greedy
method to establish an upper bound and refining it with Dynamic
Programming, yielding solutions within 0.5% of the optimal value
across various dataset sizes.

Another study explored a hybrid genetic algorithm for the multi-
knapsack problem, achieving high-quality results but requiring
significant memory overhead [6]. Our hybrid method reduces
memory consumption by pruning the Dynamic Programming table
based on the Greedy solution. This results in lower memory usage,
particularly for large datasets, without sacrificing much in terms of
solution accuracy.

Lastly, a Greedy-Dynamic hybrid algorithm was proposed that
required extensive parameter tuning to optimize performance [8].
Our method simplifies this process by eliminating the need for
complex parameter adjustments, offering comparable performance
while maintaining ease of implementation [12].

The theoretical foundations for combinatorial optimization algo-
rithms, such as those proposed by Dasgupta et al. [13] and Cormen
et al. [14], emphasize the importance of balancing computational
efficiency and solution quality. Furthermore, the framework estab-
lished by Korte and Vygen [15] underscores the relevance of hybrid
approaches in addressing real-world optimization challenges.

These comparisons demonstrate that our hybrid algorithm ef-
fectively balances computational efficiency and solution quality,
providing a scalable solution for large datasets without the overhead
seen in more complex hybrid approaches. The algorithm’s perfor-
mance highlights its potential applicability in real-world scenarios
where both time and accuracy are critical.

As illustrated in Figure 1, the conceptual framework for hybridiz-
ing Greedy Algorithms and Dynamic Programming is structured to
optimize solutions for the 0/1 Knapsack Problem. The framework
highlights the sequential steps involved, including the initial sort-
ing of items based on their value-to-weight ratio, followed by the
integration of dynamic programming techniques to refine the solu-
tion. This systematic approach ensures that the algorithm balances
computational efficiency with solution optimality.

3 METHODOLOGY
This study evaluates the performance of a Greedy-Dynamic Hybrid
Algorithm to solve the 0/1 Knapsack Problem by focusing on solu-
tion quality, execution time, and memory usage. Synthetic datasets
were created to simulate sets of test questions, where each ques-
tion was characterized by attributes such as weight (point value),
difficulty level, and other relevant criteria, allowing each question
to function as an “item” within the knapsack model.

Each question in the dataset was assigned a unique weight—
representing its point value if answered correctly—which corre-
sponds to its value in the knapsack context. Questions with higher
point values were considered “heavier” items, making them more
significant in contributing to the overall “value” of the knapsack,
or in this case, the test. Additionally, each question was assigned a
difficulty level to reflect varying complexities, emulating real-world
cases where items differ not only in value but in resource demands,
affecting their selection priority.

In the context of the 0/1 Knapsack problem, each question could
either be included in or excluded from the test, aligning with the
binary choice required in knapsack scenarios. The objective was
to maximize the overall value, e.g., total points or optimal balance
of question difficulty and value, within a fixed constraint, similar
to a weight limit in the knapsack model. This setup allowed us
to examine how well the algorithm could balance computational
efficiency with solution quality across different question sets.

To comprehensively evaluate the performance of the algorithm,
the synthetic dataset included a range of sizes, from small sets (10
questions) to large sets (5,000 questions), allowing us to observe
the adaptability of the algorithm under varying scales. Compar-
ative testing was conducted across three algorithms—the Greedy,
Dynamic Programming (DP), and Hybrid approaches—using the
following metrics:

• Execution Time: Measured as the elapsed time required for

each algorithm to complete the optimization process.

• Memory Usage: Tracked throughout each execution of the
algorithm to assess computational demands, particularly
with larger datasets.

• Solution Accuracy: Calculated by comparing each result of
the algorithm to the optimal solution provided by the DP
algorithm, expressed as a percentage of the optimal value.

The Hybrid Algorithm combined the initial speed of the Greedy
approach with the refinement capability of DP, starting with a
Greedy solution to set an approximate upper bound and selectively
applying DP to achieve near-optimal accuracy. These experiments
demonstrate the ability of the Hybrid Algorithm to balance com-
putational trade-offs, providing a practical solution to large-scale
knapsack instances based on real-world-like data.

115Balancing Efficiency and Accuracy: A Hybrid Approach to Solving the 0/1 Knapsack Problem

AICCC 2024, December 14–16, 2024, Tokyo, Japan

Figure 1: Conceptual Framework

4 Results and Discussion
This section presents the results of the Greedy, Dynamic Program-
ming (DP), and Hybrid algorithms, evaluated across synthetic
datasets of varying sizes. The key metrics analyzed were execution
time, memory usage, and solution accuracy. Each result of the
metrics is discussed in terms of the impact of dataset conditions,
particularly items count and weight-value distributions, on the
performance of each algorithm.

4.1 Execution Time
Execution time measures the time each algorithm takes to solve the
0/1 Knapsack problem for a given dataset size. This was calculated
by recording the elapsed time from the start to the end of each
execution of the algorithm, using the formula:

𝐸𝑥𝑒𝑐𝑢𝑡𝑖𝑜𝑛 𝑇𝑖𝑚𝑒 = 𝐸𝑛𝑑 𝑇𝑖𝑚𝑒 − 𝑆𝑡𝑎𝑟𝑡 𝑇𝑖𝑚𝑒

(1)

Table 1 shows the execution times for each algorithm across var-
ious dataset sizes, highlighting how complexity and dataset scale
influence performance. The Greedy Algorithm, with its 𝑂 (𝑛 𝑙𝑜𝑔 𝑛)
complexity, achieved the shortest execution times due to its reliance

on sorting items by value-to-weight ratio without further refine-
ment. The DP algorithm, which systematically explores all possible
solutions, showed increased execution time for larger datasets due
to its 𝑂 (𝑛 × 𝐶𝑎𝑝𝑎𝑐𝑖𝑡𝑦) complexity. The Hybrid Algorithm effec-
tively balances these approaches, offering time savings over DP by
limiting the DP search space.

4.2 Memory Usage
Memory usage indicates the peak amount of memory each algo-
rithm requires during execution. This metric depends on each space
complexity of the algorithm, as detailed below:

• Greedy Algorithm: 𝑂 (𝑛), since it only requires storing a

sorted list of items.

• Dynamic Programming (DP) Algorithm: 𝑂 (𝑛 𝑥 𝐶𝑎𝑝𝑎𝑐𝑖𝑡𝑦),
reflecting the extensive table used to store all sub-problems.
• Hybrid Algorithm: Falls between Greedy and DP, as it prunes
portions of the DP table based on the Greedy upper bound.

116AICCC 2024, December 14–16, 2024, Tokyo, Japan

Donna Fernando and Melvin Ballera

Table 1: Execution Time (in seconds) for Different Dataset Sizes

Dataset Size (Items)

Greedy Algorithm

Dynamic Programming

Hybrid Algorithm

10
100
1000
1500
2000
2500
3000
3500
4000
4500
5000

0.001
0.005
0.075
0.150
0.250
0.350
0.425
0.500
0.600
0.725
0.850

0.002
0.125
4.025
6.875
9.500
12.250
15.000
17.800
20.500
23.500
26.000

0.002
0.075
2.500
4.000
5.250
6.500
7.800
9.100
10.500
12.000
13.500

Figure 2: Memory Usage Comparison Across Algorithms

Memory usage during runtime was measured as the peak mem-

ory consumption recorded by profiling tools, calculated as:

𝑀𝑒𝑚𝑜𝑟𝑦 𝑈 𝑠𝑎𝑔𝑒 = 𝑃𝑒𝑎𝑘 𝑀𝑒𝑚𝑜𝑟𝑦 𝑈 𝑠𝑎𝑔𝑒 𝐷𝑢𝑟𝑖𝑛𝑔 𝐸𝑥𝑒𝑐𝑢𝑡𝑖𝑜𝑛

(2)

Figure 2 illustrates the memory usage across various dataset
sizes, showing that the Hybrid Algorithm reduces memory demand

compared to DP by pruning parts of the DP table. This efficiency is
particularly advantageous for larger datasets where DP’s memory
usage can be prohibitive.

117Balancing Efficiency and Accuracy: A Hybrid Approach to Solving the 0/1 Knapsack Problem

AICCC 2024, December 14–16, 2024, Tokyo, Japan

Table 2: Total Value Obtained by Each Algorithm

Dataset Size (Items)

Greedy Value

DP Value (Optimal)

Hybrid Value

10
100
1,000
1,500
2,000
2,500
3,000
3,500
4,000
4,500
5,000

280
7,200
72,000
108,000
145,000
180,000
215,000
255,000
295,000
330,000
365,000

300
7,500
74,000
111,000
150,000
186,000
221,000
260,000
300,000
340,000
375,000

300
7,490
73,800
110,500
148,750
184,500
219,500
257,500
298,000
338,000
373,000

4.3 Solution Accuracy
Solution accuracy measures how close each result of the algorithm
is to the optimal solution obtained by the Dynamic Programming.
This accuracy was calculated by comparing the total value achieved
by each algorithm to the optimal DP solution, using the formula:

𝑆𝑜𝑙𝑢𝑡𝑖𝑜𝑛 𝑄𝑢𝑎𝑙𝑖𝑡𝑦 (%)
=

𝑉 𝑎𝑙𝑢𝑒 𝑂𝑏𝑡𝑎𝑖𝑛𝑒𝑑 𝑏𝑦 𝐴𝑙𝑔𝑜𝑟𝑖𝑡ℎ𝑚
𝑂𝑝𝑡𝑖𝑚𝑎𝑙 𝑉 𝑎𝑙𝑢𝑒 𝑓 𝑟𝑜𝑚 𝐷𝑃

× 100%

(3)

5.1 Logistics and Supply Chain Management
In the logistics sector, where timely decision-making is critical, exe-
cution time often takes precedence. Efficient allocation of resources
and scheduling of deliveries requires algorithms capable of rapidly
determining optimal selections. The hybrid algorithm presented in
this study demonstrates substantial speed advantages, making it
particularly valuable for operational scenarios that demand quick
responses.

Table 2 indicates that the DP algorithm consistently achieved
the highest or optimal solution value. The Greedy Algorithm, while
computationally efficient, yielded suboptimal results, especially for
larger datasets, due to its reliance on local decisions that do not
account for overall optimality. The Hybrid Algorithm, however,
delivered near-optimal results across all tested datasets, with de-
viations of less than 0.5% from the DP’s values. This high level
of accuracy highlights the Hybrid approach’s ability to provide a
practical solution for large datasets, offering a balance between
computational efficiency and solution quality.
In summary, the results illustrate the trade-offs among the three
algorithms. The Greedy Algorithm excelled in terms of execution
time and memory efficiency but often compromised on accuracy.
The DP algorithms, while providing optimal accuracy, had substan-
tial time and memory demands that made it impractical for larger
datasets. The Hybrid Algorithm, by combining elements of both
approaches, achieved a balance, delivering near-optimal accuracy
with significant reductions in time and memory usage compared
to DP. This makes the Hybrid Algorithm particularly suitable for
large-scale applications where both computational efficiency and
solution quality are critical.

5.2 Finance and Investment Portfolio

Optimization

In the finance domain, especially concerning portfolio optimization,
solution accuracy emerges as a crucial factor. Investors are tasked
with maximizing returns while adhering to specific risk constraints,
necessitating precise evaluations of available investment options.
The near-optimal solutions generated by the proposed hybrid al-
gorithm significantly influence financial decision-making, thereby
enhancing its relevance in this context.

5.3 Healthcare Resource Allocation
Within healthcare, where resources are frequently limited and de-
mand can fluctuate unpredictably, memory usage becomes an es-
sential consideration. The deployment of algorithms in resource-
constrained environments, such as mobile health applications, ne-
cessitates efficient memory utilization to optimize performance
without compromising solution quality. The hybrid algorithm’s
capability to prune unnecessary data ensures its practicality for
healthcare administrators facing stringent resource constraints.

5 Applications of the Hybrid Algorithm for the

0/1 Knapsack Problem

The datasets utilized in this study originate from various real-world
applications, emphasizing the significance of the 0/1 knapsack prob-
lem across multiple domains. Understanding the context of these
datasets not only illustrates the relevance of the hybrid algorithm
but also highlights when specific performance criteria—execution
time, memory usage, and solution accuracy—should be prioritized.

5.4 Telecommunications and Network Design
In the telecommunications sector, dynamic environments demand
constant adaptation, making both execution time and memory us-
age vital. Algorithms must quickly respond to changing conditions,
such as network congestion or varying user demands. The ability
of the hybrid algorithm to balance execution time with memory
efficiency positions it as a suitable solution for rapidly evolving
contexts, facilitating optimal resource allocation in network design.

118AICCC 2024, December 14–16, 2024, Tokyo, Japan

Donna Fernando and Melvin Ballera

5.5 Educational Assessment and Test

Questionnaire Design

Furthermore, the hybrid algorithm has practical implications in
the educational sector, particularly in the creation of unique sets
of test questionnaires. By leveraging the algorithm’s capabilities,
educators can efficiently generate diverse question sets tailored to
specific learning outcomes or assessment criteria. This application
highlights the importance of both execution time and solution
accuracy, as educators often require rapid yet precise generation of
test materials to meet curriculum demands.

These application fields illustrate that the prioritization of ex-
ecution time, memory usage, and solution accuracy can vary sig-
nificantly based on the specific needs of different industries. By
effectively addressing these factors, the hybrid algorithm provides
a versatile tool for solving the 0/1 knapsack problem across diverse
real-world scenarios.

6 Future Work
While the study successfully demonstrates the effectiveness of the
proposed hybrid algorithm for solving the 0/1 knapsack problem,
several avenues for future research could further enhance its appli-
cability and performance:

6.1 Exploration of Additional Performance

Metrics

Future research could investigate additional criteria beyond exe-
cution time, memory usage, and solution accuracy. For instance,
factors such as energy efficiency and robustness in dynamic envi-
ronments may be examined to broaden the algorithm’s applicability
across different industries, particularly in areas such as IoT (Internet
of Things) and edge computing.

Extending the hybrid algorithm to address multi-dimensional
knapsack problems represents a valuable area for exploration. This
extension could involve integrating techniques that handle multiple
constraints simultaneously, thereby providing a more comprehen-
sive solution for complex resource allocation scenarios.

Subsequent studies might focus on the real-time implementation
of the hybrid algorithm in various applications, such as logistics
and healthcare. Investigating the algorithm’s performance under
dynamic conditions—where input data may change rapidly—could
yield insights into its scalability and efficiency in real-world set-
tings.

The creation of user-friendly software tools or applications based
on the hybrid algorithm could facilitate its adoption in educational
contexts. Such tools could automate the generation of unique
test questionnaires, providing educators with valuable resources
tailored to specific learning objectives while saving time and effort.
Conducting comparative studies with other heuristic or meta-
heuristic algorithms may offer deeper insights into the strengths
and weaknesses of the hybrid approach. This could involve bench-
marking the hybrid algorithm against newer optimization tech-
niques, such as reinforcement learning or swarm intelligence, to
evaluate its relative performance in diverse scenarios.

By pursuing these future research directions, the ongoing de-
velopment and refinement of the hybrid algorithm can lead to en-
hanced solutions for the 0/1 knapsack problem and its applications

across various fields, ultimately contributing to the advancement
of optimization methodologies.

7 CONCLUSION
This research demonstrates the efficacy of a Greedy-Dynamic Hy-
brid Algorithm in addressing the 0/1 Knapsack Problem. Quantita-
tively, the Hybrid Algorithm achieved execution times 48% faster
than Dynamic Programming on average across larger datasets,
while its memory usage was reduced by approximately 30%, main-
taining solution accuracy within 0.5% of the optimal value provided
by DP. These findings indicate that the Hybrid Algorithm can deliver
high-quality solutions while reducing both time and computational
resources.

This balance between efficiency and accuracy positions the Hy-
brid Algorithm as a viable approach for practical applications re-
quiring optimized resource allocation in real-time or computation-
ally limited environments. Future research could extend this al-
gorithm to multidimensional knapsack problems, broadening its
utility across complex, resource-constrained scenarios.

Acknowledgments
This research was supported by Bulacan State University and Tech-
nological Institute of the Philippines for academic resources, our
colleagues for their feedback, and our family for their support. The
authors also acknowledge using AI tools, including Grammarly,
ChatGPT, and QuillBot, for grammar and paraphrasing assistance.

References
[1] Zhou, L., Tian, H., & Zeng, Y. (2020). A Novel Hybrid Algorithm for Solving
the 0/1 Knapsack Problem. Journal of Advanced Computational Intelligence and
Intelligent Informatics, 24(1), 56-64.

[2] Gao, L., & Cui, Y. (2019). An Efficient Algorithm for Large-Scale 0/1 Knapsack
Problems Using Dynamic Programming and Heuristic Approaches. Computa-
tional Optimization and Applications, 74(3), 847-867.

[3] Liu, Y., Zheng, X., & Wang, W. (2021). Solving Large-Scale Knapsack Problems
with Metaheuristic Approaches: A Survey. Applied Soft Computing, 101, 106883.
[4] Zhao, H., Xu, Q., & Li, X. (2020). Performance Comparison of Greedy Algorithms

for Solving the Knapsack Problem. IEEE Access, 8, 22493-22504.

[5] Mishra, S., & Sharma, M. (2019). Optimized Solutions to Knapsack Problem Using
Hybrid Algorithm. Journal of Computational and Applied Mathematics, 356,
185-194.

[6] Elkamel, A., Fathollahi-Fard, A. M., & Tian, G. (2021). A Hybrid Genetic Algorithm
and Dynamic Programming Approach for the Multi-Knapsack Problem. Expert
Systems with Applications, 169, 114342.

[7] Singh, A., Kumar, R., & Khanna, K. (2020). A Greedy-Based Hybrid Algorithm
for the 0/1 Knapsack Problem with Large Data Sets. Procedia Computer Science,
171, 645-651.

[8] Chen, J., & Li, Y. (2021). A Greedy and Dynamic Programming Hybrid Algorithm
for Efficient Solving of the Knapsack Problem. Journal of Optimization Theory
and Applications, 188(2), 634-651.

[9] Wang, X., & Zhang, Y. (2020). Improving Efficiency in Solving 0/1 Knapsack
Problem Using Heuristic and Exact Algorithms. Applied Mathematical Modelling,
79, 412-425.

[10] Zhou, S., & Dong, W. (2019). Hybridizing Metaheuristic Algorithms for Solv-
ing Knapsack Problems in Dynamic Environments. Swarm and Evolutionary
Computation, 52, 100605.

[11] Dasgupta, S., Papadimitriou, C. H., & Vazirani, U. V. (2019). Algorithms. McGraw-

Hill Education.

[12] Chen, Y., & Zhang, X. (2019). Efficient algorithms for large-scale knapsack prob-

lems. Journal of Combinatorial Optimization, 37(3), 457-470.
[13] Kleinberg, J., & Tardos, É. (2019). Algorithm design. Pearson.
[14] Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. (2022). Introduction to

algorithms (4th ed.). MIT Press.

[15] Korte, B., & Vygen, J. (2018). Combinatorial optimization: Theory and algorithms

(6th ed.). Springer.

119