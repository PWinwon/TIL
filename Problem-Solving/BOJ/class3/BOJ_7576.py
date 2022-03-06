import sys

from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

C, R = map(int, input().split())

MAP = [list(map(int, sys.stdin.readline().split())) for _ in range(R)]
used = [[0 for _ in range(C)] for _ in range(R)]
que = deque()
next_que = deque()
result = 0

for r in range(R):
    for c in range(C):
        if MAP[r][c] == 1:
            que.append([r, c])
            used[r][c] = 1

while True:
    while que:
        y, x = que.popleft()
        for i in range(4):
            r_idx = y + dr[i]
            c_idx = x + dc[i]
            if 0 > r_idx or r_idx >= R or c_idx < 0 or c_idx >= C:
                continue
            if MAP[r_idx][c_idx] or used[r_idx][c_idx]:
                continue
            MAP[r_idx][c_idx] = 1
            used[r_idx][c_idx] = 1
            next_que.append([r_idx, c_idx])
    if next_que:
        result += 1
        que = next_que
        next_que = deque()
    else:
        chk = False
        for r in range(R):
            for c in range(C):
                if MAP[r][c] == 0:
                    result = -1
                    chk = True
                    break
            if chk:
                break
        break
print(result)