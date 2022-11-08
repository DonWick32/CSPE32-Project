import random
import math

class Graph:
    def __init__(self, num_of_nodes):
        self.m_num_of_nodes = num_of_nodes
        self.m_adj_matrix = [[0 for column in range(num_of_nodes)]
                             for row in range(num_of_nodes)]

    def add_edge(self, node1, node2, weight=1):
        self.m_adj_matrix[node1][node2] = weight
        self.m_adj_matrix[node2][node1] = weight
            
    def print_adj_matrix(self):
        for i in self.m_adj_matrix:
            print(i)


n = int(input("Number of vertices: "))
graph = Graph(n)

for i in range(n):
    for j in range(n):
        if (j != i and graph.m_adj_matrix[i][j] == 0):
            for k in range(n):
                if (graph.m_adj_matrix[i][k] != 0):
                    if (graph.m_adj_matrix[k][j] != 0):
                        graph.m_adj_matrix[i][j] = max(int(math.ceil(math.sqrt(graph.m_adj_matrix[i][k]**2 + graph.m_adj_matrix[k][j]**2))), graph.m_adj_matrix[i][j])
                    else:
                        graph.m_adj_matrix[i][j] = max(random.randint(0, n), graph.m_adj_matrix[i][j])
                else:
                    graph.m_adj_matrix[i][j] = max(random.randint(0, n), graph.m_adj_matrix[i][j])
        graph.m_adj_matrix[j][i] = graph.m_adj_matrix[i][j]
        
graph.print_adj_matrix()
