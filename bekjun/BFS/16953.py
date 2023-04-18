from collections import deque

n, m = map(int, input().split())

# visited = [0]*m+1

def bfs():
    q = deque()
    q.append((n,0))
    
    while q:
        x, count = q.popleft()
        
        if x == m:
            return count+1
        
        if x < m:
            q.append((x*2, count + 1))
            q.append(((x*10)+1, count + 1))
    return -1

print(bfs())
        
        
