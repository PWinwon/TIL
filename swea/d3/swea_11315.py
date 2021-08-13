# 오목판에서 'o' 가 있는 좌표일때 4방향을 모두 확인할 수 있는 함수 작성
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

# 출력값에서 result='NO'를 기본값으로 설정
# 생성한 함수에 대해 return True가 나오는 순간 result = 'YES' 저장
# result = 'YES'가 되면 나머지는 검증이 필요하지 않기때문에 조건을 주어 더이상 반복을 하지 않도록 함
for tc in range(test_case):
    N = int(input())
    lst_board = [input() for _ in range(N)]
    result = 'NO'
    for r in range(N):
        for c in range(N):
            if lst_board[r][c] == 'o' and result == 'NO':
                if omok_chk(r, c, N , 0) or omok_chk(r, c, N , 1) or omok_chk(r, c, N , 2) or omok_chk(r, c, N , 3):
                    result = 'YES'
                    break

    print('#{} {}'.format(tc+1, result))
