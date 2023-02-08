import sys
# from collections import deque

# sys.stdin = open('input.txt', 'r')

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]


# 해당 방향으로 이동하되 경계면에서는 반대로 돌아가야함.
def move_shark(speed, direction, shark_y, shark_x):
    global R, C
    while True:
        yr, xr = shark_y+dr[direction]*speed, shark_x+dc[direction]*speed
        # 이동하고자 하는 방향으로 이동시 경계 밖으로 나갈 경우!
        if yr < 0:
            speed -= shark_y
            shark_y = 0
        elif yr >= R:
            speed -= (R-1) - shark_y
            shark_y = R-1
        elif xr < 0:
            speed -= shark_x
            shark_x = 0
        elif xr >= C:
            speed -= (C-1) - shark_x
            shark_x = C-1
        # 이동 가능한 경우
        else:
            return [direction, yr, xr]
        direction = (direction + 2) % 4


R, C, M = map(int, input().split())

MAP = [[0 for _ in range(C)] for _ in range(R)]
next_MAP = [[0 for _ in range(C)] for _ in range(R)]
alive_sharks = [1 for _ in range(M+1)]
sharks_info = [[-1]]
# BFS 를 위한 que 대신 sharks_info와 alive_sharks를 이용해
# 상어의 생존 여부와 정보 최신화, 그리고 탐색, 이동!
# que = deque()


for m in range(1, M+1):
    # r, c: 좌표
    # s   : 속력
    # d   : 방향 [1~4 >> 상 하 우 좌] >> 0~3 >> 상 우 하 좌
    # z   : 크기
    r, c, s, d, z = map(int, input().split())
    next_MAP[r-1][c-1] = m
    if d == 1:
        d = 0
    elif d == 2:
        d = 2
    elif d == 3:
        d = 1
    else:
        d = 3
    sharks_info.append([r-1, c-1, s, d, z])

king_of_fishing = -1
result = 0

while king_of_fishing < (C-1):
    king_of_fishing += 1
    for r in range(R):
        for c in range(C):
            MAP[r][c] = next_MAP[r][c]

    next_MAP = [[0 for _ in range(C)] for _ in range(R)]
    de = -1

    # 현재 낚시왕이 있는 열에서 가장 가까운 상어 제거
    for y in range(R):
        temp = MAP[y][king_of_fishing]
        if temp:
            alive_sharks[temp] = 0
            result += sharks_info[temp][4]
            MAP[y][king_of_fishing] = 0
            break

    # 상어 이동
    for m in range(1, M+1):
        if alive_sharks[m] == 0:
            continue
        y, x, s, d, z = sharks_info[m]
        if s:
            dd, yr, xr = move_shark(s, d, y, x)
        else:
            dd, yr, xr = d, y, x
        # 먼저 자리 잡은 상어가 있다면?
        if next_MAP[yr][xr]:
            # 먼저 자리 잡은 상어가 크면? 지금 이동한 상어 그냥 죽고 끝내기
            if sharks_info[next_MAP[yr][xr]][4] > z:
                alive_sharks[m] = 0
                continue
            # 들어가려는 상어가 크면? 기존 상어 죽이기
            # 그리고 새로운 상어로 교체하기
            else:
                alive_sharks[next_MAP[yr][xr]] = 0
        # 먼저 자리 잡은 상어 없다면 걍 하기
        next_MAP[yr][xr] = m
        sharks_info[m][0], sharks_info[m][1], sharks_info[m][3] = yr, xr, dd

print(result)
