class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # 1. compare if len is same
        # 2. check if letter is same amount to each other

        if len(s) != len(t):
            return False
        
        cs, ct = {}, {}




        # Time complexity : O(S+T)

        
        # empty_list =[]
        # l = list(t)
        # l2 = list(s)
        # l.sort()
        # l2.sort()
        
        # while len(l) == len(l2):        
        #     for a,b in zip(l,l2):
        #         if a ==b:
        #             pass
        #         else:
        #             return False
        #     return True
        # return False

# x = Solution()
# print(x.isAnagram("anagrasm","nagaram"))
