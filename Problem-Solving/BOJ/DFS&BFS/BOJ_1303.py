import sys
from collections import deque

input = sys.stdin.readline

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

C, R = map(int, input().split())

MAP = [list(input().strip()) for _ in range(R)]

que = deque()
used = [[0 for _ in range(C)] for _ in range(R)]

result = dict()
result['B'] = 0
result['W'] = 0

for r in range(R):
    for c in range(C):
        if used[r][c] == 0:
            chk = MAP[r][c]
            que.append([r, c])
            used[r][c] = 1
            temp = 0
            while que:
                y, x = que.popleft()
                temp += 1
                for i in range(4):
                    yr, xr = y + dr[i], x + dc[i]
                    if yr < 0 or yr >= R or xr < 0 or xr >= C:
                        continue
                    if MAP[yr][xr] != chk:
                        continue
                    if used[yr][xr] == 1:
                        continue
                    que.append([yr, xr])
                    used[yr][xr] = 1
            result[chk] += temp * temp


print(result['W'], result['B'])