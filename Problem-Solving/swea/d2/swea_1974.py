T = int(input())

for i in range(T):
    sdoqu = []
    for j in range(9):
        sample_ls = list(map(int, input().split()))
        sdoqu.append(sample_ls)
    # print(sdoqu)
    result = 1

    # 스도쿠의 가로가 참인지 확인
    for x in range(9):
        check_ls = []
        for y in range(9):
            # check_ls 라는 빈 리스트를 생성해 비교할 줄의 리스트의 원소를
            # 차례대로 append 하여 in을 사용해 그 안에 비교하는 값이 유일한지 확인
            if check_ls:
                if sdoqu[x][y] in check_ls:
                    result = 0
                    break
            check_ls.append(sdoqu[x][y])
    
    # 스도쿠의 세로가 참인지 확인
    for x in range(9):
        check_ls = []
        for y in range(9):
            if check_ls:
                #세로를 확인하기 위해 x와 y의 좌표변경
                if sdoqu[y][x] in check_ls:
                    result = 0
                    break
            check_ls.append(sdoqu[y][x])
    
    # 3x3의 칸이 스도쿠로서 참인지 확인
    # x와 y로 3x3의 시작점을 지정
    for x in range(0,9,3):
        for y in range(0,9,3):
            check_ls = []
            #ck_x와 ck_y를 이용해 시작점을 기준으로 3x3에 해당하는 값을 리스트에 저장
            for ck_x in range(x,x+3):
                for ck_y in range(y,y+3):
                    if check_ls:
                        if sdoqu[ck_x][ck_y] in check_ls:
                            result = 0
                            break
                    check_ls.append(sdoqu[ck_x][ck_y])
    print(f'#{i+1} {result}')

