import sys

input = sys.stdin.readline
INF = float('inf')

N = int(input().strip())

dp = [[INF, n] for n in range(N+1)]

dp[N][0] = 0
dp[N][1] = 0

for i in range(N, 0, -1):
    if dp[i-1][0] > dp[i][0]+1:
        dp[i-1][0] = dp[i][0] + 1
        dp[i-1][1] = i
    if i % 2 == 0 and dp[i//2][0] > dp[i][0]+1:
        dp[i//2][0] = dp[i][0] + 1
        dp[i//2][1] = i
    if i % 3 == 0 and dp[i//3][0] > dp[i][0]+1:
        dp[i//3][0] = dp[i][0] + 1
        dp[i//3][1] = i


print(dp[1][0])

result = [1]
num = 1
while dp[num][1]:
    result.append(dp[num][1])
    num = dp[num][1]
result.reverse()
print(' '.join(map(str, result)))