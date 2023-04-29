import sys

sys.setrecursionlimit(10000000)

n, m, k = map(int, input().split())

graph = [[0]*m for _ in range(n)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]

for a in range(k):
    c, d = map(int, input().split())
    graph[c-1][d-1] = 1
    
def dfs(x,y):
    global count
    count += 1
    graph[x][y] = 0
    
    for a in range(4):
        nx = dx[a] + x
        ny = dy[a] + y
        
        if 0<=nx<n and 0<=ny<m and graph[nx][ny] == 1:
            dfs(nx,ny)
        

tmp = []
for a in range(n):
    for b in range(m):
        if graph[a][b] == 1:
            count = 0
            dfs(a,b)
            tmp.append(count)
            
print(max(tmp))

