import sys
from collections import deque
input = sys.stdin.readline

dr = [-2, -1, 1, 2, 2, 1, -1, -2]
dc = [1, 2, 2, 1, -1, -2, -2, -1]

T = int(input().strip())

for tc in range(T):
    N = int(input().strip())
    now_y, now_x = map(int, input().split())
    goal_y, goal_x = map(int, input().split())

    MAP = [[-1 for _ in range(N)] for _ in range(N)]
    MAP[now_y][now_x] = 0
    que = deque()
    que.append([now_y, now_x])

    while que:
        y, x = que.popleft()
        if y == goal_y and x == goal_x:
            print(MAP[y][x])
            break
        for i in range(8):
            y_idx = y + dr[i]
            x_idx = x + dc[i]
            if y_idx < 0 or y_idx >= N or x_idx < 0 or x_idx >= N:
                continue
            if MAP[y_idx][x_idx] >= 0:
                continue
            que.append([y_idx, x_idx])
            MAP[y_idx][x_idx] = MAP[y][x] + 1
