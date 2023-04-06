from collections import deque
n = int(input())
graph = []

for a  in range(n):
    tmp = [-1]*n
    graph.append(tmp)

r1,c1,r2,c2 = map(int, input().split())

d = [(-2,-1),(-2,1),(0,-2),(0,2),(2,-1),(2,1)]


def bfs(x,y):
    queue = deque([r1,c1])
    graph[x][y]= 0

    while queue:
        x,y = queue.popleft()
        
        for dy, dx in d:
            nx = dx+x
            ny = dy+y
            
            if 0<=nx<n and 0<=ny<n and graph == -1:
                queue.append((nx,ny))
                graph[nx][ny] = graph[x][y]

bfs(r1,r2)
                
print(graph[r2][c2])
                
    
    
    