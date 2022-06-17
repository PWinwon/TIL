import sys
from collections import deque

input = sys.stdin.readline

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

R, C, K = map(int, input().split())
MAP = [[0 for _ in range(C)] for _ in range(R)]
used = [[0 for _ in range(C)] for _ in range(R)]
for i in range(K):
    a, b = map(int, input().split())
    MAP[a-1][b-1] = 1

que = deque()

result = -1

for r in range(R):
    for c in range(C):
        if MAP[r][c] == 1 and used[r][c] == 0:
            que.append([r, c])
            used[r][c] = 1
            temp = 0
            while que:
                y, x = que.popleft()
                temp += 1
                for i in range(4):
                    yr, xr = y+dr[i], x+dc[i]
                    if yr < 0 or yr >= R or xr < 0 or xr >= C:
                        continue
                    if MAP[yr][xr] == 0:
                        continue
                    if used[yr][xr] == 1:
                        continue
                    used[yr][xr] = 1
                    que.append([yr, xr])
            if result < temp:
                result = temp

print(result)