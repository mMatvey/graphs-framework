import unittest
from Tests.testsUtils import *


class TestGraphClasses(unittest.TestCase):

    def test_incidences(self):
        node1 = Node(1)
        node2 = Node(2)
        node0 = Node(0)
        edge = Edge(node1, node2)
        self.assertEqual(node1.incidence_to_edge(edge), -1)
        self.assertEqual(node2.incidence_to_edge(edge), 1)
        self.assertEqual(node0.incidence_to_edge(edge), 0)
        self.assertEqual(edge.incidence_to_node(node1), -1)
        self.assertEqual(edge.incidence_to_node(node2), 1)
        self.assertEqual(edge.incidence_to_node(node0), 0)

    def test_sorted(self):
        nodes_list = [Node(1), Node(2), Node(3)]
        edges_list = [
            Edge(nodes_list[0], nodes_list[1], 5),
            Edge(nodes_list[0], nodes_list[2], 3),
            Edge(nodes_list[1], nodes_list[2], 1)
        ]
        graph = Graph(False, nodes_list, edges_list)
        self.assertEqual(graph.get_sorted_edges(),
                         [edges_list[2], edges_list[1], edges_list[0]])




if __name__ == '__main__':
    unittest.main()