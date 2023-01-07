import sys
from collections import deque

input = sys.stdin.readline

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

N, L, R = map(int, input().split())

MAP = [list(map(int, input().split())) for _ in range(N)]

result = -1
chk = 0

while True:
    if chk == N*N + 1:
        break
    chk = 1
    chk_list = [0]
    used = [[0 for _ in range(N)] for _ in range(N)]
    result += 1

    for r in range(N):
        for c in range(N):
            if used[r][c] == 0:
                que = deque()
                que.append([r, c])
                used[r][c] = chk

                total = 0
                count = 0

                while que:
                    y, x = que.popleft()
                    total += MAP[y][x]
                    count += 1
                    for i in range(4):
                        y_idx, x_idx = y + dr[i], x + dc[i]
                        if y_idx < 0 or y_idx >= N or x_idx < 0 or x_idx >= N:
                            continue
                        if used[y_idx][x_idx]:
                            continue
                        gap = abs(MAP[y][x] - MAP[y_idx][x_idx])
                        if gap < L or gap > R:
                            continue
                        used[y_idx][x_idx] = chk
                        que.append([y_idx, x_idx])

                temp = total // count
                chk_list.append(temp)
                chk += 1
    for r in range(N):
        for c in range(N):
            MAP[r][c] = chk_list[used[r][c]]

print(result)

