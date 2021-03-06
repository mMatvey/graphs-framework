from graphClasses import *


class GraphLib:
    def __init__(self):
        self.graph_file_data = []
        self.matrix_adjacency = []
        self.adjacency_list = {}

    def read_graph(self, file_path):
        """
        Читаем данные из файла
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
    wtf = Graph.read_graph_console_input()
    print(str(wtf))
    wtf.write_to_file('./superGraph.txt')
    #input()
   # A = GraphLib()
   # A.read_graph('./graph3.txt')
   # A.convert_to_adjacency_list()
    #print(A.dfs(A.prepare_to_traversal(A.adjacency_list), 5))
    #print(A.dfs(A.prepare_to_traversal(A.adjacency_list), 1))

#сохранение в файл
#матрица смежности, список смежности, список инцидентности
#удаление/добавление вершин/ребер
#DFS/BFS
#связность графа
#максимальная степень вершины
#изоморфизм
#преобразование(сведение) любой из графов свести к обычному графу
#обход всех вершин\ребер
#отсортировать ребра во взвешенном графе
