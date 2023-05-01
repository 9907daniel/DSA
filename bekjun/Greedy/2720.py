# https://www.acmicpc.net/problem/2720

t = int(input())

coins = [25, 10, 5, 1]

result = []
for _ in range(t):
    n = int(input())
    
    nums = [0,0,0,0]
    
    for a in range(4):
        nums[a] = n // coins[a]
        n = n % coins[a]

    result.append(nums)

for a in result:
    print(*a)