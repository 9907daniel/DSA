n, m = map(int, input().split())

l = list(map(int, input().split()))

l.sort()

result = []
tmp = []
visited = [False for _ in range(len(l))]
def combinations():
    if len(tmp) == m:
        if tmp not in result:
            result.append(tmp[:])
        return

    for a in range(len(l)):
        if visited[a] == False:
            tmp.append(l[a])
            visited[a] = True
            combinations()
            tmp.pop()
            visited[a] = False


combinations()

for a in result:
    print(*a)