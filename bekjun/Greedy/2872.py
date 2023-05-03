
n = int(input())

l = []
for _ in range(n):
    l.append(int(input()))

count = 0
for a in range(len(l)-1,-1,-1):
    if l[a] != n:
        count += 1
    else:
        n -= 1
print(count)




# count = 0

# for a in range(len(l)-1):
#     current_min = min(l[a+1:])
    
#     if current_min < l[a]:
#         tmp = l[a]
#         l[a] = current_min
#         l[l.index(current_min)] = l[a]
#         count += 1
        
# print(count)
    
    
    # if l[start] > l[end]:
    #     tmp = l[start]
    #     l[start] = l[end]
    #     l[end] = l[start]
        

# while l != goal:
    
