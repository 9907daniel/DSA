# https://www.acmicpc.net/problem/2309

l = []
for i in range(9):
    l.append(int(input()))
    
l.sort()
tmp = []
for a in range(6,len(l)):
    tmp = []
    for b in range(5,a):
        for c in range(4,b):
            for d in range(3,c):
                for e in range(2,d):
                    for f in range(1,e):
                        for g in range(f):
                            tmp.append(l[a])
                            tmp.append(l[b])
                            tmp.append(l[c])
                            tmp.append(l[d])
                            tmp.append(l[e])
                            tmp.append(l[f])
                            tmp.append(l[g])
                            print(tmp)
                            
                            
# print(tmp)