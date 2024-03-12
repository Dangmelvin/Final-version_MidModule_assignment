## Overview
(Recommend to open this file by Visual Studio)
Github Repo: https://github.com/Dangmelvin/Mid_assignment_Final_version_2002/tree/main

Floyd's algorithm is a classic algorithm for solving the all-pairs shortest path problem in a weighted, directed graph. This recursive implementation demonstrates the fundamental idea of the algorithm. In this document you will find the basic information regarding the Floyd's algorithm project including:

# Rewriting the floy algorithm based on interative solution by using recursive approach and PEP
# Writing Unit test, Performance test

## Floyd's Recursive Algorithm

This Python script (Floyd_Algorithm_Rewrite_Recursion.py) implements Floyd's algorithm for finding the shortest paths between all pairs of vertices in a graph. The implementation uses a recursive approach with PEP standard with requirements as below:

# Implementing Floyd Algorithm following the Python Enhancement Proposal and standard Python library to use recursion based on interative version:

def floyd(distance):
"""
A simple implementation of Floyd's algorithm
"""
for intermediate, start_node,end_node\
in itertools.product\
(range(MAX_LENGTH),range(MAX_LENGTH), range(MAX_LENGTH)):
##Assume that if start_node and end_node are the same
##then the distance would be zero
if start_node == end_node:
distance[start_node][end_node] = 0
continue
#return all possible paths and find the minimum
distance[start_node][end_node] = min(distance[start_node][end_node],
distance[start_node][intermediate] + distance[intermediate][end_node] )
#Any value that have sys.maxsize has no path
print (distance)
floyd(graph)

# Imperative Solution
The following is a distance matrix. Each list is the distance between that node and the rest of
the nodes. For example graph[0] is the distance between node 0 and nodes 0,1,2 and 3.
Unsurprisingly the distance between Node 0 and Node 0 is 0, whereas between Node 0 and
Node 1 is 7. NO_PATH indicates that there is no direct path.
NO_PATH = sys.maxsize
graph = [[0, 7, NO_PATH, 8],
[NO_PATH, 0, 5, NO_PATH],
[NO_PATH, NO_PATH, 0, 2],
[NO_PATH, NO_PATH, NO_PATH, 0]]
MAX_LENGTH = len(graph[0])
import sys
import itertools

# Require to write the unit test for each function and performance test to mearue the time unit

## Performance test

The Performance Floyd_Algorithm_Performance_test.py script demonstrates the execution time of the Floyd-Warshall algorithm for a larger graph.
Employs Python's ‘timeit’ module to precisely measure the execution time. The ‘performance_test’ function initiates by creating a deep copy of the graph to ensure a consistent starting point for each test iteration

## Unit test
The Floyd_Algorithm_Unit_test.py script demonstrates the unit test for each function of the Floyd-Warshall algorithm
The unit test code, utilizing Python's ‘unittest’ module

## License 
Distributed under the MIT License. See LICENSE.txt for more information.

## Requirements

No need specifict dictionary/binary to run the code as the code is written by basic Python dictionary only.
Recommend to open by visual studio