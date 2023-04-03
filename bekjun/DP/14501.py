# https://www.acmicpc.net/problem/14501

n = int(input())
l = []
d = [0]*16

for b in range(n):
    l.append(list(map(int,input().split())))

for a in range(n):
    for b in range(a+l[a][0], n):
        if d[b] < d[a] + l[a][1]:
            d[b] = d[a] + l[a][1]

print(max(d))

