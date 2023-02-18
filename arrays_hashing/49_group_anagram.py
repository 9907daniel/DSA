# # Level : medium
# Given an array of strings strs, group the anagrams together. 
# You can return the answer in any order.

# An Anagram is a word or phrase formed by rearranging 
# the letters of a different word or phrase, typically using all the original letters exactly once.


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        l = []
        sorted_l = []

        for a in strs:
            b = a
            new = list(b)
            new.sort()
            
            if new in sorted_l:
                for c,d in enumerate(sorted_l):
                    if new == d:
                        l[c].append(a)
            else:
                l.append([a])
                sorted_l.append(new)
        return l

