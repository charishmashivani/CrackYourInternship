#Day 11

class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        directions = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),         (0, 1),
            (1, -1), (1, 0), (1, 1)
        ]
        
        m, n = len(board), len(board[0])
        
        for i in range(m):
            for j in range(n):
                live_neighbors = 0
                
                for direction in directions:
                    ni, nj = i + direction[0], j + direction[1]
                    if 0 <= ni < m and 0 <= nj < n and abs(board[ni][nj]) == 1:
                        live_neighbors += 1
                
                if board[i][j] == 1:
                    if live_neighbors < 2 or live_neighbors > 3:
                        board[i][j] = -1
                elif board[i][j] == 0:
                    if live_neighbors == 3:
                        board[i][j] = 2
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == 2:
                    board[i][j] = 1
                elif board[i][j] == -1:
                    board[i][j] = 0
