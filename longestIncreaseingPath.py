#Day 32

class Solution:
    def longestIncreasingPath(self, matrix):
        if not matrix or not matrix[0]:
            return 0

        m, n = len(matrix), len(matrix[0])
        memo = [[-1] * n for _ in range(m)]
        
        def dfs(i, j):
            if memo[i][j] != -1:
                return memo[i][j]
            
            # Directions: right, down, left, up
            directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            max_path = 1
            
            for direction in directions:
                ni, nj = i + direction[0], j + direction[1]
                if 0 <= ni < m and 0 <= nj < n and matrix[ni][nj] > matrix[i][j]:
                    max_path = max(max_path, 1 + dfs(ni, nj))
            
            memo[i][j] = max_path
            return max_path
        
        result = 0
        for i in range(m):
            for j in range(n):
                result = max(result, dfs(i, j))
        
        return result
