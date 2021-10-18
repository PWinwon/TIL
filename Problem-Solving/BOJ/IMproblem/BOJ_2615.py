five_board = []
test_list = [0] * 21
five_board.append(test_list)
for i in range(19):
    five_board.append([0] + list(map(int, input().split())) + [0])
five_board.append(test_list)


who_win = 0
for x in range(1, 20):
    for y in range(1, 20):
        if five_board[x][y] > 0 and five_board[x][y] != five_board[x][y-1]:     #가로
            chk = five_board[x][y]
            cnt = 0
            idx_x = x
            idx_y = y
            while True:
                if five_board[idx_x][idx_y] == chk:
                    cnt += 1
                elif cnt == 5:
                    who_win = chk
                    result_x = x
                    result_y = y
                    break
                else:
                    cnt = 0
                    break
                idx_y += 1
        
        if five_board[x][y] > 0 and five_board[x][y] != five_board[x-1][y]:     #세로
            chk = five_board[x][y]
            cnt = 0
            idx_x = x
            idx_y = y
            while True:
                if five_board[idx_x][idx_y] == chk:
                    cnt += 1
                elif cnt == 5:
                    who_win = chk
                    result_x = x
                    result_y = y
                    break
                else:
                    cnt = 0
                    break
                idx_x += 1
        
        if five_board[x][y] > 0 and five_board[x][y] != five_board[x+1][y-1]:     #우상단
            chk = five_board[x][y]
            cnt = 0
            idx_x = x
            idx_y = y
            while True:
                if five_board[idx_x][idx_y] == chk:
                    cnt += 1
                elif cnt == 5:
                    who_win = chk
                    result_x = x
                    result_y = y
                    break
                else:
                    cnt = 0
                    break
                idx_x -= 1
                idx_y += 1
        
        if five_board[x][y] > 0 and five_board[x][y] != five_board[x-1][y-1]:     #우하단
            chk = five_board[x][y]
            cnt = 0
            idx_x = x
            idx_y = y
            while True:
                if five_board[idx_x][idx_y] == chk:
                    cnt += 1
                elif cnt == 5:
                    who_win = chk
                    result_x = x
                    result_y = y
                    break
                else:
                    cnt = 0
                    break
                idx_x += 1
                idx_y += 1
    


print('{}'.format(who_win))
if who_win > 0:
    print('{} {}'.format(result_x, result_y))

