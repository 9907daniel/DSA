from collections import deque

n = int(input())
graph = []
termination = [[0]*n for _ in range(n)]

for a in range(n):
    graph.append(list(map(int, input().split())))
    
for a in range(n):
    for b in range(n):
        if graph[a][b] == 9:
            x,y = a,b
        if graph[a][b] == 0:
            termination[a][b] = -1

dx = [1,-1,0,0]
dy = [0,0,-1,1]

def bfs(x,y,size):
    check = [[0]*n for _ in range(n)]
    q = deque()
    q.append((x,y,0))
    check[x][y] = 999
    go = 999
    
    while q:
        a, b, count = q.popleft()
        
        for c in range(4):
            nx = dx[c] + a
            ny = dy[c] + b
            
            if 0<=nx<n and 0<=ny<n and check[nx][ny] == 0 and graph[nx][ny] <= size:
                q.append((nx,ny,count+1))
                check[nx][ny] = count+1
    
    print(check)
    
    for i in range(n):
        for j in range(n):
            if 0 < graph[i][j] < size:
                if go > check[i][j]:
                    current_i = i
                    current_j = j
    
                
                go = min(go, check[i][j])
                
    return current_i,current_j, go


steps = 0 
size_up = 0    
size = 2
           
T = True   
while T:  
    termination[x][y] = -1
        
    if all(val != 0 for row in termination for val in row):
        print(steps)
        break
            
    q,w,e = bfs(x,y,size)

    x = q
    y = w    
    steps += e
    size_up += 1
    
    
    if size_up == size:
        size += 1

print(bfs(2,2,2))
print(bfs(0,3,2))
print(bfs(0,3,3))
        