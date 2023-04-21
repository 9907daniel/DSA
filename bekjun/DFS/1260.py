# https://www.acmicpc.net/problem/1260
from collections import deque

n,m,v = map(int, input().split())

tree = []
dfs_tree = [[] for _ in range(n+1)]


for _ in range (m):
    a = (list(map(int, input().split())))
    tree.append(a)
    
    dfs_tree[a[0]].append(a[1])
    dfs_tree[a[1]].append(a[0])
    
    
# DFS
for a in range(len(dfs_tree)):
    dfs_tree[a].sort()

visited_dfs = [False]*(10001)
order_dfs = []


def dfs(start, dfs_tree):
    visited_dfs[start] = True
    order_dfs.append(start)
    
    for i in dfs_tree[start]:
        if visited_dfs[i] == False:
            visited_dfs[i] = True
            dfs(i, dfs_tree)
    

# BFS
tree.sort()
tree = sorted(tree, key=lambda x:x[1])
visited = [False]*(10001)

def bfs(start, tree):    
    q = deque()
    q.append(start)
    visited[start] = True
    order = []
    
    while q:
        a = q.popleft()
        order.append(a)
        for b in range(m):
            if tree[b][1] == a and visited[tree[b][0]] == False:
                q.append(tree[b][0])
                visited[tree[b][0]] = True
            if tree[b][0] == a and visited[tree[b][1]] == False:
                q.append(tree[b][1])
                visited[tree[b][1]] = True  
                
    return order             


dfs(v, dfs_tree)
order = bfs(v, tree)

print(*order_dfs)
print(*order)