import sys
from collections import deque

input = sys.stdin.readline

# 상 하 좌 우 위 아래
dr = [-1, 1, 0, 0, 0, 0]
dc = [0, 0, -1, 1, 0, 0]
dl = [0, 0, 0, 0, -1, 1]

while True:
    L, R, C = map(int, input().split())
    if L == 0 and R == 0 and C == 0:
        break
    MAP = []
    for l in range(L):
        temp = [list(input().strip()) for _ in range(R)]
        MAP.append(temp)
        temp = input().strip()
    result = 0

    que = deque()
    used = [[[0 for _ in range(C)] for _ in range(R)] for _ in range(L)]

    for l in range(L):
        for r in range(R):
            for c in range(C):
                if MAP[l][r][c] == 'S':
                    que.append([l, r, c, 0])
                    used[l][r][c] = 1

    while que:
        z, y, x, cnt = que.popleft()
        if MAP[z][y][x] == 'E':
            result = cnt
            break
        for i in range(6):
            zr, yr, xr = z+dl[i], y+dr[i], x+dc[i]
            if zr < 0 or zr >= L or yr < 0 or yr >= R or xr < 0 or xr >= C:
                continue
            if MAP[zr][yr][xr] == '#':
                continue
            if used[zr][yr][xr] == 1:
                continue
            que.append([zr, yr, xr, cnt+1])
            used[zr][yr][xr] = 1
    if result:
        print('Escaped in {} minute(s).'.format(result))
    else:
        print('Trapped!')