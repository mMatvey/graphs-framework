import unittest
from graphClasses import *


class TestAdjacencyMethods(unittest.TestCase):
    nodes_list = [Node(1), Node(2), Node(3)]
    edges_list = [Edge(nodes_list[0], nodes_list[1])]
    graph = Graph(False, nodes_list, edges_list)

    def test_get_adjaincy_list(self):
        self.assertEqual(self.graph.get_adjacency_list(self.nodes_list[0]),
                         [self.nodes_list[1]], "for 0")
        self.assertEqual(self.graph.get_adjacency_list(self.nodes_list[1]),
                         [self.nodes_list[0]], "for 1")
        self.assertEqual(self.graph.get_adjacency_list(self.nodes_list[2]),
                         [], "for 2")

    def test_adjacency_to_node(self):
        self.assertEqual(self.graph.adjacency_to_node(self.nodes_list[0],
                                                      self.nodes_list[1]),
                         True, "0 to 1")
        self.assertEqual(self.graph.adjacency_to_node(self.nodes_list[1],
                                                      self.nodes_list[0]),
                         True, " 1 to 0")
        self.assertEqual(self.graph.adjacency_to_node(self.nodes_list[0],
                                                      self.nodes_list[2]),
                         False, "0 to 2")
        self.assertEqual(self.graph.adjacency_to_node(self.nodes_list[1],
                                                      self.nodes_list[2]),
                         False, "1 to 2")

    def test_adjacency_get_node_by_id(self):
        self.assertEqual(self.graph.get_node_by_id(1),
                         self.nodes_list[0], "for 0")
        self.assertEqual(self.graph.get_node_by_id(2),
                         self.nodes_list[1], "for 1")
        self.assertEqual(self.graph.get_node_by_id(3),
                         self.nodes_list[2], "for 2")

    def test_adjacency_get_list_by_id(self):
        self.assertEqual(self.graph.get_adjacency_list_by_id(1),
                         [self.nodes_list[1]], "for 0")
        self.assertEqual(self.graph.get_adjacency_list_by_id(2),
                         [self.nodes_list[0]], "for 1")
        self.assertEqual(self.graph.get_adjacency_list_by_id(3),
                         [], "for 2")

    def test_adjacency_to_node_by_id(self):
        self.assertEqual(self.graph.adjacency_to_node_by_id(1, 2),
                         True, "0 to 1")
        self.assertEqual(self.graph.adjacency_to_node_by_id(2, 1),
                         True, " 1 to 0")
        self.assertEqual(self.graph.adjacency_to_node_by_id(1, 3),
                         False, "0 to 2")
        self.assertEqual(self.graph.adjacency_to_node_by_id(2, 3),
                         False, "1 to 2")


if __name__ == '__main__':
    unittest.main()
