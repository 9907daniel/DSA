
# https://leetcode.com/problems/merge-intervals/

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        results = [intervals[0]]
        count = 0
        intervals.pop(0)

        a = 0
        while a < len(intervals):
            b = 0
            while b < len(results)-1:
                if intervals[a][0] >= results[b][0] and intervals[a][0] <= results[b][1]:
                    if intervals[a][1] <= results[b][1]:
                        a += 1
                    else:
                        results.append([results[b][0],intervals[a][1]])
                        results.pop(b)
                elif intervals[a][0] <= results[b][0] and results[b][1] >= intervals[b][1]:
                    results.append([intervals[a][0], results[b][1]])    
                    results.pop(b)
                else:
                    results.append(intervals[a])
                    a += 1
                b += 1
        print(results)