import random
import math
from re import M

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

def isSafe(v, graph, path, pos):
   
    # If the vertex is adjacent to
    # the vertex of the previously
    # added vertex
    if graph[path[pos - 1]][v] == 0:
        return False
 
    # If the vertex has already
    # been included in the path
    for i in range(pos):
        if path[i] == v:
            return False
 
    # Both the above conditions are
    # not true, return true
    return True
 
# To check if there exists
# at least 1 hamiltonian cycle
hasCycle = False
 
# Function to find all possible
# hamiltonian cycles
def hamCycle(graph):
    global hasCycle
     
    # Initially value of boolean
    # flag is false
    hasCycle = False
 
    # Store the resultant path
    path = []
    path.append(0)
 
    # Keeps the track of the
    # visited vertices
    visited = [False]*(len(graph))
 
    for i in range(len(visited)):
        visited[i] = False
 
    visited[0] = True
 
    # Function call to find all
    # hamiltonian cycles
    FindHamCycle(graph, 1, path, visited)
 
    if hasCycle:
        # If no Hamiltonian Cycle
        # is possible for the
        # given graph
        print("No Hamiltonian Cycle" + "possible ")
        return
 
# Recursive function to find all
# hamiltonian cycles
def FindHamCycle(graph, pos, path, visited):
   
    # If all vertices are included
    # in Hamiltonian Cycle
    if pos == len(graph):
       
        # If there is an edge
        # from the last vertex to
        # the source vertex
        if graph[path[-1]][path[0]] != 0:
           
            # Include source vertex
            # into the path and
            # print the path
            path.append(0)
            for i in range(len(path)):
                print(path[i], end = " ")
            print()
 
            # Remove the source
            # vertex added
            path.pop()
 
            # Update the hasCycle
            # as true
            hasCycle = True
        return
 
    # Try different vertices
    # as the next vertex
    for v in range(len(graph)):
       
        # Check if this vertex can
        # be added to Cycle
        if isSafe(v, graph, path, pos) and not visited[v]:
            path.append(v)
            visited[v] = True
 
            # Recur to construct
            # rest of the path
            FindHamCycle(graph, pos + 1, path, visited)
 
            # Remove current vertex
            # from path and process
            # other vertices
            visited[v] = False
            path.pop()

n = int(input("Number of vertices: "))
graph = Graph(n)

offset = random.randint(1, n)

for i in range(n):
    for j in range(n):
        if (graph.m_adj_matrix[j][i] != 0):
            graph.m_adj_matrix[i][j] = graph.m_adj_matrix[j][i]
        elif (i != j):
            graph.add_edge(i, j, abs(i-j) + offset)

graph.print_adj_matrix()

hamCycle(graph.m_adj_matrix)




