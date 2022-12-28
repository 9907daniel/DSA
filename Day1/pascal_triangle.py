


class Solution:
    def generate(numRows: int):
        initial_list = [1]
        empty_list = []
        
        n = 0
        m = 0
        while n < numRows: 
            for i in initial_list:
                try:
                    if initial_list[m]:
                        empty_list[m] = initial_list[m] + initial_list[m+1]
                        m += 1
                except:
                    empty_list[m] = initial_list[m]
                    m+=1
            n += 1
            
    
    print(generate(1))
        
        # n = 0
        # while n < numRows:
            
        #     # empt_dic[round(n/2)] == 
        #     for i in empt_dic:
        #         empt_dic[n]
            
        #     n += 1 
        


# Input: numRows = 5
# Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

#    1
#   1 1
#  1 2 1
# 1 3 3 1
#1 4 6 4 1