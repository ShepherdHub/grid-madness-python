import numpy as np

class Graph:
        
    def __init__(self, grid_obj):
    
        self.size = grid_obj['size']
        self.obstacles = grid_obj['obstacles']
        self.start = grid_obj['start']
        self.end = grid_obj['end']

        self.grid = np.zeros([self.size,self.size])
    

    #Below for displaying grid to terminal
    #Likely will use more efficient data structure for shortest distance algorithms
    def make_obs(self):
        #Basic Obstacles
        for obs in self.obstacles:
            self.grid[obs] = 'nan'
        return self.grid

    def terminal_display(self):
        #grid = np.zeros([self.size,self.size])
        self.grid = self.make_obs()
        print self.grid
        return self.grid