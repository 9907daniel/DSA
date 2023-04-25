import sys
sys.setrecursionlimit(10000)

m, n, k= map(int, input().split())

graph = [[0]*n for _ in range(m)]

square = []
dx = [1,-1,0,0]
dy = [0,0,1,-1]

for _ in range(k):
    square.append(list(map(int, input().split())))
    

for a in range(len(square)):
    for b in range(square[a][1], square[a][3]):
        for c in range(square[a][0], square[a][2]):
            graph[b][c] = 1


size = 1
# def dfs(x,y):
#     global size
#     stack = [(x,y)]
#     graph[x][y] = 1
    
#     while stack:
#         x, y = stack.pop()
#         for a in range(4):
#             nx = dx[a] + x
#             ny = dy[a] + y
            
#             if 0<=nx<m and 0<=ny<n and graph[nx][ny] == 0:            
#                 size += 1
#                 graph[nx][ny] = 1
#                 stack.append((nx,ny))
#                 # dfs(nx,ny)
#     return size

def dfs(x,y):
    global size
    graph[x][y] = 1
    
    for a in range(4):
        nx = dx[a] + x
        ny = dy[a] + y
        
        if 0<=nx<m and 0<=ny<n and graph[nx][ny] == 0:            
            size += 1
            dfs(nx,ny)
    return size
    

count = 0
area = []
for a in range(m):
    for b in range(n):
        if graph[a][b] == 0:
            count += 1
            size = 1
            area.append(dfs(a,b))

area.sort()
print(count)              
print(*area)


