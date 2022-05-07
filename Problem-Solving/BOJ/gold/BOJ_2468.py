import sys

from collections import deque
input = sys.stdin.readline

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def my_bfs(r, c, n):
    global N
    que = deque()
    que.append([r, c])

    while que:
        y, x = que.popleft()

        for i in range(4):
            y_idx = y + dr[i]
            x_idx = x + dc[i]
            if y_idx < 0 or y_idx >= N or x_idx < 0 or x_idx >= N:
                continue
            if used[y_idx][x_idx]:
                continue
            if MAP[y_idx][x_idx] < n:
                continue
            que.append([y_idx, x_idx])
            used[y_idx][x_idx] = 1
    return


def my_func(n):
    global result, N
    ret = 0
    for r in range(N):
        for c in range(N):
            if MAP[r][c] >= n and used[r][c] == 0:
                used[r][c] = 1
                my_bfs(r, c, n)
                ret += 1

    return ret


N = int(input().strip())
MAP = [list(map(int, input().split())) for _ in range(N)]

max_h = -1
for r in range(N):
    for c in range(N):
        if max_h < MAP[r][c]:
            max_h = MAP[r][c]

result = 0
for i in range(max_h, 0, -1):
    used = [[0 for _ in range(N)] for _ in range(N)]
    temp = my_func(i)
    de = -1
    if result < temp:
        result = temp
print(result)