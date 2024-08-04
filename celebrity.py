#Day 18

class Solution:
    def celebrity(self, mat):
        
        n = len(mat)
        
        left, right = 0, n - 1
        while left < right:
            if mat[left][right] == 1:
                left += 1
            else:
                right -= 1
        
        candidate = left
        
        for i in range(n):
            if i != candidate:
                if mat[candidate][i] == 1 or mat[i][candidate] == 0:
                    return -1
        
        return candidate
