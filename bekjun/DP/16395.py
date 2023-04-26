n, k = map(int, input().split())

d = [[1]*31 for _ in range(31)]

d[1][1] = 1
d[2][1] = 1
d[2][2] = 1

for a in range(3, n+1):
    for b in range(2,a):
        d[a][b] = d[a-1][b-1]+d[a-1][b]

print(d[n][k])

