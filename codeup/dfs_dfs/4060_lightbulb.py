import copy 

m, n = map(int, input().split())
graph = []

for a in range(m):
    graph.append(list(map(int,input().split())))

graph2 = copy.deepcopy(graph)

def dfs(y,x):
    if x < 0 or y < 0 or y >= m or x >= n:
        return False
    elif graph[y][x] == 0:
        graph[y][x] = 1
        dfs(y+1,x)
        dfs(y-1,x)
        dfs(y,x+1)
        dfs(y,x-1)
        return True
    else:
        return False

def dfs_off(y,x):
    if x < 0 or y < 0 or y >= m or x >= n:
        return False
    elif graph2[y][x] == 1:
        graph2[y][x] = 0
        dfs_off(y+1,x)
        dfs_off(y-1,x)
        dfs_off(y,x+1)
        dfs_off(y,x-1)
        return True
    else:
        return False

count = 0
for b in range(n):
    for c in range(m):
        if graph[c][b] == 0:
            dfs(c,b)
            count += 1

count_off = 0
for d in range(n):
    for e in range(m):
        if graph2[e][d] == 1:
            dfs_off(e,d)
            count_off += 1
            
print(count, count_off)