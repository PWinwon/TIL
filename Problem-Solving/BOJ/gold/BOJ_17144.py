dr = [0, -1, 0, 1]
dc = [1, 0, -1, 0]

drr = [0, 1, 0, -1]
dcc = [1, 0, -1, 0]

R, C, T = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(R)]


for r in range(R):
    if MAP[r][0] == -1:
        air_up = r
        air_down = r+1
        break

# print(air_clear)

for time in range(T):
    # 미세먼지 확산
    # 미세먼지가 저장될 2차원 배열 선언
    extend_dust = [[0 for _ in range(C)] for _ in range(R)]
    for r in range(R):
        for c in range(C):
            dust = MAP[r][c]
            if (dust//5) > 0:
                add_dust = dust//5
                cnt = 0
                for i in range(4):
                    row = r + dr[i]
                    col = c + dc[i]
                    if row < 0 or row >= R or col < 0 or col >= C:
                        continue
                    if MAP[row][col] < 0:
                        continue
                    cnt += 1
                    extend_dust[row][col] += add_dust
                extend_dust[r][c] += dust - (add_dust * cnt)
            else:
                extend_dust[r][c] += MAP[r][c]
    for r in range(R):
        for c in range(C):
            if MAP[r][c] == -1:
                continue
            MAP[r][c] = extend_dust[r][c]
    de = -1
    # 공기청정기 가동
    # 위쪽 순환
    temp_up = MAP[air_up][1]
    MAP[air_up][1] = 0
    up_idx_r = air_up
    up_idx_c = 1
    d_idx = 0
    # 우 > 상 > 좌 > 하
    while MAP[up_idx_r][up_idx_c] != -1:
        if 0 <= up_idx_r + dr[d_idx] < R and 0 <= up_idx_c + dc[d_idx] < C:
            up_idx_r += dr[d_idx]
            up_idx_c += dc[d_idx]
            if MAP[up_idx_r][up_idx_c] == -1:
                break
            temp_up, MAP[up_idx_r][up_idx_c] = MAP[up_idx_r][up_idx_c], temp_up
        else:
            d_idx += 1

    # 아래 순환
    temp_down = MAP[air_down][1]
    MAP[air_down][1] = 0
    down_idx_r = air_down
    down_idx_c = 1
    d_idx = 0
    # 우 > 하 > 좌 > 상
    while MAP[down_idx_r][down_idx_c] != -1:
        if 0 <= down_idx_r + drr[d_idx] < R and 0 <= down_idx_c + dcc[d_idx] < C:
            down_idx_r += drr[d_idx]
            down_idx_c += dcc[d_idx]
            if MAP[down_idx_r][down_idx_c] == -1:
                break
            temp_down, MAP[down_idx_r][down_idx_c] = MAP[down_idx_r][down_idx_c], temp_down
        else:
            d_idx += 1


result = 0
for r in range(R):
    for c in range(C):
        if MAP[r][c] > 0:
            result += MAP[r][c]
print(result)