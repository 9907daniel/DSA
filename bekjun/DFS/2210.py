graph = []

for _ in range(5):
    graph.append(list(map(int, input().split())))
    
combinations = []

dx = [-1,1,0,0]
dy = [0,0,1,-1]

def dfs(x,y, tmp):
    if len(tmp) == 6:
        if tmp not in combinations:
            combinations.append(list(tmp))
        return
    else:
        for a in range(4):
            nx = dx[a] + x
            ny = dy[a] + y 
            if 0<=nx<5 and 0<=ny<5 and len(tmp) < 6:
                tmp.append(graph[nx][ny])
                dfs(nx,ny, tmp)
                tmp.pop()
    

for a in range(5):
    for b in range(5):
        empty = []
        empty.append(graph[a][b])
        dfs(a,b, empty)
        
print(len(combinations))