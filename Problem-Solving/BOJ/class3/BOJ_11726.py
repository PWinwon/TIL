N = int(input())
dp = [0] * (N+1)
dp[1] = 1
dp[2] = 2

if N <= 3:
    print(N)
else:
    for n in range(3, N+1):
        dp[n] = dp[n-1] + dp[n-2]

    print(dp[N]%10007)