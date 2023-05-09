

while True:
    l = list(map(int, input().split()))
    
    
    # tmp = l[0]
    # all = []
    tmp = [l[0]]
    for a in range(1,len(l)):
        if l[a] == "}":
            if tmp[-1] == "{":
                tmp.pop()
            else:
                tmp.append(l[a])
        else:
            tmp.append(l[a])
        
        
        tmp.append(l[a])
        
