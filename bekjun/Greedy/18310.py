n = int(input())
l= list(map(int, input().split()))

l.sort()

print(l[(n-1)//2])


# tmp = []
# current = 0
# for a in range(len(l)):
#     current = abs(sum(l) - (n*l[a]))
#     tmp.append(current)
    
# print(l[tmp.index(min(tmp))])
# tmp = []
# current = abs(sum(l) - (n*l[0]))
# top = l[0]
# for a in range(1, len(l)):
#     new = abs(sum(l) - (n*l[a]))
#     if new < current:
#         current = new
#         top = l[a]
    
# print(top)
# print(l[tmp.index(min(tmp))])
