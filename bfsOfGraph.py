#Day 15

from typing import List
from collections import deque

class Solution:
    # Function to return Breadth First Traversal of given graph.
    def bfsOfGraph(self, V: int, adj: List[List[int]]) -> List[int]:
        result = []
        
        queue = deque([0])
        
        visited = [False] * V
        visited[0] = True
        
        while queue:
            node = queue.popleft()
            result.append(node)
            
            for neighbor in adj[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)
        
        return result
