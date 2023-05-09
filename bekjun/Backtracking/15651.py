from collections import deque

n, m = map(int, input().split())

l = []
tmp = []
def combinations(start):
    if len(tmp) == m:
        l.append(tmp[:])
        return
    
    for a in range(1, n+1):
        tmp.append(a)
        combinations(start+1)
        tmp.pop()
        
combinations(0)

for a in range(len(l)):
    print(*l[a])
