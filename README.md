# Chu-Liu/Edmonds Algorithm

## Overview

The Chu-Liu/Edmonds algorithm is a fundamental algorithm in graph theory, used primarily for finding the minimum spanning tree (MST) of a directed graph. This algorithm is critical in various applications, including optimizing network flows, understanding connectivity in directed networks, and solving problems in fields such as computational linguistics for tasks like dependency parsing.

## Background and History

The algorithm was independently discovered by Y. J. Chu and T. H. Liu in 1965, and Jack Edmonds in 1967. While the Chu-Liu algorithm originally tackled the shortest arborescence of a weighted directed graph, Edmonds provided a more generalized approach that enhanced its application to broader scenarios. This algorithm is particularly notable for its ability to efficiently compute minimum spanning trees in directed graphs, an essential capability in network design and data structure optimization.

## Why Chu-Liu/Edmonds Algorithm?

Unlike traditional MST algorithms like Kruskal’s or Prim’s, which are tailored for undirected graphs, the Chu-Liu/Edmonds algorithm specifically addresses the complexities associated with directed graphs. In directed graphs, the conventional MST transforms into a minimum spanning arborescence where each node (except the root) has exactly one incoming edge, making it uniquely suited for directed scenarios.

## How It Works

The Chu-Liu/Edmonds algorithm follows a specific series of steps to compute the minimum spanning tree of a directed graph. Here’s a simplified breakdown of its operation:

1. **Initialization**: Start with the selection of a root node from which the minimum spanning arborescence will originate.

2. **Minimum Incoming Edge**: For each node (except the root), select the minimum weight incoming edge. This step forms a set of edges that potentially contains cycles.

3. **Detect and Eliminate Cycles**: Identify cycles within the selected edges. Since a spanning tree cannot have cycles, they must be resolved:

   - Contract each cycle into a single super-node.
   - Recursively apply the algorithm to the graph with these contracted nodes.

4. **Expand Contracted Cycles**: Once the base case (a graph without cycles) is resolved, expand back the contracted cycles, carefully reintegrating them into the spanning tree while ensuring minimal total weight.

5. **Edge Reversal**: In some implementations, reversing the direction of edges in the contracted graph can simplify cycle reintegration and help maintain the minimum spanning tree properties during recursion.

## Conclusion

The Chu-Liu/Edmonds algorithm remains a cornerstone technique for handling directed graphs in computational theory and practice. Its ability to efficiently determine minimum spanning arborescences makes it indispensable for network analysis and related fields.

## Class Diagram

|                   Alg                    |
| :--------------------------------------: |
| + construct\*weighted_graph(self, graph) |
|          + execute(self, Graph)          |
