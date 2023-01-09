import sys
from collections import deque

input = sys.stdin.readline

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

R, C = map(int, input().split())

# d >> 0: 상, 1: 우, 2: 하, 3: 좌
rob_r, rob_c, direction = map(int, input().split())

# 빈칸: 0, 벽: 1
MAP = [list(map(int, input().split())) for _ in range(R)]
used = [[0 for _ in range(C)] for _ in range(R)]

que = deque()
# r, c, 방향, count
que.append([rob_r, rob_c, direction, 0])
used[rob_r][rob_c] = 1

result = 1

while que:
    y, x, d, cnt = que.popleft()
    if cnt == 4:
        d_r = (d + 2) % 4
        yr, xr = y+dr[d_r], x+dc[d_r]
        if yr < 0 or yr >= R or xr < 0 or xr >= C:
            break
        if MAP[yr][xr]:
            break
        que.append([yr, xr, d, 0])
    d_r = (d + 3) % 4
    yr, xr = y+dr[d_r], x+dc[d_r]
    if yr < 0 or yr >= R or xr < 0 or xr >= C:
        que.append([y, x, d_r, cnt + 1])
        continue
    if MAP[yr][xr] or used[yr][xr]:
        que.append([y, x, d_r, cnt+1])
        continue
    used[yr][xr] = 1
    que.append([yr, xr, d_r, 0])
    result += 1

print(result)
