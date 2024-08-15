#Day 29

import sys

class Solution:
    def findTheCity(self, n, edges, distanceThreshold):
        # Initialize the distance matrix
        dist = [[float('inf')] * n for _ in range(n)]
        for i in range(n):
            dist[i][i] = 0
        
        for u, v, weight in edges:
            dist[u][v] = weight
            dist[v][u] = weight
        
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if dist[i][j] > dist[i][k] + dist[k][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
        
        min_reachable = float('inf')
        best_city = -1
        
        for i in range(n):
            reachable_count = sum(1 for j in range(n) if dist[i][j] <= distanceThreshold)
            if reachable_count <= min_reachable:
                if reachable_count < min_reachable or i > best_city:
                    min_reachable = reachable_count
                    best_city = i
        
        return best_city
