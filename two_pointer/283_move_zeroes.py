class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        count = 0
        while count < len(nums):
            if len(nums[count+1:]) == count:
                return nums
            elif nums[count] == 0:
                nums.pop(nums[count])
                nums.append(0)
            else:
                count += 1
            print(nums)

new = Solution().moveZeroes(nums=[0,1,0,3,12])
print(new)