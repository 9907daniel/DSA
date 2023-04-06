from collections import deque

n = int(input())
l = []

for i in range(n):
    x = input()
    l.append([a for a in x])
    
tmp = [[-1]*n for i in range(n)]
    
dx = [-1,0,1,0]
dy = [0,1,0,-1]
x, y = 0, 0

def path():
    
    queue = deque()
    queue.append([0,0])
    tmp[0][0] = 0
    
    while queue:
        x,y = queue.popleft()
        # x = 0, y = 0
        
        for a in range(4):
            nx = dx[a] + x
            ny = dy[a] + y
        
            if nx >= 0 and ny >= 0 and nx < n and ny < n:
                if tmp[nx][ny] == -1:
                    if l[nx][ny] == 0:
                        tmp[nx][ny] = tmp[x][y] + 1
                        queue.append([nx,ny])
                    else:
                       tmp[nx][ny] = tmp[x][y]
                       queue.appendleft([nx,ny])
                
path()
print(tmp[n-1][n-1])