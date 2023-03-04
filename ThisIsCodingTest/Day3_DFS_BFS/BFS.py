from collections import deque

def bfs(graph, start):
    queue = deque([start])
    visited = [False]*len(graph)
    
    while queue:
        v = queue.popleft()
        visited[v] = True
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


# https://www.youtube.com/watch?v=xlVX7dXLS64