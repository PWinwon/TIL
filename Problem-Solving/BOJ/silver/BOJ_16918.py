import sys
from collections import deque

# sys.stdin = open('input.txt', 'r')

input = sys.stdin.readline
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

R, C, N = map(int, input().split())
MAP = [list(input().strip()) for _ in range(R)]

# print(MAP)
que = deque()

for r in range(R):
    for c in range(C):
        if MAP[r][c] == 'O':
            que.append([r, c])

# 처음에는 그냥 ㄱㄱ

time = 1
flag = 1
while time < N:
    de = -1
    if flag > 0:
        # 빈칸에 폭탄 채우기
        next_que = deque()
        for r in range(R):
            for c in range(C):
                if MAP[r][c] == '.':
                    MAP[r][c] = 'O'
        flag *= -1

    else:
        while que:
            y, x = que.popleft()
            MAP[y][x] = '.'
            for i in range(4):
                yr, xr = y+dr[i], x+dc[i]
                if yr < 0 or yr >= R or xr < 0 or xr >= C:
                    continue
                if MAP[yr][xr] == '.':
                    continue
                MAP[yr][xr] = '.'

        for r in range(R):
            for c in range(C):
                if MAP[r][c] == 'O':
                    que.append([r, c])
        flag *= -1
    time += 1

for r in range(R):
    print(''.join(map(str, MAP[r])))