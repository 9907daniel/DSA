m, h, n = map(int, input().split())
l = []
tmp = []

for a in range(n):
    l.append([0]*m)

for a in range(h):
    i,j = map(int,input().split())
    l[i-1][j] = 1
    
for a in range(m):
    tmp.append(a+1)

for a in range(m):
    for b in range(n):
        if l[b][a-1] == 1:
            tmp[a] += 1
print(l)
print(tmp)
    
        
    


    