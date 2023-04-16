from collections import deque

graph = []
n,m = map(int,input().split())

for a in range(n):
    graph.append([char for char in input()])

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def dfs(x,y,visited):
    q = deque()
    q.append((x,y,0))
    
    visited[x][y] = 0
    
    while q:
        a,b,count = q.popleft()
        
        for c in range(4):
            nx = a + dx[c]
            ny = b + dy[c]
        
            if 0<=nx<n and 0<=ny<m and graph[nx][ny] == 'L' and visited[nx][ny] == -1:
                q.append((nx,ny, count+1))
                visited[nx][ny] = count+1
                    
    compared_max = 0
    # for a in range(n):
    #     compared_max = max(max(visited[a]),compared_max)
    # return compared_max   
    return max(map(max,visited))

        
current_max = 0
compare = 0

for a in range(n):
    for b in range(m):
        visited = [[-1]*m for _ in range(n)]
        
        if graph[a][b] == 'L' and visited[a][b] == -1:
            compare = dfs(a,b,visited)
        
        current_max = max(current_max, compare)
        

print(current_max)


