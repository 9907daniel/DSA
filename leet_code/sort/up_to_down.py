n = int(input())
listed = []

for a in range(n):
    listed.append(list(map(int,input())))
    

for i in range(n):
    for j in range(i+1, n):
        if listed[i] > listed[j]:
            listed[i],listed[j] = listed[j],listed[i]
        
print(listed)