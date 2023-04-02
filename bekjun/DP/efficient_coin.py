n,m = map(int,input().split())

l = []
for a in range(n):
    l.append(int(input()))

# 10001 은 무한이라는것을 뜻한다 : max is 10000    
d = [10001]*(m+1)
d[0] = 0

# for a in range(m+1):
#     for b in range(l):
#         if a % l[b] == 0:

for i in range(n):
    for j in range(l[i],m+1):
        if d[j-l[i]] != 10001:
            d[j] = min(d[j],d[j-l[i]] + 1)

if d[m] == 10001:
    print(-1)
else:
    print(d[m])