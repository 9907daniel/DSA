n = int(input())

graph = [[0]*n for _ in range(n)]
visited = [[False]*n for _ in range(n)]

dx = [-1,1,0,0,-1,-1, 1, 1]
dy = [0,0,1,-1,-1, 1, -1, 1]


global_terminate = False
def north(x,y):
    global global_terminate
    if graph[x][y] ==1:
        global_terminate = True
        return False
    visited[x][y] = True
    if x-1 >= 0:    
        return north(x-1,y)
def south(x,y):
    global global_terminate
    if graph[x][y] ==1:
        global_terminate = True
        return False
    visited[x][y] = True
    if x+1 < n:    
        return north(x+1,y)
        
def east(x,y):
    global global_terminate
    if graph[x][y] ==1:
        global_terminate = True
        return False
    visited[x][y] = True
    if y+1 < n:    
        return east(x,y+1)
    
def west(x,y):
    global global_terminate
    if graph[x][y] ==1:
        global_terminate = True
        return False
    visited[x][y] = True
    if y-1 >= 0:    
        return east(x,y-1)
        
def northwest(x,y):
    global global_terminate
    if graph[x][y] ==1:
        global_terminate = True
        return False
    visited[x][y] = True
    if x-1 >= 0 and y-1 >=0:    
        return north(x-1,y-1)
        
def northeast(x,y):
    global global_terminate
    if graph[x][y] ==1:
        global_terminate = True
        return False
    visited[x][y] = True
    if x-1 >= 0 and y+1 < n:    
        return north(x-1,y+1)
        
def southwest(x,y):
    global global_terminate
    if graph[x][y] ==1:
        global_terminate = True
        return False
    visited[x][y] = True
    if x+1 < n and y-1 >= 0:    
        return north(x+1,y-1)
    
def southeast(x,y):
    global global_terminate
    if graph[x][y] == 1:
        global_terminate = True
        return False
    visited[x][y] = True
    if x+1 < n and y+1 < n:    
        return north(x+1,y+1)


count = 0
def combinations(start, visited):
    global count
    global global_terminate
    if start == n:
        count += 1
        return
        
    for a in range(n):
        for b in range(n):
            if visited[a][b] == False:
                tmp_visited = visited[:]
                visited[a][b] = True
                graph[a][b] = 1
                
                for c in range(8):
                    nx = dx[c] + a
                    ny = dy[c] + b
                    
                    if 0<=nx<n and 0<=ny<n:
                        if c == 0:
                            north(nx,ny)
                        if c == 1:
                            south(nx,ny)                            
                        if c == 2:
                            east(nx,ny)                
                        if c == 3:
                            west(nx,ny)     
                        if c == 4:
                            northwest(nx,ny)
                        if c == 5:
                            northeast(nx,ny)
                        if c == 6:
                            southwest(nx,ny)                            
                        if c == 7:
                            southeast(nx,ny)  
                            
                if global_terminate == False:
                    combinations(start+1, visited)

                global_terminate = False
                visited = tmp_visited
                graph[a][b] = 0

     
combinations(0, visited)
print(count)

