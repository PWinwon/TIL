from collections import deque

# 우 >> 상 >> 좌 >> 하 >> 우

# 우측, 하단, 우하
drf = [0, 1, 1]
dcf = [1, 0, 1]

def my_chk(r, c):
    chk = 0
    for i in range(3):
        r_idx = r + drf[i]
        c_idx = c + dcf[i]
        if r_idx < 0 or r_idx > 100 or c_idx < 0 or c_idx > 100:
            return False
        if MAP[r_idx][c_idx] == 0:
            return False
        chk += 1
    if chk == 3:
        return True
    else:
        return False



#    우  상  좌  하
dr = [0, -1, 0, 1]
dc = [1, 0, -1, 0]

N = int(input())
MAP = [[0 for _ in range(101)] for _ in range(101)]
result = 0
for n in range(N):
    x, y, d, g = map(int, input().split())
    MAP[y][x] = 1
    direction = []
    y_idx = y + dr[d]
    x_idx = x + dc[d]
    MAP[y_idx][x_idx] = 1
    direction.append(d)
    for g_idx in range(g):
        que = deque(direction)
        while que:
            temp = que.pop()
            d_idx = (temp + 1) % 4
            y_idx += dr[d_idx]
            x_idx += dc[d_idx]
            MAP[y_idx][x_idx] = 1
            direction.append(d_idx)


for r in range(101):
    for c in range(101):
        if MAP[r][c] == 1:
            if my_chk(r, c):
                result += 1
print(result)
