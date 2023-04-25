n = int(input())

l = list(map(int,input().split()))

tmp = []
tried = []
visited = [False for _ in range(n)]

def combination(start):    
    if len(tmp) == n:
        tried.append(tmp[:])

    for a in range(n):
        if visited[a] == False:
            tmp.append(l[a])
            visited[a] = True
            combination(start + 1)
            visited[a] = False
            tmp.pop()
            
combination(0)

calculated_values = []
for a in range(len(tried)):
    calculate = 0
    for b in range(n-1):
        calculate += abs(tried[a][b]-tried[a][b+1])
    calculated_values.append(calculate)

print(max(calculated_values))
