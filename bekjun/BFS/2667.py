from collections import deque

n = int(input())
graph = []

for a in range(n):
    graph.append(list(map(int, input())))
   
dx = [0,-1,0,1]
dy = [1,0,-1,0]
count = 0

def bfs(graph, x, y):
    if graph[x][y] == 0:
        return 0
    
    queue = deque()
    queue.append((x,y))
    house = 0
    numbs = []
    while queue:
        x,y = queue.popleft()
        if (x,y) not in numbs:
           numbs.append((x,y))
    
        for a in range(4):
            nx = x + dx[a]
            ny = y + dy[a]

            if 0<=nx<n and 0<=ny<n:
                if graph[nx][ny] == 1:
                    queue.append((nx,ny))
                    # house += 1
                    graph[nx][ny] = 0
    # return house
    return len(numbs)

tmp = []

for a in range(len(graph)):
    for b in range(len(graph)):
        if graph[a][b] == 1:
            count += 1
            x = bfs(graph, a, b)
            tmp.append(x)

              
print(count)
tmp.sort()

for a in tmp:
    print(a)