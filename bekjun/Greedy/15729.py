n = int(input())

l = list(map(int,input().split()))

current = [0 for _ in range(n)]

count = 0
for a in range(n):
    if l[a] == 1 and current[a] == 0:
        count += 1
        current[a] = 1
        if a+1 < n:
            if current[a+1] == 1:
                current[a+1] = 0
            elif current[a+1] == 0:
                current[a+1] = 1
        if a+2 < n:
            if current[a+2] == 1:
                current[a+2] = 0
            elif current[a+2] == 0:
                current[a+2] = 1
    elif l[a] == 0 and current[a] == 1:
        count += 1
        current[a] = 0
        if a+1 < n:
            if current[a+1] == 1:
                current[a+1] = 0
            elif current[a+1] == 0:
                current[a+1] = 1
        if a+2 < n:
            if current[a+2] == 1:
                current[a+2] = 0
            elif current[a+2] == 0:
                current[a+2] = 1
    
print(count)

    # if l[a] == 1 and current[a] == 0:
    #     count += 1
    #     current[a] = 1
    #     current[a+1] = 1
    #     current[a+2] = 1
    # elif l[a] == 0 and current[a] == 1:
    #     count += 1
    #     current[a] = 0
    #     if current[a+1] == 1:
    #         current[a+1] = 0
    #     elif current[a+1] == 0:
    #         current[a+1] = 1
            
    #     if current[a+2] == 1:
    #         current[a+2] = 0
    #     elif current[a+2] == 0:
    #         current[a+2] = 1


