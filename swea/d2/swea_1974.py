T = int(input())

for i in range(T):
    sdoqu = []
    for j in range(9):
        sample_ls = list(map(int, input().split()))
        sdoqu.append(sample_ls)
    # print(sdoqu)
    result = 1
    for x in range(9):
        check_ls = []
        for y in range(9):
            if check_ls:
                if sdoqu[x][y] in check_ls:
                    result = 0
                    break
            check_ls.append(sdoqu[x][y])
    
    for x in range(9):
        check_ls = []
        for y in range(9):
            if check_ls:
                if sdoqu[y][x] in check_ls:
                    result = 0
                    break
            check_ls.append(sdoqu[y][x])
    
    for x in range(0,9,3):
        for y in range(0,9,3):
            check_ls = []
            for ck_x in range(x,x+3):
                for ck_y in range(y,y+3):
                    if check_ls:
                        if sdoqu[ck_x][ck_y] in check_ls:
                            result = 0
                            break
                    check_ls.append(sdoqu[ck_x][ck_y])
    print(f'#{i+1} {result}')

