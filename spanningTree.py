#Day 29

import heapq

class Solution:
    def spanningTree(self, V, adj):
        min_heap = []
        min_edge = [float('inf')] * V
        in_mst = [False] * V
        total_weight = 0
        
        min_edge[0] = 0
        heapq.heappush(min_heap, (0, 0))
        
        while min_heap:
            weight, u = heapq.heappop(min_heap)
            
            if in_mst[u]:
                continue
            
            total_weight += weight
            in_mst[u] = True
            
            for v, w in adj[u]:
                if not in_mst[v] and w < min_edge[v]:
                    min_edge[v] = w
                    heapq.heappush(min_heap, (w, v))
        
        return total_weight
