list1 = list(map(int, input().split()))

list2 = list(map(int, input().split()))

dict1 = {}
dict2 = {}
tmp = set()

for a in list1:
    if a not in dict1:
        dict1[a] = 0
    dict1[a] += 1
    
for a in list2:
    if a not in dict1:
        dict1[a] = 0
    
for a in list2:
    if a not in dict2:
        dict2[a] = 0
    dict2[a] += 1
    
for a in list1:
    if a not in dict2:
        dict2[a] = 0
        
def combination(start, count):
    if start == 4:
        tmp.add(count)
        return
    
    if start % 2 == 0:
        for key,val in dict1.items():
            if val != 0:
                dict1[key] -= 1
                if key not in dict2:
                    dict2[key] = 0
                dict2[key] += 1
                combination(start+1, count-key)
                dict1[key] += 1
                dict2[key] -= 1
    else:
        for key,val in dict2.items():
            if val != 0:
                dict2[key] -= 1
                if key not in dict1:
                    dict1[key] = 0
                dict1[key] += 1
                combination(start+1, count+key)
                dict1[key] -= 1
                dict2[key] += 1
            
combination(0, 1000)
print(len(tmp))
                
# visited1 = [False*11]
# visited2 = [False*11]

# count = 0
# def combination(start):
#     if start == 5:
#         tmp.append(count)
    
#     if start % 2 == 0:
#         for a in range(len(list1)):
#             if visited1[a] == False:
#                 visited1[a] = True
#                 list2.append(list1[a])
#                 list1.pop()
                
#                 combination(start+1)
                
#                 list2.append(list1[a])
                
#                 list2.pop()
                
#                 list2[a] = False
#     else:
#         for a in range(len(list1)):
#             if visited[a] == False:
#                 visited[a] = True
#                 tmp.append(list1[a])
#                 combination(start+1)
#                 visited[a] = False
#                 tmp.pop()

