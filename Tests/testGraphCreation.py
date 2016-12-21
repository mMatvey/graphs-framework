import unittest
from graphClasses import Node, Graph, Edge
from graph import GraphLib
from random import randint
from graphExceptions import *


def generate_random_params():
    """
    create random list nodes, edges and random bool directed
    :return: bool, list_edges, list_nodes
    """
    directed = bool(randint(0, 1))
    nodes_number = randint(5, 25)
    edges_number = randint(nodes_number, nodes_number*2)
    nodes_ids = set()  # убедиться, что все id уникальны
    for i in range(0, nodes_number):
        nodes_ids.add(randint(1, nodes_number))
    nodes_ids = list(nodes_ids)  # для индексации
    nodes = []
    for node_id in nodes_ids:
        nodes.append(Node(node_id))  # создаём узел с уникальным id
    edges_set = set()
    for i in range(1, edges_number):
        first_node, second_node = nodes[randint(0, len(nodes)-1)], \
                                  nodes[randint(0, len(nodes)-1)]
        edges_set.add(Edge(first_node, second_node))
    edges = list(edges_set)
    return directed, nodes, edges


def generate_random_params_strings():
    """
    params in string for parsing testing, creating graph from strings
    :return:
    """
    directed = bool(randint(0, 1))
    nodes_number = randint(5, 25)
    edges_number = randint(nodes_number, nodes_number*2)
    nodes_ids = set()  # убедиться, что все id уникальны
    for i in range(0, nodes_number):
        nodes_ids.add(randint(1, nodes_number))
    nodes_ids = list(nodes_ids)  # для индексации
    nodes = " ".join(map(str, nodes_ids), )
    edges_set = set()
    for i in range(1, edges_number):
        first_node_id, second_node_id = nodes_ids[randint(0, len(nodes_ids)-1)], \
                                         nodes_ids[randint(0, len(nodes_ids)-1)]
        edges_set.add((first_node_id, second_node_id))
    edges = ""
    for pair in list(edges_set):
        edges += str(pair[0]) + "," + str(pair[1]) + " "
    return directed, nodes, edges


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
