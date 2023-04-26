
n, m = map(int, input().split())

graph = []

for a in range(n):
    graph.append(list(map(int,input().split())))

dp = [[0]*m for _ in range(n)]

dp[0][0] = graph[0][0]

for a in range(n):
    for b in range(m):
        if a > 0 and b > 0:
            dp[a][b] = graph[a][b] + max(dp[a-1][b], dp[a][b-1])
        elif a >0 and b == 0:
            dp[a][b] = graph[a][b] + dp[a-1][b]
        elif b >0 and a == 0:
            dp[a][b] = graph[a][b] + dp[a][b-1]

            
print(dp[n-1][m-1])


# possible = []
# def dfs(x,y, count):
#     count += graph[x][y]
#     visited[x][y] = True

#     if x == n-1 and y == m-1:
#         possible.append(count)
#         return
        
    
#     for w in range(3):
#         nx = x + dx[w]
#         ny = y + dy[w]
        
#         if 0<=nx<n and 0<=ny<m and visited[nx][ny] == False:
#             dfs(nx,ny, count)
            

# dfs(0,0,0)
            
# print(max(possible))