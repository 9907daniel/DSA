import copy
t = int(input())
results = []

for _ in range(t):
    n, d = map(int, input().split())
    graph = []

    for _ in range(n):
        graph.append(list(map(int, input().split())))

    def step_one(graph, tmp_graph):
        for a in range(n):
            graph[a][((n+1)//2)-1]= tmp_graph[a][a]
        return graph
    def step_two(graph, tmp_graph):
        for a in range(n):
            graph[a][(n-1)-a] = tmp_graph[a][((n+1)//2)-1]
        return graph
    def step_three(graph, tmp_graph):
        for a in range(n):
            graph[((n+1)//2)-1][(n-1)-a] = tmp_graph[a][(n-1)-a]
        return graph
    def step_four(graph, tmp_graph):
        for a in range(n):
            graph[a][a] = tmp_graph[((n+1)//2)-1][a]
        return graph

    def reverse_one(graph, tmp_graph):
        for a in range(n):
            graph[a][a]= tmp_graph[a][((n+1)//2)-1]
        return graph
    def reverse_two(graph, tmp_graph):
        for a in range(n):
            graph[a][((n+1)//2)-1] = tmp_graph[a][(n-1)-a]
        return graph
    def reverse_three(graph, tmp_graph):
        for a in range(n):
            graph[a][(n-1)-a] = tmp_graph[((n+1)//2)-1][(n-1)-a]
        return graph
    def reverse_four(graph, tmp_graph):
        for a in range(n):
            graph[((n+1)//2)-1][a] = tmp_graph[a][a]
        return graph
                
    if d > 0:
        for _ in range(d//45):
            tmp_graph = copy.deepcopy(graph)
            graph = step_one(graph, tmp_graph)
            graph =step_two(graph, tmp_graph)
            graph = step_three(graph, tmp_graph)
            graph = step_four(graph, tmp_graph)
    else:
        for _ in range(abs(d//45)):
            tmp_graph = copy.deepcopy(graph)
            graph = reverse_one(graph, tmp_graph)
            graph =reverse_two(graph, tmp_graph)
            graph = reverse_three(graph, tmp_graph)
            graph = reverse_four(graph, tmp_graph)
    results.append(graph)
    
for a in results:
    for b in a:
        print(*b)    




