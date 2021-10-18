N, B = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]


def my_sqare(bd, bdt):
    temp = [[0 for _ in range(N)] for _ in range(N)]
    bdt = list(zip(*bdt))
    for r in range(N):
        lst1 = bd[r]
        for c in range(N):
            lst2 = bdt[c]
            for i in range(N):
                temp[r][c] += lst1[i] % 1000 * lst2[i] % 1000
                temp[r][c] = temp[r][c] % 1000
    return temp


def my_fun2(bd):
    for r in range(N):
        for c in range(N):
            if bd[r][c] >= 1000:
                bd[r][c] = bd[r][c]%1000
    return bd


def my_fun(num):
    if num == 1:
        return my_fun2(board)
    mat = my_fun(num//2)
    mat = my_sqare(mat, mat)
    if num % 2:
        mat = my_sqare(mat, board)
    return mat


result = my_fun(B)
for row in range(N):
    print(' '.join(map(str, result[row])))