from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

for _ in range(10):
    T = int(input())
    miro = [list(map(int, input())) for _ in range(16)]
    used = [[0 for _ in range(16)] for _ in range(16)]
    que = deque()
    que.append([1, 1])
    used[1][1] = 1
    result = 0
    while que:
        temp = que.popleft()
        row = temp[0]
        col = temp[1]
        if miro[row][col] == 3:
            result = 1
            break
        for i in range(4):
            r = row + dr[i]
            c = col + dc[i]
            if r < 0 or r > 15 or c < 0 or c > 15:
                continue
            if used[r][c] == 1:
                continue
            if miro[r][c] == 1:
                continue
            que.append([r, c])
            used[r][c] = 1
    print('#{} {}'.format(T, result))