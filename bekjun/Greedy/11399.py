n = int(input())

l = list(map(int,input().split()))

l.sort()
d = [0]*(n)

d[0] = l[0]

for a in range(1,n):
    d[a] = l[a] + d[a-1]
    
print(sum(d))