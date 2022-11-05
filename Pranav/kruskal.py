import random

class Graph:
    def __init__(self, num_of_nodes, directed = False):
        self.m_num_of_nodes = num_of_nodes
        self.m_directed = directed

        self.m_adj_matrix = [[0 for column in range(num_of_nodes)]
                             for row in range(num_of_nodes)]
        
        self.graph = []
        
    def add_edge(self, node1, node2, weight=1):
        self.m_adj_matrix[node1][node2] = weight
        self.graph.append([node1,node2,weight])

        if not self.m_directed:
            self.m_adj_matrix[node2][node1] = weight
            self.graph.append([node2,node1,weight])            
            
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
        i, e = 0, 0
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
        print("Edge \tWeight")
        for u, v, weight in result:
            print("%d - %d \t %d" % (u, v, weight))

    def print_adj_matrix(self):
        for i in self.m_adj_matrix:
            print(i)

n = int(input("Number of vertices: "))
graph = Graph(n)

offset = random.randint(1, n*n)

for i in range(n):
    for j in range(n):
        if (graph.m_adj_matrix[j][i] != 0):
            graph.m_adj_matrix[i][j] = graph.m_adj_matrix[j][i]
        elif (i != j):
            graph.add_edge(i, j, random.randint(1,n))

graph.print_adj_matrix()

graph.kruskal_algo()