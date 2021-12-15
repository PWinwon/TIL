from collections import deque


def swan_chk(q):
    ret_que = deque()

    while q:
        y, x = q.popleft()

        for i in range(4):
            y_idx = y + dr[i]
            x_idx = x + dc[i]

            if y_idx < 0 or y_idx >= R or x_idx < 0 or x_idx >=C:
                continue
            if used[y_idx][x_idx]:
                continue

            if MAP[y_idx][x_idx] == 'L':
                return 'S'

            elif MAP[y_idx][x_idx] == 'X':
                ret_que.append([y_idx, x_idx])

            elif MAP[y_idx][x_idx] == '.':
                q.append([y_idx, x_idx])
            used[y_idx][x_idx] = 1

    return ret_que


def melt_ice():
    ice_side_cnt = len(ice_side)

    for j in range(ice_side_cnt):
        y, x = ice_side.popleft()
        MAP[y][x] = '.'
        for i in range(4):
            y_idx = y + dr[i]
            x_idx = x + dc[i]

            if y_idx < 0 or y_idx >= R or x_idx < 0 or x_idx >= C:
                continue
            if MAP[y_idx][x_idx] == 'X' and ice_melt_time[y_idx][x_idx] == 0:
                ice_side.append([y_idx, x_idx])
                ice_melt_time[y_idx][x_idx] = ice_melt_time[y][x] + 1



dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


R, C = map(int, input().split())

MAP = [list(input()) for _ in range(R)]
used = [[0 for _ in range(C)] for _ in range(R)]
ice_melt_time = [[0 for _ in range(C)] for _ in range(R)]

ice_side = deque()

for r in range(R):
    for c in range(C):
        if MAP[r][c] == 'L':
            swan = [r, c]
            break

for r in range(R):
    for c in range(C):
        if MAP[r][c] == 'X':
            for i in range(4):
                r_idx = r + dr[i]
                c_idx = c + dc[i]

                if r_idx < 0 or r_idx >= R or c_idx < 0 or c_idx >= C:
                    continue
                if MAP[r_idx][c_idx] == '.' or MAP[r_idx][c_idx] == 'L':
                    ice_melt_time[r][c] = 1
                    ice_side.append([r, c])
                    break

# 백조를 que에 추가

que = deque()
que.append([swan[0], swan[1]])
used[swan[0]][swan[1]] = 1
result = 0
while True:
    que = swan_chk(que)
    if que == 'S':
        print(result)
        break
    melt_ice()
    result += 1