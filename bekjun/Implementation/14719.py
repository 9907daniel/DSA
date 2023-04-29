h,w = map(int, input().split())

l = list(map(int, input().split()))


current_wall = l[0]
end_wall = l[-1]
count = 0
tmp = [] 
check = True

for a in range(1,len(l)):
    if a == len(l)-1:
        lower_wall = min(end_wall, current_wall)
        
        tmp_count = 0
        for b in range(len(tmp)):
            if tmp[b] > lower_wall:
                check = False
            else:
                tmp_count += tmp[b]

        if check:
            count += tmp_count
    
    
    
    elif l[a] >= current_wall:
        for a in range(len(tmp)):
            count += (current_wall-tmp[a])

        tmp = []
        current_wall = l[a]

    else:
        tmp.append(l[a])
        

            
print(count)