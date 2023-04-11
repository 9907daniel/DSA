# https://www.acmicpc.net/problem/2748
# 피보나치 2

n = int(input())
d = [0]*93
d[0] = 0
d[1] = 1

for a in range(2,n+2):
    d[a] = d[a-1] + d[a-2]
    
print(d[n])