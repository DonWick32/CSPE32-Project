import random
import sys
import math

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

    def printMST(self, parent):
        print("Edge \tWeight")
        for i in range(1, self.m_num_of_nodes):
            print(parent[i], "-", i, "\t", self.m_adj_matrix[i][parent[i]])

    # A utility function to find the vertex with
    # minimum distance value, from the set of vertices
    # not yet included in shortest path tree
    def minKey(self, key, mstSet):
 
        # Initialize min value
        min = sys.maxsize
 
        for v in range(self.m_num_of_nodes):
            if key[v] < min and mstSet[v] == False:
                min = key[v]
                min_index = v
 
        return min_index
 
    # Function to construct and print MST for a graph
    # represented using adjacency matrix representation
    def primMST(self):
 
        # Key values used to pick minimum weight edge in cut
        key = [sys.maxsize] * self.m_num_of_nodes
        parent = [None] * self.m_num_of_nodes  # Array to store constructed MST
        # Make key 0 so that this vertex is picked as first vertex
        key[0] = 0
        mstSet = [False] * self.m_num_of_nodes
 
        parent[0] = -1  # First node is always the root of
 
        for cout in range(self.m_num_of_nodes):
 
            # Pick the minimum distance vertex from
            # the set of vertices not yet processed.
            # u is always equal to src in first iteration
            u = self.minKey(key, mstSet)
 
            # Put the minimum distance vertex in
            # the shortest path tree
            mstSet[u] = True
 
            # Update dist value of the adjacent vertices
            # of the picked vertex only if the current
            # distance is greater than new distance and
            # the vertex in not in the shortest path tree
            for v in range(self.m_num_of_nodes):
 
                # graph[u][v] is non zero only for adjacent vertices of m
                # mstSet[v] is false for vertices not yet included in MST
                # Update the key only if graph[u][v] is smaller than key[v]
                if self.m_adj_matrix[u][v] > 0 and mstSet[v] == False and key[v] > self.m_adj_matrix[u][v]:
                    key[v] = self.m_adj_matrix[u][v]
                    parent[v] = u 
        self.printMST(parent)


n = int(input("Number of vertices: "))
graph = Graph(n)

offset = random.randint(1, n*n)

# for i in a:
#     for j in b:
#         if (j != i and graph.m_adj_matrix[i][j] == 0):
#             for k in c:
#                 if (graph.m_adj_matrix[i][k] != 0):
#                     if (graph.m_adj_matrix[k][j] != 0):
#                         graph.m_adj_matrix[i][j] = max(int(math.ceil(math.sqrt(graph.m_adj_matrix[i][k]**2 + graph.m_adj_matrix[k][j]**2))), graph.m_adj_matrix[i][j])
#                     else:
#                         graph.m_adj_matrix[i][j] = max(random.randint(0, n*n), graph.m_adj_matrix[i][j])
#                 else:
#                     graph.m_adj_matrix[i][j] = max(random.randint(0, n*n), graph.m_adj_matrix[i][j])
#         graph.m_adj_matrix[j][i] = graph.m_adj_matrix[i][j]


for i in range(n):
    for j in range(n):
        if (i != j):
            graph.m_adj_matrix[i][j] = math.ceil(math.sqrt((((i - j)*(math.gcd(i,j) + math.lcm(i, j)))**2)*2) * 100)

graph.print_adj_matrix()

graph.primMST()
