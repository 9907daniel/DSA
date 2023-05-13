
# 1 - house, 2 - chicken
# chicken 거리 = closest chicken to house
# city chicken 거리 = sum of all chicken 거리

from itertools import combinations

n, m = map(int, input().split())

graph = []
dx = [1,-1,0,0]
dy = [0,0,1,-1]

for _ in range(n):
    graph.append(list(map(int, input().split())))
            
            
coordinate = []
house = []
for a in range(n):
    for b in range(n):
        if graph[a][b] == 2:
            coordinate.append([a,b])
        elif graph[a][b] == 1:
            house.append([a,b])


current_min = 1e8

for a in combinations(coordinate, m):
    town_length = 0

    for b in range(len(house)):
        current = 1e8
        for c in range(len(a)):
            add=0
            add += abs(house[b][0]-a[c][0])
            add += abs(house[b][1]-a[c][1])
            current = min(current, add)
        town_length += current
    current_min = min(current_min, town_length)
    
print(current_min)
            

# results = []
# tmp = []
# visited= [False for _ in range(len(coordinate))]

# def combinations(start):
#     if start == m:
#         results.append(tmp[:])
#         return
    
#     for a in range(start, len(coordinate)):
#         if visited[a] != True:
#             tmp.append(coordinate[a])
#             visited[a] = True
#             combinations(start+1)
#             tmp.pop()
#             visited[a] = False


# combinations(0)


# tmp_graph = [[999]*n for _ in range(n)]
# distance_graph = [[0]*n for _  in range(n)]

# def dfs(x,y, count, map_visited):
#     map_visited[x][y] = True
#     if graph[x][y] == 2:
#         print(tmp_graph[x][y], count)

#         tmp_graph[x][y] = min(count, tmp_graph[x][y])
    
#     for a in range(4):
#         nx = dx[a] + x
#         ny = dy[a] + y
        
#         if 0<=nx<n and 0<=ny<n and map_visited[nx][ny] == False:
#             dfs(nx,ny, count+1, map_visited)
            
# for a in range(n):
#     for b in range(n):
#         if graph[a][b] == 1:
#             map_visited = [[False]*n for _ in range(n)]
#             dfs(a,b, 0, map_visited)

# # combinations(0)
# # print(tmp_graph)





