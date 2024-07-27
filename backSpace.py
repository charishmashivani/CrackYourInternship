#Day 10

class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        def build_final_string(string):
            stack = []
            for char in string:
                if char == '#':
                    if stack:
                        stack.pop()
                else:
                    stack.append(char)
            return "".join(stack)
        
        final_s = build_final_string(s)
        final_t = build_final_string(t)
        
        return final_s == final_t
