# https://leetcode.com/problems/remove-element/description/

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        print(nums)

        a = 0
        while a < len(nums):
            if nums[a] == val:
                nums.pop(a)
            else:
                a +=1
        print(nums)
