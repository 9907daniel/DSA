k = int(input())
w,h = map(int, input().split())
graph = []
for a in range(h):
    graph.append(list(input().split()))

result = []

def board(graph, x, y, count, k_count):
    # print(count)
    if x < 0 or y < 0 or x >= w or y >= h:
        return False
    if graph[y][x] == 1:
        return False
    if y == h-1 and x == w-1:
        print(count)
        # result.append(count)
    count += 1

    while k_count < k:
        # count += 1
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
        # count += 1
        graph[y][x] = 1
        board(graph, x+1, y, count, k_count)
        board(graph, x-1, y, count, k_count)
        board(graph, x, y+1, count, k_count)
        board(graph, x, y-1, count, k_count)

board(graph, 0, 0, 0, 0)
# print(min(result))

    
    
    
    
    
