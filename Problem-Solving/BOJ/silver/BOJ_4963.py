dr = [-1, 1, 0, 0, -1, 1, -1, 1]
dc = [0, 0, -1, 1, -1, -1, 1, 1]

from collections import deque

def my_func(row, col):
    que = deque()
    que.append([row, col])
    while que:
        y, x = que.popleft()
        for i in range(8):
            y_idx = y + dr[i]
            x_idx = x + dc[i]
            if y_idx < 0 or y_idx >= H or x_idx < 0 or x_idx >= W:
                continue
            if MAP[y_idx][x_idx] == 0:
                continue
            if used[y_idx][x_idx] == 1:
                continue
            used[y_idx][x_idx] = 1
            que.append([y_idx, x_idx])
    return




while True:
    W, H = map(int, input().split())
    if W == 0 and H == 0:
        break
    MAP = [list(map(int, input().split())) for _ in range(H)]
    used = [[0 for _ in range(W)] for _ in range(H)]
    result = 0
    for r in range(H):
        for c in range(W):
            if MAP[r][c] == 1 and used[r][c] == 0:
                my_func(r, c)
                result += 1
    print(result)