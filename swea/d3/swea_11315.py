# num 이 0일때는 가로, 1일때는 세로, 2일때 우하단, 3일때 좌하단
def omok_chk(row, col, n, num):
    dr_row = [0, 1, 1, 1]
    dr_col = [1, 0, 1, -1]
    cnt = 0
    while True:
        if col >= 0 and col < n and row >= 0 and row < n and lst_board[row][col] == 'o':
            cnt += 1
        else:
            if cnt >= 5:
                return True
            else:
                return False
        row += dr_row[num]
        col += dr_col[num]



test_case = int(input())

for tc in range(test_case):
    N = int(input())
    lst_board = [input() for _ in range(N)]
    result = 'NO'
    for r in range(N):
        for c in range(N):
            if lst_board[r][c] == 'o':
                if omok_chk(r, c, N , 0) or omok_chk(r, c, N , 1) or omok_chk(r, c, N , 2) or omok_chk(r, c, N , 3):
                    result = 'YES'
    
    print('#{} {}'.format(tc+1, result))
