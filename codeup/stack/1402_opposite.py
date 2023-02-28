n = int(input())
l = list(map(int,input().split()))

res = []
while len(l) > 0:
    res.append(l[-1])
    l.pop()

print(res)
