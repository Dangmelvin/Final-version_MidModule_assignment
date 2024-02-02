import unittest
from unittest.mock import patch
from io import StringIO

NO_PATH = float('inf')

def floyd_recursive(distance, intermediate, start_node, end_node, MAX_LENGTH):
    if start_node == end_node:
        distance[start_node][end_node] = 0

    distance[start_node][end_node] = min(
        distance[start_node][end_node],
        distance[start_node][intermediate] + distance[intermediate][end_node]
    )

    if intermediate < MAX_LENGTH - 1:
        floyd_recursive(distance, intermediate + 1, start_node, end_node, MAX_LENGTH)
    elif start_node < MAX_LENGTH - 1:
        floyd_recursive(distance, 0, start_node + 1, end_node, MAX_LENGTH)
    elif end_node < MAX_LENGTH - 1:
        floyd_recursive(distance, 0, 0, end_node + 1, MAX_LENGTH)

class TestFloydRecursive(unittest.TestCase):

    def setUp(self):
        self.NO_PATH = float('inf')
        self.MAX_LENGTH = None
        self.test_graph = [
            [0, 7, self.NO_PATH, 8],
            [self.NO_PATH, 0, 5, self.NO_PATH],
            [self.NO_PATH, self.NO_PATH, 0, 2],
            [self.NO_PATH, self.NO_PATH, self.NO_PATH, 0]
        ]

    def test_floyd_recursive_same_node(self):
        # Test when start_node and end_node are the same
        test_distance = [row[:] for row in self.test_graph]
        floyd_recursive(test_distance, 0, 0, 0, len(self.test_graph[0]))
        self.assertEqual(test_distance, self.test_graph)

    def test_floyd_recursive_different_nodes(self):
        # Test when start_node and end_node are different
        test_distance = [row[:] for row in self.test_graph]
        floyd_recursive(test_distance, 0, 0, 1, len(self.test_graph[0]))
        # Assert specific values based on your expectations for this case

    @patch('sys.stdout', new_callable=StringIO)
    def test_floyd_recursive_output(self, mock_stdout):
        # Test the printed output of the function
        test_distance = [row[:] for row in self.test_graph]
        floyd_recursive(test_distance, 0, 0, 1, len(self.test_graph[0]))
        expected_output = "inf inf 5 8\n"
        self.assertEqual(mock_stdout.getvalue(), expected_output)

if __name__ == '__main__':
    unittest.main()

