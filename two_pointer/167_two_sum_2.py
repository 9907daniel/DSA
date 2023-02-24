# Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, 
# find two numbers such that they add up to a specific target number. 
# Let these two numbers be numbers[index1] and numbers[index2] 
# where 1 <= index1 < index2 <= numbers.length.

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start = 0
        end = len(numbers)-1
        while start < end:
            if numbers[start]+numbers[end]==target:
                return [start+1,end+1]
            elif numbers[start]+numbers[end] > target:
                end -= 1
            elif numbers[start]+numbers[end] < target:
                start +=1
