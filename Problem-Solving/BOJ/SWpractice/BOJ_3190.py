# 1은 사과 2는 뱀
# 우 하 좌 상
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

from collections import deque


N = int(input())
K = int(input())
MAP = [[0 for _ in range(N)] for _ in range(N)]
actions = deque()
for k in range(K):
    y, x = map(int, input().split())
    MAP[y-1][x-1] = 1
L = int(input())
for l in range(L):
    actions.append(list(input().split()))
time = 0
dir_idx = 0
snake = [0, 0]
que = deque()
que.append([0, 0])
MAP[0][0] = 2
game_over = False
while True:
    if actions:
        act = actions.popleft()
        act_time = int(act[0])
        dir_snake = act[1]
    else:
        act_time = 10000
    while time < act_time:
        r = snake[0] + dr[dir_idx]
        c = snake[1] + dc[dir_idx]
        if r < 0 or r >= N or c < 0 or c >= N:
            game_over = True
            break
        if MAP[r][c] == 2:
            game_over = True
            break
        elif MAP[r][c] == 1:
            MAP[r][c] = 2
            snake = [r, c]
            que.append([r, c])
        else:
            tail = que.popleft()
            MAP[r][c] = 2
            MAP[tail[0]][tail[1]] = 0
            snake = [r, c]
            que.append([r, c])
        time += 1
    if game_over:
        break
    if dir_snake == 'L':
        dir_idx = (dir_idx-1) % 4
    else:
        dir_idx = (dir_idx+1) % 4
print(time+1)
