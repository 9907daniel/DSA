n, m = map(int, input().split())
l = sorted(list(map(int, input().split())))

result = []
tmp = []
visited = [False]*n

def combinations():
    if len(tmp) == m:
        if tmp not in result:
            print(*tmp[:])
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


# 이게 더 맞는 코드다
# N, M = map(int, input().split())
# L = list(map(int, input().split()))

# L.sort()
# visited = [False] * N
# out = []

# def solve(depth, N, M):
#     if depth == M:
#         print(' '.join(map(str, out)))
#         return
#     overlap = 0
#     for i in range(N):
#         if not visited[i] and overlap != L[i]:
#             visited[i] = True
#             out.append(L[i])
#             overlap = L[i]
#             solve(depth+1, N, M)
#             visited[i] = False
#             out.pop()

# solve(0, N, M)

