N = input()
l = list(map(int, input().split()))
B, C = map(int, input().split())

count = 0
tmp = []
for a in l:
    a -= B
    if a < C:
        count = 2
    elif a%C == 0:
        count = (a//C)+1
    else:
        count = (a//C)+2
    tmp.append(count)
    
print (sum(tmp))
    


            