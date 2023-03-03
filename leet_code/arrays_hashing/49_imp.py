# Instead of sorting --> count the number of each alphabetic char
# Use hash map

# O(m*n) -> number of strs that is given * 26(alphabet)

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        res = {}
        
        
        for s in strs:
            count = [0]*26
            # [0,0...,0]
            
            for c in s:
                count[ord(c)-ord("a")]
                # ord(a) -> 80 -> 80-80 = count[0]
            
            if count in res:
                res.append(s)
                
            