class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        for a, b in enumerate(s):
            if b in t:
                bk = t.index(b)
                t = t[bk+1:]
            else:
                return False
        return True