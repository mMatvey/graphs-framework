import unittest
from graph import Node, Edge, Graph, GraphLib
from random import randint


def generate_graph():
    """
    create graph with random nodes, edges, directed
    :return: random graph
    """
    directed, edges, nodes = generate_random_params()
    return Graph(directed, edges, nodes)


def generate_random_params():
    """
    create random list nodes, edges and random bool directed
    :return: bool, liest_edges, list_nodes
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
    return directed, edges, nodes

def generate_random_params_strings():
    """
    params in string for parsing testing, creating grapth from strings
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
    return directed, edges, nodes

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

    def test_graph_creation(self):
        for i in range(0, 5):
            directed, edges, nodes = generate_random_params()
            graph = Graph(directed, edges, nodes)
            if graph:
                self.assertEqual(directed, graph.directed)
                self.assertEqual(edges, graph.edges_list)
                self.assertEqual(nodes, graph.nodes_list)

    def test_graph_creation_by_strings(self):
        for i in range(0, 5):
            directed, edges, nodes = generate_random_params_strings()
            graph = Graph(directed, edges, nodes)
            if graph:
                self.assertEqual(directed, graph.directed)
                self.assertEqual(edges, graph.edges_list)
                self.assertEqual(nodes, graph.nodes_list)
            else:
                raise graph[1]  # returned tuple(False, exception)


if __name__ == '__main__':
    unittest.main()