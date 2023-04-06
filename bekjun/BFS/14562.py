from collections import deque

def bfs(S, T):
    q = deque()
    q.append((S, T, 0))
    check = [-1]*(200)
    while q:
        node, t, c = q.popleft()
        if node <= t and check[node] == -1:
            q.append((node*2, t+3, c+1))
            q.append((node+1, t, c+1))
            if node == t:
                return c

C = int(input())
for _ in range(C):
    S, T = map(int, input().split())
    print(bfs(S, T))


# from collections import deque

# t = int(input())
# l = []

# for a in range(t):
#     l.append(list(map(int, input().split())))
    
# # track = [1]
# # for a in range(l):
# # print(track)
    
# def bfs(x,y, z):
#     queue = deque()
#     print(queue, z)
#     queue.append((x,y,z))
#     print(deque)
#     # check = [-1]*200

#     while queue:
#         a,b,c = queue.popleft()
#         print(a,b,c)
#         if a == b:
#             return c
#         # if(a*2) <= (b+3):
#         else:
#             queue.append((a*2,b+3,c+1))
#             queue.append((a+1,b,c+1))
        
# for a in range(t):
#     print(bfs(l[a][0],l[0][1],0))
    