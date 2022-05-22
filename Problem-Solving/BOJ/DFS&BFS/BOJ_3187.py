import sys
from collections import deque

input = sys.stdin.readline

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

R, C = map(int,input().split())
MAP = [list(input().strip()) for _ in range(R)]

used = [[0 for _ in range(C)] for _ in range(R)]

wolf_cnt = 0
sheep_cnt = 0

for r in range(R):
    for c in range(C):
        if (MAP[r][c] == 'k' or MAP[r][c] == 'v') and used[r][c] == 0:
            wolf_temp = 0
            sheep_temp = 0

            que = deque()
            que.append([r, c])
            used[r][c] = 1

            while que:
                y, x = que.popleft()
                if MAP[y][x] == 'v':
                    wolf_temp += 1
                elif MAP[y][x] == 'k':
                    sheep_temp += 1

                for i in range(4):
                    y_idx, x_idx = y + dr[i], x + dc[i]
                    if y_idx < 0 or y_idx >= R or x_idx < 0 or x_idx >= C:
                        continue
                    if MAP[y_idx][x_idx] == '#':
                        continue
                    if used[y_idx][x_idx] == 1:
                        continue
                    que.append([y_idx, x_idx])
                    used[y_idx][x_idx] = 1

            if wolf_temp >= sheep_temp:
                wolf_cnt += wolf_temp
            else:
                sheep_cnt += sheep_temp

print(sheep_cnt, wolf_cnt)
