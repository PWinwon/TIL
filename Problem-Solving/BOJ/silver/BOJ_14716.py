from collections import deque

dr = [-1, 1, 0, 0, -1, 1, -1, 1]
dc = [0, 0, -1, 1, -1, -1, 1, 1]


def my_func(row, col):
    que = deque()
    que.append([row, col])
    while que:
        rr, cc = que.popleft()
        for i in range(8):
            r_idx = rr + dr[i]
            c_idx = cc + dc[i]
            if r_idx < 0 or r_idx >= R or c_idx < 0 or c_idx >= C:
                continue
            if MAP[r_idx][c_idx] == 0 or used[r_idx][c_idx] == 1:
                continue
            used[r_idx][c_idx] = 1
            que.append([r_idx, c_idx])
    return

R, C = map(int, input().split())

MAP = [list(map(int, input().split())) for _ in range(R)]
used = [[0 for _ in range(C)] for _ in range(R)]
result = 0
for r in range(R):
    for c in range(C):
        if MAP[r][c] == 1 and used[r][c] == 0:
            used[r][c] = 1
            my_func(r, c)
            result += 1
print(result)
