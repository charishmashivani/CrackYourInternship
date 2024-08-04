#Day 18

class Solution(object):
    def removeDuplicates(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        stack = []
        
        for char in s:
            if stack and stack[-1][0] == char:
                count = stack[-1][1] + 1
                if count == k:
                    stack.pop()
                else:
                    stack[-1] = (char, count)
            else:
                stack.append((char, 1))
        
        result = []
        for char, count in stack:
            result.append(char * count)
        
        return ''.join(result)
