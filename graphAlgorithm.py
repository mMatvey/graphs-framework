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