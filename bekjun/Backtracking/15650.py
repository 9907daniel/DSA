n,m = map(int, input().split())

result = []

def dfs(start):
    if len(result) == m:
        print(*result)
        return
    
    for a in range(start, n+1):
        if a not in result:
            result.append(a)
            dfs(a+1)
            result.pop()

dfs(1)

# visited = [False] * (n+1)
# result = []
# tried = []

# def combination(nums):
    
#     if nums == m:

#         sort_result = sorted(result)
#         if sort_result in tried:
#             return
#         else:
#             print(*sort_result)
#             tried.append(sort_result)
            
#     for a in range(1, n+1):
#         if visited[a] == False:
#             visited[a] = True
#             result.append(a)
            
#             combination(nums+1)
#             visited[a] = False
#             result.pop()
            
# combination(0)