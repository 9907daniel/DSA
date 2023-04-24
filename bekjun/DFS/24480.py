n, m, r = map(int, input().split())

tree = [[] for _ in range(n+1)]
visited = [False] * (n+1)
order = [0]*(n+1)

for _ in range(m):
    a, b = map(int, input().split())
    
    tree[a].append(b)
    tree[b].append(a)
    
count = 1

def dfs(start):
    global count
    visited[start] = True
    
    order[start] = count
    
    tree[start].sort(reverse=True)
    
    for i in tree[start]:
        if not visited[i]:
            count += 1
            dfs(i)

dfs(r)

for a in order[1:]:
    print(a)
