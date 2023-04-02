n = int(input())
d = [0]*1001


d[1] = 1
d[2] = 3

for i in range(3, n+1):
    d[i] = d[i-1]+ (2*d[i-2])
    
print(d[n])
    



    
# def tiles(n):
#     for i in range(1,n+1):
#         if n == 1:
#             d[1] = 1
#             return d[1]
        
#         elif n == 2:
#             d[2] = 3
#             return d[2]
        
#         elif d[i] != 0:
#             return d[i] + tiles(i-1)
#         else:
#             d[i] = tiles(i-1) +1        
# print(tiles(n))