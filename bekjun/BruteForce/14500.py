n,m = map(int, input().split())

graph = []

for _ in range(n):
    graph.append(list(map(int, input().split())))

dp = [[0]*m for _ in range(n)]

def shape_a(x,y):
    count_a = graph[x][y]
    count_b = graph[x][y]

    for a in range(3):
        if y + a + 1 < m:
            count_a += graph[x][y+a+1]
        else:
            count_a = 0
            break
                
    for a in range(3):
        if y + a + 1 < m:
            count_b += graph[x+a+1][y]
        else:
            count_b = 0
            break
    count = max(count_a, count_b)
    return count

def shape_b(x,y):
    count = 0
    for a in range(2):
        for b in range(2):
            if x+a < n and y+b < m:
                count += graph[x+a][y+b]
            else:
                return 0
    return count

def shape_c(x,y):
    # count = 0
    count_a = 0
    count_b = 0
    count_c = 0
    count_d = 0
    count = []
    previous = True
    
    for a in range(3):
        if x+a < n:
            count_a += graph[x+a][y]
        else:
            count_a = 0
            previous = False
            break
    if x+2 < n and y+1 < m and previous:
        count_a += graph[x+2][y+1]
    else:
        count_a = 0
        previous = True
    
    count.append(count_a)

    for a in range(3):
        if x-a < n:
            count_b += graph[x-a][y]
        else:
            count_b = 0
            previous = False
            break
    if x-2 < n and y+1 < m and previous:
        count_a += graph[x+2][y+1]
    else:
        count_a = 0
        previous = True
    
    
    
    
    return count
    
def shape_d(x,y):
    count = 0
    for a in range(2):
        if x + a < n:
            count += graph[x+a][y]
        else:
            return 0
    
    for a in range(2):
        if x+1+a<n and y+1<m:
            count += graph[x+1+a][y+1]
        else:
            return 0
    return count

def shape_e(x,y):
    count = 0
    
    for a in range(3):
        if y+a < m:
            count += graph[x][y+a]
        else:
            return 0
    if x+1 < n and y+1 < m:
        count += graph[x+1][y+1]
    else:
        return 0
    return count

for a in range(n):
    for b in range(m):
        dp[a][b] = max(dp[a][b], shape_a(a,b))
        dp[a][b] = max(dp[a][b], shape_b(a,b))
        dp[a][b] = max(dp[a][b], shape_c(a,b))
        dp[a][b] = max(dp[a][b], shape_d(a,b))
        dp[a][b] = max(dp[a][b], shape_e(a,b))
    
current_max = 0
for a in range(n):
    current_max = max(current_max, max(dp[a]))

print(current_max)





for a in range(n):
    print(*dp[a])

 
# for a in range(n):
#     for b in range(m):
#         if a == 3 and b == 0:
#                 dp[a][b] = max(dp[a][b], shape_a(a,b))
#                 print(dp[a][b]) 
#                 dp[a][b] = max(dp[a][b], shape_b(a,b))
#                 print(dp[a][b]) 
#                 dp[a][b] = max(dp[a][b], shape_c(a,b))
#                 print(dp[a][b]) 
#                 dp[a][b] = max(dp[a][b], shape_d(a,b))
#                 print(dp[a][b]) 
#                 dp[a][b] = max(dp[a][b], shape_e(a,b))  
#                 print(dp[a][b]) 
    
