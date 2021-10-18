#    상 좌 하 우
dr = [-1, 0, 1, 0]
dc = [0, -1, 0, 1]


N, K = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]
used = [['' for _ in range(N)] for _ in range(N)]

players = []
for i in range(K):
    R, C, idx = map(int, input().split())
    used[R-1][C-1] += str(i)
    players.append([R, C, idx])

result = 0
while result < 1000:
    for j in range(K):
        r = players[j][0]
        c = players[j][1]
        idx = players[j][2]
        if used[r][c][0] == str(j):
            row = r + dr[idx]
            col = c + dc[idx]
            if row < 0 or row >= N or col < 0 or col >= N or MAP[row][col] == 2:
                idx = (idx + 2) % 4
                row = r + dr[idx]
                col = c + dc[idx]

            used[row][col] += used[r][c]
            used[r][c] = ''
        else:
            pass
