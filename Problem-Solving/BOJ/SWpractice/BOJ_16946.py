from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def cnt_zero(row, col, mycnt):
    global R, C
    que = deque()
    que.append([row, col])
    ret = 1
    while que:
        y, x = que.popleft()
        for i in range(4):
            y_idx = y + dr[i]
            x_idx = x + dc[i]
            if y_idx < 0 or y_idx >= R or x_idx < 0 or x_idx >= C:
                continue
            if my_MAP[y_idx][x_idx]:
                continue
            if MAP[y_idx][x_idx] == '1':
                continue
            que.append([y_idx, x_idx])
            my_MAP[y_idx][x_idx] = mycnt
            ret += 1
    return ret




R, C = map(int, input().split())

MAP = [input() for _ in range(R)]

my_MAP = [[0 for _ in range(C)] for _ in range(R)]
lst = [0]

result = [[0 for _ in range(C)] for _ in range(R)]

cnt = 1
for r in range(R):
    for c in range(C):
        if MAP[r][c] == '0' and my_MAP[r][c] == 0:
            my_MAP[r][c] = cnt
            ret = cnt_zero(r, c, cnt)
            lst.append(ret)
            cnt += 1

for r in range(R):
    for c in range(C):
        if MAP[r][c] == '1':
            temp = set()
            for i in range(4):
                r_idx = r + dr[i]
                c_idx = c + dc[i]
                if r_idx < 0 or r_idx >= R or c_idx < 0 or c_idx >= C:
                    continue
                if my_MAP[r_idx][c_idx] == 0:
                    continue
                temp.add(my_MAP[r_idx][c_idx])
            result[r][c] += 1
            for t in temp:
                result[r][c] += lst[t]
                result[r][c] %= 10


for r in range(R):
    print(''.join(list(map(str, result[r]))))