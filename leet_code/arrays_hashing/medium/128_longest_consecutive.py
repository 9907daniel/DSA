# Given an unsorted array of integers nums, return the length 
# of the longest consecutive elements sequence.

# You must write an algorithm that runs in O(n) time.

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        result = []

        def rec(a, count):
            count += 1
            if a+1 in nums:
                rec(a+1,count)
            else:
                result.append(count)

        for a in nums:
            rec(a,0)

        return max(result, default=0)
    

        # tmp = []
        # nums.sort()

        # result = []
        # count = 1
        # first = 0
        # second = 1

        # if len(nums) == 1:
        #     return 1
        # else:
        #     while second < len(nums):
        #         if nums[second] not in tmp:
        #             tmp.append(nums[second])
        #             if second == len(nums)-1 and nums[second]-1 == nums[first]:
        #                 count += 1
        #                 result.append(count)
        #                 first += 1
        #                 second += 1
        #             elif nums[first]+1 != nums[second]:
        #                 result.append(count)
        #                 count = 1
        #                 first += 1
        #                 second += 1
        #             else:
        #                 count += 1
        #                 first += 1
        #                 second +=1
        #         else:
        #             first += 1
        #             second += 1
        #     return max(result, default=0)