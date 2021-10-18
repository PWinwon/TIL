dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def my_func(row, col, chk, res):
    global max_val
    if max_val == 26:
        return
    if max_val < res:
        max_val = res
    for i in range(4):
        rr = row + dr[i]
        cc = col + dc[i]
        if rr < 0 or rr >= R or cc < 0 or cc >= C:
            continue
        if used[ord(MAP[rr][cc]) - ord('A')] >= 1:
            continue
        used[ord(MAP[rr][cc]) - ord('A')] += 1
        my_func(rr, cc, chk+MAP[rr][cc], res+1)
        used[ord(MAP[rr][cc]) - ord('A')] -= 1
    return


R, C = map(int, input().split())
MAP = [list(input()) for _ in range(R)]
used = [0] * 26
used[ord(MAP[0][0]) - ord('A')] += 1
max_val = 0
my_func(0, 0, MAP[0][0], 1)
print(max_val)