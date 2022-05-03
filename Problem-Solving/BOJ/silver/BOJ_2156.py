import sys

input = sys.stdin.readline

N = int(input().strip())
lst = [0]
for n in range(N):
    lst.append(int(input().strip()))

dp = [0]
dp.append(lst[1])

if N > 1:
    dp.append(lst[1]+lst[2])

for i in range(3, N+1):
    dp.append(max(dp[i-1], dp[i-3] + lst[i-1] + lst[i], dp[i-2] + lst[i]))
print(dp[N])