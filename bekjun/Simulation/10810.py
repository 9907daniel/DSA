n, m = map(int, input().split())
l = []
d = [0]*n

for a in range(m):
    l.append(list(map(int, input().split())))
    
for a in range(len(l)):
    for b in range(l[a][0]-1, l[a][1]):
        d[b] = l[a][2]

for x in range(n):

    print(d[x], '', end='')
