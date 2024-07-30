#Day 3

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        bracketMap = {')': '(', '}': '{', ']': '['}
        stack = []
        for char in s:
            if char in bracketMap:
                topElement = stack.pop() if stack else '#'
                if bracketMap[char] != topElement:
                    return False
            else:
                stack.append(char)
        return not stack
