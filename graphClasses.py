from graph import GraphLib
from graphExceptions import *


class Graph:

    def __init__(self, directed=False, nodes_list=[], edges_list=[]):
        """
        :param nodes_list: список узлов [Node, Node, ...]
        :param edges_list: список рёбер [Edge, Edge, ...]
        :param directed: Ориентирован ли граф [True, False]
        """
        self.directed = directed
        self.nodes_list = nodes_list
        check_ids = self.__check_uniques_nodes_ids__()
        if check_ids:
            raise GraphCreationException("Вершины графа имеют неуникальный идентификатор: " +
                                         str(check_ids))
        self.edges_list = edges_list

    def __check_uniques_nodes_ids__(self):
        """
        Проверка, есть ли повторяющиеся id среди вершин графа
        если есть - возвращает его идентификатор
        :return: повторяющийся id вершины,
        если нет повторов - False
        """
        uniq_nodes = set()
        for node in self.nodes_list:
            if node in uniq_nodes:
                return node.node_id
            else:
                uniq_nodes.add(node)
        return 0

    def nodes_to_string(self):
        """
        Возвращает строку - id вершин через пробелы
        :return: string: Node_id Node_id Node_id
        """
        nodes_string = ""
        for node in self.nodes_list:
            nodes_string += str(node) + " "
        return nodes_string

    def edges_to_string(self):
        """
        Возвращает строку - рёбра в формате
        node_id_out,node_id_in:weight weight > 0
        node_id_out,node_id_in weight==0
        через пробел
        :return:str
        """
        edges_string = ""
        for edge in self.edges_list:
            edges_string += str(edge) + " "
        return edges_string

    def __str__(self):
        return "Directed?: " + str(self.directed) + '\n' \
            + "Nodes: " + self.nodes_to_string() + '\n' \
            + "Edges: " + self.edges_to_string()

    def get_matrix(self):
        """
        Получаем матрицу смежности
        """
        return GraphLib.graph_to_matrix(self)

    def get_list(self):
        """
        Получаем список смежности
        """
        return GraphLib.graph_to_list(self)

    def get_adjacency_list(self, node):
        """
        Получить список смежных вершин для переданной вершины
        в текущем графе
        :param node: Node
        :return: [Node, Node, Node]
        """
        adj = []
        for edge in self.edges_list:
            incidence_to_edge = node.incidence_to_edge(edge)
            if incidence_to_edge:
                adj.append(edge.node_out if incidence_to_edge == -1
                           else edge.node_in)
        return adj

    def adjacency_to_node(self, first_node, second_node):
        """
        Проверяеим являются ли переданные вершины смежными
        :param first_node: Node
        :param second_node: Node
        :return: True/False
        """
        return bool(second_node in self.get_adjacency_list(first_node))

    def get_node_by_id(self, node_id):
        """
        Возвращает вершину графу по переданному id
        :param node_id: переданный id
        :return: Node
        """
        return [node for node in self.nodes_list
                if node.node_id == node_id][0]

    def get_adjacency_list_by_id(self, node_id):
        """
        Список смежных вершин для вершины с переданным id
        в текущем графе
        :param node_id: id нужной вершины
        :return: list [Node Node Node]
        """
        return self.get_adjacency_list(self.get_node_by_id(node_id))

    def adjacency_to_node_by_id(self, first_node_id, second_node_id):
        """
        Проверка на смежность для вершин с переданным id в текущем графе
        :param first_node_id:
        :param second_node_id:
        :return: True\False
        """
        return self.get_node_by_id(first_node_id) in \
            self.get_adjacency_list_by_id(second_node_id)

    @classmethod
    def read_graph_console_input(cls):
        """
        После диалога с пользователем возвращает заданным им граф
        :return: new Graph object
        """
        directed_line = input("Граф ориентированный?(пустая строка - нет): ")
        nodes_line = input("Введити номера узлов через пробел: ")
        edges_line = input("Введити рёбра( node1,node2 node3,node4): ")
        return Graph.create_graph_from_strings(directed_line, nodes_line, edges_line)

    @classmethod
    def create_graph_from_strings(cls, directed_line, nodes_line, edges_line):
        """
        Создаёт граф на основе переданных строк с консоли или считанных из файла
        :rtype: Graph
        :param directed_line: Если пусто\0  - граф неориентированный
        :param nodes_line: формат "node_id1 node_id2 node_id3"
        :param edges_line: формат "node_id1,node_id2 node_id3,node_id4"
        :return: new Graph object
        """
        directed = bool(directed_line)
        nodes_ids = list(map(int, nodes_line.split()))  # from str to int
        nodes = []
        for node_id in nodes_ids:
            nodes.append(Node(node_id))
        edges = []
        get_node_by_id = lambda node_id, nodes_list: \
            [node for node in nodes_list if node.node_id == node_id][0]
        import re
        for pair in edges_line.split():  # dec,dec:dec
            weight = 0
            reg_expr = re.match(r'(\d+),(\d+):?(\d+)?', pair)
            first_node_id = int(reg_expr.group(1))
            second_node_id = int(reg_expr.group(2))
            if reg_expr.group(3):
                weight = int(reg_expr.group(3))
            edges.append(Edge(get_node_by_id(first_node_id, nodes),
                              get_node_by_id(second_node_id, nodes),
                              weight))
        return Graph(directed, nodes, edges)

<<<<<<< HEAD
    def _create_notDirectedGraph_string(self, nodes_line, edges_line, directed=False):
        """

        :param nodes_line:
        :param edges_line:
        :return:
        """
    def add_edge(self, node_in, node_out):
        """

        :param nodes_line:
        :param edges_line:
        :return:
        """
        

=======
>>>>>>> 89f0ff4d5c24b83b6a0528b72f68878d7e7f3422
class Edge:

    def __init__(self, node_out, node_in, weight=0):
        """
        :param node_in:  в которое входит ребро
        :param node_out: из которого выходит ребро
        :return:
        """
        self.node_in = node_in
        self.node_out = node_out
        self.edge_weight = weight
        if type(node_in) != type(node_out):
            raise EdgeCreationException("Вершины должны быть одного типа")

    def __str__(self):
        """
        Возвращает строку - рёбра в формате
        node_id_out,node_id_in:weight weight > 0
        node_id_out,node_id_in weight==0
        через пробел
        :return: string
        """
        weight_str = ""
        if self.edge_weight:
            weight_str = ":" + str(self.edge_weight)
        else:
            weight_str = ""
        return str(self.node_out) + "," + str(self.node_in) + weight_str

    def __key(self):
        return tuple(self.__dict__.values())

    def __eq__(self, other):
        return self.__key() == other.__key()

    def __hash__(self):
        return hash(self.__key())

    def incidence_to_node(self, node):
        """
        Проверяет на инцидентность данное ребро
        с переданной вершиной
        :param node: переданная вершина
        :return: -1 если этот узел - исток, 1 если сток, 0 если не инцидентно
        """
        return node.incidence_to_edge(self)


class Node:

    def __init__(self, node_id):
        self.node_id = node_id

    def __str__(self):
        return str(self.node_id)

    def __key(self):
        return tuple(self.__dict__.values())

    def __eq__(self, other):
        return self.__key() == other.__key()

    def __hash__(self):
        return hash(self.__key())

    def incidence_to_edge(self, edge):
        """
        Проверяет на инцидентность с ребром
        :param edge: ребро для проверки
        :return: -1 если этот узел - исток, 1 если сток, 0 если не инцидентно
        """
        if self == edge.node_in:
            return -1
        elif self == edge.node_out:
            return 1
        else:
            return 0