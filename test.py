from graph import Graph
from dijkstra import dijkstra
import a_star
#Practice obstacles
#[(3,0),(3,1),(3,2),(3,4),(3,5),(3,6),(4,6),(5,6),(6,6)]
#[(0,4),(1,4),(2,4),(3,4),(5,4),(6,4),(7,4),(8,4),(9,4)]
#[(0,4),(1,4),(2,4),(3,4),(5,4),(6,4),(7,4),(8,4)]

test_grid = {'size':10, 'obstacles':[(3,0),(3,1),(3,2),(3,4),(3,5),(3,6),(4,6),(5,6),(6,6)], 'start':(0,0),'end':(9,9)}
g = Graph(test_grid)
p = g.make_obs()

#Testing Dijkstra
_,_,path = dijkstra(test_grid)

#Testing A*
#path = a_star.a_star(test_grid)

for v in path:
    p[v] = 111
    #print v
print p