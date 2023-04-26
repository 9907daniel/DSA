n, k = map(int, input().split())

coins = []

for _ in range(n):
    coins.append(int(input()))
    
dp = [0]*10000000


tmp = []
count = 0
for a in range(len(coins)):
    while a > 0:
        if a > coins[a]:
            pass
        else:
            break