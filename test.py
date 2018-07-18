from graph import Graph
from dijkstra import dijkstra
test_grid = {'size':10, 'obstacles':[(3,0),(3,1),(3,2),(3,3),(3,4),(3,5),(3,6),(4,6),(5,6),(6,6)], 'start':(0,0),'end':(9,9)}
g = Graph(test_grid)
_,_,path = dijkstra(test_grid)
p = g.make_obs()
for v in path:
    p[v] = 111
    print v
print p