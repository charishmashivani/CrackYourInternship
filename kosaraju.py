#Day 28

from collections import defaultdict, deque

class Solution:
    
    # Function to perform DFS and fill the stack with finish times
    def dfs(self, v, adj, visited, stack):
        visited.add(v)
        for neighbor in adj[v]:
            if neighbor not in visited:
                self.dfs(neighbor, adj, visited, stack)
        stack.append(v)
    
    # Function to perform DFS on the transposed graph
    def dfsTranspose(self, v, transpose_adj, visited):
        visited.add(v)
        for neighbor in transpose_adj[v]:
            if neighbor not in visited:
                self.dfsTranspose(neighbor, transpose_adj, visited)
    
    # Function to find number of strongly connected components in the graph
    def kosaraju(self, V, adj):
        # Step 1: Fill vertices in stack according to their finishing times
        stack = []
        visited = set()
        for i in range(V):
            if i not in visited:
                self.dfs(i, adj, visited, stack)
        
        # Step 2: Create the transpose of the graph
        transpose_adj = defaultdict(list)
        for v in range(V):
            for neighbor in adj[v]:
                transpose_adj[neighbor].append(v)
        
        # Step 3: Perform DFS on the transposed graph
        visited = set()
        scc_count = 0
        while stack:
            v = stack.pop()
            if v not in visited:
                self.dfsTranspose(v, transpose_adj, visited)
                scc_count += 1
        
        return scc_count
