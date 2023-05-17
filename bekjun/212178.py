from itertools import permutations

n, m = map(int, input().split())

l = []

for _ in range(m):
    l.append(list(map(int, input().split())))
    
tmp_l = [a for a in range(1,n+1)]
    
combi = list(permutations(tmp_l, 2))

# visited = [[False]*(n+1)]
    

def dfs(chicken_location, start, count, distance, node_visited):
    
    node_visited[start] = True
    
    if chicken_location[start]:
        distance.append(count*2)
    
    for a in range(len(l)):
        if l[a][0] == start and node_visited[start] != True:
            dfs(chicken_location, l[a][0], count + 1, distance, node_visited)
        if l[a][1] == start and node_visited[start] != True:
            dfs(chicken_location, l[a][1], count + 1, distance, node_visited)

    return distance
    
results = []

for a in range(len(combi)):
    visited = [False for _ in range(n+1)]
    visited[combi[a][0]] = True
    visited[combi[a][1]] = True    
    
    tmp = []
    node_visited = [False for _ in range(n+1)]
    for a in range(n):
       results.append(dfs(visited, a, 0, tmp, node_visited))
       
print(results)



