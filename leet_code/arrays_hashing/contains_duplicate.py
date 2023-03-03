# Given an integer array nums, 
# return true if any value appears at least twice 
# in the array, and return false if every element 
# is distinct.

# EX) 
# input : nums = [1,2,3,1]
# output : true

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        empty_list = []
        for a in nums:
            if a not in empty_list:
                empty_list.append(a)
            else:
                return True