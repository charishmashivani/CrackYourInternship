#Day 28

from collections import defaultdict, deque

class Solution(object):
    def eventualSafeNodes(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[int]
        """
        n = len(graph)
        
        reverse_graph = defaultdict(list)
        out_degree = [0] * n
        in_degree = [0] * n
        
        for u in range(n):
            for v in graph[u]:
                reverse_graph[v].append(u)
                out_degree[u] += 1
                in_degree[u] += 1
        
        terminal_nodes = deque()
        for i in range(n):
            if out_degree[i] == 0:
                terminal_nodes.append(i)
        
        safe_nodes = []
        while terminal_nodes:
            node = terminal_nodes.popleft()
            safe_nodes.append(node)
            for predecessor in reverse_graph[node]:
                in_degree[predecessor] -= 1
                if in_degree[predecessor] == 0:
                    terminal_nodes.append(predecessor)
        
        return sorted(safe_nodes)
