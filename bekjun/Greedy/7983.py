n = int(input())
l = []
tmp = []
for a in range(n):
    l.append(list(map(int, input().split())))

for a in range(len(l)):
    l[a] = l[a][1]-l[a][0]

print(min(l)-1)


