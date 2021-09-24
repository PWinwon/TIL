dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def my_func(row, col, now, k, tot):
    global result
    if tot > result:
        result = tot
    for i in range(4):
        rr = row + dr[i]
        cc = col + dc[i]
        if rr < 0 or rr >= N or cc < 0 or cc >= N:
            continue
        if used[rr][cc] == 1:
            continue
        if now <= MAP[rr][cc]:
            temp = MAP[rr][cc] - now
            if k == 1 and temp < K:
                used[rr][cc] = 1
                my_func(rr, cc, MAP[rr][cc]-temp-1, 0, tot+1)
                used[rr][cc] = 0
            continue
        else:
            used[rr][cc] = 1
            my_func(rr, cc, MAP[rr][cc], k, tot+1)
            used[rr][cc] = 0
    return


test_case = int(input())

for tc in range(test_case):
    N, K = map(int, input().split())
    MAP = [list(map(int, input().split())) for _ in range(N)]
    used = [[0 for _ in range(N)] for _ in range(N)]
    t = 0
    for i in range(N):
        max_val = max(MAP[i])
        if t < max_val:
            t = max_val
    result = 0
    for r in range(N):
        for c in range(N):
            if MAP[r][c] == t:
                used[r][c] = 1
                my_func(r, c, t, 1, 1)
                used[r][c] = 0
    print('#{} {}'.format(tc+1, result))