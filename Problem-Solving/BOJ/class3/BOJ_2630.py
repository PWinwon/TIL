import sys

def my_func(rs, re, cs, ce, n):
    global bres, wres

    chk = MAP[rs][cs]
    flag = True

    for r in range(rs, re):
        for c in range(cs, ce):
            if MAP[r][c] != chk:
                flag = False
                break
    if flag:
        if chk:
            bres += 1
        else:
            wres += 1
    else:
        my_func(rs, rs+n//2, cs, cs+n//2, n//2)
        my_func(rs, rs+n//2, cs+n//2, ce, n//2)
        my_func(rs+n//2, re, cs, cs+n//2, n//2)
        my_func(rs+n//2, re, cs+n//2, ce, n//2)
    return


N = int(input())
MAP = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

bres = 0
wres = 0

my_func(0, N, 0, N, N)

print(wres)
print(bres)