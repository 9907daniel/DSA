n = int(input())
d = [-1] * 50001


d[3],d[5] = 1,1

for a in range(6,n+1):
    if d[a-3] == -1 and d[a-5] == -1:
        d[a] == -1
    else:      
        d[a] = min(d[a-3],d[a-5])+1    


print(d[n])

# for a in range(3,n+1):
#     if a == 3:
#         d[a] = 1
#     elif a == 5:
#         d[a] = 1
#     elif a == 8:
#         d[a] = 2
#     elif a % 3 == 0:
#         d[a] = d[a-3]+1
#     elif a % 5 == 0:
#         d[a] = d[a-5]+1
#     elif a % 8 == 0:
#         d[a] = d[a-8]+2
        
# print(d[n])