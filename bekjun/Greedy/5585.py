n = int(input())

coins = [500,100,50,10,5,1]

current = 1000 - n

count = 0
for a in range(len(coins)):
    count += current // coins[a]
    current = current % coins[a]
    
print(count)