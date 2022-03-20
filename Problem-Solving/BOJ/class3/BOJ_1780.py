import sys

def my_func(sr, er, sc, ec, cnt):
    global res_1, res_2, res_3

    chk = MAP[sr][sc]
    flag = True
    for r in range(sr, er):
        for c in range(sc, ec):
            if MAP[r][c] != chk:
                flag = False
                break
    if flag:
        if chk < 0:
            res_1 += 1
        elif chk > 0:
            res_3 += 1
        else:
            res_2 += 1
        return
    else:
        m = cnt // 3
        for y in range(sr, er, m):
            for x in range(sc, ec, m):
                my_func(y, y+m, x, x+m, m)

        return




N = int(input())
MAP = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

res_1 = 0
res_2 = 0
res_3 = 0

my_func(0, N, 0, N, N)

print(res_1)
print(res_2)
print(res_3)