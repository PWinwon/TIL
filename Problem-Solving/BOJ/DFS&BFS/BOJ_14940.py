import sys
from collections import deque

input = sys.stdin.readline

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

R, C = map(int, input().split())

MAP = [list(map(int, input().split())) for _ in range(R)]

used = [[-1 for _ in range(C)] for _ in range(R)]

que = deque()

for r in range(R):
    for c in range(C):
        if MAP[r][c] == 2:
            que.append([r, c])
            used[r][c] = 0

        if MAP[r][c] == 0:
            used[r][c] = 0

while que:
    y, x = que.popleft()
    for i in range(4):
        yr, xr = y + dr[i], x + dc[i]
        if yr < 0 or yr >= R or xr < 0 or xr >= C:
            continue
        if MAP[yr][xr] == 0:
            continue
        if used[yr][xr] != -1:
            continue
        que.append([yr, xr])
        used[yr][xr] = used[y][x] + 1

for r in range(R):
    print(' '.join(map(str, used[r])))