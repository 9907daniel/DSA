import heapq

n, k = map(int,input().split())


# l = []
# heapq.heapify(l)
# for a in range(n):

l = [1 for _ in range(n)]

while count > k:
    count = 0
    for a in l:
        if a != 0:
            count += 1
            
    for a in range(len(l)):
        for b in range(len(l)):
            if l[a] == l[b]:
                l[a] = l[a] + l[b]
                l[b] = 0
                break
        # if l[a]
        
        



    

    