import sys
from collections import deque

input = sys.stdin.readline

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

R, C = map(int, input().split())

MAP = [list(map(int, input().split())) for _ in range(R)]
used = [[0 for _ in range(C)] for _ in range(R)]
que = deque()

result_cnt = 0
result_max = 0

for r in range(R):
    for c in range(C):
        if MAP[r][c] == 1 and used[r][c] == 0:
            used[r][c] = 1
            que.append([r, c])
            result_cnt += 1
            temp = 0
            while que:
                y, x = que.popleft()
                temp += 1
                for i in range(4):
                    y_idx = y + dr[i]
                    x_idx = x + dc[i]
                    if y_idx < 0 or y_idx >= R or x_idx < 0 or x_idx >= C:
                        continue
                    if MAP[y_idx][x_idx] == 0 or used[y_idx][x_idx] == 1:
                        continue
                    used[y_idx][x_idx] = 1
                    que.append([y_idx, x_idx])

            if temp > result_max:
                result_max = temp

print(result_cnt)
print(result_max)