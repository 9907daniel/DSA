from collections import deque

n, m = map(int, input().split())
l = [[]]

for _ in range(m):
    l.append(list(map(int, input().split())))

def bfs(start, l):
    count = [0]*(n+1)
    visited = [start]
    queue = deque([start])
    # visited[start] = 1

    while queue:
        # count += len(queue)
        x = queue.popleft()
        for a in l[x]:
            if a not in visited:
                count[a] += count[x] + 1
                queue.append(a)
                visited.append(a)

    return sum(count)

for a in range(1, n+1):
    print(bfs(a, l))
