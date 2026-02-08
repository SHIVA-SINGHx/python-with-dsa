from collections import deque

class Graph:
    def __init__(self, vertex):
        self.mat = [ [0]*vertex for x in range(vertex)] ## jitne vertex honge like(8) utne kaa matrix ban jayga and sbme 0 fill ho jayga
        self.size = vertex

        
    # Add edges in undirected graph? 
    def add_edge(self, source, destination):
        if(0 <= source < self.size and 0 <= destination < self.size ):
            self.mat[source][destination] = 1
            self.mat[destination][source] = 1
            
        else:
            print("Invalid Edge")
           
    def BFS(self, source):
        visited_arr = [False] * self.size # jitne size ka element honge sb mai false fill ho jayga
        queue = deque([source])
        visited_arr[source] = True
        
        while(queue):
            v = queue.popleft()
            print(v, end=" ")
            
            for i in range(self.size):
                if (self.mat[v][i] == 1 and visited_arr[i] == False):
                    visited_arr[i] = True
                    queue.append(i)
                    
g = Graph(8) ## how many vertex in there here's 8
g.add_edge(0,1) # 0 to 1 connected
g.add_edge(0,3) # 0 to 3 connected
g.add_edge(1,3) # 1 to 3 connected
g.add_edge(3,5) # 3 to 5 connected
g.add_edge(3,4) # 3 to 4 connected
g.add_edge(4,5) # 4 to 5 connected
g.add_edge(4,6) # 4 to 6 connected
g.add_edge(6,2) # 6 to 2 connected
g.add_edge(6,7) # 6 to 7 connected

g.BFS(0) ## start from 0
            
        
        
        