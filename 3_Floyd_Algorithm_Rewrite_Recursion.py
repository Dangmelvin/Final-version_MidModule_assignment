import sys
import itertools

NO_PATH = float('inf')

def floyd_recursive(distance, intermediate, start_node, end_node):
    """
    A recursive implementation of Floyd's algorithm
    """
    global MAX_LENGTH
    
    # Base case: if start_node and end_node are the same, distance is zero
    if start_node == end_node:
        distance[start_node][end_node] = 0

    # Update the distance using recursion
    distance[start_node][end_node] = min(
        distance[start_node][end_node],
        distance[start_node][intermediate] + distance[intermediate][end_node]
    )
    
    # Recursive calls for all possible intermediate nodes
    if intermediate < MAX_LENGTH - 1:
        floyd_recursive(distance, intermediate + 1, start_node, end_node)
    elif start_node < MAX_LENGTH - 1:
        floyd_recursive(distance, 0, start_node + 1, end_node)
    elif end_node < MAX_LENGTH - 1:
        floyd_recursive(distance, 0, 0, end_node + 1)
    return
def floyd(distance):
    """
    Wrapper function for the recursive implementation of Floyd's algorithm
    """
    global MAX_LENGTH
    
    for intermediate, start_node, end_node in itertools.product(
            range(MAX_LENGTH), range(MAX_LENGTH), range(MAX_LENGTH)
    ):
        floyd_recursive(distance, intermediate, start_node, end_node)
    
    # Print the resulting distance matrix
    for row in distance:
        print(row)

# Example usage
graph = [
    [0, 7, NO_PATH, 8],
    [NO_PATH, 0, 5, NO_PATH],
    [NO_PATH, NO_PATH, 0, 2],
    [NO_PATH, NO_PATH, NO_PATH, 0]
]

MAX_LENGTH = len(graph[0])
floyd(graph)
