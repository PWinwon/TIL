
# num 이 0일때는 가로, 1일때는 세로, 2일때 우하단, 3일때 좌하단
def omok_chk(row, col, n, num):
    dr_row = [0, 1, 1, 1]
    dr_col = [1, 0, 1, -1]
    idx_r = 0
    idx_c = 0
    cnt = 0
    while True:
        if col < n and lst_board[row + idx_r][col + idx_c] == 'o':
            cnt += 1
        else:
            return False
        if cnt == 5:
            return True
        idx_r += dr_row[num]
        idx_c += dr_col[num]



test_case = int(input())

for tc in range(test_case):
    N = int(input())
    lst_board = [list(input().split()) for _ in range(N)]

    for r in range(N):
        for c in range(N):
            if lst_board[r][c] == 'o':
                omok_chk(r, c, N , 0)
                omok_chk(r, c, N , 1)
                omok_chk(r, c, N , 2)
                omok_chk(r, c, N , 3)
