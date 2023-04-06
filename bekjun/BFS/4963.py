from collections import deque

def bfs(graph, x, y, n, m):
    queue = deque()
    queue.append((x,y))
    
    dx = [-1,0,1,0,-1,-1,1,1]
    dy = [0,1,0,-1,-1,1,-1,1]
    
    while queue:
        a,b = queue.popleft()
        for i in range(8):
            nx = dx[i] + x
            ny = dy[i] +y
            
            if 0<=nx<n and 0<=ny<m:
                queue.append((nx,ny))
                if graph[nx][ny] == 1:
                    graph[nx][ny] = 0
                      
tmp = []

while True:
    y,x = map(int, input().split())
    graph = []
    count = 0
    
    if x == 0 and y == 0:
        break
    else:
        for a in range(x):
            graph.append(list(map(int, input().split())))
    # graph = [list(map(int, input().strip().split())) for _ in range(x)]
            
    for a in range(x):
        for b in range(y):
            if graph[a][b] == 1:
                bfs(graph, 0, 0, a, b)
                count +=1
    
    tmp.append(count)

            
    
for a in tmp:
    print(a)