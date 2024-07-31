#Day 14

class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        answer = [0] * len(temperatures)
        stack = []

        for i, current_temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < current_temp:
                index = stack.pop()
                answer[index] = i - index
            stack.append(i)

        return answer
