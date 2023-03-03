# https://leetcode.com/problems/maximum-number-of-balloons/description/

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        count = 0
        count_list = [0,0,0,0,0]
        balloon = ["b","a","l","o","n"]

        for a in text:
            if a in balloon:
                count_list[balloon.index(a)] += 1
        
        while (count_list[0] >= 1 and count_list[1] >= 1 and
            count_list[2] >= 2 and count_list[3] >= 2 and count_list[4] >= 1):

            count_list[0] -= 1
            count_list[1] -= 1
            count_list[4] -= 1
            count_list[2] -= 2
            count_list[3] -= 2
            count += 1
        
        return count