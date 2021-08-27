#    하 우 우상 우하
dr = [1, 0, -1, 1]
dc = [0, 1, 1, 1]


def omok_chk(rr, cc):
    for i in range(4):
        r = rr + dr[i]
        c = cc + dc[i]
        cnt = 1
        while 0 <= r < N and 0 <= c < N:
            if board[r][c] == 'o':
               cnt += 1
            else:
                break
            r += dr[i]
            c += dc[i]
        if cnt >= 5:
            return True
    return False


test_case = int(input())

for tc in range(test_case):
    N = int(input())
    board = [input() for _ in range(N)]
    result = 'NO'
    for row in range(N):
        for col in range(N):
            if board[row][col] == 'o' and omok_chk(row, col):
                result = 'YES'
                break
        if result == 'YES':
            break
    print('#{} {}'.format(tc+1, result))