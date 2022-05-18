import sys
from collections import deque

input = sys.stdin.readline

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


T = int(input().strip())

for tc in range(T):
    R, C = map(int, input().split())

    MAP = [list(input().strip()) for _ in range(R)]
    used = [[0 for _ in range(C)] for _ in range(R)]

    que = deque()
    result = 0
    for r in range(R):
        for c in range(C):
            if used[r][c] == 0 and MAP[r][c] == '#':
                used[r][c] = 1
                que.append([r, c])

                while que:
                    y, x = que.popleft()
                    for i in range(4):
                        ny, nx = y+dr[i], x+dc[i]
                        if ny < 0 or ny >= R or nx < 0 or nx >= C:
                            continue
                        if MAP[ny][nx] == '.':
                            continue
                        if used[ny][nx] == 1:
                            continue
                        used[ny][nx] = 1
                        que.append([ny, nx])
                result += 1
    print(result)