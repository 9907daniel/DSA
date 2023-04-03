T = int(input())
l = []

for a in range(T):
    l.append(list(map(int,input().split())))

d = [[1]*31 for _ in range(31)]


for i in range(1,31):
    d[1][i] = i 

for i in range(2,31):
    for j in range(i+1,31):
        d[i][i] = 1
        d[i][j] = d[i][j-1] + d[i-1][j-1]

for a in range(len(l)):
    x = l[a][0]
    y = l[a][1]
    print(d[x][y])
    


# for a in range(len(l)):
#     for a in range(len(l[a])):
#         d = [0*a]*b
#         print(d)