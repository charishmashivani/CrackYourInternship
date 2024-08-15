#Day 29

class Solution:
    def calcEquation(self, equations, values, queries):
        from collections import defaultdict
        import math

        # Step 1: Build the graph
        graph = defaultdict(dict)
        for (u, v), value in zip(equations, values):
            graph[u][v] = value
            graph[v][u] = 1 / value

        # Step 2: Initialize the distance matrix for Floyd-Warshall
        variables = set(graph.keys())
        dist = {var: {v: float('inf') for v in variables} for var in variables}
        for var in variables:
            dist[var][var] = 1
        
        for u in graph:
            for v in graph[u]:
                dist[u][v] = graph[u][v]

        # Step 3: Floyd-Warshall algorithm to compute all-pairs shortest paths
        for k in variables:
            for i in variables:
                for j in variables:
                    if dist[i][k] < float('inf') and dist[k][j] < float('inf'):
                        dist[i][j] = min(dist[i][j], dist[i][k] * dist[k][j])

        # Step 4: Process each query
        result = []
        for u, v in queries:
            if u in dist and v in dist[u] and dist[u][v] < float('inf'):
                result.append(dist[u][v])
            else:
                result.append(-1.0)

        return result
