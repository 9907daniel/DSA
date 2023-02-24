# Using Monotonic Stack

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #[30,40,50,60]
    
        res = [0]*len(temperatures)
        #[0][0][0][0]
        stack = []

        for i,t in enumerate(temperatures):
          # 0 30
          # 1 40
          # 2 50
          # 3 60
            while stack and t>stack[-1][0]:
                stackT, stackInd = stack.pop()
                res[stackInd] = (i-stackInd)
            stack.append([t, i])
            # 30 0
        return res