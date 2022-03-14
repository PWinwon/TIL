N = int(input())
dp = [0, 1, 2] + [0]* (N+1)

for n in range(3, N+1):
    dp[n] = dp[n-1] + dp[n-2]

print(dp[N]%10007)