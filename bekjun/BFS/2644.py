from collections import deque

n = int(input())
x, y = map(int,input().split())

nums = int(input())
graph = []

for a in range(nums):
    graph.append(list(map(int, input().split())))
    
visited = [False]* (n+1)

def bfs(start, end):
    queue =deque()
    queue.append((start, 0))
    
    while queue:
        current, count = queue.popleft()
        
        
        if current == end:
            return count
        
        for b in range(len(graph)):
            if graph[b][0] == current and visited[graph[b][1]] == False:
                queue.append((graph[b][1], count+1))
                visited[current] = True
                
            elif graph[b][1] == current and visited[graph[b][0]] == False:
                queue.append((graph[b][0], count+1))
                visited[current] = True
    return -1
        
print(bfs(x,y))