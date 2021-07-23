def line_check(lines):
    check = []
    for j in range(9):
        if check:
            if lines[j] in check:
                return 0
        check.append(list[j])
    return 1


def sdoqu_mir(s):
    result = s
    for x in range(9):
        for y in range(9):
            result[x][y] = s[y][x]
    return result


T = int(input())

for i in range(T):
    sdoqu = []
    for j in range(9):
        sample_list = list(map(int, input().split()))
        sdoqu.append(sample_list)
    result = 1
    m_sdoqu = sdoqu_mir(sdoqu)
    for sdo in sdoqu:
        if line_check(sdo):
            continue
        else:
            result = 0
            break
    for m in m_sdoqu:
        if line_check(sdo):
            continue
        else:
            result = 0
            break
    for x in range(0,9,3):
        for y in range(0,9,3):
            sqare_list = []
            for ck_x in range(x,x+3):
                for ck_y in range(y, y+3):
                    sqare_list.append(sdoqu[ck_x][ck_y])
            if line_check(sdo):
                continue
            else:
                result = 0
                break
    print(f'#{i+1} {result}')

