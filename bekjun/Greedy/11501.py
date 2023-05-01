t = int(input())
sums =[]
for _ in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    
    tmp = []
    current_max = l[-1]
    for a in range(len(l)-2, -1, -1):
        current_max = max(current_max, l[a])
        tmp.append(current_max - l[a])
    
    sums.append(sum(tmp))

for a in sums:
    print(a)
