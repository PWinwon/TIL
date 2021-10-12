    #우하 좌하 좌상 우상
dr = [1, 1, -1, -1]
dc = [1, -1, -1, 1]


def dv_chk():
    for i in range(4):
        if not dv[i]:
            return False
    return True


def path_chk(row, col, idx, cnt):
    global result
    if idx == 4:
        if row+dr[3] == y and col+dc[3] == x and result < cnt and dv_chk():
            result = cnt
        return
    r = row + dr[idx]
    c = col + dc[idx]
    if 0 <= r < N and 0 <= c < N and used[MAP[r][c]] == 0 and dv[idx] != 0:
        dv[idx+1] += 1
        used[MAP[r][c]] = 1
        path_chk(r, c, idx, cnt+1)
        dv[idx+1] -= 1
        used[MAP[r][c]] = 0
    path_chk(row, col, idx+1, cnt)
    return


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    MAP = [list(map(int, input().split())) for _ in range(N)]
    used = [0] * 101
    dv = [1] + [0] * 4
    result = -1
    for y in range(N):
        for x in range(N):
            used[MAP[y][x]] = 1
            path_chk(y, x, 0, 1)
            used[MAP[y][x]] = 0
    print('#{} {}'.format(tc, result))