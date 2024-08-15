class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]
        
        def dfs(x, y):
            directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            stack = [(x, y)]
            while stack:
                cx, cy = stack.pop()
                for dx, dy in directions:
                    nx, ny = cx + dx, cy + dy
                    if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny] and grid[nx][ny] == '1':
                        visited[nx][ny] = True
                        stack.append((nx, ny))
        
        num_islands = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and not visited[i][j]:
                    visited[i][j] = True
                    num_islands += 1
                    dfs(i, j)
        
        return num_islands
