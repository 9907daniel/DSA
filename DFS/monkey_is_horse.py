k = int(input())
w,h = map(int, input().split())
graph = []
for a in range(h):
    graph.append(list(map(int,input().split())))

result = []

def board(graph, x, y, count, k_count):
    # while 0 in graph:
    if x < 0 or y < 0 or x >= w or y >= h:
        return False
    if graph[y][x] == 1:
        return False
    if y == h-1 and x == w-1:
        result.append(k_count + count)

    while k_count < k:
        k_count += 1
        graph[y][x] = 1
        board(graph, x+2, y+1, count, k_count)
        board(graph, x+2, y-1, count, k_count)
        board(graph, x-2, y+1, count, k_count)
        board(graph, x-2, y-1, count, k_count)
        board(graph, x+1, y+2, count, k_count)
        board(graph, x-1, y+2, count, k_count)
        board(graph, x+1, y-2, count, k_count)
        board(graph, x-1, y-2, count, k_count)
    
    if k_count >= k:
        count += 1
        graph[y][x] = 1
        board(graph, x+1, y, count, k_count)
        board(graph, x, y+1, count, k_count)
        board(graph, x-1, y, count, k_count)
        board(graph, x, y-1, count, k_count)

board(graph, 0, 0, 0, 0)
if result == []:
    print(-1)
else: 
    print(result)

    
    
# 0 0 0 0 0 0
# 0 0 0 0 1 0
# 0 0 1 1 1 0
# 0 0 0 1 0 0
# 0 0 0 0 0 0