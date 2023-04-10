from collections import deque

n = int(input())
m = int(input())
graph = []
visited = [False]*(m+1)

for a in range(m):
    graph.append(list(map(int, input().split())))


def bfs(i,j, a):
    # count = 0
    q = deque()
    q.append((i,j))
    visited[a] = True
    checked = []
    
    while q:
        x, y = q.popleft()
        
        for a in range(m):
            if visited[a] != True:
                if graph[a][0] == x or graph[a][1] == y or graph[a][1] == x or graph[a][0] == y:
                    if graph[a][0] not in checked:
                        checked.append(graph[a][0])
                    if graph[a][1] not in checked:
                        checked.append(graph[a][1])
                    
                    q.append((graph[a][0],graph[a][1]))
                    visited[a] = True

    print(checked)
    return len(checked)-1

count = 0
for a in range(m):
    if graph[a][0] == 1 or graph[a][1] == 1:
        print(bfs(graph[a][0],graph[a][1], a))
        count += 1
        break
    
if count == 0:
    print(count)

        
