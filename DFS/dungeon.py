
n,m = map(int,input().split())
graph = []
res = []

for i in range(n):
    graph.append(list(map(int,input())))
    
def dfs(steps, y,x):
    if x < 0 or y < 0 or x >= m or y >=n:
        return False
    if x == m-1 and y == n-1:
        steps +=1
        res.append(steps)
    
    if graph[y][x] == 1:
        graph[y][x] = 0
        steps += 1
        dfs(steps, y+1, x)
        dfs(steps, y-1, x)
        dfs(steps, y, x+1)
        dfs(steps, y, x-1)
    return False
        

# steps = 0

# for y in range(n):
#     for x in range(m):
#         if graph[y][x] == True:
#             print(steps)
dfs(0,0,0)
print(min(res))

    
            