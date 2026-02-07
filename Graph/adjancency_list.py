class Graph:
    def __init__(self):
        self.adjList = {}
        
    def add_vertex(self, vertex):
        if vertex not in self.adjList:
            self.adjList[vertex] = []
            
    def addEdge(self, source, destination):
        self.add_vertex(source)
        self.add_vertex(destination)
        
        self.adjList[source].append(destination)
        self.adjList[destination].append(source)
        
        
    def print(self):
        for vertex in self.adjList:
            print(vertex, "-> ", self.adjList[vertex], end=" ")
            
            
## self point to the object like if i have 3-4 obj g1,g2,g3,g4 if i ask you which g1 or g2 here self came to the picture it knows where to point        
             
g = Graph()
g.addEdge(1,2)
g.addEdge(2,3)
g.addEdge(1,4)
g.addEdge(4,3)
g.addEdge(2,4)
g.addEdge(4,5)
g.addEdge(3,5)

g.print()