#######
# 0. m, n, h
# 1. n 단위로 dfs를 끊기
# 2. 하나의 루프가 끝났을떄, 모든 층의 인접 층에 익은 토마토를 복 붙 
#
#
# - 한개 내의 dfs 안에 count 기록
# - max(로 쵯 비교)
######


# - 시작점을 지정안하고 큐에 1을 전부 넣는다
# - 삼차 BFS -> nx,ny,nz (6방햐을 설정해준다)
# - Visited 을 사용하는거를 습관하 시키자
# - 한번에 여러 곳에서 일어나고, 이를 count 하고 싶을때는, 모든 event를 queue에 담아준다.

from collections import deque

m, n, h = map(int, input().split())

graph= []
# [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]],  graph[0]
# [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]],  graph[1]

for _ in range(h): 
    l = []
    for _ in range(n):
        l.append(list(map(int, input().split())))
    graph.append(l)
# print(graph)
    
dx = [1,0,-1,0,0,0]
dy = [0,1,0,-1,0,0]
dz = [0,0,0,0,1,-1]
queue = deque()

visited = [[[False]*m for _ in range(n)]for _ in range(h)]

def bfs():
    while queue:
        a,b,c = queue.popleft()
        
        for i in range(6):
            nx = dx[i] + a
            ny = dy[i] + b
            nz = dz[i] + c

            if 0 <= nx < n and 0 <= ny < m and 0<= nz<h:
                if graph[nz][nx][ny] == 0 and visited[nz][nx][ny] == False:
                    queue.append((nx,ny,nz))
                    graph[nz][nx][ny] = graph[c][a][b] + 1
                    visited[nz][nx][ny] = True
                    
                    
        # if z == 0 and h > 1:
        #     if graph[z+1][a][b] == 0:
        #         graph[z+1][a][b] = 1
        # elif z == h-1 and h > 1:
        #     if graph[z-1][a][b] ==0:
        #         graph[z-1][a][b] = 1
        # elif 0 < z < h-1 and h > 1:
        #     if graph[z+1][a][b] == 0:
        #         graph[z+1][a][b] = 1
        #     if graph[z-1][a][b] ==0:
        #         graph[z-1][a][b] = 1
        
# bfs(graph)

# count = 0
for c in range(h):    
    for a in range(n):
        for b in range(m):
            if graph[c][a][b] == 1 and visited[c][a][b] == 0:
                queue.append((a,b,c))
                visited[c][a][b] = True
bfs()

answer = 0
for a in graph:
    for b in a:
        for c in b:
            if c == 0:
                print(-1)
                exit(0)
        answer = max(answer, max(b))

print(answer-1) 
                
                # print(graph)
                # count += 1

# if 0 in graph:
#     print(-1)
# else:
#     print(count)