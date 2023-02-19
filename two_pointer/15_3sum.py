# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] 
# such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.xs

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        a = 0
        b = 1
        c = len(nums)-1
        l = []

        nums.sort()

        while (a is not c-2):
            print(a, b, c)
            if nums[a]+nums[b]+nums[c] ==0:
                if [nums[a], nums[b], nums[c]] not in l: 
                    l.append([nums[a], nums[b], nums[c]])
                c -= 1
            elif b == c-1:
                a += 1
                b = a+1
            else:
                b += 1

        if a == b-1 and a == c-2:
            if nums[a]+nums[b]+nums[c] ==0:
                if [nums[a], nums[b], nums[c]] not in l:
                    l.append([nums[a], nums[b], nums[c]])

        return l