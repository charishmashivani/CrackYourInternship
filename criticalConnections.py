#Day 32

class Solution:
    def criticalConnections(self, n, connections):
        from collections import defaultdict

        # Create an adjacency list
        graph = defaultdict(list)
        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)
        
        # Initialize variables to track discovery times and lowest points
        discovery_time = [-1] * n
        low = [-1] * n
        self.time = 0
        result = []

        def dfs(node, parent):
            discovery_time[node] = low[node] = self.time
            self.time += 1
            
            for neighbor in graph[node]:
                if discovery_time[neighbor] == -1:  # Not visited
                    dfs(neighbor, node)
                    low[node] = min(low[node], low[neighbor])
                    
                    if low[neighbor] > discovery_time[node]:
                        result.append([node, neighbor])
                elif neighbor != parent:
                    low[node] = min(low[node], discovery_time[neighbor])
        
        # Start DFS from the first node
        dfs(0, -1)
        
        return result
