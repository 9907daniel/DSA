n, l = map(int, input().split())

d = list(map(int,input().split()))

d.sort()

count = 1
current = d[0]
for a in range(1, len(d)):
    if d[a] > (current + l)-1:
        count += 1
        current = d[a]
        
print(count)
        