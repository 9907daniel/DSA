N = input()
l = list(map(int, input().split()))
B, C = map(int, input().split())

count = 0

for a in range(len(l)):
    if B > C:
        count += 1
        l[a] -= B    
    while l[a] > 0:
        count += 1
        l[a] -= C

print(count)
            