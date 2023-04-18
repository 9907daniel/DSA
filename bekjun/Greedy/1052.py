n, k = map(int,input().split())

tmp = 1

# while tmp < k:
#     tmp = tmp * 2

# for a in range(n):
    
d = [1]*n
    
while True:
    for a in d:
        if a in d:
            d.pop(a)
            d.pop(a)
            d.append(2*a)
    


    