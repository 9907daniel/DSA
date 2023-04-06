n = int(input())
x, y = 1, 1

plans = input().split()

dx = [0,0,-1,1]
dy = [-1,1,0,0]
moves = ['L','R','U','D']

for plan in plans:
    for i in range(len(moves)):
        if plan == moves[i]:
            nx = dx[i] + x
            ny = dy[i] + y
        
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    
    x,y = nx, ny
    
print(x,y)
    


# l = list(input().split())

# cx = 1
# cy = 1

# dx = [0,-1,0,1]
# dy = [1,0,-1,0]

# for a in range(len(l)):
#     # if 
    
#     if l[a] == 'D':
#         if cy+1 <= n:
#             cy += dy[0]     
#     elif l[a] == 'U':
#         if cy-1 >= 1:
#             cy += dy[2]
#     elif l[a] == 'R':
#         if cx+1 <= n:
#             cx += dx[3]
#     elif l[a] == 'L':
#         if cx-1 >= 1:
#             cx += dx[1]
            
# print(cx, cy)
    
        
    
    
     