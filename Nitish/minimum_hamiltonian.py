# A class to represent a graph object
# class Graph:
 
#     # Constructor
#     def __init__(self, edges, n):
 
#         # A list of lists to represent an adjacency list
#         self.adjList = [[] for _ in range(n)]
 
#         # add edges to the undirected graph
#         for (src, dest) in edges:
#             self.adjList[src].append(dest)
#             self.adjList[dest].append(src)

import random

cost = 0
temp = 0

class Graph:
    def __init__(self, num_of_nodes, directed = False):
        self.m_num_of_nodes = num_of_nodes
        self.m_directed = directed
        self.minTotalCost = 0

        self.m_adj_matrix = [[0 for column in range(num_of_nodes)]
                             for row in range(num_of_nodes)]

    def add_edge(self, node1, node2, weight=1):
        self.m_adj_matrix[node1][node2] = weight

        if not self.m_directed:
            self.m_adj_matrix[node2][node1] = weight

    def print_adj_matrix(self):
        for i in self.m_adj_matrix:
            print(i)
 
 
    def hamiltonianPaths(graph, v, visited, path, n):
        global minCost
        minCost = temp
    
        # if all the vertices are visited, then the Hamiltonian path exists
        if len(path) == n:
            # print the Hamiltonian path
            print(path)
            total = sum(path)
            if (total < minCost):
                minCost = total
                cost = total
            return
    
        # Check if every edge starting from vertex `v` leads to a solution or not
        for w in range (len(graph.m_adj_matrix[v])):
    
            # process only unvisited vertices as the Hamiltonian
            # path visit each vertex exactly once
            if not visited[w]:
                visited[w] = True
                path.append(w)
    
                # check if adding vertex `w` to the path leads to the solution or not
                graph.hamiltonianPaths(graph, w, visited, path, n)
    
                # backtrack
                visited[w] = False
                path.pop()
 
 
    def findHamiltonianPaths(graph, n):
    
        # start with every node
        for start in range(n):
    
            # add starting node to the path
            path = [start]
        
            # mark the start node as visited
            visited = [False] * n
            visited[start] = True
        
            graph.hamiltonianPaths(graph, start, visited, path, n)
 
n = int(input("Number of vertices: "))
graph = Graph(n)

# offset = random.randint(1, n*n)

for i in range(n):
    for j in range(n):
        if (graph.m_adj_matrix[j][i] != 0):
            graph.m_adj_matrix[i][j] = graph.m_adj_matrix[j][i]
        elif (i != j):
            # graph.add_edge(i, j, abs(i-j) + offset)
            graph.add_edge(i, j, random.randint(1,n))

graph.print_adj_matrix()

print("Minimum cost = ", cost)