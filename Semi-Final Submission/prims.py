import random
import sys
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

class Graph:

    def __init__(self, num_of_nodes):
        self.m_num_of_nodes = num_of_nodes
        self.m_adj_matrix = [[0 for column in range(num_of_nodes)]
                             for row in range(num_of_nodes)]
        self.m_prims_mst = [[0 for column in range(num_of_nodes)]
                             for row in range(num_of_nodes)]       

    def add_edge(self, node1, node2, weight=1):
        self.m_adj_matrix[node1][node2] = weight
        self.m_adj_matrix[node2][node1] = weight            

    def print_adj_matrix(self):
        for i in self.m_adj_matrix:
            print(i)

    def printMST(self, parent):
        print("Edge \tWeight")
        for i in range(1, self.m_num_of_nodes):
            print(parent[i], "-", i, "\t", self.m_adj_matrix[i][parent[i]])
            self.m_prims_mst[parent[i]][i] = self.m_prims_mst[i][parent[i]]= self.m_adj_matrix[i][parent[i]]

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


n = int(input("Number of vertices: "))
graph = Graph(n)

for i in range(n):
    for j in range(n):
        if (graph.m_adj_matrix[j][i] != 0):
            graph.m_adj_matrix[i][j] = graph.m_adj_matrix[j][i]
        elif (i != j):
            graph.add_edge(i, j, random.randint(1,n*n))

graph.print_adj_matrix()
graph.primMST()
G = nx.from_numpy_matrix(np.matrix(graph.m_prims_mst))
plt.subplot(222)
layout = nx.circular_layout(G, graph.m_num_of_nodes**3)
plt.title("Minimum Spanning Tree using Prims's Algorithm")
nx.draw(G, layout, node_size = 500, with_labels = True, font_weight='bold', font_size=15)
labels = nx.get_edge_attributes(G,'weight')
nx.draw_networkx_edge_labels(G, pos = layout, edge_labels=labels)
G = nx.from_numpy_matrix(np.matrix(graph.m_adj_matrix))
plt.subplot(221)
layout = nx.circular_layout(G, graph.m_num_of_nodes**3)
plt.title(f"Complete Graph with {graph.m_num_of_nodes} vertices")
nx.draw(G, layout, node_size = 500, with_labels = True, font_weight='bold', font_size=15)
labels = nx.get_edge_attributes(G,'weight')
nx.draw_networkx_edge_labels(G, pos = layout, edge_labels=labels)
plt.show()
