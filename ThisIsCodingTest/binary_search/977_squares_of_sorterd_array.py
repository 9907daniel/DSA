# Given an integer array nums sorted in non-decreasing order, return an array of the squares of 
# each number sorted in non-decreasing order.

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        l = []
        start = 0
        end = len(nums)-1

        while start <= end:
            if nums[start]*nums[start] > nums[end]*nums[end]:
                l.append(nums[start]*nums[start])
                start += 1
            elif nums[start]*nums[start] < nums[end]*nums[end]:
                l.append(nums[end]*nums[end])
                end -=1
            elif nums[start]*nums[start] == nums[end]*nums[end]:
                l.append(nums[start]*nums[start])
                # l.append(nums[end]*nums[end])
                start +=1 
                # end -=1
        return (l[::-1])
        
        # l = []
        # for a in nums:
        #     l.append(a*a)
        # l.sort()
        # return l