def my_dfs(y, x, cnt, hap):
    global result, R, C
    if cnt == 4:
        if result < hap:
            result = hap
        return

    for i in range(4):
        y_idx = y + dr[i]
        x_idx = x + dc[i]
        if y_idx < 0 or y_idx >= R or x_idx < 0 or x_idx >= C:
            continue
        if used[y_idx][x_idx]:
            continue
        used[y_idx][x_idx] = 1
        my_dfs(y_idx, x_idx, cnt+1, hap + MAP[y_idx][x_idx])
        used[y_idx][x_idx] = 0
    return


def my_except(y, x):
    global result, R, C

    ret = MAP[y][x]
    cnt = 4
    min_result = 1001

    for i in range(4):
        if cnt == 2:
            return
        y_idx = y + dr[i]
        x_idx = x + dc[i]
        if y_idx < 0 or y_idx >= R or x_idx < 0 or x_idx >= C:
            cnt -= 1
            continue

        ret += MAP[y_idx][x_idx]
        if min_result > MAP[y_idx][x_idx]:
            min_result = MAP[y_idx][x_idx]

    if cnt == 4:
        ret -= min_result

    if result < ret:
        result = ret
    return


dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

R, C = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(R)]
used = [[0 for _ in range(C)] for _ in range(R)]
result = -1
for r in range(R):
    for c in range(C):
        used[r][c] = 1
        my_dfs(r, c, 1, MAP[r][c])
        used[r][c] = 0
        my_except(r, c)

print(result)