#Day 29

class Solution:
    def shortest_distance(self, matrix):
        n = len(matrix)
        
        inf = float('inf')
        for i in range(n):
            for j in range(n):
                if matrix[i][j] == -1 and i != j:
                    matrix[i][j] = inf
        
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if matrix[i][k] < inf and matrix[k][j] < inf:
                        matrix[i][j] = min(matrix[i][j], matrix[i][k] + matrix[k][j])
        
        for i in range(n):
            for j in range(n):
                if matrix[i][j] == inf:
                    matrix[i][j] = -1
        
        return matrix
