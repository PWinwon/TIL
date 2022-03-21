def my_func(sr, er, sc, ec, n):
    global result
    chk = MAP[sr][sc]
    flag = True
    for r in range(sr, er):
        if flag == False:
            break
        for c in range(sc, ec):
            if MAP[r][c] != chk:
                flag = False
                break

    if flag:
        result += chk
    else:
        m = n // 2
        result += '('
        for y in range(sr, er, m):
            for x in range(sc, ec, m):
                my_func(y, y+m, x, x+m, m)

        result += ')'
        return


N = int(input())
MAP = [list(input()) for _ in range(N)]
result = ''
my_func(0, N, 0, N, N)
print(result)