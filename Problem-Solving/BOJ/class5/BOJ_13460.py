import sys
from collections import deque

input = sys.stdin.readline

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

flag = ['R', 'B']


def move_ball(yy, xx, xxy, xxx, d):
    mby, mbx = yy, xx
    while True:
        nby, nbx = mby+dr[d], mbx+dc[d]
        if MAP[nby][nbx] == 'O':
            return (nby, nbx)
        elif MAP[nby][nbx] == '#' or (nby == xxy and nbx == xxx):
            return (mby, mbx)
        mby, mbx = nby, nbx


R, C = map(int, input().split())
MAP = [list(input().strip()) for _ in range(R)]

que = deque()

red_ball = [-1, -1]
blue_ball = [-1, -1]
for r in range(R):
    for c in range(C):
        if MAP[r][c] == 'R':
            red_ball[0] = r
            red_ball[1] = c
        elif MAP[r][c] == 'B':
            blue_ball[0] = r
            blue_ball[1] = c

temp = []
temp.append(red_ball[0])
temp.append(red_ball[1])
temp.append(blue_ball[0])
temp.append(blue_ball[1])
temp.append(0)

que.append(temp)
result = -1

while que:
    ry, rx, by, bx, cnt = que.popleft()
    if MAP[ry][rx] == 'O':
        result = cnt
        break
    if cnt >= 10:
        continue
    y_red_flag = 1
    x_red_flag = 1
    # 빨간거 먼저할지, 파란거 먼저할지
    # 파란게 더크다! 더 아래쪽에 있다! or 더 오른쪽에 있다!
    # 상 방향은 빨간거 먼저해야댐 좌 방향은 빨간거 먼저해야댐
    # 하 방향은 파란거 먼저해야댐 우 방향은 파란거 먼저해야댐
    if ry < by:
        y_red_flag *= -1
    if rx < bx:
        x_red_flag *= -1
    for i in range(2):
        if y_red_flag < 0:
            ryr, rxr = move_ball(ry, rx, by, bx, i)
            byr, bxr = move_ball(by, bx, ryr, rxr, i)
            y_red_flag *= -1
        else:
            byr, bxr = move_ball(by, bx, ry, rx, i)
            ryr, rxr = move_ball(ry, rx, byr, bxr, i)
            y_red_flag *= -1
        if MAP[byr][bxr] == 'O':
            continue
        que.append([ryr, rxr, byr, bxr, cnt + 1])

    for i in range(2, 4):
        if x_red_flag < 0:
            ryr, rxr = move_ball(ry, rx, by, bx, i)
            byr, bxr = move_ball(by, bx, ryr, rxr, i)
            x_red_flag *= -1
        else:
            byr, bxr = move_ball(by, bx, ry, rx, i)
            ryr, rxr = move_ball(ry, rx, byr, bxr, i)
            x_red_flag *= -1
        if MAP[byr][bxr] == 'O':
            continue
        que.append([ryr, rxr, byr, bxr, cnt + 1])

print(result)
