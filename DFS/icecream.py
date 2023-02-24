
n,m = map(int, input().split())

graph = []
count = 0
for i in range(n):
    graph.append(list(map(int,input())))
    
def dfs(y,x):
     if x < 0 or y <0 or x >= m or y >=n:
         return False
     
     elif graph[y][x] == 0:
         graph[y][x] = 1
         
         dfs(y+1,x)
         dfs(y-1,x)
         dfs(y,x+1)
         dfs(y,x-1)
         return True
     
     else:
         return False

for y in range(n):
    for x in range(m):
        if dfs(y,x) == True:
            count += 1
            
print(count) 
    
    
    
# def dfs(y,x):
#      if x < 0 or y <0 or x >= m or y >=n:
#          return False
#      elif graph[y+1][x] == 0:
#          graph[y][x] = 1
#          dfs(y+1,x)
#      elif graph[y-1][x] == 0:
#          graph[y][x] = 1
#          dfs(y-1,x)
#      elif graph[y][x+1] == 0:
#          graph[y][x] = 1
#          dfs(y,x+1)
#      elif graph[y][x-1] == 0:
#          graph[y][x] = 1
#          dfs(y,x-1)
#      else:
#         graph[y][x] = 1
#      return False


# for y in range(n):
#     for x in range(m):
#         if graph[y][x] == 0:
#             dfs(y,x)
#             count += 1
            
# print(count)
