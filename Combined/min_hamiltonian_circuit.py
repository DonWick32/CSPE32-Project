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
        print(start, end = ' ')
        self.visited[start] = True
        for i in range(self.m_num_of_nodes):
            if (self.mst_adj[start][i] !=0 and (not self.visited[i])):
                self.DFS(i)

    def DFS_Random(self):
        temp = [i for i in range(1, self.m_num_of_nodes)]
        random.shuffle(temp)
        self.dfs_sequence = list(temp)
        self.dfs_sequence.insert(0, 0)
        # temp = temp.reverse()
        # temp.append(0)
        # temp = temp.reverse()
        # self.dfs_sequence = temp
    
    def Cost_Calculation(self):
        for i in range(self.m_num_of_nodes - 1):
            self.ham_cost += self.m_adj_matrix[self.dfs_sequence[i]][self.dfs_sequence[i+1]]
        self.ham_cost += self.m_adj_matrix[self.dfs_sequence[-1]][self.dfs_sequence[0]]
        


# n = int(input("Number of vertices: "))
# graph = Graph(n)

# for i in range(n):
#     for j in range(n):
#         if (j != i and graph.m_adj_matrix[i][j] == 0):
#             for k in range(n):
#                 if (graph.m_adj_matrix[i][k] != 0):
#                     if (graph.m_adj_matrix[k][j] != 0):
#                         graph.m_adj_matrix[i][j] = max(int(math.ceil(math.sqrt(graph.m_adj_matrix[i][k]**2 + graph.m_adj_matrix[k][j]**2))), graph.m_adj_matrix[i][j])
#                     else:
#                         graph.m_adj_matrix[i][j] = max(random.randint(0, n*n), graph.m_adj_matrix[i][j])
#                 else:
#                     graph.m_adj_matrix[i][j] = max(random.randint(0, n*n), graph.m_adj_matrix[i][j])
#         graph.m_adj_matrix[j][i] = graph.m_adj_matrix[i][j]

# graph.print_adj_matrix()
# graph.primMST()
# graph.DFS_Random()
# print(graph.dfs_sequence)
# graph.Cost_Calculation()
# print(graph.ham_cost)

v = []
t = []

for n in range(1, 100):

    start = timer()
    graph = Graph(n)

    for i in range(n):
        for j in range(n):
            if (j != i and graph.m_adj_matrix[i][j] == 0):
                for k in range(n):
                    if (graph.m_adj_matrix[i][k] != 0):
                        if (graph.m_adj_matrix[k][j] != 0):
                            graph.m_adj_matrix[i][j] = max(int(math.ceil(math.sqrt(graph.m_adj_matrix[i][k]**2 + graph.m_adj_matrix[k][j]**2))), graph.m_adj_matrix[i][j])
                        else:
                            graph.m_adj_matrix[i][j] = max(random.randint(j, n*n), graph.m_adj_matrix[i][j])
                    else:
                        graph.m_adj_matrix[i][j] = max(random.randint(j, n*n), graph.m_adj_matrix[i][j])
            graph.m_adj_matrix[j][i] = graph.m_adj_matrix[i][j]
    
    graph.primMST()
    graph.DFS_Random()
    print(graph.dfs_sequence)
    graph.Cost_Calculation()
    end = timer()
    v.append(n)
    t.append(end-start)
    print(f"{n} -> {end-start}")

plt.plot(v,t)
# x_cords = range(1,100)
# y_cords = [x*math.log2(x)/10000 for x in x_cords]
# plt.plot(x_cords, y_cords)
plt.xlabel("Number of Vertices")
plt.ylabel("Time Taken (in seconds)")
plt.title("Time Taken for generating minimum Hamiltonian Circuit")
plt.show()

