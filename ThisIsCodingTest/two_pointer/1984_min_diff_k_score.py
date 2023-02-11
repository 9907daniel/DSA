class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        result = float("inf")
        nums.sort()
        l, r = 0, k-1

        while r < len(nums):
            result = min(result, nums[r]-nums[l])
            l,r = l+1, r+1
        return result
