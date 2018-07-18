import numpy as np
import math

class Graph:
        
    def __init__(self, grid_obj):
    
        self.size = grid_obj['size']
        self.obstacles = grid_obj['obstacles']
        self.graph = {}

        #For testing block below
        self.grid = np.zeros([self.size,self.size])
        
    #*******TESTING: TERMINAL DISPLAY*******
    def make_obs(self):
        #Basic Obstacles
        for obs in self.obstacles:
            self.grid[obs] = 'nan'
        return self.grid
     
    def terminal_display(self):
        self.grid = self.make_obs()
        print self.grid
    #*******END TESTING: TERMINAL DISPLAY*******

    def adjacency(self,i,j  ):
        #Better way with something similar to networkx?

        #adj = [(i,j+1),(i+1,j+1),(i+1,j),(i+1,j-1),(i,j-1),(i-1,j-1),(i-1,j),(i-1,j+1)]
        adj = [(i,j+1),(i+1,j),(i,j-1),(i-1,j)]
        dia = [(i+1,j+1),(i+1,j-1),(i-1,j-1),(i-1,j+1)]
        
        if i == 0:
            #Corner cases
            if j == 0:
                #adj = adj[0:3]
                adj = adj[0:2]
                dia = [dia[0]]
            elif j == self.size-1:
                #adj = adj[2:5]
                adj = adj[1:3]
                dia = [dia[1]]
            #Side
            else:
                #adj = adj[0:5]
                adj = adj[0:3]
                dia = dia[0:2]

        elif i == self.size-1:
            #Corner cases
            if j == 0:
                #Better way?
                #adj = adj[6:8]+[adj[0]]
                adj = [adj[3]]+[adj[0]]
                dia = [dia[3]]

            elif j == self.size-1:
                #adj = adj[4:7]
                adj = adj[2:4]
                dia = [dia[2]]

            #Side
            else:
                #adj = [adj[0]]+adj[4:8]
                adj = [adj[0]]+adj[2:4]
                dia = dia[2:4]
        
        #Sides
        elif j == 0:
            #adj = adj[6:8]+adj[0:3]
            adj = [adj[3]]+adj[0:2]
            dia = [dia[3]]+[dia[0]]

        elif j == self.size-1:
            #adj = adj[2:7]
            adj = adj[1:4]
            dia = dia[1:3]

        #Remove adjacent obstacles
        for obs in self.obstacles:
            if obs in adj:
                adj.remove(obs)
            if obs in dia:
                dia.remove(obs)
        
        #Convert to dict
        adj = {v:1 for v in adj}
        for d in dia:
            adj[d] = math.sqrt(2)

        return adj

    def build_graph_dict(self):
        for i in range(self.size):
            for j in range(self.size):
                #Do not add obstacles
                if (i,j) in self.obstacles:
                    continue
                self.graph[(i,j)] = self.adjacency(i,j)
        
        #Returns dict of dicts (SFW)
        return self.graph