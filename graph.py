import os

class GraphLib:
    def __init__(self):
        self.graph_file_data = []
        self.matrix_adjacency = []
        self.adjacency_list = {}
    def read_graph(self, file_path):
        '''
        Читаем данные из файла

        ----------
        Аргументы:
        ----------
        file_path - путь к файлу, из которого читаем данные
        ----------
          Пример:
        ----------
        >>> a = GraphLib()
        >>> a.read_graph('./graph3.txt')
        ----------
        '''
        with open(file_path, "r") as file:
            data = ''
            for line in file:
                data += line
            self.graph_file_data = data.splitlines()
            file.close()
        
    
    def convert_to_adjacency_matrix(self):
        '''
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
        '''
        for i in range(len(self.graph_file_data)):
            self.matrix_adjacency.append(list(self.graph_file_data[i]))
        for i in range(len(self.matrix_adjacency)):
            for j in range(len(self.matrix_adjacency[i])):
                self.matrix_adjacency[i][j] = int(self.matrix_adjacency[i][j])
    def convert_to_adjacency_list(self):
        '''
        Заполняем список смежности,
        если загрузили из файла список смежности

        ----------
          Пример:
        ----------
        >>> a = GraphLib()
        >>> a.read_graph('./graph3.txt')
        >>> a.convert_to_adjacency_list()
        ----------
        '''
        for i in range(len(self.graph_file_data)):
            god_bless_us = []
            self.adjacency_list[int(self.graph_file_data[i][0][0])] = \
            list(self.graph_file_data[i][2:])
            for j in range(len(self.adjacency_list[i])):
                god_bless_us.append(int(self.adjacency_list[i][j]))
            self.adjacency_list[i] = god_bless_us
    def convert_from_matrix_to_adjacency_list(self):
        '''
        Преобразование из матрицы, которая хранится в файле, в список
        Предварительно необходимо прочитать файл

        ----------
          Пример:
        ----------
        >>> a = GraphLib()
        >>> a.read_graph('./graph3.txt')
        >>> a.convert_to_adjacency_matrix()
        ----------
        '''
        for i in range(len(self.graph_file_data)):
            adj_vert = []
            vert = self.graph_file_data[i]
            for j in range(len(vert)):
                if vert[j] == '1':
                    adj_vert.append(j)
            self.adjacency_list[i] = adj_vert
    def convert_from_list_to_adjacency_matrix(self):
        '''
        Преобразование из списка, который хранится в файле, в матрицу
        Предварительно необходимо прочитать файл

        ----------
          Пример:
        ----------
        >>> a = GraphLib()
        >>> a.read_graph('./graph3.txt')
        >>> a.convert_to_adjacency_matrix()
        ----------
        '''
        graph_len = len(self.graph_file_data)
        for i in range(graph_len):
            row = self.graph_file_data[i].split()[1]
            adjs = [ 
                1 if i in [int(v) for v in row]
                else 0
                for i in range(graph_len)
            ]
            self.matrix_adjacency.append(adjs)
        asd = 1

#не работает
#почему меняется adj_vert?????????
    def save_in_file_matrix_view(self, file_path):
        '''
        Сохраняем в файл матрицу смежности

        ----------
        Аргументы:
        ----------
        file_path - путь к файлу, в который сохраняем
        ----------
          Пример:
        ----------
        >>> a.save_in_file_matrix_view('./graph2.txt')
        ----------
        '''
        vert = ''
        for i in range(len(self.matrix_adjacency)):
            asd = str(self.matrix_adjacency[i]).replace('[', '')
            asd = asd.replace(',', '')
            asd = asd.replace(']', '')
            asd = asd.replace(' ', '')
            jesus = ''.join(asd)
            vert += jesus + '\n'
        with open(file_path, "w") as f:
            f.write(vert)
        f.close()
    def save_in_file_list_view(self, file_path):
        '''
        Сохраняем в файл список смежности

        ----------
        Аргументы:
        ----------
        file_path - путь к файлу, в который сохраняем
        ----------
          Пример:
        ----------
        >>> a.save_in_file_list_view('./graph2.txt')
        ----------
        '''
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

class Graph:
    def __init__(self):
        self.edges_list
        self.numb_vertices
        self.numb_edges
        self.directed

class Edgenode:
    def __init__(self):
        self.adjancency
        self.weight
        self.next

a = GraphLib()
a.read_graph('./graph3.txt')
#a.convert_to_adjacency_matrix()
#print(a.graph_file_data)
#print(a.matrix_adjacency)
#a.convert_from_matrix_to_adjacency_list()
#print(a.adjacency_list)
#a.save_in_file_matrix_view('./graph2.txt')
#a.convert_to_adjacency_list()
#a.save_in_file_list_view('./graph2.txt')
#print(a.adjacency_list)
a.convert_from_list_to_adjacency_matrix()
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
