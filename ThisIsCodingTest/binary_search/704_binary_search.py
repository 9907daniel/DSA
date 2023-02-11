class Solution:
    def search(self, nums: list[int], target: int) -> int:

        lb = 0
        up = len(nums)-1

        while lb <= up:
            mid = (lb+up)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                lb = mid +1
            elif nums[mid] > target:
                up = mid -1         
        return -1
            
nums = [-1,0,3,5,9,12]
target = 200
new = Solution()

print(new.search(nums,target))