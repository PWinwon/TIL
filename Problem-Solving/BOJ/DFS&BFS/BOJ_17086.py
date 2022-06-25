import sys
from collections import deque

input = sys.stdin.readline

dr = [-1, 1, 0, 0, -1, 1, -1, 1]
dc = [0, 0, -1, 1, -1, -1, 1, 1]

R, C = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(R)]

result = -1

for r in range(R):
    for c in range(C):
        if MAP[r][c] == 0:
            que = deque()
            que.append([r, c])

            used = [[-1 for _ in range(C)] for _ in range(R)]
            used[r][c] = 0

            while que:
                y, x = que.popleft()
                if MAP[y][x] == 1:
                    if result < used[y][x]:
                        result = used[y][x]
                    break
                for i in range(8):
                    yr, xr = y + dr[i], x + dc[i]
                    if yr < 0 or yr >= R or xr < 0 or xr >= C:
                        continue
                    if used[yr][xr] >= 0:
                        continue
                    que.append([yr, xr])
                    used[yr][xr] = used[y][x] + 1

print(result)