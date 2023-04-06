# https://www.acmicpc.net/problem/1946

t = int(input())
tmp = []

for a in range(t):
    l = []
    count = 0
    
    n = int(input())
    for a in range(n):
        l.append(list(map(int, input().split())))
    
    # l = sorted(l, key=lambda x:x[0])
        
    for a in range(len(l)): 
        check = True
        for b in range(len(l)):   
            if l[a][1] > l[b][1] and l[a][0] > l[b][0]:
                check = False
                break
        if check == True:
            count += 1
    tmp.append(count)
    
for a in tmp:
    print(a)
    
        

