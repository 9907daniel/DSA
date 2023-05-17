from collections import deque

n ,m = map(int, input().split())

graph = []

for _ in range(n):
    l = [int(b) for b in input()]
    graph.append(l)
        
visited = [[False]*m for _ in range(n)]

dx = [1,-1,0,0]
dy = [0,0,-1,1]

def dfs(x,y, count):
    q = deque()
    q.append((x,y, 0))
    
    while q:
        a,b,c  = q.pop()
        
        visited[a][b] = True
        graph[a][b] = c
        
        for d in range(4):
            nx = dx[d] + a
            ny = dy[d] + b
            
            if 0<=nx<n and 0<=ny<m and visited[nx][ny] == False and graph[nx][ny] == 1:
                q.append((nx,ny, c+1))
    return c
    
print(dfs(0,0,0))

for a in range(n):
    print(*graph[a])


# print(visited[n-1][m-1])
