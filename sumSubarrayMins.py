#Day 14 

class Solution(object):
    def sumSubarrayMins(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        MOD = 10**9 + 7
        n = len(arr)
        
        prev_smaller = [0] * n
        next_smaller = [0] * n
        
        stack = []
        for i in range(n):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            prev_smaller[i] = i - stack[-1] if stack else i + 1
            stack.append(i)
        
        stack = []
        for i in range(n-1, -1, -1):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
            next_smaller[i] = stack[-1] - i if stack else n - i
            stack.append(i)
        
        result = 0
        for i in range(n):
            result = (result + arr[i] * prev_smaller[i] * next_smaller[i]) % MOD
        
        return result
