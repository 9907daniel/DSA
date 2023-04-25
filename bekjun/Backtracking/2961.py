n = int(input())

food = []
visited = [False for _ in range(n)]

for _ in range(n):
    food.append(list(map(int, input().split())))

types = []
tmp = []
def combination(start):    
    if len(tmp) > 0:
        if tmp not in types:
            sour = 0
            bitter = 0
            
            for a in range(len(tmp)):
                if a == 0:
                    sour = tmp[a][0]
                    bitter = tmp[a][1]
                else:
                    sour = sour * tmp[a][0]
                    bitter += tmp[a][1]
      
            types.append(abs(sour-bitter))
    
    for a in range(start, n):
        if visited[a] != True:
            tmp.append(food[a])
            visited[a] = True
            combination(start+1)
            tmp.pop()
            visited[a] = False
combination(0)

print(min(types))

