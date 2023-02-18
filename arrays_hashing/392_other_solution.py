class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0
        
        while i < len(s) and t < len(t):
            if s[i] == s[j]:
                i += 1        
            j += 1
            
        return True if i == len(s) else False
            
       