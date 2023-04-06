from collections import deque

n = int(input())
m = int(input())
l = []
visited = [False]*n

for a in range(m):
    l.append(list(map(int, input().split())))

count = 0

def bfs(l,start,visited, count):
    queue = deque([start])
    visited[start] = True
    
    while queue:
        x = queue.popleft()
        for i in l[x]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                count += 1
                
bfs(l,0,visited, 0)