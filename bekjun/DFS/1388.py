n, m = map(int, input().split())

graph = []

for _ in range(n):
    row = input()
    graph.append([a for a in row])
    
visited = [[0]*m for _ in range(n)]

dx = [1,-1,0,0]
dy = [0,0,-1,1]

def dfs(x,y):
    visited[x][y] = 1
    
    if graph[x][y] == '|':
        for i in range(2):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0<=nx<n and 0<=ny<m and graph[nx][ny] == '|' and visited[nx][ny] == 0:
                dfs(nx,ny)
    
    elif graph[x][y] == '-':
        for i in range(2,4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0<=nx<n and 0<=ny<m and graph[nx][ny] == '-' and visited[nx][ny] == 0:
                dfs(nx,ny)
                
    return visited
        
count = 0
for a in range(n):
    for b in range(m):
        if graph[a][b] == '-' and visited[a][b] == 0 or graph[a][b] == '|' and visited[a][b] == 0:
            dfs(a,b)
            count += 1

print(count)