n = int(input())

dp = [[1]*10 for _ in range(n+1)]

dp[1] = [1,1,1,1,1,1,1,1,1,1]

if n >= 2:
    dp[2] = [1,2,3,4,5,6,7,8,9,10]

for a in range(3, n+1):
    for b in range(10):
        dp[a][b] = sum(dp[a-1][:b+1]) 

print(sum(dp[n])%10007)

