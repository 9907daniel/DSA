# # Given two strings s and t, return true if t is an anagram of s, and false otherwise.
# # An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

# # Input: s = "anagram", t = "nagaram"
# # Output: true

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        empty_list =[]
        l = list(t)
        l2 = list(s)
        l.sort()
        l2.sort()
        
        while len(l) == len(l2):        
            for a,b in zip(l,l2):
                if a ==b:
                    pass
                else:
                    return False
            return True
        return False

x = Solution()
print(x.isAnagram("anagrasm","nagaram"))
