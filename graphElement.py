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