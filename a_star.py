import numpy as np
import math
import heapq
from graph import Graph



def euclidean(point, end):
    return math.sqrt((point[0]-end[0])**2+(point[1]-end[1])**2)

def reconstruct_path(came_from, current):
    total_path = [current]
    while current in came_from.keys():
        current = came_from[current]
        total_path.append(current)
    return total_path

def a_star(grid_obj):
    
    start = grid_obj['start']
    end = grid_obj['end']

    g = Graph(grid_obj)
    graph = g.build_graph_dict()
    
    closed_set = []
    open_heap = []
    came_from = {}
       
    g_score = {v:float('inf') for v in graph}
    g_score[start] = 0
    f_score = {v:float('inf') for v in graph}
    f_score[start] = euclidean(start, end)
    heapq.heappush(open_heap,[f_score[start],start])
    
    while open_heap:
        cur_f, cur_v = heapq.heappop(open_heap)
        
        if cur_v == end:
            return reconstruct_path(came_from, cur_v)
        
        closed_set.append(cur_v)

        for adj, adj_dist in graph[cur_v].items():
            
            if adj in closed_set:
                continue
            
            tentative_g_score = g_score[cur_v] + adj_dist

            if tentative_g_score >= g_score[adj]:
                continue

            came_from[adj] = cur_v
            g_score[adj] = tentative_g_score
            f_score[adj] = g_score[adj] + euclidean(adj, end)
            heapq.heappush(open_heap, [f_score[adj],adj])
            
                
        





 