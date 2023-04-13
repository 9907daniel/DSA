n = int(input())
wine = []
d = [0]*(n)

for a in range(n):
    wine.append(int(input()))
    
d[0] = wine[0]
d[1] = wine[1] + wine[0]
d[2] = max(wine[2]+wine[1], wine[2]+wine[0])

for a in range(3, n):
    if a == n-1:
        d[a] = max(d[a-2],wine[a], d[a-1]+wine[a])        
    else:
        d[a] = max(d[a-2]+wine[a], d[a-1]+wine[a+1])

print(d[-1])