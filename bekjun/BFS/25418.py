from collections import deque

a, k = map(int, input().split())

def bfs():
    count = 0
    queue = deque()
    queue.append((a,k,count))
    visited = [-1]*(k*2+1)
    
    while queue:
        x, y, z = queue.popleft()

        if x ==y:
            return z

        if x < y and visited[x+1] == -1:
            queue.append((x+1,y, z+1))
            visited[x+1] = 0
        if x < y and visited[x*2] == -1:
            queue.append((x*2,y, z+1))  
            visited[x*2] = 0
    return -1          

print(bfs())
            
    