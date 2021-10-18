from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


R, C = map(int, input().split())
MAP = [list(input()) for _ in range(R)]
used = [[-1 for _ in range(C)] for _ in range(R)]
que = deque()
fire = []
for r in range(R):
    for c in range(C):
        if MAP[r][c] == 'S':
            que.append([r, c, 'S'])
            used[r][c] = 0
        elif MAP[r][c] == '*':
            fire.append([r, c, '*'])
for f in fire:
    que.append(f)
result = 0
while que:
    temp = que.popleft()
    row = temp[0]
    col = temp[1]
    wh = temp[2]
    if result:
        break
    for i in range(4):
        r = row + dr[i]
        c = col + dc[i]
        if r < 0 or r >= R or c < 0 or c >= C:
            continue
        if wh == 'S' and MAP[r][c] == 'D':
            result = used[row][col] + 1
            break
        if MAP[r][c] != '.':
            continue
        if MAP[row][col] == '*':
            MAP[r][c] = '*'
            que.append([r, c, '*'])
            used[r][c] = 0
            continue
        if used[r][c] > -1:
            continue
        que.append([r, c, wh])
        used[r][c] = used[row][col] + 1

if result:
    print(result)
else:
    print('impossible')