from graph import Graph
test_grid = {'size':10, 'obstacles':[(3,3),(3,4),(3,5),(3,6),(4,6),(5,6),(6,6)], 'start':(0,0),'end':(9,9)}
g = Graph(test_grid)
g.terminal_display()