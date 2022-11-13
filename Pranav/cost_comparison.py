import random
import math
import sys
import matplotlib.pyplot as plt
x1 = []
y1 = []
x2 = []
y2 = []


class Graph:
    def __init__(self, num_of_nodes):
        self.m_adj_matrix = [[0 for column in range(num_of_nodes)]
                             for row in range(num_of_nodes)]
        self.m_num_of_nodes = num_of_nodes
        self.visited = [0 for n in range(num_of_nodes)]
        self.graph = []
        self.dfs_sequence = []
        self.mst_adj = [[0 for column in range(num_of_nodes)]
                             for row in range(num_of_nodes)]
        self.ham_cost = 0
        self.mst_cost = 0

    def add_edge(self, node1, node2, weight=1):
        self.m_adj_matrix[node1][node2] = weight
        self.m_adj_matrix[node2][node1] = weight

    def print_adj_matrix(self):
        for i in self.m_adj_matrix:
            print(i)
            
    def costMST(self, parent):
        for i in range(1, self.m_num_of_nodes):
            #print(parent[i], "-", i, "\t", self.m_adj_matrix[i][parent[i]])
            self.mst_adj[parent[i]][i] = self.m_adj_matrix[i][parent[i]]
            self.mst_adj[i][parent[i]] = self.m_adj_matrix[i][parent[i]]
            self.mst_cost = self.mst_cost + self.m_adj_matrix[i][parent[i]]

    def minKey(self, key, mstSet):
        min = sys.maxsize
        for v in range(self.m_num_of_nodes):
            if key[v] < min and mstSet[v] == False:
                min = key[v]
                min_index = v

        return min_index

    def primMST(self):
        key = [sys.maxsize] * self.m_num_of_nodes
        parent = [None] * self.m_num_of_nodes
        key[0] = 0
        mstSet = [False] * self.m_num_of_nodes

        parent[0] = -1

        for cout in range(self.m_num_of_nodes):
            u = self.minKey(key, mstSet)
            mstSet[u] = True
            for v in range(self.m_num_of_nodes):
                if self.m_adj_matrix[u][v] > 0 and mstSet[v] == False and key[v] > self.m_adj_matrix[u][v]:
                    key[v] = self.m_adj_matrix[u][v]
                    parent[v] = u
        self.costMST(parent)

    def DFS(self, start):
        self.dfs_sequence.append(start)
        self.visited[start] = True
        for i in range(self.m_num_of_nodes):
            if (self.mst_adj[start][i] != 0 and (not self.visited[i])):
                self.DFS(i)

    def Cost_Calculation(self):
        for i in range(self.m_num_of_nodes - 1):
            self.ham_cost += self.m_adj_matrix[self.dfs_sequence[i]
                                               ][self.dfs_sequence[i+1]]
        self.ham_cost += self.m_adj_matrix[self.dfs_sequence[-1]
                                           ][self.dfs_sequence[0]]



for n in range(3, 100):
    x1.append(n)
    x2.append(n)
    a = random.randint(5,8)
    graph = Graph(n)
    for i in range(n):
        for j in range(n):
            if (i != j):
                graph.m_adj_matrix[i][j] = graph.m_adj_matrix[j][i] = random.randint(a,2*a-1)
    graph.print_adj_matrix()
    graph.primMST()
    graph.DFS(random.randint(0, n-1))
    #print(graph.dfs_sequence)
    graph.Cost_Calculation()
    y1.append(graph.ham_cost)
    y2.append(2*graph.mst_cost)


plt.plot(x1, y1, label="minimum hamilton cost")
plt.plot(x2, y2, label="2 x cost of MST")
plt.xlabel("Number of vertices")
plt.ylabel("Cost value")
plt.legend()
plt.show()
