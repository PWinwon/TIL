import sys
from collections import deque

# sys.stdin = open('input.txt', 'r')

input = sys.stdin.readline
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

R, C = map(int, input().split())

MAP = [list(map(int, input().split())) for _ in range(R)]
used = [[0 for _ in range(C)] for _ in range(R)]

que = deque()
next_que = deque()

result1 = 0
result2 = 0

que.append([0, 0])
used[0][0] = 1

while que:
    y, x = que.popleft()
    for i in range(4):
        yr, xr = y+dr[i], x+dc[i]
        if yr < 0 or yr >= R or xr < 0 or xr >= C:
            continue
        if used[yr][xr]:
            continue
        used[yr][xr] = 1
        if MAP[yr][xr]:
            next_que.append([yr, xr])
            MAP[yr][xr] = 0
            result2 += 1
        else:
            que.append([yr, xr])

de = -1
ret = result2
while next_que:
    que = next_que
    next_que = deque()
    ret = result2
    result2 = 0
    while que:
        y, x = que.popleft()
        for i in range(4):
            yr, xr = y + dr[i], x + dc[i]
            if yr < 0 or yr >= R or xr < 0 or xr >= C:
                continue
            if used[yr][xr]:
                continue
            used[yr][xr] = used[y][x] + 1
            if MAP[yr][xr]:
                next_que.append([yr, xr])
                MAP[yr][xr] = 0
                result2 += 1
            else:
                que.append([yr, xr])

    result1 += 1

print(result1)
print(ret)
