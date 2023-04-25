import sys
sys.setrecursionlimit(100000)

n = int(input())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

visited = [[False]*n for _ in range(n)]
dx = [1,-1,0,0]
dy = [0,0,1,-1]

cost = []
tmp = 0
four = 0
def dfs(visited, count, tmp):
    # coordiante = []
    # tmp_tmp = tmp
    global four
    if count == 2:
        cost.append(tmp)
        return 
    
    for a in range(n):
        for b in range(n):
            if visited[a][b] == False:
                # copy_visited = visited[:]   
                visited[a][b] = True
                for c in range(4):
                    nx = dx[c] + a
                    ny = dy[c] + b
                
                    if 0<= nx < n and 0<=ny<n and visited[nx][ny] == False:
                        four += 1
                    else:
                        break
                    
                if four == 4:
                    tmp += graph[a][b]
                    for w in range(4):
                        nx = dx[w] + a
                        ny = dy[w] + b
                        visited[nx][ny] = True
                        tmp += graph[nx][ny]
                    dfs(visited, count + 1, tmp)
                    
                    for d in range(4):
                        nx = dx[d] + a
                        ny = dy[d] + b
                        if 0<=nx< n and 0<=ny<n:
                            visited[nx][ny] = False
                            tmp -= graph[nx][ny]
                # tmp = 0
                four = 0
                visited[a][b] = False
    return
                        
dfs(visited, 0, 0)     
print(min(cost))

    

                 