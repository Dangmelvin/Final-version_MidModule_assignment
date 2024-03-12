NO_PATH = float('inf')
graph = [[0, 7, NO_PATH, 8],
         [NO_PATH, 0, 5, NO_PATH],
         [NO_PATH, NO_PATH, 0, 2],
         [NO_PATH, NO_PATH, NO_PATH, 0]]
MAX_LENGTH = len(graph[0])

def floyd_recursive(distance, intermediate, start_node, end_node):
    if start_node == end_node:
        return 0
    
    if intermediate == MAX_LENGTH:
        return distance[start_node][end_node]
    
    without_intermediate = floyd_recursive(distance, intermediate + 1, start_node, end_node)
    with_intermediate = floyd_recursive(distance, intermediate + 1, start_node, intermediate) + floyd_recursive(distance, intermediate + 1, intermediate, end_node)
    
    return min(without_intermediate, with_intermediate)

def floyd(distance):
    for start_node in range(MAX_LENGTH):
        for end_node in range(MAX_LENGTH):
            if start_node != end_node:
                distance[start_node][end_node] = floyd_recursive(distance, 0, start_node, end_node)

# Distance matrix
floyd(graph)

# Print the result
for row in graph:
    print(row)
