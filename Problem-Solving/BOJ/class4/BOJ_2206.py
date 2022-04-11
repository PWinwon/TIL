import sys

from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

R, C = map(int, input().split())
MAP = [list(map(int, list(sys.stdin.readline().strip()))) for _ in range(R)]

used = [[[0]*2 for _ in range(C)] for _ in range(R)]
que = deque()
que.append([R-1, C-1, 0])
used[R-1][C-1][0] = 1

result = -1

while que:
    y, x, flag = que.popleft()
    if y == 0 and x == 0:
        result = used[y][x][flag]
        break

    for i in range(4):
        r = y + dr[i]
        c = x + dc[i]
        if r < 0 or r >= R or c < 0 or c >= C:
            continue
        if used[r][c][flag]:
            continue
        if MAP[r][c] == 1:
            if flag:
                continue
            else:
                que.append([r, c, 1])
                used[r][c][1] = used[y][x][flag] + 1
                continue
        que.append([r, c, flag])
        used[r][c][flag] = used[y][x][flag] + 1

print(result)