
# Given an array of integers temperatures represents the daily temperatures, 
# return an array answer such that answer[i] is the number of days you have to wait 
# after the ith day to get a warmer temperature. 
# If there is no future day for which this is possible, keep answer[i] == 0 instead.


# Unviable solution : time complexity too big
# Too much brute force


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = []
        tmp = []
        for a in range(len(temperatures)):
            count = 0
            for b in range(a,len(temperatures)):
                if temperatures[a] < temperatures[b]:
                    answer.append(count)
                    break
                elif b != len(temperatures)-1 and temperatures[a] >= temperatures[b]:
                    count +=1  
                else: 
                    answer.append(0)
        return answer
