import sys
from collections import deque

input = sys.stdin.readline

dr = {'-': 0, '|': 1}
dc = {'-': 1, '|': 0}

R, C = map(int, input().split())

MAP = [list(input().strip()) for _ in range(R)]
used = [[0 for _ in range(C)] for _ in range(R)]
que = deque()

result = 0

for r in range(R):
    for c in range(C):
        if used[r][c] == 0:
            chk = MAP[r][c]

            result += 1
            que.append([r, c])
            used[r][c] = 1

            while que:
                y, x = que.popleft()
                yr = y + dr[chk]
                xr = x + dc[chk]
                if yr < 0 or yr >= R or xr < 0 or xr >= C:
                    continue
                if MAP[yr][xr] != chk:
                    continue
                if used[yr][xr] == 1:
                    continue
                que.append([yr, xr])
                used[yr][xr] = 1

print(result)