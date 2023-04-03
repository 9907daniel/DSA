# https://www.acmicpc.net/problem/1932

n = int(input())
l = []

for a in range(n):
    l.append(list(map(int, input().split())))

for a in range(1,len(l)):
    for b in range(len(l[a])):
        if b == 0:
            l[a][b] = l[a-1][0] + l[a][b]
        elif b == len(l[a])-1:
            l[a][b] = l[a-1][b-1] + l[a][b]
        else:
            l[a][b] = max(l[a-1][b],l[a-1][b-1]) + l[a][b]

print(max(l[n-1]))