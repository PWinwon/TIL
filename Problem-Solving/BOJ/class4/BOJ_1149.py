import sys
input = sys.stdin.readline

N = int(input().strip())
colors = [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * 3 for _ in range(N)]
dp[0] = colors[0]

for i in range(1, N):
    dp[i][0] = colors[i][0] + min(dp[i-1][1], dp[i-1][2])
    dp[i][1] = colors[i][1] + min(dp[i-1][0], dp[i-1][2])
    dp[i][2] = colors[i][2] + min(dp[i-1][0], dp[i-1][1])

print(min(dp[N-1]))