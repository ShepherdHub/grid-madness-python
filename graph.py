import numpy as np


class Graph:
        
    def __init__(self, grid_obj):
    
        self.size = grid_obj['size']
        self.obstacles = grid_obj['obstacles']
        self.start = grid_obj['start']
        self.end = grid_obj['end']

        self.grid = np.zeros([self.size,self.size])
        self.graph = {}

    #Below for displaying grid to terminal
    #Likely will use more efficient data structure for shortest distance algorithms
    def make_obs(self, graph_type):
        #Basic Obstacles
        if graph_type == 'vis':
            for obs in self.obstacles:
                self.grid[obs] = 'nan'
            return self.grid
        
 


    def terminal_display(self):
        self.grid = self.make_obs(graph_type = 'vis')
        print self.grid

    def adjacency(self,i,j):
        #Not just a grid; (0,0) needs to connect to (1,0), (0,1) AND (1,1) networkx doesn't do this that I'm aware of
        #Better way?

        adj = [(i,j+1),(i+1,j+1),(i+1,j),(i+1,j-1),(i,j-1),(i-1,j-1),(i-1,j),(i-1,j+1)]
        
        if i == 0:
            #Corner cases
            if j == 0:
                adj = adj[0:3]
            elif j == self.size-1:
                adj = adj[2:5]
            #Side
            else:
                adj = adj[0:5]

        elif i == self.size-1:
            #Corner cases
            if j == 0:
                #Better way?
                adj = adj[6:8]+[adj[0]]
            elif j == self.size-1:
                adj = adj[4:7]
            #Side
            else:
                adj = [adj[0]]+adj[4:8]
        
        #Sides
        elif j == 0:
            adj = adj[6:8]+adj[0:3]
        elif j == self.size-1:
            adj = adj[2:7]

        #Remove adjacent obstacles
        for obs in self.obstacles:
            if obs in adj:
                adj.remove(obs)


        return adj

    def build_graph_dict(self):
        for i in range(self.size):
            for j in range(self.size):
                #Do not add obstacles
                if (i,j) in self.obstacles:
                    continue
                self.graph[(i,j)] = self.adjacency(i,j)
    
        return self.graph