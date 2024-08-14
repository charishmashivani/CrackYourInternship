#Day 28

from collections import deque

class Solution(object):
    def maxDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        # Step 1: Initialize BFS with all land cells
        queue = deque()
        distance = [[-1] * n for _ in range(n)]
        
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    queue.append((r, c))
                    distance[r][c] = 0
        
        if not queue:
            return -1
        
        # Step 2: Perform BFS
        max_dist = -1
        while queue:
            r, c = queue.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and distance[nr][nc] == -1:
                    distance[nr][nc] = distance[r][c] + 1
                    max_dist = max(max_dist, distance[nr][nc])
                    queue.append((nr, nc))
        
        return max_dist if max_dist > 0 else -1
