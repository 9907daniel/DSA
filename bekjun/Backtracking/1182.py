n,s = map(int, input().split())

l = list(map(int, input().split()))

count = 0
current = []
def combination(start, idx):
    global count
    if start == n+1:
        return
    
    for a in range(idx, n):
        if l[a] not in current:
            current.append(l[a])
            if sum(current) == s:
                count += 1
            idx += 1
            combination(start+1, idx)
            current.pop()
            
combination(0,0)
print(count)
