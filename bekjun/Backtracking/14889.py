n = int(input())

graph = []
visited = [False for _ in range(n)]

for _ in range(n):
    graph.append(list(map(int,input().split())))
    
difference = 200000000

chosen = []
def combination(start):
    global difference

    if start == n//2:
        team1 = 0
        team2 = 0
        for a in range(n):
            for b in range(n):
                if visited[a] and visited[b]:
                    team1 += graph[a][b]
                elif visited[a] == False and visited[b] == False:
                    team2 += graph[a][b]
        
        difference = min(difference, abs(team1-team2))
        return
    
    for a in range(n):
            if visited[a] == False:
                visited[a] = True
                combination(start + 1)
                visited[a] = False
                
combination(0)
print(difference)
    
    
    
    
    
    
    
    
    
    
    

# team = []
# def combination(together, start):
#     if len(team) == n:
#         combination2(team, 0)
#         return
        
#     for a in range(start, len(together)):
#         if a not in team:
#             team.append(together[a])
#             combination(together, a+1)
#             team.pop()

# difference = []
# added = []
# def combination2(together,start):
#     if len(difference) == n//2:
#         added.append(abs((sum(together)-sum(difference))-sum(difference)))
#         return
#     for a in range(start, len(together)):
#         if a not in difference:
#             difference.append(together[a])
#             combination2(together,a+1)
#             difference.pop()
    
# together = []
# for a in range(n):
#     for b in range(n):
#         if a != b:
#             if visited[a][b] == False:
#                 together.append(graph[a][b]+graph[b][a])
#                 visited[a][b] = True
#                 visited[b][a] = True

# combination(together, 0)
# print(min(added))