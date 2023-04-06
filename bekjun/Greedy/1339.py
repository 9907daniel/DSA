n = int(input())
l = []
d = [0]*100

for a in range(n):
    l.append(input())
    
for a in range(len(l)):
    for b in range(len(l[a])):
        d[ord(l[a][b])] += 1
    
print(d)
    
# for a in range(len(l[1])):
#     d[ord(l[0][a])] += 1
    
# d.sort()
# d.reverse()
# # for a in range(10):
# #     for b in range(d[a]):
# #         d[a][b] = d[a][b]*d[a][b]
        
# print(d)
# # print(sum(d))
    