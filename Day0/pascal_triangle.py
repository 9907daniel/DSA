# Input: numRows = 5
# Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

#    1
#   1 1
#  1 2 1
# 1 3 3 1
#1 4 6 4 1

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        answer = []
        for i in range(numRows):
            tmp = []
            for j in range(i+1):
                if j == 0 or j == i:
                    tmp.append(1)
                else:
                    tmp.append(answer[i-1][j-1] + answer[i-1][j])
            answer.append(tmp)
        return answer


# Time Complexity : O(n)
# Take : utilize previous list[i-1] to add

