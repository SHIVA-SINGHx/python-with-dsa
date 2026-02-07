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
           
    
    def dfs(self, source):
        visited = [False] * self.size
        stack = [source]
        
        while(stack):
            
            v = stack.pop()
            
            if(visited[v]== False):
                print(v, end=" -> ")
                visited[v] = True
                
            for i in range(self.size):
                if self.mat[v][i] == 1 and visited[i] == False:
                    stack.append(i)
                    
                    
g = Graph(6) #inserting 6 vertex here
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(2, 3)
g.add_edge(2, 4)
g.add_edge(3, 5)
g.add_edge(4, 5)


g.dfs(0)
 