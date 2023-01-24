import sys
from collections import deque

input = sys.stdin.readline

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def bfs():
    global queJh, queFire, R, C
    ret = 0

    while True:
        ret += 1

        temp = []
        while queFire:
            y, x = queFire.popleft()
            for i in range(4):
                yr, xr = y+dr[i], x+dc[i]
                if yr < 0 or yr >= R or xr < 0 or xr >= C:
                    continue
                if MAP[yr][xr] == '.' or MAP[yr][xr] == '$':
                    temp.append([yr, xr])
                    MAP[yr][xr] = 'F'

        queFire = deque(temp)

        temp = []
        while queJh:
            y, x = queJh.popleft()

            if y == 0 or y == R-1 or x == 0 or x == C-1:
                return ret

            for i in range(4):
                yr, xr = y+dr[i], x+dc[i]
                if yr < 0 or yr >= R or xr < 0 or xr >= C:
                    continue
                if MAP[yr][xr] == '.':
                    temp.append([yr, xr])
                    MAP[y][x] = '$'
                    MAP[yr][xr] = 'J'

        queJh = deque(temp)
        if not queJh:
            return False


R, C = map(int, input().split())
MAP = [list(input().strip()) for _ in range(R)]

queJh = deque()
queFire = deque()
used = [[0 for _ in range(C)] for _ in range(R)]

for r in range(R):
    for c in range(C):
        if MAP[r][c] == 'F':
            queFire.append([r, c])
        elif MAP[r][c] == 'J':
            queJh.append([r, c])

r = bfs()
if r:
    print(r)
else:
    print('IMPOSSIBLE')

