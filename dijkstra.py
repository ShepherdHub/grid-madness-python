import numpy as np
import heapq
from graph import Graph

def dijkstra(grid_obj):
    
    start = grid_obj['start']
    end = grid_obj['end']
    
    g = Graph(grid_obj)
    graph = g.build_graph_dict()
    
    dist = {v:float('inf') for v in graph}
    dist[start] = 0
    
    Q = []
    prev = {}
    path = []
    
    for v,d in dist.items():

        heapq.heappush(Q,[d,v])
    
    while Q:
        cur_d, cur_v = heapq.heappop(Q)
        
        for adj, adj_dist in graph[cur_v].items():
            alt = dist[cur_v]+adj_dist
            if alt < dist[adj]:
                dist[adj] = alt
                prev[adj] = cur_v
    
    u = end
    while u in prev:
        path.insert(0,u)
        u = prev[u]
        #print prev[u]
    path.insert(0,u)

    return dist, prev, path