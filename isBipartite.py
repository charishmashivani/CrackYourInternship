#Day 32

from collections import deque

class Solution:
    def isBipartite(self, V, adj):
        color = [-1] * V
        
        def bfs_check(start):
            queue = deque([start])
            color[start] = 0
            
            while queue:
                node = queue.popleft()
                
                for neighbor in adj[node]:
                    if color[neighbor] == -1:
                        color[neighbor] = 1 - color[node]
                        queue.append(neighbor)
                    elif color[neighbor] == color[node]:
                        return False
            
            return True
        
        for i in range(V):
            if color[i] == -1:
                if not bfs_check(i):
                    return False
        
        return True
