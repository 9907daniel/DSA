num = int(input())
d = []*(num+1)

for a in range(num):
    k = int(input())
    n = int(input())
    d[k] = [[0]*n]      

print(d)
    
    
    


# d[0] = [1]*n


# for a in range(1, k+1):
#     for b in range(1,n+1):
#         d[a][b] = sum(d[a-1][:b])
        