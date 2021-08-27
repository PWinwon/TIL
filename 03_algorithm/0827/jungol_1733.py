#     우, 하, 우상, 우하
dr = [0, 1, -1, 1]
dc = [1, 0, 1, 1]
#       좌 상 좌하 좌상
rchk = [0, -1, 1, -1]
cchk = [-1, 0, -1, -1]


def omok_chk(rr, cc, chk):
    for i in range(4):
        r_c = rr+rchk[i]
        c_c = cc+cchk[i]
        if 0 <= r_c < 19 and 0 <= c_c < 19 and board[r_c][c_c] == chk:
            continue
        cnt = 1
        r = rr + dr[i]
        c = cc + dc[i]
        while 0 <= r < 19 and 0 <= c < 19:
            if board[r][c] == chk:
                cnt += 1
            else:
                break
            r = r + dr[i]
            c = c + dc[i]
        if cnt == 5:
            return True
    return False


board = [list(map(int, input().split())) for _ in range(19)]

result = 0
res_y = 0
res_x = 0
for row in range(19):
    for col in range(19):
        if board[row][col] != 0:
            temp = board[row][col]
            if omok_chk(row, col, temp):
                result = temp
                res_y = row+1
                res_x = col+1
                break
    if result:
        break

if result:
    print(result)
    print(res_y, res_x)
else:
    print(result)
