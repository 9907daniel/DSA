import sys
sys.setrecursionlimit(100000000)

# 1) executre first order
# 2) if 1 -> clockwise, if -1 -> anticlockwise, if 0 -> clockwise
# 3) record if 1 / -1
# 4) rotate designated clock
# 5) for loop the 4 clocks (if not rotated)
# 6) if graph[a][1] != graph[a][2] -> anti-rotate

graph = []
for _ in range(4):
    l = list(input())
    graph.append([int(a) for a in l])

k = int(input())
order = []
for _ in range(k):
    order.append(list(map(int, input().split())))
    

def clock_rotation(clock_num, direction):
    first_right = graph[0][2]
    second_left = graph[1][2]
    second_right = graph[1][6]
    third_left = graph[2][2]
    third_right = graph[2][6]
    fourth_left = graph[3][6]
    
    rotated = [False for a in range(4)]
    
    if clock_num == 0:
        if direction == 1:
            if second_right != first:
                anti_clock_rotation(1, count+1)
        else:
            pass
            
            
    if clock_num == 1:
        if graph[0][2] != graph[1][6]:
            anti_clock_rotation(0)
        if graph[2][6] != graph[1][2]:
            anti_clock_rotation(2)
    if clock_num == 2:
        if graph[1][2] != graph[2][6]:
            anti_clock_rotation(1)
        if graph[3][6] != graph[2][2]:
            anti_clock_rotation(3)
    if clock_num == 3:
        if graph[2][2] != graph[3][6]:
            anti_clock_rotation(2)
            
    tmp = graph[clock_num][0]
    graph[clock_num][0] = graph[clock_num][7]
    graph[clock_num][7] = graph[clock_num][6]
    graph[clock_num][6] = graph[clock_num][5]
    graph[clock_num][5] = graph[clock_num][4]
    graph[clock_num][4] = graph[clock_num][3]
    graph[clock_num][3] = graph[clock_num][2]
    graph[clock_num][2] = graph[clock_num][1]
    graph[clock_num][1] = tmp
    

    return
            
                        
def anti_clock_rotation(clock_num, count):
    tmp = graph[clock_num][0]
    graph[clock_num][0] = graph[clock_num][1]
    graph[clock_num][1] = graph[clock_num][2]
    graph[clock_num][2] = graph[clock_num][3]
    graph[clock_num][3] = graph[clock_num][4]
    graph[clock_num][4] = graph[clock_num][5]
    graph[clock_num][5] = graph[clock_num][6]
    graph[clock_num][6] = graph[clock_num][7]
    graph[clock_num][7] = tmp
    
    if clock_num == 0:
        if graph[1][6] != graph[0][2]:
            clock_rotation(1)
    elif clock_num == 1:
        if graph[0][2] != graph[1][6]:
            clock_rotation(0)
        if graph[2][6] != graph[1][2]:
            clock_rotation(2)
    elif clock_num == 2:
        if graph[1][2] != graph[2][6]:
            clock_rotation(1)
        if graph[3][6] != graph[2][2]:
            clock_rotation(3)
    elif clock_num == 3:
        if graph[2][2] != graph[3][6]:
            clock_rotation(2)
    return
# def clock_rotation(clock_num, count):
#     if clock_num == 0:
#         if graph[1][6] != graph[0][2]:
#             anti_clock_rotation(1, count+1)
#     elif clock_num == 1:
#         if graph[0][2] != graph[1][6]:
#             anti_clock_rotation(0)
#         if graph[2][6] != graph[1][2]:
#             anti_clock_rotation(2)
#     elif clock_num == 2:
#         if graph[1][2] != graph[2][6]:
#             anti_clock_rotation(1)
#         if graph[3][6] != graph[2][2]:
#             anti_clock_rotation(3)
#     elif clock_num == 3:
#         if graph[2][2] != graph[3][6]:
#             anti_clock_rotation(2)
            
#     tmp = graph[clock_num][0]
#     graph[clock_num][0] = graph[clock_num][7]
#     graph[clock_num][7] = graph[clock_num][6]
#     graph[clock_num][6] = graph[clock_num][5]
#     graph[clock_num][5] = graph[clock_num][4]
#     graph[clock_num][4] = graph[clock_num][3]
#     graph[clock_num][3] = graph[clock_num][2]
#     graph[clock_num][2] = graph[clock_num][1]
#     graph[clock_num][1] = tmp
    

#     return
            
                        
# def anti_clock_rotation(clock_num, count):
#     tmp = graph[clock_num][0]
#     graph[clock_num][0] = graph[clock_num][1]
#     graph[clock_num][1] = graph[clock_num][2]
#     graph[clock_num][2] = graph[clock_num][3]
#     graph[clock_num][3] = graph[clock_num][4]
#     graph[clock_num][4] = graph[clock_num][5]
#     graph[clock_num][5] = graph[clock_num][6]
#     graph[clock_num][6] = graph[clock_num][7]
#     graph[clock_num][7] = tmp
    
#     if clock_num == 0:
#         if graph[1][6] != graph[0][2]:
#             clock_rotation(1)
#     elif clock_num == 1:
#         if graph[0][2] != graph[1][6]:
#             clock_rotation(0)
#         if graph[2][6] != graph[1][2]:
#             clock_rotation(2)
#     elif clock_num == 2:
#         if graph[1][2] != graph[2][6]:
#             clock_rotation(1)
#         if graph[3][6] != graph[2][2]:
#             clock_rotation(3)
#     elif clock_num == 3:
#         if graph[2][2] != graph[3][6]:
#             clock_rotation(2)
#     return


for a in range(k):
    if order[a][1] == 1:
        clock_rotation(order[a][0]-1, order[a][1])
    elif order[a][1] == -1:
        anti_clock_rotation(order[a][0]-1, 0)
        
count = 0
if graph[0][0] == 1:
    count += 1
if graph[1][0] == 1:
    count += 2
if graph[2][0] == 1:
    count += 4
if graph[3][0] == 1:
    count += 8
    
print(count)