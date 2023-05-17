from collections import deque
import copy

n, m = map(int, input().split())

graph = []
dx = [-1,1,0,0]
dy = [0,0,-1,1]

for a in range(n):
    graph.append(list(map(int, input().split())))
    

def bfs(coordinates):
    tmp_graph = copy.deepcopy(graph)
    
    q = deque()

    for a in range(n):
        for b in range(m):
            if tmp_graph[a][b] == 2:
                q.append([a,b])
    
    while q:
        x,y = q.popleft()
        for z in range(4):
            nx = dx[z] + x
            ny = dy[z] + y
            if 0<=nx<n and 0<=ny<m and tmp_graph[nx][ny] == 0:
                tmp_graph[nx][ny] = 2
                q.append([nx,ny])

    safezone = 0
    for a in range(n):
        for b in range(m):
            if tmp_graph[a][b] == 0:
                safezone += 1
    
    return safezone
        
current_max = 0
def combinations(start):
    global current_max
    
    if start == 3:
        current_max = max(current_max, bfs(graph))
        return current_max
        
    for a in range(n):
        for b in range(m):
            if graph[a][b] == 0:
                graph[a][b] = 1
                combinations(start+1)
                graph[a][b] = 0

combinations(0)
print(current_max)



# tmp = []
# virus = []
# for a in range(n):
#     for b in range(m):
#         if graph[a][b] == 0:
#             tmp.append([a,b])
#         elif graph[a][b] ==2:
#             virus.append([a,b])
            
# combinations = list(permutations(tmp, 3))

    
    # for a in range(3):
    #     tmp_graph[coordinates[a][0]][coordinates[a][1]] = 1
        
    # for a in range(len(virus)):
    #     q.append([virus[a][0],virus[a][1],0])


# current_max = 0
# for a in range(len(combinations)):
#     current_max = max(current_max, dfs(combinations[a]))