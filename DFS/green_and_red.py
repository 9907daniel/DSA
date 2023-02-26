# 적록색약은 빨간색과 초록색의 차이를 거의 느끼지 못한다. 따라서, 
# 적록색약인 사람이 보는 그림은 아닌 사람이 보는 그림과는 좀 다를 수 있다.

# 크기가 N×N인 그리드의 각 칸에 R(빨강), G(초록), B(파랑) 중 하나를
# 색칠한 그림이 있다. 그림은 몇 개의 구역으로 나뉘어져 있는데, 
# 구역은 같은 색으로 이루어져 있다. 또, 같은 색상이 상하좌우로 인접해 있는 경우에 
# 두 글자는 같은 구역에 속한다. 
# (색상의 차이를 거의 느끼지 못하는 경우도 같은 색상이라 한다)

# https://www.acmicpc.net/problem/10026

from collections import deque

n,m = map(int,input().split())
graph = []

for i in range(n):
    graph.append(list(map(str,input())))
    













# def dfs(y,x):
#     if x < 0 or y < 0 or x >= n or y >= n:
#         return False
    
#     if graph[y][x] != 0:
        
    
    # if graph[y+1][x] == graph[y][x]:
    #     graph[y][x] == 0
    #     dfs(y+1,x)
    #     return True
    # if graph[y-1][x] == graph[y][x]:
    #     graph[y][x] == 0
    #     dfs(y-1,x)
    #     return True
    # if graph[y][x-1] == graph[y][x]:
    #     graph[y][x] == 0
    #     dfs(y,x-1)
    #     return True
    # if graph[y][x+1] == graph[y][x]:
    #     graph[y][x] == 0
    #     dfs(y,x+1)
    #     return True
    # else: 
    #     return False


# count = 0

# for y in range(n):
#     for x in range(m):
#         # if garaph[y][x] != 0:
#             # dfs(y,x)
#         if dfs(y,x) is True:
#             count += 1

# print(count)



            