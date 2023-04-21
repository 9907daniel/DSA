n,m = map(int, input().split())

graph = []

for _ in range(n):
    graph.append(list(map(int,input().split())))
    
dx = [-1,1,0,0]
dy = [0,0,1,-1]

count = []

def dfs(a,b):
    
    graph[a][b] = -1
    
    for i in range(4):
        nx = a + dx[i]
        ny = b + dy[i]

        if 0<= nx < n and 0<= ny < m and graph[nx][ny] == 1:
            dfs(nx,ny)
            

count = 0
for a in range(n):
    for b in range(n):
        if graph[a][b] == 1:
            dfs(a,b)
            count += 1

print(count)
