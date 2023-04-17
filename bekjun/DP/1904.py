n = int(input())

d = [0]*(n+1)

d[1] = 1
if n >= 2:
    d[2] = 2

for a in range(3,n+1):
    d[a] = (d[a-1] + d[a-2])%15746

print(d[n])

