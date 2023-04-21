# https://www.acmicpc.net/problem/15649

n, m = map(int, input().split())

visited = [False]*(n+1)
result = []
tmp = []

def combination(nums):
    
    if nums == m:
        print(*result)
        return 
    
    
    for a in range(1, n+1):
        if visited[a] == False:
            result.append(a)    
            visited[a] = True
            combination(nums+1)
            visited[a] = False
            result.pop()
        
combination(0)

        