from collections import deque
from itertools import combinations as c

n, m = map(int, input().split())
graph = []

dx = [-1,0,1,0]
dy = [0,1,0,-1]

for a in range(n):
    graph.append(list(map(int, input().split())))
    
tmp = []
for a in range(n):
    for b in range(n):
        if graph[a][b] == 2:
            tmp.append((a,b))
            graph[a][b] = -2
        elif graph[a][b] == 1:
            graph[a][b] = -1

combination = c(tmp, m)

def bfs(graph, x, y):
    queue = deque()
    queue.append([x,y])
    
    while queue:
        i,j = queue.popleft()   
        for c in range(4):
            nx = dx[c] + i
            ny = dy[c] + j      
            if 0<=nx<n and 0<=ny<n:
                if graph[nx][ny] == 0:
                    queue.append([nx,ny])
                    graph[nx][ny] += 1
        # for a in range(n):
        #     for b in range(n):
        #         if graph[a][b] > 0:
        #             graph[a][b] += 1

                        
for c in combination:
    queue = deque()
    for a,b in c:
        queue.append(c)
    
    bfs(graph, a, b)
    
print(graph)
    