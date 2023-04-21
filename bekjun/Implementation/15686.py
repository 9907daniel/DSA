from collections import deque
from itertools import combinations

n, m = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
    
visited = [[-1]*n for _ in range(n)]
    
dx = [-1,1,0,0]
dy = [0,0,-1,1]
    

distance = []

def bfs(x,y):
    distance_count = []
    q = deque()
    q.append((x,y, 0))
    visited[x][y] = 0
    
    while q:
        a,b,count = q.popleft()
        
        for c in range(4):
            nx = dx[c] + a
            ny = dy[c] + b
        
            if 0<=nx<n and 0<=ny<n and visited[nx][ny] == -1:
                q.append((nx,ny, count + 1))
                visited[nx][ny] = count + 1
            
    for a in range(n):
        for b in range(n):
            if graph[a][b] == 2:
                distance_count.append(abs((a-x))+abs((b-y)))
                
    return distance_count
                

def graph_reform():
    listed = []
    for a in range(n):
        for b in range(n):
            if graph[a][b] == 1:
                listed.append([a,b])
    



for a in range(n):
    for b in range(n):
        if graph[a][b] == 1:
            distance.append(bfs(a,b))
    
            
print(distance)

