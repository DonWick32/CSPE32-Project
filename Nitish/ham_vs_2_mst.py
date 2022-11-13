import random
import sys
import math
from timeit import default_timer as timer
import matplotlib.pyplot as plt

class Graph:
    def __init__(self, num_of_nodes):
        self.m_num_of_nodes = num_of_nodes
        self.m_adj_matrix = [[0 for column in range(num_of_nodes)]
                             for row in range(num_of_nodes)]
        self.mst_adj = [[0 for column in range(num_of_nodes)]
                             for row in range(num_of_nodes)]
        self.visited = [False] * num_of_nodes
        self.dfs_sequence = []
        self.ham_cost = 0
        self.mst_cost = 0


    def add_edge(self, node1, node2, weight=1):
        self.m_adj_matrix[node1][node2] = weight
        self.m_adj_matrix[node2][node1] = weight            

    def print_adj_matrix(self):
        for i in self.m_adj_matrix:
            print(i)

    def printMST(self, parent):
        # print("Edge \tWeight")
        for i in range(1, self.m_num_of_nodes):
            # print(parent[i], "-", i, "\t", self.m_adj_matrix[i][parent[i]])
            self.mst_adj[parent[i]][i] = self.m_adj_matrix[i][parent[i]]
            self.mst_adj[i][parent[i]] = self.m_adj_matrix[i][parent[i]]
            self.mst_cost += self.m_adj_matrix[i][parent[i]]


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
        self.printMST(parent)

    def DFS(self, start):
        self.dfs_sequence.append(start)
        # print(start, end = ' ')
        self.visited[start] = True
        for i in range(self.m_num_of_nodes):
            if (self.mst_adj[start][i] !=0 and (not self.visited[i])):
                self.DFS(i)
        
    
    def Cost_Calculation(self):
        for i in range(self.m_num_of_nodes - 1):
            self.ham_cost += self.m_adj_matrix[self.dfs_sequence[i]][self.dfs_sequence[i+1]]
        self.ham_cost += self.m_adj_matrix[self.dfs_sequence[-1]][self.dfs_sequence[0]]

v = []
ham_cost = []
mst_cost = []

for n in range(1, 400):
    graph = Graph(n)

    for i in range(n):
        for j in range(n):
            if (i != j):
                # graph.m_adj_matrix[i][j] = graph.m_adj_matrix[j][i] = math.ceil(math.sqrt((((i - j)/(math.gcd(i,j) + math.lcm(i, j)) + i)**2)*2)*10)
                graph.m_adj_matrix[i][j]  = graph.m_adj_matrix[j][i] = math.ceil(math.sqrt(2*(((math.sqrt(i))-(math.sqrt(j)))**2)))

    graph.primMST()
    graph.DFS(random.randint(0, n-1))
    # print(graph.dfs_sequence)
    graph.Cost_Calculation()
    print(graph.ham_cost, graph.mst_cost)
    v.append(n)
    ham_cost.append(graph.ham_cost)
    mst_cost.append(2*graph.mst_cost)

plt.plot(v,ham_cost,label="Minimum Hamiltonian Cost")
plt.plot(v,mst_cost,label="2 x Cost of Minimum Spanning Tree")
plt.xlabel("Number of Vertices")
plt.ylabel("Total Cost")
plt.title("Cost Comparision")
plt.legend()
plt.show()

