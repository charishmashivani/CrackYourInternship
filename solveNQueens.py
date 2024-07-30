#Day 13

class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        def is_not_under_attack(row, col):
            return col not in columns and \
                   (row - col) not in diagonals1 and \
                   (row + col) not in diagonals2
        
        def place_queen(row, col):
            columns.add(col)
            diagonals1.add(row - col)
            diagonals2.add(row + col)
            board[row] = col
        
        def remove_queen(row, col):
            columns.remove(col)
            diagonals1.remove(row - col)
            diagonals2.remove(row + col)
            board[row] = -1
        
        def add_solution():
            solution = []
            for row in range(n):
                solution.append(''.join('Q' if c == board[row] else '.' for c in range(n)))
            result.append(solution)
        
        def backtrack(row):
            if row == n:
                add_solution()
                return
            
            for col in range(n):
                if is_not_under_attack(row, col):
                    place_queen(row, col)
                    backtrack(row + 1)
                    remove_queen(row, col)
        
        columns = set()
        diagonals1 = set()
        diagonals2 = set()
        board = [-1] * n
        result = []
        
        backtrack(0)
        return result
