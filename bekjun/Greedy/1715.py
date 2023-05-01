import heapq

n = int(input())

l = []

for _ in range(n):
    l.append(int(input()))
    
heapq.heapify(l)

if len(l) == 1:
    print(0)
else:
    compound = 0

    while len(l) > 1:
        a1 = heapq.heappop(l)
        a2 = heapq.heappop(l)
        compound += a1+a2
        heapq.heappush(l, a1+a2)
        
    print(compound)



# for a in range(len(l)):
#     tmp = l[a] + l[a+1]
    
    
    
    
    
    
#     tmp = l[a] + l[a+1]
#     compount += tmp
#     l.append(tmp)
#     l[a] = 0
#     l[a+1] = tmp
#     l.sort()

# print(compount)

# compound = 0
# tmp = 0
# while len(l) > 1:
#     min_a = min(l)
#     l.pop(l.index(min_a))
#     min_b = min(l)
#     l.pop(l.index(min_b))
#     tmp = min_a+min_b
#     compound += min_a+min_b
    
#     l.append(tmp)

# print(compound)
    
    
    # compound += l[a] + l[a+1]



# tmp = l[0]+l[1]
# result = l[0]+l[1]
# for a in range(3, len(l)-1, 2):
#     if tmp < l[a]:
#         tmp = l[a] + tmp
#         result += tmp
#     else:
#         tmp = l[a] + l[a+1]
#         result += tmp
