n, m = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
    
calculate = []
for _ in range(m):
    calculate.append(list(map(int, input().split())))
    
dp = [[0]*n for _ in range(n)]

dp[0][0] = graph[0][0]
for a in range(n):
    for b in range(n):
        if a == 0 and b == 0:
            dp[a][b] = graph[a][b]
        elif a == 0:
            dp[a][b] = graph[a][b] + dp[a][b-1]
        elif b ==0:
            dp[a][b] = graph[a][b] + dp[a-1][b]
        else:
            dp[a][b] = graph[a][b] + dp[a-1][b] + dp[a][b-1] - dp[a-1][b-1]
    
for a in range(m):
    x1,y1 = calculate[a][0]-1, calculate[a][1]-1
    x2,y2 = calculate[a][2]-1, calculate[a][3]-1
    

    if x1 == 0 and y1 == 0:
        count = dp[x2][y2]
    elif y1 == 0:
        count = dp[x2][y2] - dp[x1-1][y2]
    elif x1 ==0:
        count = dp[x2][y2] - dp[x2][y1-1]
    else:
        if x1 == x2 and y2 == y2:
            count = graph[x2][y2]
        else:
            count = dp[x2][y2] - dp[x1-1][y2] - dp[x2][y1-1] + graph[x1-1][y1-1]
    
    print(count)