#   상 좌 하 우
dr = [-1, 0, 1, 0]
dc = [0, -1, 0, 1]


def chk_dir(r_idx, c_idx, idx):
    r_idx += dr[idx]
    c_idx += dc[idx]
    while 0 <= r_idx < N and 0 <= c_idx < N:
        if MAP[r_idx][c_idx] != 0:
            return False
        r_idx += dr[idx]
        c_idx += dc[idx]
    return True


def draw_dir(r_idx, c_idx, idx, num):
    ret_cnt = 0
    r_idx += dr[idx]
    c_idx += dc[idx]
    while 0 <= r_idx < N and 0 <= c_idx < N:
        MAP[r_idx][c_idx] = num
        r_idx += dr[idx]
        c_idx += dc[idx]
        ret_cnt += 1
    return ret_cnt


def my_func(level, cnt, co):
    global result, max_val
    if level == cores_cnt:
        if max_val <= co:
            if max_val == co and result > cnt:
                max_val = co
                result = cnt
            elif max_val < co:
                max_val = co
                result = cnt
        return
    if max_val < co and result < cnt:
        return
    row = cores[level][0]
    col = cores[level][1]
    for i in range(4):
        if chk_dir(row, col, i):
            ret = draw_dir(row, col, i, 1)
            my_func(level+1, cnt + ret, co+1)
            draw_dir(row, col, i, 0)
    my_func(level+1, cnt, co)
    return


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    MAP = [list(map(int, input().split())) for _ in range(N)]
    cores = []
    cores_cnt = 0
    max_val = 0
    result = 12 * 12
    for y in range(N):
        for x in range(N):
            if MAP[y][x] != 0 and y != 0 and y != N-1 and x != 0 and x != N-1:
                cores.append([y, x])
                cores_cnt += 1
    my_func(0, 0, 0)
    print('#{} {}'.format(tc, result))