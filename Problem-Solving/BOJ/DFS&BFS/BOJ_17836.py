import sys
from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

input = sys.stdin.readline
INF = float('inf')

R, C, T = map(int, input().split())

MAP = [list(map(int, input().split())) for _ in range(R)]
used = [[[INF, INF] for _ in range(C)] for _ in range(R)]

used[0][0][0] = 0

que = deque()
# r, c, 검유무,
que.append([0, 0, 0])

while que:
    y, x, chk = que.popleft()
    for i in range(4):
        yr, xr = y + dr[i], x + dc[i]
        if yr < 0 or yr >= R or xr < 0 or xr >= C:
            continue
        if MAP[yr][xr] > chk and MAP[yr][xr] != 2:
            continue
        if used[yr][xr][chk] <= used[y][x][chk] + 1:
            continue
        if MAP[yr][xr] == 2:
            used[yr][xr][1] = used[y][x][chk] + 1
            que.append([yr, xr, 1])
            continue
        used[yr][xr][chk] = used[y][x][chk] + 1
        que.append([yr, xr, chk])

result = min(used[R-1][C-1])
if result > T:
    print('Fail')
else:
    print(result)
