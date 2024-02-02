import timeit
import itertools

NO_PATH = float('inf')

def floyd_recursive(distance, intermediate, start_node, end_node):
    if start_node == end_node:
        distance[start_node][end_node] = 0

    distance[start_node][end_node] = min(
        distance[start_node][end_node],
        distance[start_node][intermediate] + distance[intermediate][end_node]
    )

    if intermediate < MAX_LENGTH - 1:
        floyd_recursive(distance, intermediate + 1, start_node, end_node)
    elif start_node < MAX_LENGTH - 1:
        floyd_recursive(distance, 0, start_node + 1, end_node)
    elif end_node < MAX_LENGTH - 1:
        floyd_recursive(distance, 0, 0, end_node + 1)

def floyd(distance):
    for intermediate, start_node, end_node in itertools.product(
            range(MAX_LENGTH), range(MAX_LENGTH), range(MAX_LENGTH)
    ):
        floyd_recursive(distance, intermediate, start_node, end_node)

# Example usage
graph = [
    [0, 7, NO_PATH, 8],
    [NO_PATH, 0, 5, NO_PATH],
    [NO_PATH, NO_PATH, 0, 2],
    [NO_PATH, NO_PATH, NO_PATH, 0]
]

MAX_LENGTH = len(graph[0])

# Performance test
def performance_test():
    test_distance = [row[:] for row in graph]
    floyd(test_distance)

# Measure the execution time
execution_time = timeit.timeit(performance_test, number=1)
print(f"Performance Test Execution Time: {execution_time:.6f} seconds")

