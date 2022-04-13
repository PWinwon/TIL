import sys

N = int(input())
MAP = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
cnt = 2
for i in range(1, N):
    for j in range(cnt):
        if j == 0:
            MAP[i][j] = MAP[i][j] + MAP[i-1][j]
        elif i == j:
            MAP[i][j] = MAP[i][j] + MAP[i-1][j-1]
        else:
            MAP[i][j] = max(MAP[i-1][j-1], MAP[i-1][j]) + MAP[i][j]
    cnt += 1
print(max(MAP[N-1]))