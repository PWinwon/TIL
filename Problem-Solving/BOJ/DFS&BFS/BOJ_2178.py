import sys
from collections import deque

#     상, 하, 좌, 우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

N, M = map(int, sys.stdin.readline().split())
miro = [list(map(int, input())) for _ in range(N)]
used = [[0 for _ in range(M)] for _ in range(N)]

que = deque()
que.append([0, 0])
used[0][0] = 1
result = 0
while que:
    temp = que.popleft()
    r = temp[0]
    c = temp[1]
    if (r, c) == (N-1, M-1):
        result = used[r][c]
        break
    for i in range(4):
        if 0 > r+dr[i] or r+dr[i] >= N or 0 > c+dc[i] or c+dc[i] >= M:
            continue
        if miro[r+dr[i]][c+dc[i]] == 1 and used[r+dr[i]][c+dc[i]] == 0:
            used[r+dr[i]][c+dc[i]] = used[r][c] + 1
            que.append([r+dr[i], c+dc[i]])


print(result)