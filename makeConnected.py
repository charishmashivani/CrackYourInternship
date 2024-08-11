#Day 25

from collections import defaultdict, deque

class Solution:
    def makeConnected(self, n, connections):
        if len(connections) < n - 1:
            return -1
        
        graph = defaultdict(list)
        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)

        def bfs(start_node):
            queue = deque([start_node])
            visited.add(start_node)
            while queue:
                node = queue.popleft()
                for neighbor in graph[node]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)
        
        visited = set()
        num_components = 0
        
        for i in range(n):
            if i not in visited:
                bfs(i)
                num_components += 1
        
        return num_components - 1
