import sys
from collections import deque

# sys.stdin = open('input.txt', 'r')


def grow_tree():
    global N
    que = deque()
    for r in range(N):
        for c in range(N):
            if MAP[r][c] > 0:
                cnt = 0
                for i in range(4):
                    yr, xr = r+dr[i], c+dc[i]
                    if 0 <= yr < N and 0 <= xr < N:
                       if MAP[yr][xr] > 0:
                           cnt += 1
                que.append([r, c, cnt])

    while que:
        y, x, c = que.popleft()
        MAP[y][x] += c
    de = -1
    return


def expand_tree():
    global N
    que = deque()
    for r in range(N):
        for c in range(N):
            if MAP[r][c] > 0:
                cnt = 0
                expandLst = []
                for i in range(4):
                    yr, xr = r+dr[i], c+dc[i]
                    if 0 <= yr < N and 0 <= xr < N:
                        if MAP[yr][xr] == 0 and herbMAP[yr][xr] == 0:
                            cnt += 1
                            expandLst.append([yr, xr])

                for i in range(cnt):
                    que.append([expandLst[i][0], expandLst[i][1], MAP[r][c] // cnt])

    while que:
        y, x, c = que.popleft()
        MAP[y][x] += c
    de = -1
    return


def kill_tree():
    global N, K, C
    max_val = 0
    mr, mc = -1, -1

    for r in range(N):
        for c in range(N):
            if herbMAP[r][c] > 0:
                herbMAP[r][c] -= 1

    for r in range(N):
        for c in range(N):
            if MAP[r][c] >= 0:
                temp = MAP[r][c]
                if MAP[r][c] != 0:
                    for i in range(4):
                        for k in range(1, K+1):
                            yr, xr = r+(dkr[i]*k), c+(dkc[i]*k)
                            if yr < 0 or yr >= N or xr < 0 or xr >= N:
                                break
                            if MAP[yr][xr] <= 0:
                                break
                            temp += MAP[yr][xr]
                if temp > max_val:
                    max_val = temp
                    mr, mc = r, c
    de = -1
    MAP[mr][mc] = 0
    herbMAP[mr][mc] = C
    for i in range(4):
        for k in range(1, K+1):
            yr, xr = mr+dkr[i]*k, mc+dkc[i]*k
            if yr < 0 or yr >= N or xr < 0 or xr >= N:
                break
            if MAP[yr][xr] <= 0:
                if MAP[yr][xr] == 0:
                    herbMAP[yr][xr] = C
                break
            MAP[yr][xr] = 0
            herbMAP[yr][xr] = C
    de = -1
    return max_val


def simulation():
    grow_tree()
    expand_tree()
    ret = kill_tree()
    return ret


input = sys.stdin.readline
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

dkr = [-1, 1, 1, -1]
dkc = [1, 1, -1, -1]

N, M, K, C = map(int, input().split())

MAP = [list(map(int, input().split())) for _ in range(N)]
herbMAP = [[0 for _ in range(N)] for _ in range(N)]

answer = 0
for m in range(M):
    answer += simulation()

print(answer)