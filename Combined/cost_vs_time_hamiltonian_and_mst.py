import random
import math
import sys
import matplotlib.pyplot as plt
x1=[]
y1=[]
x2=[]
y2=[]
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
        self.graph = []
        self.currcycle = [0] * self.m_num_of_nodes

    def add_edge(self, node1, node2, weight):
        self.m_adj_matrix[node1][node2] = weight
        self.m_adj_matrix[node2][node1] = weight
        self.graph.append([node1,node2,weight])
        self.graph.append([node2,node1,weight])

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

    def Solution(self):
        if(self.hasCycle == False):
            print("No Hamilton cycle possible!")
            return 0
        #print("Minimum Hamilton cycle : ")
        #for vertex in self.currcycle:
           # print(vertex, end=" ")
        #print("0")
        return self.val
    
    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])
            
    def apply_union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1
            
    def kruskal_algo(self):
        result = []
        i, e, s = 0, 0, 0
        self.graph = sorted(self.graph, key=lambda item: item[2])
        parent = []
        rank = []
        for node in range(self.m_num_of_nodes):
            parent.append(node)
            rank.append(0)
        while e < self.m_num_of_nodes - 1:
            u, v, w = self.graph[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent, v)
            if x != y:
                e = e + 1
                result.append([u, v, w])
                self.apply_union(parent, rank, x, y)
        #print("kruskal\n")
        for u,v,weight in result:
            #print("%d - %d \t %d" % (u, v, weight))
            s+=weight
        return s
    
    def print_adj_matrix(self):
        for i in self.m_adj_matrix:
            print(i)

    
for n in range(3,11):
    x1.append(n)
    x2.append(n)
    t, h = 0, 0
    graph = Graph(n)
    for i in range(n):
        for j in range(i+1,n):
            graph.add_edge(i,j,random.randint(10,19))
    #graph.print_adj_matrix()
    graph.hamCycle()
    h = graph.Solution()
    t = 2*graph.kruskal_algo()
    y1.append(h)
    y2.append(t)
    
plt.plot(x1,y1,label="Minimum Hamiltonian Cost")
plt.plot(x2,y2,label="2 x Cost of Minimum Spanning Tree")
plt.xlabel("Number of Vertices")
plt.ylabel("Total Cost")
plt.title("Cost Comparision")
plt.legend()
plt.show()