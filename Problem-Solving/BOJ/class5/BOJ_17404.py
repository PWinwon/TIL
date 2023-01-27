import sys

input = sys.stdin.readline

N = int(input().strip())

lst = [list(map(int, input().split())) for _ in range(N)]

INF = float('inf')

result = INF

for c in range(3):
    dp = [[0 for _ in range(3)] for _ in range(N)]
    for i in range(3):
        if i == c:
            dp[0][i] = lst[0][i]
        else:
            dp[0][i] = INF

    for i in range(1, N):
        dp[i][0] = lst[i][0] + min(dp[i-1][1], dp[i-1][2])
        dp[i][1] = lst[i][1] + min(dp[i-1][0], dp[i-1][2])
        dp[i][2] = lst[i][2] + min(dp[i-1][0], dp[i-1][1])

    for i in range(3):
        if i != c:
            result = min(result, dp[-1][i])

print(result)