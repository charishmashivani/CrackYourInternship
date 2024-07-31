#Day 14

class Solution(object):
    def mctFromLeafValues(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        stack = []
        total_cost = 0
        
        for value in arr:
            while stack and stack[-1] <= value:
                top = stack.pop()
                if stack:
                    total_cost += top * min(stack[-1], value)
                else:
                    total_cost += top * value
            stack.append(value)
        while len(stack) > 1:
            top = stack.pop()
            total_cost += top * stack[-1]
        
        return total_cost
