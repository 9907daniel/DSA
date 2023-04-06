from collections import deque

def bfs(graph, x, y, n, m):
    queue = deque()
    queue.append((x,y))
    
    dx = [-1,0,1,0,-1,-1,1,1]
    dy = [0,1,0,-1,-1,1,-1,1]
    
    while queue:
        a,b = queue.popleft()
        for i in range(8):
            nx = dx[i] + a
            ny = dy[i] + b
            
            if 0<=nx<n and 0<=ny<m:
                if graph[nx][ny] == 1:
                    queue.append((nx,ny))
                    graph[nx][ny] = 0
                      
tmp = []
while True:
    m,n = map(int, input().split())
    
    if m == 0 and n == 0:
        break
    
    graph = []
    count = 0
    
    for _ in range(n):
        graph.append(list(map(int, input().split())))
            
    for a in range(n):
        for b in range(m):
            if graph[a][b] == 1:
                bfs(graph, a, b, n, m)
                count +=1
    
    tmp.append(count)
    
for a in tmp:
    print(a)