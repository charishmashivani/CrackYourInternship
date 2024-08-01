#Day 15

def dfsOfGraph(self, V, adj):
        result = []
        
        visited = [False] * V
        
        def dfs(v):
            visited[v] = True
            result.append(v)
            for neighbor in adj[v]:
                if not visited[neighbor]:
                    dfs(neighbor)
        
        dfs(0)
        
        return result
