import sys
from collections import deque

input = sys.stdin.readline

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

R, C = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(R)]
used = [[0 for _ in range(C)] for _ in range(R)]

que = deque()
out_que = deque()

# 외곽 먼저 돌면서 외부공기 찾기
for r in range(R):
    for c in range(C):
        if (r == 0 or r == R-1 or c == 0 or c == C-1) and MAP[r][c] == 0:
            MAP[r][c] = 2
            out_que.append([r, c])

            while out_que:
                y, x = out_que.popleft()
                for i in range(4):
                    yr, xr = y+dr[i], x+dc[i]
                    if yr < 0 or yr >= R or xr < 0 or xr >= C:
                        continue
                    if MAP[yr][xr]:
                        continue
                    out_que.append([yr, xr])
                    MAP[yr][xr] = 2
        elif MAP[r][c] == 1:
            que.append([r, c])

result = 0

while True:
    melting_cheeses = deque()
    next_que = deque()
    while que:
        y, x = que.popleft()
        cnt = 4
        for i in range(4):
            yr, xr = y+dr[i], x+dc[i]
            if yr < 0 or yr >= R or xr < 0 or xr >= C:
                continue
            if MAP[yr][xr] == 2:
                continue
            cnt -= 1
        # 1시간 뒤 녹는 치즈라면?
        if cnt >= 2:
            melting_cheeses.append([y, x])
        else:
            next_que.append([y, x])

    while melting_cheeses:
        y, x = melting_cheeses.popleft()
        MAP[y][x] = 2
        for i in range(4):
            yr, xr = y+dr[i], x+dc[i]
            if yr < 0 or yr >= R or xr < 0 or xr >= C:
                continue
            if MAP[yr][xr]:
                continue
            MAP[yr][xr] = 2
            melting_cheeses.append([yr, xr])
    result += 1
    if next_que:
        que = next_que
    else:
        break

print(result)


