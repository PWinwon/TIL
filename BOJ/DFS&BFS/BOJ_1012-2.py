from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


T = int(input())

for tc in range(T):
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
                result += 1
                used[r][c] = 1
                que = deque()
                que.append([r, c])
                while que:
                    temp = que.popleft()
                    for idx in range(4):
                        row = temp[0] + dr[idx]
                        col = temp[1] + dc[idx]
                        if row < 0 or row >= N or col < 0 or col >= M:
                            continue
                        if used[row][col] == 1 or MAP[row][col] == 0:
                            continue
                        que.append([row, col])
                        used[row][col] = 1

    print(result)