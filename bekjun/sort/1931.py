n = int(input())
l = []

for a in range(n):
    l.append(list(map(int, input().split())))

s = sorted(l, key = lambda x:x[0])
s = sorted(s, key=lambda x:x[1])
tmp = []

count = 1
tmp = s[0][1]
for a in range(1,n):
    if s[a][0] >= tmp:
        count += 1
        tmp = s[a][1]
print(count)
    

