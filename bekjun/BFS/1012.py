from collections import deque

def bfs(graph, x,y):
    q = deque()
    q.append((x,y))
    graph[x][y] = 0

    
    while q:
        a,b = q.popleft()

        for w in range(4):
            nx = a + dx[w]
            ny = b + dy[w]
            
            if 0<=nx<n and 0<=ny<m and graph[nx][ny] == 1:
                graph[nx][ny] = 0
                q.append((nx,ny))
    return

t = int(input())
result = []
dx = [0,0,1,-1]
dy = [1,-1,0,0]

for turns in range(t):
    m,n,k = map(int, input().split())

    graph = [[0]*m for _ in range(n)]

    food = []
    for a in range(k):
        x_cord, y_cord = map(int, input().split())
        graph[y_cord][x_cord] = 1
                                
    count = 0
    for a in range(n):
        for b in range(m):
            if graph[a][b] == 1:
                bfs(graph, a,b)
                count += 1
    print(count)
    # result.append(count)

# for a in result:
#     print(a)
