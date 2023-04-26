n = int(input())

dp = [0 for _ in range(n+1)]

if n == 1:
    dp[1] = 3
else:
    dp[1] = 3
    dp[2] = 7


if n > 2:
    for a in range(3, n+1):
        dp[a] = (dp[a-2]) + (dp[a-1]*2)
        dp[a] %= 9901
    print(dp[n])
else:
    print(dp[n])






# n = int(input())
# dp = [[0]*(n+1) for _ in range(n+1)]
# dp[1][0] = 1
# dp[1][1] = 2

# count = 0
# for a in range(2,n+1):
#     for b in range(a+1):
#         if b == a:
#             dp[a][b] = 2
#         elif b == 0:
#             dp[a][b] = 1    
#         elif b == 1:
#             dp[a][b] = a*2
#         else:
#             dp[a][b] = dp[a-1][b] + (dp[a-1][b-1]-count)*2
#     count += 1

# print(sum(dp[n])%9901)
