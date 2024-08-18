#Day 32

class Solution:
    def removeBoxes(self, boxes):
        def dp(i, j, k):
            if i > j:
                return 0
            if memo[i][j][k] != -1:
                return memo[i][j][k]

            res = (k + 1) * (k + 1) + dp(i + 1, j, 0)
            
            for m in range(i + 1, j + 1):
                if boxes[m] == boxes[i]:
                    res = max(res, dp(i + 1, m - 1, 0) + dp(m, j, k + 1))

            memo[i][j][k] = res
            return res

        n = len(boxes)
        memo = [[[-1] * n for _ in range(n)] for _ in range(n)]
        return dp(0, n - 1, 0)
