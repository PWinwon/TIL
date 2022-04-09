from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

N = int(input())
MAP = [list(map(int, input().split())) for _ in range(N)]

sy, sx = -1, -1
for r in range(N):
    for c in range(N):
        if MAP[r][c] == 9:
            sy, sx = r, c
            MAP[sy][sx] = 0
            break

que = deque()
baby = 2
exp = 0
result = 0
while True:
    que.append([sy, sx, 0])
    used = [[0 for _ in range(N)] for _ in range(N)]
    used[sy][sx] = 1
    eats = []
    while que:
        sr, sc, cnt = que.popleft()
        for i in range(4):
            r_idx = sr + dr[i]
            c_idx = sc + dc[i]
            if r_idx < 0 or r_idx >= N or c_idx < 0 or c_idx >= N:
                continue
            if MAP[r_idx][c_idx] > baby:
                continue
            if used[r_idx][c_idx]:
                continue
            que.append([r_idx, c_idx, cnt + 1])
            used[r_idx][c_idx] = 1
            if 0 < MAP[r_idx][c_idx] < baby:
                eats.append([cnt+1, r_idx, c_idx])

    if eats:
        eats.sort()
        a, b, c = eats[0]
        sy = b
        sx = c
        MAP[sy][sx] = 0
        result += a
        exp += 1
        if baby == exp:
            baby += 1
            exp = 0
    else:
        break

print(result)