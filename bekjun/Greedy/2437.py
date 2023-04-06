n = int(input())
l = list(map(int,input().split()))
l.sort()

p = []
n = []

for a in l:
    if a > 0:
        p.append(a)
    else:
        n.append(a)

for a in n:
    if 
        



# target = 1
# for i in l:
#     print(i, target)
#     if target < i:
#         break
#     target += i
#     print(target)
    
# print(target)



# print(l)

# tmp = []
# for a in range(len(l)):
#     tmp.append(l[a])
#     for b in range(a+1,len(l)):
#         tmp.append(l[a+1]+tmp[-1])
        
# # tmp.sort()
# print(tmp)

# d = [[0]]*n

# for a in range(len(l)):
#     d[a][0] = l[a]
#     for b in range(a+1,len(l)):
#         d[a].append(l[b]+d[a][-1])

# tmp = []
# for a in range(len(d)):
#     for b in range(len(d[a])):
#         tmp.append(d[a][b])
# tmp.sort()
# print(tmp)


