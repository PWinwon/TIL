#       하 우하 좌하
dir_r = [1, 1, 1]
dir_c = [0, 1, -1]


def queen_mark(row, col, num):
    for idx in range(3):
        r = row
        c = col
        while 0 <= r+dir_r[idx] < N and 0 <= c+dir_c[idx] < N:
            r += dir_r[idx]
            c += dir_c[idx]
            chess[r][c] += num
    return


def queen_path(level):
    global cnt
    if level == N:
        cnt += 1
        return
    for i in range(N):
        if chess[level][i] > 0:
            continue
        queen_mark(level, i, 1)
        queen_path(level+1)
        queen_mark(level, i, -1)
    return


N = int(input())
chess = [[0 for _ in range(N)] for _ in range(N)]
cnt = 0
queen_path(0)
print(cnt)