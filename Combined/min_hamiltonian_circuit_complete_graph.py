import random
import sys

class Graph:
    def __init__(self, num_of_nodes):
        self.m_adj_matrix = [[0 for column in range(num_of_nodes)]
                             for row in range(num_of_nodes)]
        self.m_num_of_nodes = num_of_nodes
        self.list = []
        self.visited = [0 for n in range(num_of_nodes)]
        self.hasCycle = False
        self.count = 0
        self.val = sys.maxsize
        self.currcycle = [0] * self.m_num_of_nodes

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
        print("Hamiltonian cycle : ", end = "")
        for vertex in self.currcycle:
            print(vertex, end=" ")
        print(self.currcycle[0])
        print("Length = ",self.val)

    def print_adj_matrix(self):
        for i in self.m_adj_matrix:
            print(i)


n = int(input("Number of vertices: "))
graph = Graph(n)

for i in range(n):
    for j in range(n):
        if (graph.m_adj_matrix[j][i] != 0):
            graph.m_adj_matrix[i][j] = graph.m_adj_matrix[j][i]
        elif (i != j):
            graph.add_edge(i, j, random.randint(1,n*n))

graph.print_adj_matrix()
print("\n")
graph.hamCycle()
graph.printSolution()
