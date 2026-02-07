class Graph:
    def __init__(self, vertex):
        self.mat = [ [0]*vertex for x in range(vertex)]
        self.size = vertex

        
    # Add edges in undirected graph? 
    def add_edge(self, source, destination):
        if(0 <= source < self.size and 0 <= destination < self.size ):
            self.mat[source][destination] = 1
            self.mat[destination][source] = 1
            
        else:
            print("Invalid Edge")
            
    def print(self):
        for row in self.mat:
           print(' '.join(map(str, row)))
           
    def bfs(self, source):
        return
        