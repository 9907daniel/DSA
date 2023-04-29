from itertools import permutations

n = int(input())

l = list(map(int, input().split()))

multiple = list(map(int, input().split()))
spreaded = []
for a in range(len(multiple)):
    for b in range(multiple[a]):
        spreaded.append(a+1)


visited = [False for _ in range(len(spreaded))]

tmp = []
calculated = []
count = 0

def combinations(tmp):
    global count
    for a in range(len(l)):
        if a == 0:
            count += l[a]
        else:
            if tmp[a-1] == 1:
                count += l[a]
            elif tmp[a-1] == 2:
                count -= l[a]
            elif tmp[a-1] == 3:
                count = count * l[a]
            elif tmp[a-1] == 4:
                if count < 0 :
                    count = (count // l[a])+1
                else:
                    count = count//l[a]
    calculated.append(count)
    count =0
    return
    
new_combinations = list(permutations(spreaded, len(spreaded)))
for a in new_combinations:
    combinations(a)

print(max(calculated))
print(min(calculated))
    
    
    # for a in range(len(spreaded)):
    #     if visited[a] == False:
    #         tmp.append(spreaded[a])
    #         visited[a] = True
    #         combinations(start + 1)
    #         tmp.pop()
    #         visited[a] = False
    


# def combinations(start):
#     global count
    
#     if len(tmp) == len(spreaded):
#         for a in range(len(l)):
#             if a == 0:
#                 count += l[a]
#             else:
#                 if tmp[a-1] == 1:
#                     count += l[a]
#                 elif tmp[a-1] == 2:
#                     count -= l[a]
#                 elif tmp[a-1] == 3:
#                     count = count * l[a]
#                 elif tmp[a-1] == 4:
#                     if count < 0 :
#                         count = (count // l[a])+1
#                     else:
#                         count = count//l[a]
#         calculated.append(count)
#         count =0
#         return
    
#     new_combinations = list(permutations())

    
#     for a in range(len(spreaded)):
#         if visited[a] == False:
#             tmp.append(spreaded[a])
#             visited[a] = True
#             combinations(start + 1)
#             tmp.pop()
#             visited[a] = False
    
    
# combinations(0)
# print(max(calculated))
# print(min(calculated))