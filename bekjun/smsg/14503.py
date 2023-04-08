from collections import deque

n, m = map(int, input().split())

r,c,d = map(int, input().split())

dx = [-1,0,1,0]
dy = [0,1,0,-1]
graph = []
visited = [[-1]*m for _ in range(n)]
count = 0

for a in range(n):
    graph.append(list(map(int, input().split())))
    
def dfs():
    q = deque()
    q.append((r,c,d,1))
    visited[r][c] = 1
    graph[r][c] = -1
    
    while q:

        x,y,direction,count = q.popleft()
        check = 0

        for a in range(4):
            nx = x + dx[a]
            ny = y + dy[a]
            
            if 0<=nx<n and 0<=ny<m:
                if visited[nx][ny] != -1 or graph[nx][ny] == 1:
                    check += 1
                             
        if check == 4:
            if direction == 0:
                if graph[x+1][y] != 1:
                    q.append((x+1,y,direction, count))
                    graph[x+1][y] = -1
                    visited[x+1][y] = 1
                else:
                    return count
            elif direction == 1:
                if graph[x][y-1] != 1:
                    q.append((x,y-1,direction, count))
                    graph[x][y-1] = -1
                    visited[x][y-1] = 1
                else:
                    return count
            elif direction == 2:
                if graph[x-1][y] != 1:
                    q.append((x-1,y,direction, count))
                    graph[x-1][y] = -1
                    visited[x-1][y] = 1                
                else:
                    return count
            elif direction == 3:
                if graph[x][y+1] != 1:
                    q.append((x,y+1,direction, count))
                    graph[x][y+1] = -1
                    visited[x][y+1] = 1
                else:
                    return count
        else:
            if direction == 0:   
                compass = 3
            elif direction == 1:
                compass = 0
            elif direction == 2:
                compass = 1
            elif direction == 3:
                compass = 2
                
            move_x = x + dx[compass]
            move_y = y + dy[compass]

            for _ in range(4):
                if 0<=move_x<n and 0<=move_y<m and graph[move_x][move_y] == 0:
                    q.append((move_x,move_y,compass, count+1))
                    graph[move_x][move_y] = -1
                    visited[move_x][move_y] = 1
                    break
                else:
                    if compass == 0:
                        compass= 3
                    else:     
                        compass -= 1
                move_x = x + dx[compass]
                move_y = y + dy[compass]
print(dfs())

                            