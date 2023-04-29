
t = int(input())
tmp = []

for a in range(t):
    l = []
    count = 0
    
    n = int(input())
    for a in range(n):
        l.append(list(map(int, input().split())))
    
    l.sort(key = lambda x: x[0])
        
    count = 1
    for a in range(1, len(l)):
        for b in range(a-1, -1, -1):
            if b == 0 and l[a][1] < l[b][1]:
                count += 1
            elif l[a][1] < l[b][1]:
                continue
            else:
                break         
    
    tmp.append(count)

for a in tmp:
    print(a)
    
    
    