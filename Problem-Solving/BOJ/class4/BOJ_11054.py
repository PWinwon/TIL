import sys

# sys.stdin = open('input.txt', 'r')

N = int(input().strip())
lst = list(map(int, input().split()))

dp_up = [1 for _ in range(N)]
dp_down = [1 for _ in range(N)]

for n in range(N):
    for i in range(n):
        if lst[n] > lst[i]:
            dp_up[n] = max(dp_up[n], dp_up[i] + 1)

for n in range(N-1, -1, -1):
    for i in range(N-1, n-1, -1):
        if lst[n] > lst[i]:
            dp_down[n] = max(dp_down[n], dp_down[i] + 1)

result = -1
for i in range(N):
    temp = dp_up[i] + dp_down[i] - 1
    if result < temp:
        result = temp
print(result)