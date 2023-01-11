import sys
from collections import deque

input = sys.stdin.readline
INF = float('inf')

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def fill_MAP(chk, sr, sc, d):
    global R, C
    que = deque()
    que.append([sr, sc])

    while que:
        y, x = que.popleft()
        yr, xr = y+dr[d], x+dc[d]
        if yr < 0 or yr >= R or xr < 0 or xr >= C:
            continue
        if MAP[yr][xr] == 6:
            continue
        que.append([yr, xr])
        if 1 <= MAP[yr][xr] <= 5:
            continue
        MAP[yr][xr] = chk

    return

def count_MAP():
    global R, C
    ret = 0
    for r in range(R):
        for c in range(C):
            if MAP[r][c] == 0:
                ret += 1
    return ret


def dfs(n):
    global cctv_cnt, result
    if n == cctv_cnt:
        ret = count_MAP()
        if ret < result:
            result = ret
        return
    cctv = cctves[n]
    num = MAP[cctv[0]][cctv[1]]
    if num == 1:
        for i in range(4):
            fill_MAP(7, cctv[0], cctv[1], i)
            dfs(n+1)
            fill_MAP(0, cctv[0], cctv[1], i)
    elif num == 2:
        for i in [0, 2]:
            fill_MAP(7, cctv[0], cctv[1], i)
            fill_MAP(7, cctv[0], cctv[1], i+1)
            dfs(n+1)
            fill_MAP(0, cctv[0], cctv[1], i)
            fill_MAP(0, cctv[0], cctv[1], i+1)
    elif num == 3:
        for i in range(4):
            fill_MAP(7, cctv[0], cctv[1], i)
            fill_MAP(7, cctv[0], cctv[1], (i + 1) % 4)
            dfs(n + 1)
            fill_MAP(0, cctv[0], cctv[1], i)
            fill_MAP(0, cctv[0], cctv[1], (i + 1) % 4)
    elif num == 4:
        for i in range(4):
            fill_MAP(7, cctv[0], cctv[1], i)
            fill_MAP(7, cctv[0], cctv[1], (i + 1) % 4)
            fill_MAP(7, cctv[0], cctv[1], (i - 1) % 4)
            dfs(n + 1)
            fill_MAP(0, cctv[0], cctv[1], i)
            fill_MAP(0, cctv[0], cctv[1], (i + 1) % 4)
            fill_MAP(0, cctv[0], cctv[1], (i - 1) % 4)
    else:
        fill_MAP(7, cctv[0], cctv[1], 0)
        fill_MAP(7, cctv[0], cctv[1], 1)
        fill_MAP(7, cctv[0], cctv[1], 2)
        fill_MAP(7, cctv[0], cctv[1], 3)
        dfs(n+1)
        fill_MAP(0, cctv[0], cctv[1], 0)
        fill_MAP(0, cctv[0], cctv[1], 1)
        fill_MAP(0, cctv[0], cctv[1], 2)
        fill_MAP(0, cctv[0], cctv[1], 3)
    return


R, C = map(int, input().split())

MAP = [list(map(int, input().split())) for _ in range(R)]

cctves = []
cctv_cnt = 0
total = 0
result = INF

for r in range(R):
    for c in range(C):
        if 1 <= MAP[r][c] <= 5:
            cctves.append([r, c])
            cctv_cnt += 1
        if MAP[r][c] == 0:
            total += 1

de = -1
dfs(0)
print(result)