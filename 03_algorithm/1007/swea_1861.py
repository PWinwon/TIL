def my_func(row, col, cnt):
    memo[row][col] = cnt
    for i in range(4):
        r = row + dr[i]
        c = col + dc[i]
        if r < 0 or r >= N or c < 0 or c >= N:
            continue
        if memo[r][c] > cnt:
            continue
        if MAP[row][col] - MAP[r][c] != 1:
            continue
        my_func(r, c, cnt+1)
    return


dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    MAP = [list(map(int, input().split())) for _ in range(N)]
    memo = [[-1 for _ in range(N)] for _ in range(N)]
    max_cnt = 0
    result = N**2 + 1
    for y in range(N):
        for x in range(N):
            if memo[y][x] == -1:
                my_func(y, x, 0)
    for y in range(N):
        for x in range(N):
            if max_cnt < memo[y][x]:
                max_cnt = memo[y][x]
                result = MAP[y][x]
            elif max_cnt == memo[y][x] and result > MAP[y][x]:
                result = MAP[y][x]

    print('#{} {} {}'.format(tc, result, max_cnt+1))