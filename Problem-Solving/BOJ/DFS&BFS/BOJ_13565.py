import sys
from collections import deque

input = sys.stdin.readline

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

R, C = map(int, input().split())

MAP = [list(input().strip()) for _ in range(R)]
used = [[0 for _ in range(C)] for _ in range(R)]
que = deque()
result = 0

for c in range(C):
    if MAP[0][c] == '0' and used[0][c] == 0:
        que.append([0, c])
        used[0][c] = 1

        while que:
            y, x = que.popleft()
            if y == R-1:
                result = 1
                break
            for i in range(4):
                yr, xr = y+dr[i], x + dc[i]
                if yr < 0 or yr >= R or xr < 0 or xr >= C:
                    continue
                if MAP[yr][xr] == '1':
                    continue
                if used[yr][xr] == 1:
                    continue
                que.append([yr, xr])
                used[yr][xr] = 1

if result:
    print('YES')
else:
    print('NO')