
#
# amount of friends 2 3 .... n n+1
#
#
# 2 - 11
# 2 3 4 5 6 8 9 10 
# 
# n
#
# n + 1
#

import math

class UserMainCode(object):
    @classmethod

    def primecheck(self, n:int):
        count = 2
        while count in range(int(math.sqrt(n))):
            if n % 1 ==0:
                return False
            count += 1
        return True
        
    def friendsGroups(self, n=int(input())):
        tmp = (n+1)/2
        count =1
        
        if tmp % 2 == 0:
            tmp  += 1
        else:
            tmp += 2

        for a in range(int(tmp), n+1):
            if self.primecheck(a):
                count += 1
            a += 2
        print(count)
                
    # print(friendsGroups(5))

userCode = UserMainCode()
userCode.friendsGroups()
