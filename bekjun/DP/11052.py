n = int(input())
l = list(map(int, input().split()))

d = [0]*1001
d[0] = l[0]*n

for a in range(1,n):
    d[a] = d[a-1] + l[0]
    
print(d)

# print(d[n-1])