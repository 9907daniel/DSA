n = int(input())

d = [0]* 1000001

d[0] = [0]
d[1] = [1]
d[2] = [1,2]
d[3] = [1,3]

tmp = []
for a in range(4,n+1):
    if a%3 == 0 and a%2 ==0:
        if len(d[a//3]) <= len(d[a//2]) and len(d[a//3]) <= len(d[a-1]):
            d[a] = d[a//3][:]
            d[a].append(a)
        elif len(d[a//3]) > len(d[a//2]) and len(d[a//2]) <= len(d[a-1]):
            d[a] = d[a//2][:]
            d[a].append(a) 
        else:
            d[a] = d[a-1][:]
            d[a].append(a)
    elif a%3 == 0:
        if len(d[a//3]) <= len(d[a-1]):
            d[a] = d[a//3][:]
            d[a].append(a)
        else:
            d[a] = d[a-1][:]
            d[a].append(a)        
    elif a%2 == 0:
        if len(d[a//2]) <= len(d[a-1]):
            d[a] = d[a//2][:]
            d[a].append(a)
        else:
            d[a] = d[a-1][:]
            d[a].append(a) 
    else:
        d[a] = d[a-1][:]
        d[a].append(a)    
        
d[n].reverse()
    

print(len(d[n])-1)
    
for a in d[n]:
    print(a, end = ' ')
        
    