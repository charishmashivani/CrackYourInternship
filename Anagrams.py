#Day 12

class Solution:
    def Anagrams(self, words, n):
        '''
        words: list of word
        n:      no of words
        return : list of group of anagram {list will be sorted in driver code (not word in grp)}
        '''
        from collections import defaultdict
        anagram_groups = defaultdict(list)
        for word in words:
            sorted_word = ''.join(sorted(word))
            anagram_groups[sorted_word].append(word)
        result = list(anagram_groups.values())
        
        return result
