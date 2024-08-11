#Day 25

from typing import List

class Solution:
    def isCycle(self, V: int, adj: List[List[int]]) -> bool:
        def dfs(node, parent):
            visited[node] = True
            for neighbor in adj[node]:
                if not visited[neighbor]:
                    if dfs(neighbor, node):
                        return True
                elif neighbor != parent:
                    return True
            return False
        
        visited = [False] * V
        
        for i in range(V):
            if not visited[i]:
                if dfs(i, -1):
                    return 1
        
        return 0
