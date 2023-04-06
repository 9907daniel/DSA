n = int(input())
l = []
for a in range(n):
    l.append(list(map(int, input().split())))    
    
t = [x for x in range(n)]
t1 = []
t2 = []

for a in range(int(n//2)):
    
    
    
    
    for b in range(len(t)):
        for c in range(len(t)):
            t.pop(b)
            t.pop(c)
            if b == c:
                continue
            else:
                t1.append(l[t[b]][t[c]] + l[t[c]][t[b]])
        