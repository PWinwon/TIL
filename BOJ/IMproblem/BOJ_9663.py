#       상, 하, 좌, 우, 우상, 우하, 좌상, 좌하
dir_r = [-1, 1, 0, 0, -1, 1, -1, 1]
dir_c = [0, 0, -1, 1, 1, 1, -1, -1]


def my_visit(r, c, num):
    visited[r][c] += num
    for j in range(8):
        row = r
        col = c
        while 0 <= row + dir_r[j] < N and 0 <= col+dir_c[j] < N:
            row += dir_r[j]
            col += dir_c[j]
            visited[row][col] += num
    return


def save_queen(level):
    global cnt
    if level == N:
        cnt += 1
        return
    for i in range(N):
        if visited[level][i] >= 1:
            continue
        my_visit(level, i, 1)
        save_queen(level+1)
        my_visit(level, i, -1)
    return


N = int(input())
cnt = 0
visited = [[0 for _ in range(N)] for _ in range(N)]
save_queen(0)
print(cnt)