#Day 25

from typing import List

class Solution:
    def isCyclic(self, V: int, adj: List[List[int]]) -> bool:
        def dfs(node):
            visited[node] = True
            recStack[node] = True
            
            for neighbor in adj[node]:
                if not visited[neighbor]:
                    if dfs(neighbor):
                        return True
                elif recStack[neighbor]:
                    return True
            
            recStack[node] = False
            return False
        
        visited = [False] * V
        recStack = [False] * V
        
        for i in range(V):
            if not visited[i]:
                if dfs(i):
                    return 1
        
        return 0
