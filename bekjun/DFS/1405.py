k,e,w,s,n = map(int, input().split())

graph = [[False]*(k+2) for _ in range(k+2)]

count = 0
clean_count = 0
dx = [-1,1,0,0]
dy = [0,0,1,-1]

# steps = 0
def dfs(x,y,steps):
    global count, clean_count
    
    if graph[x][y]:
        count += 1
    
    
    graph[x][y] = True
    
    if steps == k:
        clean_count += 1
        return
    
    for a in range(4):
        nx = dx[a] + x
        ny = dy[a] + y
        
        dfs(nx,ny, steps+1)
    
    
        
    


dfs(k//2, k//2, 1)