from collections import deque

n = int(input())
graph1 = []
graph2 = []

for _ in range(n):
    x = input()
    graph1.append([a for a in x])
    graph2.append([a for a in x])
    
for a in range(n):
    for b in range(n):
        if graph2[a][b] == 'G':
            graph2[a][b] = 'R'
     
dx = [-1,1,0,0]
dy = [0,0,-1,1]

    
def bfs(a,b,color, graph):
    q = deque()
    q.append((a,b))
    graph[a][b] = 0
    
    while q:
        x,y = q.popleft()
    
        for c in range(4):
            nx = dx[c] + x
            ny = dy[c] + y
            
            if 0<=nx<n and 0<=ny<n:
                if graph[nx][ny] == color:
                    q.append((nx,ny))
                    graph[nx][ny] = 0

count = 0
count2 = 0


for a in range(n):
    for b in range(n):
        if graph1[a][b] == 'R' or graph1[a][b] == 'G' or graph1[a][b] == 'B':
            bfs(a,b,graph1[a][b], graph1)
            count += 1

for a in range(n):
    for b in range(n):
        if graph2[a][b] == 'R' or graph2[a][b] == 'B':
            bfs(a,b,graph2[a][b], graph2)
            count2 += 1
                   
print(count)
print(count2)