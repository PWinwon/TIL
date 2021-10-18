dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def dfs(row, col):
    for idx in range(4):
        rr = row+dr[idx]
        cc = col+dc[idx]
        if rr < 0 or rr >= N or cc < 0 or cc >= M:
            continue
        if used[rr][cc] == 1:
            continue
        if MAP[rr][cc] == 0:
            continue
        used[rr][cc] = 1
        dfs(rr, cc)
    return

test_case = int(input())

for tc in range(test_case):
    M, N, K = map(int, input().split())
    MAP = [[0 for _ in range(M)] for _ in range(N)]
    used = [[0 for _ in range(M)] for _ in range(N)]
    for k in range(K):
        x, y = map(int, input().split())
        MAP[y][x] = 1
    result = 0
    for r in range(N):
        for c in range(M):
            if MAP[r][c] == 1 and used[r][c] == 0:
                used[r][c] = 1
                dfs(r, c)
                result += 1
    print(result)