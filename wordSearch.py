class Solution:
    def exist(self, board, word):
        if not board or not word:
            return False
        
        m, n = len(board), len(board[0])
        
        def dfs(x, y, word_index):
            if word_index == len(word):
                return True
            if x < 0 or x >= m or y < 0 or y >= n or board[x][y] != word[word_index]:
                return False
            
            temp, board[x][y] = board[x][y], '#'
            found = (dfs(x+1, y, word_index+1) or
                     dfs(x-1, y, word_index+1) or
                     dfs(x, y+1, word_index+1) or
                     dfs(x, y-1, word_index+1))
            
            board[x][y] = temp
            return found
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0] and dfs(i, j, 0):
                    return True
        
        return False
