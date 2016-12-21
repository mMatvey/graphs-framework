from random import randint
from graphClasses import *


def generate_graph():
    """
    create graph with random nodes, edges, directed
    :return: random graph
    """
    directed, nodes, edges = generate_random_params()
    return Graph(directed, nodes, edges)


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


if __name__ == '__main__':
    pass