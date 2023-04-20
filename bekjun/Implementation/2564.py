m, n = map(int, input().split())

num = int(input())
l = []

for a in range(num):
    l.append(list(map(int, input().split())))

x, y = map(int, input().split())

graph = [[0,0] for _ in range(num)]

if x == 3:
    new_x = 0
    new_y = y
elif x == 4:
    new_x = m
    new_y = y
elif x == 1:
    new_y = 0
    new_x = y
elif x == 2:
    new_y = n
    new_x = y

for a in range(len(l)):
    if l[a][0] == 1:
        graph[a][0] = 0
    elif l[a][0] == 2:
        graph[a][0] = n
    elif l[a][0] == 3:
        graph[a][1] = 0
    elif l[a][0] == 4:
        graph[a][1] = m
    
    if l[a][0] == 1 or l[a][0] == 2:
        graph[a][1] = l[a][1]
    elif l[a][0] == 3 or l[a][0] == 4:
        graph[a][0] = l[a][1]
    
count = 0
for a in range(len(graph)):
    if new_y == 0 and graph[a][0] == n or new_y == n and graph[a][0] == 0:
        count += min(new_x+graph[a][1], (m-new_x)+(m-graph[a][1]))
        count += n
        print(count)
    elif new_x == 0 and graph[a][1] == m or new_x == m and graph[a][1] == 0:
        count += min(new_y+graph[a][0], (n-new_y)+(n-graph[a][0]))
        count += m
        print(count)
    else:
        count += abs((new_y-graph[a][0])+(new_x-graph[a][1]))
        print(count)

print(count)
