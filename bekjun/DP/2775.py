T = int(input())
d = [[n+1 for n in range(14)]]
for i in range(14):
    d.append([0]*14)

for a in range(1,15):
    for b in range(14):
        if b == 0:
            d[a][b] = d[a-1][b]
        else:
            d[a][b] = d[a-1][b] + d[a][b-1]

tmp = []
for a in range(T):
    k = int(input())
    n = int(input())
    tmp.append(d[k][n-1])

for a in tmp:
    print(a)
