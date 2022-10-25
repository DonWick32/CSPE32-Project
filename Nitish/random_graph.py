import random

class Graph:
    def __init__(self, num_of_nodes, directed = False):
        self.m_num_of_nodes = num_of_nodes
        self.m_directed = directed

        self.m_adj_matrix = [[0 for column in range(num_of_nodes)]
                             for row in range(num_of_nodes)]

    def add_edge(self, node1, node2, weight=1):
        self.m_adj_matrix[node1][node2] = weight

        if not self.m_directed:
            self.m_adj_matrix[node2][node1] = weight

    def print_adj_matrix(self):
        for i in self.m_adj_matrix:
            print(i)


n = int(input("Number of vertices: "))
graph = Graph(n)

offset = random.randint(1, 100)

for i in range(n):
    for j in range(n):
        if (graph.m_adj_matrix[j][i] != 0):
            graph.m_adj_matrix[i][j] = graph.m_adj_matrix[j][i]
        elif (i != j):
            graph.add_edge(i, j, abs(i-j) + offset)

graph.print_adj_matrix()
