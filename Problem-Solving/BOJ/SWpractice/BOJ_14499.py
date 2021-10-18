# 1: 동 2: 서 3: 북 4: 남
dr = [0, 0, 0, -1, 1]
dc = [0, 1, -1, 0, 0]


def rotation_dice(idx):
    if idx == 1:
        my_dice[1], my_dice[3], my_dice[6], my_dice[4] = my_dice[3], my_dice[6], my_dice[4], my_dice[1]
    elif idx == 2:
        my_dice[1], my_dice[3], my_dice[6], my_dice[4] = my_dice[4], my_dice[1], my_dice[3], my_dice[6]
    elif idx == 3:
        my_dice[1], my_dice[5], my_dice[6], my_dice[2] = my_dice[2], my_dice[1], my_dice[5], my_dice[6]
    else:
        my_dice[1], my_dice[5], my_dice[6], my_dice[2] = my_dice[5], my_dice[6], my_dice[2], my_dice[1]
    return


R, C, y, x, K = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(R)]
commands = list(map(int, input().split()))
# index 1이 바닥, 6이 하늘
my_dice = [0] * 7

for com in commands:
    y += dr[com]
    x += dc[com]
    if y < 0 or y >= R or x < 0 or x >= C:
        y -= dr[com]
        x -= dc[com]
        continue
    rotation_dice(com)
    if MAP[y][x] == 0:
        MAP[y][x] = my_dice[1]
        print(my_dice[6])
    else:
        my_dice[1] = MAP[y][x]
        MAP[y][x] = 0
        print(my_dice[6])