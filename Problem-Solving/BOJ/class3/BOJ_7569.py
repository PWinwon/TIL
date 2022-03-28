from collections import deque

def chk(d):
    for h in range(H):
        for r in range(R):
            for c in range(C):
                if MAP[h][r][c] == 0:
                    return -1
    return d

# 상 하 좌 우 위 아래
dr = [-1, 1, 0, 0, 0, 0]
dc = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

C, R, H = map(int, input().split())

MAP = []
for h in range(H):
    temp = [list(map(int, input().split())) for _ in range(R)]
    MAP.append(temp)

old_tmt = []
total_cnt = C * R * H
cnt_m1 = 0
cnt_1 = 0
for h in range(H):
    for r in range(R):
        for c in range(C):
            if MAP[h][r][c] == 1:
                old_tmt.append([h, r, c, 0])
                cnt_1 += 1
            elif MAP[h][r][c] == -1:
                cnt_m1 += 1
if total_cnt == cnt_m1 + cnt_1:
    print(0)
else:
    que = deque(old_tmt)
    used = [[[0 for _ in range(C)] for _ in range(R)] for _ in range(H)]
    for h, r, c, t in old_tmt:
        used[h][r][c] = 1
    result = 0
    while que:
        z, y, x, cnt = que.popleft()
        for i in range(6):
            z_idx = z + dz[i]
            y_idx = y + dr[i]
            x_idx = x + dc[i]
            if z_idx < 0 or z_idx >= H or y_idx < 0 or y_idx >= R or x_idx < 0 or x_idx >= C:
                continue
            if MAP[z_idx][y_idx][x_idx]:
                continue
            if used[z_idx][y_idx][x_idx]:
                continue
            que.append([z_idx, y_idx, x_idx, cnt + 1])
            used[z_idx][y_idx][x_idx] = 1
            MAP[z_idx][y_idx][x_idx] = 1
            result = cnt + 1

    result = chk(result)
    print(result)