class Graph:
    def __init__(self, directed=False):
        self.edges_list = []
        self.nodes_list = []
        self.directed = directed


class Edge:
    def __init__(self, node_in, node_out):
        self.node_in = node_in
        self.node_out = node_out
        self.weight = 0


class Node:
    def __init__(self, node_id):
        self.node_id = node_id


class GraphLib:
    def __init__(self):
        self.graph_file_data = []
        self.matrix_adjacency = []
        self.adjacency_list = {}

    def read_graph(self, file_path):
        """
        Читаем данные из файла
        ----------
          Пример:
        ----------
        >>> a = GraphLib()
        >>> a.read_graph('./graph3.txt')
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
        >>> a.read_graph('./graph1.txt')
        >>> a.convert_to_adjacency_matrix()
        >>> print(a.matrix_adjacency)
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
        >>> a.read_graph('./graph3.txt')
        >>> a.convert_to_adjacency_list()
        ----------
        :return:
        """
        for i in range(len(self.graph_file_data)):
            god_bless_us = []
            self.adjacency_list[int(self.graph_file_data[i][0][0])] = list(self.graph_file_data[i][2:])
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
        >>> a.read_graph('./graph3.txt')
        >>> a.convert_to_adjacency_matrix()
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
        >>> a.read_graph('./graph3.txt')
        >>> a.convert_to_adjacency_matrix()
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
        Аргументы:
        ----------
        ----------
          Пример:
        ----------
        >>> a.save_in_file_matrix_view('./graph2.txt')
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
        >>> a.save_in_file_list_view('./graph2.txt')
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
        >>> a.add_vertex_in_matrix()
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
        >>> a.add_vertex_in_list()
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
        >>> a.delete_vertex_from_list(3)
        ----------
        :param num_vertex: номер вершины, которую удаляем
        :return:
        """
        for i, key in enumerate(self.adjacency_list):
            for j in range(len(self.adjacency_list[i])):
                if num_vertex == self.adjacency_list[i][j]:
                    del self.adjacency_list[i][j]
                    break
        del self.adjacency_list[num_vertex]

    # def delete_vertex_from_matrix(self, num_vertex):
        '''
        Удаляем вершину из списка смежности

        ----------
        Аргументы:
        ----------
        num_vertex - номер вершины, которую удаляем
        ----------
          Пример:
        ----------
        >>> a.delete_vertex_from_list(3)
        ----------
        '''




a = GraphLib()
a.read_graph('./graph1.txt')
a.convert_to_adjacency_matrix()
#print(a.graph_file_data)
#print(a.matrix_adjacency)
a.convert_from_matrix_to_adjacency_list()
#print(a.adjacency_list)
#a.save_in_file_matrix_view('./graph2.txt')
#a.convert_to_adjacency_list()
#a.save_in_file_list_view('./graph2.txt')
#print(a.adjacency_list)
#a.convert_from_list_to_adjacency_matrix()
a.add_vertex_in_matrix()
a.add_vertex_in_list()
a.delete_vertex_from_list(4)


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
