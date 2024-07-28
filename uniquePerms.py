#Day 11

from itertools import permutations

class Solution:
    def uniquePerms(self, arr, n):
        all_perms = permutations(arr)
        
        unique_perms = set(all_perms)
        
        sorted_unique_perms = sorted(list(map(list, unique_perms)))
        
        return sorted_unique_perms
