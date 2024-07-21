class Solution(object):
    def reverseWords(self, s):
        words = s.split()
        words.reverse()
        reversed_s = ' '.join(words)
        return reversed_s
