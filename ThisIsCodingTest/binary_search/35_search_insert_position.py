# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

# You must write an algorithm with O(log n) runtime complexity.

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        lb = 0
        up = len(nums)-1

        while lb <= up:
            mid = (lb+up)//2
            if nums[mid] < target:
                lb = mid +1
            elif nums[mid] > target:
                up = mid -1
            else:
                return mid

        if target < nums[mid]:
            return mid
        else:
            return mid+1