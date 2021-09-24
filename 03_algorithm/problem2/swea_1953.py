from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

canGo = [ # 상           # 하             #좌              #우
    [],
    [[0,1,1,0,0,1,1,0],[0,1,1,0,1,0,0,1],[0,1,0,1,1,1,0,0],[0,1,0,1,0,0,1,1]],
    [[0,1,1,0,0,1,1,0],[0,1,1,0,1,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]],
    [[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,1,0,1,1,1,0,0],[0,1,0,1,0,0,1,1]],
    [[0,1,1,0,0,1,1,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,1,0,1,0,0,1,1]],
    [[0,0,0,0,0,0,0,0],[0,1,1,0,1,0,0,1],[0,0,0,0,0,0,0,0],[0,1,0,1,0,0,1,1]],
    [[0,0,0,0,0,0,0,0],[0,1,1,0,1,0,0,1],[0,1,0,1,1,1,0,0],[0,0,0,0,0,0,0,0]],
    [[0,1,1,0,0,1,1,0],[0,0,0,0,0,0,0,0],[0,1,0,1,1,1,0,0],[0,0,0,0,0,0,0,0]],
]
# canGo[now 구조물타입] [ 방향 t] [ next 구조물타입]

test_case = int(input())

for tc in range(test_case):
    N, M, R, C, L = map(int, input().split())
    MAP = [list(map(int, input().split())) for _ in range(N)]
    used = [[0 for _ in range(M)] for _ in range(N)]
    que = deque()
    que.append([R, C])
    used[R][C] = 1
    result = 1
    while que:
        temp = que.popleft()
        row = temp[0]
        col = temp[1]
        if used[row][col] >= L:
            break
        for i in range(4):
            r = row + dr[i]
            c = col + dc[i]
            if r < 0 or r >= N or c < 0 or c >= M:
                continue
            if MAP[r][c] == 0:
                continue
            if used[r][c] > 0:
                continue
            if canGo[MAP[row][col]][i][MAP[r][c]] == 0:
                continue
            used[r][c] += used[row][col] + 1
            que.append([r, c])
            result += 1
    print('#{} {}'.format(tc+1, result))