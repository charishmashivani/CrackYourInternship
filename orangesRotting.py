#Day 15

from collections import deque

class Solution:
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return -1
        
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        fresh_count = 0
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh_count += 1
        
        if fresh_count == 0:
            return 0
        
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        minutes_passed = 0
        
        while queue:
            level_size = len(queue)
            for _ in range(level_size):
                r, c = queue.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh_count -= 1
                        queue.append((nr, nc))
            minutes_passed += 1
        
        return minutes_passed - 1 if fresh_count == 0 else -1
