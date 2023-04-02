n = int(input())
l = []

for a in range(n):
    l.append(int(input()))

d = [0]*(max(l)+1)
d[1] = 1
d[2] = 2
d[3] = 4

for a in l:
    for b in range(4,a+1):
        d[b] = d[b-1]+d[b-2]+d[b-3]
    print(d[a])