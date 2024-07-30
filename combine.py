#Day 13

class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        def backtrack(start, combination):
            if len(combination) == k:
                result.append(list(combination))
                return
            for i in range(start, n + 1):
                combination.append(i)
                backtrack(i + 1, combination)
                combination.pop()
        
        result = []
        backtrack(1, [])
        return result
