def sdoqu_chk(lst):
    sample = []
    idx = 0
    while idx < 9:
        for i in range(len(sample)):
            if sample[i] == lst[idx]:
                return True
        sample.append(lst[idx])
        idx += 1
    return False

test_case = int(input())

for tc in range(test_case):
    sdoqu = [list(map(int, input().split())) for _ in range(9)]
    sdoqu2 = list(zip(*sdoqu))
    result = 1
    for r in range(9):
        if sdoqu_chk(sdoqu[r]):
            result = 0
        if sdoqu_chk(sdoqu2[r]):
            result = 0
        if result == 0:
            break
    for r in range(0, 9, 3):
        if result == 0:
            break
        sqare = []
        for c in range(0, 9, 3):
            for y in range(r, r+3):
                for x in range(c, c+3):
                    sqare.append(sdoqu[y][x])

            if sdoqu_chk(sqare):
                result = 0
    print('#{} {}'.format(tc+1, result))