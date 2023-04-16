n = int(input())

d = [0]*50000

d[0] = 1
d[1] = 4
d[2] = 9
d[3] = 16

for a in range(4,n):
    d[a] = d[a-1]+d[a-2]


