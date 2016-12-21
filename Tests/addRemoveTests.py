import unittest
from Tests.testsUtils import *
from graphExceptions import *


class TestAdd(unittest.TestCase):

    def test_add_node(self):
        for time in range(5):
            directed, nodes, edges = generate_random_params()
            nodes = list(set(nodes)) # совпадения в другом тесте
            test_graph = Graph(directed=False, nodes_list=[], edges_list=[])
            for node in nodes:
                test_graph.add_node(node)
            for edge in edges:
                test_graph.add_edge(edge)
            self.assertEqual(set(nodes), set(test_graph._nodes_list))
            self.assertEqual(set(edges), set(test_graph._edges_list))

    def test_add_node_same_id(self):
        test_graph = Graph(directed=False, nodes_list=[], edges_list=[])
        test_graph.add_node(Node(1))
        try:
            test_graph.add_node(Node(1))
            raise False
        except GraphException as exception:
            self.assertEqual(type(exception) == GraphException, True)


class TestRemove(unittest.TestCase):

    def test_remove_node(self):
        for time in range(5):
            directed, nodes, edges = generate_random_params()
            nodes = list(set(nodes)) # совпадения в другом тесте
            test_graph = Graph(directed=False, nodes_list=nodes, edges_list=edges)
            import copy
            copy_nodes = copy.deepcopy(nodes)
            for node in copy_nodes:
                test_graph.remove_node(Node(node.node_id))
            self.assertEqual([], test_graph._nodes_list)
            self.assertEqual([], test_graph._edges_list)

    def test_remove_by_id(self):
        nodes = [Node(1), Node(2), Node(3)]
        edges = [
            Edge(nodes[0], nodes[1], 0),
            Edge(nodes[1], nodes[2], 0),
            Edge(nodes[0], nodes[2], 0)
        ]
        test_graph = Graph(directed=False, nodes_list=nodes, edges_list=edges)
        for i in range(1, 4):
                test_graph.remove_node_by_id(i)
        self.assertEqual([], test_graph._nodes_list)
        self.assertEqual([], test_graph._edges_list)


if __name__ == '__main__':
    unittest.main()