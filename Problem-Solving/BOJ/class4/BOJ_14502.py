import sys
import copy

from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def my_bfs():
    MAPC = copy.deepcopy(MAP)
    que = deque()

    for r in range(R):
        for c in range(C):
            if MAP[r][c] == 2:
                que.append([r, c])

    while que:
        y, x = que.popleft()
        for i in range(4):
            y_idx = y + dr[i]
            x_idx = x + dc[i]
            if y_idx < 0 or y_idx >= R or x_idx < 0 or x_idx >= C:
                continue
            if MAPC[y_idx][x_idx] != 0:
                continue
            que.append([y_idx, x_idx])
            MAPC[y_idx][x_idx] = 2

    cnt = 0
    for r in range(R):
        for c in range(C):
            if MAPC[r][c] == 0:
                cnt += 1
    return cnt


def my_wall(x):
    global result
    if x == 3:
        ret = my_bfs()
        if result < ret:
            result = ret
        return
    for r in range(R):
        for c in range(C):
            if MAP[r][c] == 0:
                MAP[r][c] = 1
                my_wall(x + 1)
                MAP[r][c] = 0
    return


R, C = map(int, input().split())
MAP = [list(map(int, sys.stdin.readline().split())) for _ in range(R)]
result = -1

my_wall(0)
print(result)