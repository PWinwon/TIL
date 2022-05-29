import sys

input = sys.stdin.readline
INF = float('inf')

N = int(input().strip())
M = int(input().strip())

MAP = [[INF for _ in range(N)] for _ in range(N)]

for m in range(M):
    a, b, c = map(int, input().split())
    MAP[a-1][b-1] = min(MAP[a-1][b-1], c)

for k in range(N):
    MAP[k][k] = 0
    for i in range(N):
        for j in range(N):
            MAP[i][j] = min(MAP[i][j], MAP[i][k] + MAP[k][j])

for row in MAP:
    for i in range(N):
        if row[i] == INF:
            row[i] = 0
    print(' '.join(map(str, row)))