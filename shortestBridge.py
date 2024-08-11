#Day 25

from collections import deque

class Solution:
    def shortestBridge(self, grid):
        n = len(grid)
        
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        def bfs(start_points):
            queue = deque(start_points)
            distance = 0
            
            while queue:
                for _ in range(len(queue)):
                    x, y = queue.popleft()
                    for dx, dy in directions:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < n and 0 <= ny < n:
                            if grid[nx][ny] == 1 and (nx, ny) not in visited:
                                return distance
                            if grid[nx][ny] == 0 and (nx, ny) not in visited:
                                visited.add((nx, ny))
                                queue.append((nx, ny))
                distance += 1
            return -1
        
        def dfs(x, y, island_points):
            stack = [(x, y)]
            while stack:
                cx, cy = stack.pop()
                if (cx, cy) in visited:
                    continue
                visited.add((cx, cy))
                island_points.append((cx, cy))
                for dx, dy in directions:
                    nx, ny = cx + dx, cy + dy
                    if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 1 and (nx, ny) not in visited:
                        stack.append((nx, ny))
        
        visited = set()
        island1 = []
        found_first_island = False
        
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1 and not found_first_island:
                    dfs(i, j, island1)
                    found_first_island = True
                    break
            if found_first_island:
                break

        visited = set(island1)
        min_flips = bfs(island1)
        
        return min_flips
