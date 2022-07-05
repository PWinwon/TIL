import sys
from collections import deque

input = sys.stdin.readline

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

R, C = map(int, input().split())

MAP = [list(map(int, input().split())) for _ in range(R)]

T = int(input().strip())

TMAP = [[0 for _ in range(C)] for _ in range(R)]

for r in range(R):
    for c in range(C):
        temp = (MAP[r][c*3] + MAP[r][c*3+1] + MAP[r][c*3+2]) / 3
        if temp >= T:
            TMAP[r][c] = 255
        else:
            TMAP[r][c] = 0

que = deque()
used = [[0 for _ in range(C)] for _ in range(R)]

result = 0
for r in range(R):
    for c in range(C):
        if TMAP[r][c] == 255 and used[r][c] == 0:
            result += 1
            que.append([r, c])
            used[r][c] = 1

            while que:
                y, x = que.popleft()
                for i in range(4):
                    yr, xr = y + dr[i], x + dc[i]
                    if yr < 0 or yr >= R or xr < 0  or xr >= C:
                        continue
                    if TMAP[yr][xr] != 255 or used[yr][xr] == 1:
                        continue
                    que.append([yr, xr])
                    used[yr][xr] = 1

print(result)