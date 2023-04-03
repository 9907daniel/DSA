n = int(input())

l = list(map(int, input().split()))

d = l[:]

for a in range(n):
    for b in range(a):
        if l[a] > l[b]:
            d[a] = max(d[a],d[b]+l[a])

print(d)



# for a in range(n):
#     for b in range(0, a):
#         tmp = [0]
#         if l[b] < l[a]:
#             tmp.append(d[b])
#         print(tmp)  
#     d[a] = max(tmp) + l[a]
            
# print(d)
