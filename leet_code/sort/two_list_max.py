n, k = map(int, input().split())

a = list(map(int,input().split()))
b = list(map(int,input().split()))

c = 0
while c < k:
    for i,j in enumerate(a):
        if min(a) < max(b):
            a[a.index(min(a))] = max(b)
            b[b.index(max(b))] = min(a) 
            c += 1


print(a)
print(sum(a))