class Graph:
    def __init__(self, directed=False, nodes_list=[], edges_list=[] ):
        """
        :param nodes_list: список узлов [Node, Node, ...]
        :param edges_list: список рёбер [Edge, Edge, ...]
        :param directed: Ориентирован ли граф [True, False]
        """
        self.edges_list = edges_list
        self.nodes_list = nodes_list
        self.directed = directed

    def __str__(self):
        nodes_string = ""
        for node in self.nodes_list:
            nodes_string += str(node) + " "
        edges_string = ""
        for edge in self.edges_list:
            edges_string += str(edge) + " "
        return "Directed?: " + str(self.directed) + '\n' \
                + "Nodes: " + nodes_string + '\n' \
                + "Edges: " + edges_string

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


class Edge:

    def __init__(self, node_in, node_out, weight=None):
        """
        :param node_in:  в которое входит ребро
        :param node_out: из которого выходит ребро
        :return:
        """
        self.node_in = node_in
        self.node_out = node_out
        self.edge_weight = weight

    def __str__(self):
        return str(self.node_in) + ", " + str(self.node_out) + " "

    def __key(self):
        return tuple(self.__dict__.values())

    def __eq__(x, y):
        return x.__key() == y.__key()

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

    def __eq__(x, y):
        return x.__key() == y.__key()

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
#не справился
    def adjacency_list(self, graph):
        adj = []
        for i in graph.edges_list:
            if (i.incidence_to_node(i.node_in) and i.incidence_to_node(i.node_out)):
                adj.append(i.node_out)
        return adj


