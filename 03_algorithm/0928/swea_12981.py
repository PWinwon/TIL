from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def my_func(row, col):
    que = deque()
    que.append([row, col])
    while que:
        temp = que.popleft()
        rr = temp[0]
        cc = temp[1]
        for idx in range(4):
            y = rr + dr[idx]
            x = cc + dc[idx]
            if y < 0 or y >= N or x < 0 or x >= M:
                continue
            if MAP[y][x] == 0:
                continue
            if used[y][x] != 0:
                continue
            used[y][x] = 1
            que.append([y, x])
    return


test_case = int(input())

for tc in range(test_case):
    N, M = map(int, input().split())
    MAP = [list(map(int, input().split())) for _ in range(N)]
    used = [[0 for _ in range(M)] for _ in range(N)]
    result = 0
    for r in range(N):
        for c in range(M):
            if MAP[r][c] == 2 and used[r][c] == 0:
                used[r][c] = 1
                my_func(r, c)
                result += 1
    print('#{} {}'.format(tc+1, result))