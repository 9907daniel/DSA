
class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # Solution using a copy of the array

        non_zero = []
        zero = []
        
        for a in range(len(nums)):
            if nums[a]==0:
                zero.append(nums[a])
            elif nums[a]!=0:
                non_zero.append(nums[a])
        return non_zero + zero
                
        # Solution using two pointers to sitch pointers, everytime non zeor value.   
                
        left = 0
        right = 0
        
        while right < len(nums):
            if nums[right] != 0:
                tmp = nums[left]
                nums[left] = nums[right]
                nums[right] = tmp
                left += 1
            right += 1

new = Solution().moveZeroes(nums=[0,1,0,3,12])
print(new)
