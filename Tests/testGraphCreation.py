import unittest
from Tests.testsUtils import *


class TestGraphCreation(unittest.TestCase):

    def test_graph_creation(self):
        for i in range(0, 5):
            directed, nodes, edges = generate_random_params()
            graph = Graph(directed, nodes, edges)
            self.assertEqual(directed, graph.directed)
            self.assertEqual(edges, graph._edges_list)
            self.assertEqual(nodes, graph._nodes_list)

    def test_graph_creation_by_strings(self):
        for i in range(0, 5):
            directed, nodes_str, edges_str = generate_random_params_strings()
            graph = Graph.create_graph_from_strings(directed,
                                                    nodes_str,
                                                    edges_str)
            nodes = []
            edges = []
            for node in nodes_str.split():
                nodes.append(Node(int(node)))
            for pair in edges_str.split():
                pair = pair.split(",")
                edges.append(Edge(Node(int(pair[0])),
                                  Node(int(pair[1]))))
            self.assertEqual(directed, graph.directed)
            self.assertEqual(nodes, graph._nodes_list)
            self.assertEqual(edges, graph._edges_list)


    def test_ununiq_nodes_ids(self):
        nodes_ununiq_ids = [Node(randint(1,100)), Node(randint(1,100))]
        nodes_ununiq_ids.append(nodes_ununiq_ids[randint(0,1)])
        edges = [Edge(nodes_ununiq_ids[0],
                      nodes_ununiq_ids[1])]
        try:
            graph = Graph(False, nodes_ununiq_ids,
                          edges)
            assert False;
        except GraphCreationException as exception:
            self.assertEqual(type(exception) == GraphCreationException, True)

    def test_edge_creation(self):
        try:
            params = (Node(1), "")
            edge = Edge(node_in=params[0], node_out=params[1])
            raise False
        except EdgeCreationException as exception:
            self.assertEqual(type(exception) == EdgeCreationException, True)
        try:
            params = (None, Node(1))
            edge = Edge(params[0], params[1])
            raise False
        except EdgeCreationException as exception:
            self.assertEqual(type(exception) == EdgeCreationException, True)




if __name__ == '__main__':
    unittest.main()
