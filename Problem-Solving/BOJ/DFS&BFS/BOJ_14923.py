import sys
from collections import deque

input = sys.stdin.readline
INF = float('inf')

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

R, C = map(int, input().split())

start = list(map(int, input().split()))
end = list(map(int, input().split()))

MAP = [list(map(int, input().split())) for _ in range(R)]

used = [[[INF, INF] for _ in range(C)] for _ in range(R)]

result = INF

que = deque()
que.append([start[0]-1, start[1]-1, 1])
used[start[0]-1][start[1]-1][1] = 0

while que:
    y, x, chk = que.popleft()
    for i in range(4):
        yr, xr = y+dr[i], x+dc[i]
        if yr < 0 or yr >= R or xr < 0 or xr >= C:
            continue
        if MAP[yr][xr] == 1 and chk == 0:
            continue
        temp = chk
        if MAP[yr][xr] == 1:
            temp = 0

        if used[yr][xr][temp] <= used[y][x][chk] + 1:
            continue

        used[yr][xr][temp] = used[y][x][chk] + 1
        que.append([yr, xr, temp])

result = min(used[end[0]-1][end[1]-1])
if result == INF:
    print(-1)
else:
    print(result)