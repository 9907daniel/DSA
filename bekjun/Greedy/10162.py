
t = int(input())

l = [360, 60 , 10]

result = [0,0,0]

for a in range(len(l)):
    result[a] = t // l[a]
    t = t % l[a]
    
if t == 0:
    print(*result)
else:
    print(-1)
    