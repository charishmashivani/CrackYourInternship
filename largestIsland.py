#Day 32

class Solution:
    def largestIsland(self, grid):
        n = len(grid)
        
        def dfs(x, y, index):
            if x < 0 or x >= n or y < 0 or y >= n or grid[x][y] != 1:
                return 0
            grid[x][y] = index
            area = 1
            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                area += dfs(x + dx, y + dy, index)
            return area
        
        index = 2 
        area_map = {0: 0}
        
        # Step 1: Label each island with a unique index and compute their area
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    area_map[index] = dfs(i, j, index)
                    index += 1
        
        # Step 2: Find the maximum area possible by changing one 0 to 1
        max_area = max(area_map.values())
        
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    seen = set()
                    new_area = 1
                    for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                        ni, nj = i + dx, j + dy
                        if 0 <= ni < n and 0 <= nj < n and grid[ni][nj] > 1:
                            seen.add(grid[ni][nj])
                    for index in seen:
                        new_area += area_map[index]
                    max_area = max(max_area, new_area)
        
        return max_area
