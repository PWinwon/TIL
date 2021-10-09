dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def my_func(level, row, col, path):
    global result
    if level == 7:
        if path in ret.keys():
            return
        else:
            result += 1
            ret[path] = 1
            return
    for i in range(4):
        r = row + dr[i]
        c = col + dc[i]
        if r < 0 or r >= 4 or c < 0 or c >=4:
            continue
        my_func(level+1, r, c, path+MAP[row][col])
    return


T = int(input())

for tc in range(1, T+1):
    MAP = [list(input().split()) for _ in range(4)]
    ret = {}
    result = 0
    for y in range(4):
        for x in range(4):
            my_func(0, y, x, '')
    print('#{} {}'.format(tc, result))