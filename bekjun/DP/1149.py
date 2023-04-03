n = int(input())
l = []

for a in range(n):
    l.append(list(map(int,input().split())))

d = [[0,0,0]]*1001
d[1] = l[0]

for a in range(2,n+1):    
    # for b in range(l):
    d[a][0] = min(d[a-1][1],d[a-1][2]) + l[a-1][0]
    d[a][1] = min(d[a-1][0],d[a-1][2]) + l[a-1][1]
    d[a][2] = min(d[a-1][1],d[a-1][0]) + l[a-1][2]

print(min(d[n]))
    
