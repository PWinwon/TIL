import sys

N, M = map(int, input().split())

MAP = [list(map(int, input().split())) for _ in range(N)]

MSUM = [[0 for _ in range(N+1)] for _ in range(N+1)]

for r in range(N):
    for c in range(N):
        MSUM[r+1][c+1] = MAP[r][c] + MSUM[r+1][c] + MSUM[r][c+1] - MSUM[r][c]



for m in range(M):
    y1, x1, y2, x2 = map(int, sys.stdin.readline().split())
    ret = MSUM[y2][x2] - MSUM[y1-1][x2] - MSUM[y2][x1-1] + MSUM[y1-1][x1-1]
    print(ret)