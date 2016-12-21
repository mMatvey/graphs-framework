#from graph import GraphLib
from graphExceptions import *


class Graph:

    def __init__(self, directed=False, nodes_list=[], edges_list=[]):
        """
        :param nodes_list: список узлов [Node, Node, ...]
        :param edges_list: список рёбер [Edge, Edge, ...]
        :param directed: Ориентирован ли граф [True, False]
        """
        self.directed = directed
        self._nodes_list = nodes_list
        check_ids = self.__check_uniques_nodes_ids__()
        if check_ids:
            raise GraphCreationException("Вершины графа имеют неуникальный идентификатор: " +
                                         str(check_ids))
        self._edges_list = edges_list

    def __check_uniques_nodes_ids__(self):
        """
        Проверка, есть ли повторяющиеся id среди вершин графа
        если есть - возвращает его идентификатор
        :return: повторяющийся id вершины,
        если нет повторов - False
        """
        uniq_nodes = set()
        for node in self._nodes_list:
            if node in uniq_nodes:
                return node.node_id
            else:
                uniq_nodes.add(node)
        return 0

    def get_sorted_edges(self, key_func=False, reversed=False):
        """
        Возвращает отсортированный по возврастанию веса
        список рёбер(если key не указан)
        :param key_func: функция, принимающая каждое ребро
         и возвращающая ключ для сравнения (см default ниже)
         :param reversed: развернуть порядок следования
        :return: list(Edge Edge Edge)
        """
        default_key = lambda edge: edge.edge_weight  # вернуть вес переданного ребра
        if not key_func:
            return sorted(self._edges_list, key=default_key, reverse=reversed)
        else:
            return sorted(self._edges_list, key=key_func, reverse=reversed)

    def add_node(self, node):
        """
        Необходимо добавлять вершины через этот метод!
        чтобы избежать повторов индификаторов
        :param node:
        """
        self._nodes_list.append(node)
        check_ids = self.__check_uniques_nodes_ids__()
        if check_ids:
            raise GraphException("Индификатор уже занят: " + str(node))

    def add_edge(self, edge):
        """
        Добавляет ребро в список рёбер графа
        :param edge:
        :return:
        """
        self._edges_list.append(edge)
        self._edges_list = set(self._edges_list)  # избавляемся
        self._edges_list = list(self._edges_list)  # от одинаковых рёбер

    def remove_edge(self, edge):
        """
        Удаляет ребро из списка рёбер
        :param edge:
        """
        self._edges_list.remove(edge)

    def get_edge_by_params(self, node_out, node_in, weight=0):
        """
        Возвращает ребро по известным вершинам и весу
        :param node_out: вершина, из которой исходит ребро
        :param node_in: вершина, в которую входит ребро
        :param weight: вес ребра
        :return: Edge
        """
        return Edge(node_out=node_out, node_in=node_in, weight=weight)

    def get_edge_by_ids(self, node_out_id, node_in_id, weight=0):
        """
        Возвращает ребро по индфикаторам вершин и весу
        :param node_out_id: индификатор вершины, из которой исходит ребро
        :param node_in_id: индификатор вершины, в которую исходит ребро
        :param weight: вес ребра
        """
        return self.get_edge_by_params(Node(node_out_id),
                                       Node(node_in_id),
                                       weight=weight)

    def remove_node(self, node):
        """
        Удаляет вершину из списка и все инцидетные рёбра
        :param node:
        """
        edges_to_remove = []
        for edge in self._edges_list:
            if edge.incidence_to_node(node):
                edges_to_remove.append(edge)
        self._nodes_list.remove(node)
        for edge in edges_to_remove:
            self.remove_edge(edge)

    def remove_node_by_id(self, node_id):
        """
        Удалят вершину из списку и все инцидентные рёбра
        :param node_id: индиикатор вершины
        """
        self.remove_node(self.get_node_by_id(node_id))

    def nodes_to_string(self):
        """
        Возвращает строку - id вершин через пробелы
        :return: string: Node_id Node_id Node_id
        """
        nodes_string = ""
        for node in self._nodes_list:
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
        for edge in self._edges_list:
            edges_string += str(edge) + " "
        return edges_string

    def __str__(self):
        return "Directed?: " + str(self.directed) + '\n' \
            + "Nodes: " + self.nodes_to_string() + '\n' \
            + "Edges: " + self.edges_to_string()

    def get_list(self):
        """
        Получаем список смежности для обхода
        """
        adj_list = {}
        for i in range(len(self._nodes_list)):
            adj_list[i] = self.get_adjacency_list_by_id(i+1)
        for i in range(len(self._nodes_list)):
            for j in range(len(adj_list[i])):
                adj_list[i][j] = adj_list[i][j].node_id - 1
        for i in range(len(self._nodes_list)):
            adj_list[i] = set(adj_list[i])
        return adj_list

    def get_adjacency_list(self, node):
        """
        Получить список смежных вершин для переданной вершины
        в текущем графе
        :param node: Node
        :return: [Node, Node, Node]
        """
        adj = []
        for edge in self._edges_list:
            incidence_to_edge = node.incidence_to_edge(edge)
            if incidence_to_edge:
                adj.append(edge.node_in if incidence_to_edge == -1
                           else edge.node_out)
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
        return [node for node in self._nodes_list
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

    def read_file(self, file_path):
        """
        Читает информацию из файла
        """
        graph_file_data = []
        with open(file_path, "r") as file:
            data = ''
            for line in file:
                data += line
            graph_file_data = data.splitlines()
            file.close()
        for i, key in enumerate(graph_file_data):
            graph_file_data[i] = key.split(": ")[1]
        self.directed = graph_file_data[0]
        self.nodes_list.append(int(graph_file_data[1].split()))
        return graph_file_data

    @classmethod
    def dfs(cls, graph, start, visited=None):
        """
        :param graph: множество, равное списку смежности
        :param start: начало прохода
        :return visited: множество посещенных вершин
        """
        if visited is None:
            visited = set()
        visited.add(start)
        for next in graph[start] - visited:
            cls.dfs(graph, next, visited)
        return visited
    @classmethod
    def bfs(cls, graph, start):
        """
        :param graph: множество, равное списку смежности
        :param start: начало прохода
        :return visited: множество посещенных вершин
        """
        visited, queue = set(), [start]
        while queue:
            vertex = queue.pop(0)
            if vertex not in visited:
                visited.add(vertex)
                queue.extend(graph[vertex] - visited)
        return visited

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
        if self == edge.node_out:
            return -1
        elif self == edge.node_in:
            return 1
        else:
            return 0

class Matrix:
    def __init__(self, matrix=[]):
        self.matrix = matrix

    def print_matrix(self):
        #for i in range(len(self.matrix)):
        for row in self.matrix:
            print(row)
