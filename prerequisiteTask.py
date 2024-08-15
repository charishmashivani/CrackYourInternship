#Day 29

from collections import deque, defaultdict

class Solution:
    def isPossible(self, N, P, prerequisites):
        """
        :type N: int
        :type P: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        adj = defaultdict(list)
        in_degree = [0] * N
        
        for dest, src in prerequisites:
            adj[src].append(dest)
            in_degree[dest] += 1
        
        queue = deque([i for i in range(N) if in_degree[i] == 0])
        visited_count = 0
        
        while queue:
            node = queue.popleft()
            visited_count += 1
            for neighbor in adj[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        return visited_count == N
