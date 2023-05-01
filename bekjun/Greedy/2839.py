n = int(input())

bag = [5,3]

result = [0,0]

count = 0
while n > 0:
    if n < 15:
        if n == 14:
            count += 4
        elif n == 13:
            count += 3
        elif n == 12:
            count += 4
        elif n == 11:
           count += 3 
        elif n == 10:
            count += 2
        elif n == 9:
            count += 3
        elif n == 8:
            count += 2
        elif n == 6:
            count += 2
        elif n == 5:
            count += 1
        elif n == 3:
            count += 1
        else:
            count = -1
        break    
    else:
        n -= 5
        count += 1
print(count)



# count_5 = 0
# for a in range(len(bag)):
#     result[a] = n//bag[a]
#     n = n % bag[a]
    
# if n == 0:
#     print(sum(result))
# else:
#     print(-1)