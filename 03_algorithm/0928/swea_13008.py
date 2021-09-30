from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

test_case = int(input())

for tc in range(test_case):
    H, W, N = map(int, input().split())
    MAP = [list(input()) for _ in range(H)]
    now = [[0, 0, 0]]
    for tar in range(1, N+1):
        que = deque()
        used = [[0 for _ in range(W)] for _ in range(H)]
        for n in now:
            que.append([n[0], n[1], n[2]])
            used[n[0]][n[1]] = 1
        now = []
        while que:
            temp = que.popleft()
            row = temp[0]
            col = temp[1]
            cnt = temp[2]
            if int(MAP[row][col]) == tar:
                now.append([row, col, cnt])
                break
            for i in range(4):
                r = row + dr[i]
                c = col + dc[i]
                if r < 0 or r >= H or c < 0 or c >= W:
                    continue
                if MAP[r][c] == '#':
                    continue
                if used[r][c] == 1:
                    continue
                used[r][c] = 1
                que.append([r, c, cnt+1])
    print('#{} {}'.format(tc+1, now[0][2]))