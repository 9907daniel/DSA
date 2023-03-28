
n,k = map(int, input().split())

a = list(map(int,input().split()))
b = list(map(int,input().split()))


for c in range(k):
    a[a.index(min(a))], b[b.index(max(b))] = b[b.index(max(b))], a[a.index(min(a))]
    
    # a.append(max(b))
    # b.append(min(a))
    # a.pop(min(a))
    # b.pop(min(b))

print(a)
print(b)