class GraphLib:
    def __init__(self):
        self.graph_file_data = []
        self.matrix_adjacency = []
        self.adjacency_list = {}

    @classmethod
    def read_graph_console_input(cls):
        """
        После диалога с пользователем возвращает заданным им граф
        :return: new Graph object
        """
        directed_line = input("Граф ориентированный?(пустая строка - нет): ")
        nodes_line = input("Введити номера узлов через пробел: ")
        edges_line = input("Введити рёбра( node1,node2 node3,node4): ")
        return GraphLib.create_graph_from_strings(directed_line, nodes_line, edges_line)

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
            [node for node in nodes_list if node.node_id == node_id]
        for pair in edges_line.split():
            first_node_id, second_node_id = map(int, pair.split(","))
            edges.append(Edge(get_node_by_id(first_node_id, nodes),
                              get_node_by_id(second_node_id, nodes)))
        return Graph(directed, nodes, edges)

    def read_graph(self, file_path):
        """
        Читаем данные из файла
        ----------
          Пример:
        ----------
        >>> a = GraphLib()
        >>> A.read_graph('./graph3.txt')
        ----------
        :param file_path: путь к файлу, из которого читаем данные
        :return:
        """
        with open(file_path, "r") as file:
            data = ''
            for line in file:
                data += line
            self.graph_file_data = data.splitlines()
            file.close()

    def convert_to_adjacency_matrix(self):
        """
        Заполняем матрицу смежности,
        если загрузили из файла матрицу смежности
        ----------
          Пример:
        ----------
        >>> a = GraphLib()
        >>> A.read_graph('./graph1.txt')
        >>> A.convert_to_adjacency_matrix()
        >>> print(A.matrix_adjacency)
        ----------
        :return:
        """
        for i in range(len(self.graph_file_data)):
            self.matrix_adjacency.append(list(self.graph_file_data[i]))
        for i in range(len(self.matrix_adjacency)):
            for j in range(len(self.matrix_adjacency[i])):
                self.matrix_adjacency[i][j] = int(self.matrix_adjacency[i][j])

    def convert_to_adjacency_list(self):
        """
        Заполняем список смежности,
        если загрузили из файла список смежности
        ----------
          Пример:
        ----------
        >>> a = GraphLib()
        >>> A.read_graph('./graph3.txt')
        >>> A.convert_to_adjacency_list()
        ----------
        :return:
        """
        for i in range(len(self.graph_file_data)):
            god_bless_us = []
            self.adjacency_list[int(self.graph_file_data[i][0][0])] = \
            list(self.graph_file_data[i][2:])
            for j in range(len(self.adjacency_list[i])):
                god_bless_us.append(int(self.adjacency_list[i][j]))
            self.adjacency_list[i] = god_bless_us

    def convert_from_matrix_to_adjacency_list(self):
        """
        Преобразование из матрицы, которая хранится в файле, в список
        Предварительно необходимо прочитать файл
        ----------
          Пример:
        ----------
        >>> a = GraphLib()
        >>> A.read_graph('./graph3.txt')
        >>> A.convert_to_adjacency_matrix()
        ----------
        :return:
        """
        for i, c in enumerate(self.graph_file_data):
            adj_vert = []
            vert = self.graph_file_data[i]
            for j, key in enumerate(vert):
                if key == '1':
                    adj_vert.append(j)
            self.adjacency_list[i] = adj_vert

    def convert_from_list_to_adjacency_matrix(self):
        """
        Преобразование из списка, который хранится в файле, в матрицу
        Предварительно необходимо прочитать файл
        ----------
          Пример:
        ----------
        >>> a = GraphLib()
        >>> A.read_graph('./graph3.txt')
        >>> A.convert_to_adjacency_matrix()
        ----------
        :return:
        """
        graph_len = len(self.graph_file_data)
        for i in range(graph_len):
            row = self.graph_file_data[i].split()[1]
            adjs = [
                1 if i in [int(v) for v in row]
                else 0
                for i in range(graph_len)
            ]
            self.matrix_adjacency.append(adjs)

    def save_in_file_matrix_view(self, file_path):
        """
        Сохраняем в файл матрицу смежности
        ----------
          Пример:
        ----------
        >>> A.save_in_file_matrix_view('./graph2.txt')
        ----------
        :param file_path: путь к файлу, в который сохраняем
        :return:
        """

        vert = ''
        for i in range(len(self.matrix_adjacency)):
            asd = str(self.matrix_adjacency[i]).replace('[', '')
            asd = asd.replace(',', '')
            asd = asd.replace(']', '')
            asd = asd.replace(' ', '')
            jesus = ''.join(asd)
            vert += jesus + '\n'
        with open(file_path, "w") as file:
            file.write(vert)
        file.close()

    def save_in_file_list_view(self, file_path):
        """
         Сохраняем в файл список смежности
        ----------
          Пример:
        ----------
        >>> A.save_in_file_list_view('./graph2.txt')
        ----------
        :param file_path: путь к файлу, в который сохраняем
        :return:
        """
        items = list(self.adjacency_list.items())
        with open(file_path, "w") as f:
            for i in range(len(self.adjacency_list)):
                key = str(items[i][0])
                value = str(items[i][1]).replace('[', '')
                value = value.replace(',', '')
                value = value.replace(']', '')
                value = value.replace(' ', '')
                f.write(key + ' ' + value + '\n')
        f.close()

    def add_vertex_in_matrix(self):
        """
        Добавляем вершину в матрицу смежности
        ----------
          Пример:
        ----------
        >>> A.add_vertex_in_matrix()
        ----------
        :return:
        """
        if self.matrix_adjacency:
            for i, key in enumerate(self.matrix_adjacency):
                key.append(0)
            vert = []
            for i in range(len(self.matrix_adjacency) + 1):
                vert.append(0)
            self.matrix_adjacency.append(vert)

    def add_vertex_in_list(self):
        """
        Добавляем вершину в список смежности
        ----------
          Пример:
        ----------
        >>> A.add_vertex_in_list()
        ----------
        :return:
        """
        if self.adjacency_list:
            self.adjacency_list[len(self.adjacency_list)] = []

    def delete_vertex_from_list(self, num_vertex):
        """
        Удаляем вершину из списка смежности
        ----------
          Пример:
        ----------
        >>> A.delete_vertex_from_list(3)
        ----------
        :param num_vertex: номер вершины, которую удаляем
        :return:
        """
        del self.adjacency_list[num_vertex]
        for i in self.adjacency_list:
            if num_vertex in self.adjacency_list[i]:
                self.adjacency_list[i].remove(num_vertex)

    def delete_vertex_from_matrix(self, num_vertex):
        """
        Удаляем вершину из списка смежности

        num_vertex - номер вершины, которую удаляем
        ----------
          Пример:
        ----------
        >>> A.delete_vertex_from_list(3)
        ----------
        """
        del self.matrix_adjacency[num_vertex]
        for i in range(len(self.matrix_adjacency)):
            del self.matrix_adjacency[i][num_vertex]
        # doesn't work currently yet
    def graph_to_matrix(self):
        """
        Получаем из списка смежности матрицу смежности

        num_vertex - номер вершины, которую удаляем
        ----------
          Пример:
        ----------
        >>> A.convert_to_matrix()
        ----------
        """
        self.matrix_adjacency = []
        graph_len = len(self.adjacency_list)
        for i in range(graph_len):
            row = self.adjacency_list[i]
            adjs = [
                1 if i in [int(v) for v in row]
                else 0
                for i in range(graph_len)
            ]
            self.matrix_adjacency.append(adjs)
        return self.matrix_adjacency
    def graph_to_list(self):
        """
        Получаем из списка смежности матрицу смежности

        num_vertex - номер вершины, которую удаляем
        ----------
          Пример:
        ----------
        >>> A.graph_to_list()
        ----------
        """
        self.adjacency_list = {}

        graph_len = len(self.matrix_adjacency)
        for i in range(graph_len):
            adjs = []
            row = self.matrix_adjacency[i]
            for v in range(graph_len):
                if row[v] == 1:
                    adjs.append(v)
            self.adjacency_list[i] = adjs
        return self.adjacency_list
    @classmethod
    def prepare_to_traversal(cls, graph):
        """
        :param graph: список смежности
        :return sets: множество, равное списку смежности:
        """
        sets = {}
        for i in graph:
            sets[i] = set(graph[i])
        return sets
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

#A = GraphLib()
#A.read_graph('./graph1.txt')
#A.convert_to_adjacency_matrix()
#print(A.graph_file_data)
#print(A.matrix_adjacency)
#A.convert_from_matrix_to_adjacency_list()
#print(A.adjacency_list)
#A.save_in_file_matrix_view('./graph2.txt')
#A.convert_to_adjacency_list()
#A.save_in_file_list_view('./graph2.txt')
#print(A.adjacency_list)
#A.convert_from_list_to_adjacency_matrix()
#A.add_vertex_in_matrix()
#A.add_vertex_in_list()
#A.delete_vertex_from_list(4)

#A.delete_vertex_from_matrix(4)
#print(A.graph_to_matrix())
#print(A.graph_to_list())
if __name__ == '__main__':
    wtf = GraphLib.read_graph_console_input()
    print(str(wtf))
    input()
    #A = GraphLib()
    #A.read_graph('./graph3.txt')
    #A.convert_to_adjacency_list()
    #print(A.dfs(A.prepare_to_traversal(A.adjacency_list), 5))
    #print(A.dfs(A.prepare_to_traversal(A.adjacency_list), 1))
#графы оргафы 
#сохранение в файл
#матрица смежности, список смежности, список инцидентности
#удаление/добавление вершин/ребер
#DFS/BFS
#связность графа
#максимальная степень вершины
#изоморфизм
#преобразование(сведение) любой из графов свести к обычному графу
#список вершин, список ребер
#обход всех вершин\ребер
#отсортировать ребра во взвешенном графе
