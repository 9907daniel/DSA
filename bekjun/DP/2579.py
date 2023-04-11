n = int(input())

steps = []
d = [0]*(n)

for _ in range(n):
    steps.append(int(input()))
    
for a in range(n):
    d[a] = steps[a]
        
for a in range(3,n):
    d[steps.index(min(steps[a-3:a+1]))] = 0
    
print(d)
    
    
    # if d[a] == min(steps[a-3:a+1]):
    #     d[a] 
    # d[a] = steps[a] + steps[a-1] + steps[a-2] + steps[a-3] - min(steps[a-3:a+1])
    # d[]
    # # find min index and make it 0
    
    
# 4개중 min,제거하고 0으로 대치
    