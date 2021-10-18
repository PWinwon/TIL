def check_sdoqu(list,tf):
    # check_ls 라는 빈 리스트를 생성해 비교할 줄의 리스트의 원소를
    # 차례대로 append 하여 in을 사용해 그 안에 비교하는 값이 유일한지 확인
    check_ls = []
    for l in range(len(list)):
        if list[l] in check_ls:
            return 0
        check_ls.append(list[l])
    return tf

T = int(input())

for i in range(T):
    sdoqu = []
    for j in range(9):
        sample_ls = list(map(int, input().split()))
        sdoqu.append(sample_ls)
    result = 1
    # 가로와 세로를 각각의 리스트에 저장
    # check_sdoqu 함수를 이용해 각각의 리스트가 참인지 확인
    for x in range(9):
        check_sero = []
        check_garo = []
        for y in range(9):
            check_garo.append(sdoqu[x][y])
            check_sero.append(sdoqu[y][x])
        result = check_sdoqu(check_garo, result)
        result = check_sdoqu(check_sero, result)
    # 3x3의 칸이 스도쿠로서 참인지 확인
    # x와 y로 3x3의 시작점을 지정
    for x in range(0,9,3):
        for y in range(0,9,3):
            check_sqare = []
            #ck_x와 ck_y를 이용해 시작점을 기준으로 3x3에 해당하는 값을 리스트에 저장
            for ck_x in range(x,x+3):
                for ck_y in range(y,y+3):
                    check_sqare.append(sdoqu[ck_x][ck_y])
            result = result = check_sdoqu(check_sqare, result)
    print(f'#{i+1} {result}')

