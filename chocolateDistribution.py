class Solution:

    def findMinDiff(self, A, N, M):
        A.sort()
        
        min_diff = float('inf')
        
        for i in range(N - M + 1):
            diff = A[i + M - 1] - A[i]
            if diff < min_diff:
                min_diff = diff
        
        return min_diff
