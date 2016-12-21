from graphClasses import *

if __name__ == '__main__':
    graph = Graph.read_from_file("./superGraph.txt")
    task_node_id = 6
    task_node = graph.get_node_by_id(task_node_id)
    adjacency_nodes = graph.get_adjacency_list(task_node)
    adjacency_edges = []
    for edge in graph._edges_list:
        if (edge.node_in==task_node or edge.node_out == task_node):
            adjacency_edges.append(edge)
    print(sorted(adjacency_edges, key=lambda edge: edge.edge_weight, reverse=True)[0])
    input()

