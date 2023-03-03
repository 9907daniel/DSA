class Solution:
    def isPalindrome(self, s: str) -> bool:

        new_s = ''.join(filter(str.isalnum, s))
        new_lower = new_s.lower()

        start_pointer = 0
        end_pointer = len(new_lower) -1

        while start_pointer < end_pointer:
            if new_lower[start_pointer] == new_lower[end_pointer]:
                start_pointer += 1
                end_pointer -= 1
            else:
                return False
        return True



    def impPalindrome(self, s: str) -> bool:
        newStr = ""
        
        for c in s:
            if c.isalnum(): 
            # if c is alphanumerical
                newStr += c.lower()
        return newStr == newStr[::-1]
                        # reverse string
                        
                        
class newSoltuion:                     
    def nonPreBuiltPalindrome(self, s:str) --> bool:
        l, r = 0, len(s)-1
        
        while l<r:
            while l<r and not self.alphaNum(s[l]):
                l += 1
            while r>l and not self.alphaNum(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l,r = l+1, r-1
        return True
        
    def alphaNum(self, c):
        (ord('A') <= ord(c) <= ord('Z') or 
         ord('a') <= ord(c) <= ord('z') or
         ord('0') <= ord(c) <= ord('9')
         )