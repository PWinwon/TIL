import sys
from collections import deque

input = sys.stdin.readline

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

R, C, K = map(int, input().split())

MAP = [[0 for _ in range(C)] for _ in range(R)]
used = [[0 for _ in range(C)] for _ in range(R)]

que = deque()

for k in range(K):
    x1, y1, x2, y2 = map(int, input().split())

    for x in range(x1, x2):
        for y in range(y1, y2):
            MAP[y][x] = 1


result1 = 0
result2 = []

for r in range(R):
    for c in range(C):
        if MAP[r][c] == 0 and used[r][c] == 0:
            result1 += 1
            temp = 0
            que.append([r, c])
            used[r][c] = 1

            while que:
                y, x = que.popleft()
                temp += 1
                for i in range(4):
                    yr, xr = y+dr[i], x+dc[i]
                    if yr < 0 or yr >= R or xr < 0 or xr >= C:
                        continue
                    if MAP[yr][xr] == 1:
                        continue
                    if used[yr][xr] == 1:
                        continue
                    que.append([yr, xr])
                    used[yr][xr] = 1

            result2.append(temp)

print(result1)
result2.sort()
print(' '.join(map(str, result2)))