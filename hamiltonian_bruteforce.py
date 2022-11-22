import random
import sys
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

class Graph:
    def __init__(self, num_of_nodes):
        self.m_adj_matrix = [[0 for column in range(num_of_nodes)]
                             for row in range(num_of_nodes)]
        self.m_num_of_nodes = num_of_nodes
        self.list = []
        self.visited = [0 for n in range(num_of_nodes)]
        self.visited_dfs = [0 for n in range(num_of_nodes)]
        self.dfs_sequence = []
        self.hasCycle = False
        self.count = 0
        self.val = sys.maxsize
        self.currcycle = [0] * self.m_num_of_nodes
        self.ham_circuit = []
        self.ham_matrix = [[0 for column in range(num_of_nodes)]
                             for row in range(num_of_nodes)]
        self.ham_cost = 0

    def add_edge(self, node1, node2, weight):
        self.m_adj_matrix[node1][node2] = weight
        self.m_adj_matrix[node2][node1] = weight

    def isSafe(self, v, pos, path):
        if self.m_adj_matrix[path[pos-1]][v] == 0:
            return False

        for vertex in path:
            if vertex == v:
                return False

        return True

    def hamCycleUtil(self, path, pos):
        if pos == self.m_num_of_nodes:
            if self.m_adj_matrix[path[pos-1]][path[0]] != 0:
                    value=0
                    path.append(0)
                    for i in range(len(path)-1):
                        value += self.m_adj_matrix[path[i]][path[i+1]]
                    if(value<self.val):
                        self.val=value
                        for j in range(len(path)-1):
                            self.currcycle[j]=path[j]
                    path.pop()
                    self.hasCycle = True
                    return

        for v in range(1, self.m_num_of_nodes):

            if (self.isSafe(v, pos, path) == True and self.visited[v] == False):

                path.append(v)
                self.visited[v] = True

                self.hamCycleUtil(path, pos+1)
                self.visited[v] = False
                path.pop()

        return False

    def hamCycle(self):
        path = [-1]
        path[0] = 0
        self.visited[0] = 1
        self.hamCycleUtil(path, 1)

    def printSolution(self):
        if(self.hasCycle == False):
            print("No Hamilton cycle possible!")
            return
        print("Minimum Hamiltonian cycle : ", end = "")
        for vertex in self.currcycle:
            print(vertex, end=" ")
            self.ham_circuit.append(vertex)
        print(self.currcycle[0])
        self.ham_circuit.append(self.currcycle[0])
        print("Total Length = ",self.val)
        for i in range(self.m_num_of_nodes):
            self.ham_matrix[self.ham_circuit[i]][self.ham_circuit[i+1]] = self.ham_matrix[self.ham_circuit[i+1]][self.ham_circuit[i]] = self.m_adj_matrix[self.ham_circuit[i]][self.ham_circuit[i+1]]

    def print_adj_matrix(self):
        for i in self.m_adj_matrix:
            print(i)

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

        vertices = list(range(self.m_num_of_nodes))
        random.shuffle(vertices)

        for i in vertices:
            if (self.mst_adj[start][i] != 0 and (not self.visited[i])):
                self.DFS(i)

    def Cost_Calculation(self):
        for i in range(self.m_num_of_nodes - 1):
            self.ham_cost += self.m_adj_matrix[self.dfs_sequence[i]
                                               ][self.dfs_sequence[i+1]]
        self.ham_cost += self.m_adj_matrix[self.dfs_sequence[-1]
                                           ][self.dfs_sequence[0]]

n = int(input("Enter number of vertices: "))
graph = Graph(n)

for i in range(n):
    for j in range(n):
        if (graph.m_adj_matrix[j][i] != 0):
            graph.m_adj_matrix[i][j] = graph.m_adj_matrix[j][i]
        elif (i != j):
            graph.add_edge(i, j, random.randint(1,n*n))

print()
print("The Adjacency Matrix of a randomly generated weighted complete graph:\n")
graph.print_adj_matrix()
print()
graph.hamCycle()
graph.printSolution()
print()

colors = ["#00CED1"]*(graph.m_num_of_nodes)

G = nx.from_numpy_matrix(np.matrix(graph.m_adj_matrix))
plt.subplot(121)
layout = nx.circular_layout(G, graph.m_num_of_nodes**3)
plt.title(f"Complete Graph with {graph.m_num_of_nodes} vertices")
nx.draw(G, layout, node_size = 500, with_labels = True, font_weight='bold', font_size=15, node_color=colors)
labels = nx.get_edge_attributes(G,'weight')
nx.draw_networkx_edge_labels(G, pos = layout, edge_labels=labels)

colors = ["#FF2800"]
colors.extend(["#00CED1"]*(graph.m_num_of_nodes - 1))

G = nx.from_numpy_matrix(np.matrix(graph.ham_matrix))
plt.subplot(122)
layout = nx.circular_layout(G, graph.m_num_of_nodes**3)
plt.title("Minimum Hamiltonian Cycle using Brute Force Approach")
nx.draw(G, layout, node_size = 500, with_labels = True, font_weight='bold', font_size=15, node_color=colors)
labels = nx.get_edge_attributes(G,'weight')
nx.draw_networkx_edge_labels(G, pos = layout, edge_labels=labels)
plt.show()
