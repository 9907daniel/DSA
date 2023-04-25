import sys
sys.setrecursionlimit(100000000)

n, m = map(int, input().split())

graph = []

for _ in range(n):
    graph.append(list(map(int, input().split())))
    
dx = [-1,1,0,0]
dy = [0,0,-1,1]

count = 0
def dfs(x,y):
    graph[x][y] = 0
    global count
    count += 1
    
    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y
        
        if 0<=nx<n and 0<=ny<m and graph[nx][ny] == 1:
            dfs(nx, ny)
            
    return count

area = []
for a in range(n):
    for b in range(m):
        if graph[a][b] == 1:
            count = 0
            area.append(dfs(a,b))

if len(area) > 0:
    print(len(area))
    print(max(area))
else:
    print(0)
    print(0)
