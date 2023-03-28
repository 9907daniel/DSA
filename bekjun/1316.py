n = int(input())
l = []

for i in range(n):
    l.append(input())
    
count = 0
tmp = []
boo = True

for a in l:
    for b in a:
        if b not in tmp:
            tmp.append(b)
            pass
        elif tmp[-1] == b:
            pass
        else:
            boo = False
            break
        boo = True
    if boo:
        count += 1
    tmp = [] 
    
print(count)