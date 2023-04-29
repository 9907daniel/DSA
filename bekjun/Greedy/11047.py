n, k = map(int, input().split())

coins = []

for _ in range(n):
    coins.append(int(input()))

coins.reverse()

count = 0
a = 0
while True:
    # for a in range(len(coins)):
    
    if k - coins[a] < 0:
        a += 1
    elif k - coins[a] == 0:
        count += 1
        break
    elif k - coins[a] > 0:
        k -= coins[a]
        count += 1
        
print(count)