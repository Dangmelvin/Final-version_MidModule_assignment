import unittest

NO_PATH = float('inf')

def floyd_recursive(distance, intermediate, start_node, end_node, MAX_LENGTH):
    if start_node == end_node:
        return 0
    
    if intermediate == MAX_LENGTH:
        return distance[start_node][end_node]
    
    without_intermediate = floyd_recursive(distance, intermediate + 1, start_node, end_node, MAX_LENGTH)
    with_intermediate = floyd_recursive(distance, intermediate + 1, start_node, intermediate, MAX_LENGTH) + floyd_recursive(distance, intermediate + 1, intermediate, end_node, MAX_LENGTH)
    
    return min(without_intermediate, with_intermediate)

def floyd(distance):
    MAX_LENGTH = len(distance[0])
    for start_node in range(MAX_LENGTH):
        for end_node in range(MAX_LENGTH):
            if start_node != end_node:
                distance[start_node][end_node] = floyd_recursive(distance, 0, start_node, end_node, MAX_LENGTH)

class TestFloyd(unittest.TestCase):
    def test_floyd_algorithm(self):
        graph = [
            [0, 7, NO_PATH, 8],
            [NO_PATH, 0, 5, NO_PATH],
            [NO_PATH, NO_PATH, 0, 2],
            [NO_PATH, NO_PATH, NO_PATH, 0]
        ]
        expected_result = [
            [0, 7, 12, 8],
            [NO_PATH, 0, 5, 7],
            [NO_PATH, NO_PATH, 0, 2],
            [NO_PATH, NO_PATH, NO_PATH, 0]
        ]
        
        floyd(graph)
        
        self.assertEqual(graph, expected_result)

if __name__ == '__main__':
    unittest.main()
