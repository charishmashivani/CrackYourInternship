class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""

        prefix = strs[0]

        for i in range(1, len(strs)):
            string = strs[i]
            while not string.startswith(prefix):
                prefix = prefix[:len(prefix) - 1]
                if not prefix:
                    return ""

        return prefix
