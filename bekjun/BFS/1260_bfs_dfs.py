from collections import deque

m,n,i = map(int,input().split())
graph = [] 

for a in range(n):
    graph.append(list(input().split()))
    
    
def bfs(graph, i):
    queue = deque(graph[i])
    visited = []
    
    while queue:
        v = queue.popleft()
        visited.append(v)
        print(queue)
        for a in v:
            if a not in visited:
                queue.append(a)

bfs(graph, 0)
                

