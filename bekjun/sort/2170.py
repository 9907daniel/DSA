n = int(input())
l = []

for a in range(n):
    l.append(list(map(int, input().split())))

s = sorted(l, key = lambda x:x[0])
s = sorted(s, key = lambda x:x[1])

count = 0
tmp = []
for a in range(len(l)):
    if a == 0:
        tmp.append(l[a])
    else:
        if l[a][0] <= tmp[count][1]:
            tmp.append([tmp[count][0],l[a][1]])
            tmp.pop(count)
        else:
            tmp.append(l[a])
            count += 1
        
length = 0
for a in range(len(tmp)):
    length += (tmp[a][1]-tmp[a][0])

print(length)