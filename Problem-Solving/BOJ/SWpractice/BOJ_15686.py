from collections import deque
from itertools import combinations

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


N, M = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]
used = [[-1 for _ in range(N)] for _ in range(N)]
result = 0
cnt = 0
chicken = []
for r in range(N):
    for c in range(N):
        if MAP[r][c] == 2:
            chicken.append([r, c])
        elif MAP[r][c] == 1:
            cnt += 1

for lst in list(combinations(chicken, M)):
    que = deque()
    used = [[0 for _ in range(N)] for _ in range(N)]
    chk = 0
    res = 0
    for l in lst:
        que.append(l)
        used[l[0]][l[1]] += 1
    while que:
        row, col = que.popleft()
        for i in range(4):
            r = row + dr[i]
            c = col + dc[i]
            if r < 0 or r >= N or c < 0 or c >= N:
                continue
            if used[r][c] > 0:
                continue
            if MAP[r][c] == 1:
                chk += 1
                res += used[row][col]
            que.append([r, c])
            used[r][c] += used[row][col] + 1
        if chk == cnt:
            break
        if result != 0 and res > result:
            break
    if result == 0:
        result = res
    elif result > res:
        result = res
print(result)