n,m,r = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

type = list(map(int, input().split()))

def one(graph):
    start = 0
    end = n-1
    while start < end:
        tmp = graph[start]
        graph[start] = graph[end]
        graph[end] = tmp
        start += 1
        end -= 1
    return graph

def two(graph):
    start = 0
    end = m-1
    while start < end:
        for a in range(n):
            tmp = graph[a][start]
            graph[a][start] = graph[a][end]
            graph[a][end] = tmp
        start += 1
        end -= 1
    return graph

def three(graph,n,m):
    start = 0
    end = n-1
    new_graph = [[0]*n for _ in range(m)]
    while end >= 0:
        tmp = []
        for a in range(m):
            tmp.append(graph[start][a])
        for b in range(len(tmp)):
            new_graph[b][end] = tmp[b]
        start += 1
        end -= 1
    return new_graph, n, m

def four(graph,n,m):
    start = 0
    new_graph = [[0]*n for _ in range(m)]
    while start < n:
        tmp = []
        for a in range(m):
            tmp.append(graph[start][a])
        tmp.reverse()
        for b in range(m):
            new_graph[b][start] = tmp[b]
        start += 1
    return new_graph, n, m

def five(graph):
    new_graph = [[0]*m for _ in range(n)]

    for c,a in enumerate(graph):
        for b in range(len(a)):
            if c <= (n//2)-1 and b <= (m//2)-1:
                new_graph[c][b+((m//2))] = a[b]
                
            elif c <= (n//2)-1 and b > (m//2)-1:
                new_graph[c+(n//2)][b] = a[b]
                
            elif c > (n//2)-1 and  b <= (m//2)-1:
                new_graph[c-(n//2)][b] = a[b]                
                
            elif c > (n//2)-1 and b > (m//2)-1:
                new_graph[c][b-((m//2))] = a[b]
    return new_graph
    
def six(graph):
    new_graph = [[0]*m for _ in range(n)]

    for c,a in enumerate(graph):
        for b in range(len(a)):
            if c <= (n//2)-1 and b <= (m//2)-1:                
                new_graph[c+(n//2)][b] = a[b]

            elif c <= (n//2)-1 and b > (m//2)-1:
                new_graph[c][b-((m//2))] = a[b]
                
            elif c > (n//2)-1 and  b <= (m//2)-1:
                new_graph[c][b+((m//2))] = a[b]                
                
            elif c > (n//2)-1 and b > (m//2)-1:
                new_graph[c-(n//2)][b] = a[b]
                
    return new_graph
    
    
for a in type:
    if a == 1:
        graph = one(graph)
    elif a == 2:
        graph = two(graph)
    elif a == 3:
        graph, m ,n = three(graph, len(graph), len(graph[0]))
    elif a ==4:
        graph, m, n = four(graph, len(graph), len(graph[0]))
    elif a==5:
        graph = five(graph)
    elif a==6:
        graph = six(graph)


for a in graph:        
    print(*a)






