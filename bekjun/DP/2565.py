n = int(input())

antena = []

for a in range(n):
    antena.append(list(map(int, input().split())))
    
d = [[] for _ in range(n+1)]
p = [[] for _ in range(n+1)]


def dp():
    pass


for a in range(n):
    for b in range(a+1, n):
        if antena[a][1] > antena[b][1]:
            print(a, b)
            print(antena[a][1] , antena[b][1])
            d[a].append(b)
        

print(d)


    # for b in range(a-1, -1, -1):
    #     if antena[a] < antena[b]:
    #         d[a].append(b)


# for a in range(1,n+1):
#     if antena[a] < a:
        
    
#     for b in range(a, antena[a])
#     d.append[a]()
    
#     antena[a]
    
    
#     for b in range(n):
        