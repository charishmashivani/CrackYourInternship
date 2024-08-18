#Day 32

from collections import defaultdict, deque
from typing import List

class Solution:
    def findOrder(self, alien_dict: List[str], N: int, K: int) -> str:
        # Step 1: Create an adjacency list for the graph
        adj_list = defaultdict(list)
        in_degree = {chr(i + ord('a')): 0 for i in range(K)}
        
        # Step 2: Build the graph
        for i in range(N - 1):
            word1 = alien_dict[i]
            word2 = alien_dict[i + 1]
            min_len = min(len(word1), len(word2))
            for j in range(min_len):
                if word1[j] != word2[j]:
                    adj_list[word1[j]].append(word2[j])
                    in_degree[word2[j]] += 1
                    break
        
        # Step 3: Topological Sort using Kahn's Algorithm (BFS)
        queue = deque([node for node in in_degree if in_degree[node] == 0])
        topo_order = []
        
        while queue:
            current = queue.popleft()
            topo_order.append(current)
            
            for neighbor in adj_list[current]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        # Step 4: Check if topological sorting is valid
        if len(topo_order) < K:
            return ""
        
        return "".join(topo_order)
