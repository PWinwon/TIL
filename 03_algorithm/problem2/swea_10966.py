from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

test_case = int(input())

for tc in range(test_case):
    N, M = map(int, input().split())
    MAP = [input() for _ in range(N)]
    used = [[-1 for _ in range(M)] for _ in range(N)]
    que = deque()
    for r in range(N):
        for c in range(M):
            if MAP[r][c] == 'W':
                que.append([r, c])
                used[r][c] = 0
    while que:
        temp = que.popleft()
        row = temp[0]
        col = temp[1]
        for idx in range(4):
            r = row + dr[idx]
            c = col + dc[idx]
            if r < 0 or r >= N or c < 0 or c >= M:
                continue
            if used[r][c] > -1:
                continue
            que.append([r, c])
            used[r][c] = used[row][col] + 1
    result = 0
    for r in range(N):
        for c in range(M):
            if MAP[r][c] == 'L':
                result += used[r][c]
    print('#{} {}'.format(tc+1, result))