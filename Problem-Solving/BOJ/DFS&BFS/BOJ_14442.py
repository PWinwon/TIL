import sys
from collections import deque

input = sys.stdin.readline
INF = float('inf')

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

R, C, K = map(int, input().split())
MAP = [list(input().strip()) for _ in range(R)]
used = [[[INF for _ in range(K+1)] for _ in range(C)] for _ in range(R)]

que = deque()
# r, c, cnt, k
que.append([0, 0, 0])
used[0][0][0] = 1

while que:
    y, x, k = que.popleft()
    for i in range(4):
        yr, xr = y + dr[i], x + dc[i]
        if yr < 0 or yr >= R or xr < 0 or xr >= C:
            continue
        if MAP[yr][xr] == '1' and k < K and used[yr][xr][k+1] > used[y][x][k] + 1:
            que.append([yr, xr, k+1])
            used[yr][xr][k+1] = used[y][x][k] + 1
        if MAP[yr][xr] == '0' and used[yr][xr][k] > used[y][x][k] + 1:
            que.append([yr, xr, k])
            used[yr][xr][k] = used[y][x][k] + 1

result = min(used[R-1][C-1])
if result == INF:
    print(-1)
else:
    print(result)