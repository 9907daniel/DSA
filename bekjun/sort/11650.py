n = int(input())
l = []

for a in range(n):
    l.append(list(map(int, input().split())))
    
for b in range(len(l)):
    for c in range(b+1, len(l)):
        l.sort


# for b in range(len(l)):
#     for c in range(b+1, len(l)):
#         if l[b][0] == l[c][0]:
#             if l[b][1] > l[c][1]:
#                 l[b][1], l[c][1] = l[c][1], l[b][1]
#         else:
#             if l[b][0] > l[c][0]:
#                 l[b], l[c] = l[c], l[b]
                
# for d in l:
#     print(d[0], d[1])
