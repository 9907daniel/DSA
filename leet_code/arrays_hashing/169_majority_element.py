
# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ times. 
# You may assume that the majority element always exists in the array.

# ex ) list = [3,2,2,3,3] --> return 3 


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = [0]*(max(nums)+1)

        for a,b in enumerate(nums):
            count[b] += 1
        return count.index(max(count))
    
        # O(n+m)