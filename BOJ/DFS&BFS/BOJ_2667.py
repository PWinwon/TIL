dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def dfs(row, col):
    global cnt
    cnt += 1
    for idx in range(4):
        rr = row+dr[idx]
        cc = col+dc[idx]
        if rr < 0 or rr >= N or cc < 0 or cc >= N:
            continue
        if used[rr][cc] == 1:
            continue
        if MAP[rr][cc] == 0:
            continue
        used[rr][cc] = 1
        dfs(rr, cc)
    return


N = int(input())
MAP = [list(map(int, list(input()))) for _ in range(N)]
used = [[0 for _ in range(N)] for _ in range(N)]
result = []


for r in range(N):
    for c in range(N):
        if MAP[r][c] == 1 and used[r][c] == 0:
            cnt = 0
            used[r][c] = 1
            dfs(r, c)
            result.append(cnt)
result.sort()
print(len(result))
for i in result:
    print(i)