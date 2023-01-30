import sys

input = sys.stdin.readline


def result_print():
    for a in range(9):
        print(''.join(map(str, SDQ[a])))
    return


def dfs(y, x, flag):
    if flag:
        return flag
    if y == 9:
        result_print()
        return True
    if x == 9:
        flag = dfs(y+1, 0, flag)
        return flag
    if SDQ[y][x] == 0:
        for i in range(9):
            if garo_used[y][i] == 0 and sero_used[i][x] == 0 and square_used[(y//3)*3 + x//3][i] == 0:
                garo_used[y][i] = 1
                sero_used[i][x] = 1
                square_used[(y // 3) * 3 + x // 3][i] = 1
                SDQ[y][x] = i+1
                flag = dfs(y, x+1, flag)
                garo_used[y][i] = 0
                sero_used[i][x] = 0
                square_used[(y // 3) * 3 + x // 3][i] = 0
                SDQ[y][x] = 0
    else:
        flag = dfs(y, x+1, flag)
    return flag


SDQ = [list(map(int, list(input().strip()))) for _ in range(9)]

garo_used = [[0 for _ in range(9)] for _ in range(9)]
sero_used = [[0 for _ in range(9)] for _ in range(9)]
square_used = [[0 for _ in range(9)] for _ in range(9)]

for r in range(9):
    for c in range(9):
        if SDQ[r][c]:
            garo_used[r][SDQ[r][c]-1] = 1
            sero_used[SDQ[r][c]-1][c] = 1
            square_used[(r//3)*3 + c//3][SDQ[r][c]-1] = 1

dfs(0, 0, False)