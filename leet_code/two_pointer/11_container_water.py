# https://leetcode.com/problems/container-with-most-water/

class Solution:
    def maxArea(self, height: List[int]) -> int:

        water = []
        start = 0
        end = len(height)-1
        if len(height) > 2:
            while start <= end:
                if min(height[start+1],height[end])-min(height[start],height[end]) > 1:
                    start += 1
                elif min(height[start],height[end-1])-min(height[start],height[end]) >1:
                    end -= 1
                else:
                    water.append((end-start)*min(height[start],height[end]))
                    start += 1
                    end -= 1
        else:
            return min(height)
        return max(water)