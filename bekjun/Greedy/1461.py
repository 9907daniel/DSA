n, m = map(int,input().split())
l = list(map(int,input().split()))
l.sort()

p = []
n = []
count = 0


if abs(l[0]) < l[-1]:
    l.reverse()
    
while True:
    if len(l) <= m:
        





# for a in l:
#     if a > 0:
#         p.append(a)
#     else:
#         n.append(a)
# p.reverse()

# while True:
#     if len(n) <= m:
#         count += abs(min(n))
#         break
#     # else:
#     count += abs(n[-m])
#     n = n[:-m]
        
# while True:
#     if len(p) <= m:
#         print(max(p))
#         count += max(p)
#         break
#     # else:
#     print(p, p[-m])
#     count += p[-m]
#     p = p[:-m]
# print(count)
    
    
        
    
    
    
    
    
    
    
    
    
    
    

# if l[0] < 0 and abs(l[0]) > l[-1]:
#     pass
# else:
#     l.reverse()

# while True:
#     print(l)
#     print(count)
#     if len(l) <= m:
#         count += l[0]
#         break
#     else:
#         if l
#         count += (abs(l[-1])*2)
        
#     for a in range(m):
#         l.pop()
# print(count)