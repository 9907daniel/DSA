n = int(input())
l = list(map(int, input().split()))

d = [0]*100

d[0] = l[0]
d[1] = max(d[1],l[1])

for a in range(2,n):
    d[a] = max(d[a-2]+l[a], d[a-1])

print(d[n-1])


# for a in range(3,n+1):
#     d[a] = l[a-1] + d[a-2]
# print(d[n])



