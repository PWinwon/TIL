# 931개
# 971개 >> T won 해결

def tik_chk(row, col, idx, ox_chk):
    dir_r = [0, 1, 1, 1]
    dir_c = [1, 0, 1, -1]
    cnt = 0
    tcnt = 0
    if row + dir_r[idx] >= 0 and row + dir_r[idx] < 4 and col + dir_c[idx] >= 0 and col + dir_c[idx] < 4 and ox_chk == 'T':
        ox_chk = tik_tok[row + dir_r[idx]][col + dir_c[idx]]
    while True:
        if row >= 0 and row < 4 and col >= 0 and col < 4 and (tik_tok[row][col] == ox_chk or tik_tok[row][col] == 'T'):
            cnt += 1
        elif cnt == 4:
            if ox_chk == '.':
                return False
            return ox_chk
        else:
            return False
        row += dir_r[idx]
        col += dir_c[idx]


test_case = int(input())

for tc in range(test_case):
    tik_tok = [input() for _ in range(4)]
    if tc != (test_case - 1):
        de = input()
    result = 'Game has not completed'
    pnt_cnt = 0
    for r in range(4):
        for c in range(4):
            if tik_tok[r][c] != '.':
                chk = tik_tok[r][c]
                if tik_chk(r, c, 0, chk) or tik_chk(r, c, 1, chk) or tik_chk(r, c, 2, chk) or tik_chk(r, c, 3, chk):
                    chk = (tik_chk(r, c, 0, chk) or tik_chk(r, c, 1, chk) or tik_chk(r, c, 2, chk) or tik_chk(r, c, 3, chk))
                    result = '{} won'.format(chk)
                    break
            elif tik_tok[r][c] == '.':
                pnt_cnt += 1
    if pnt_cnt == 0 and result == 'Game has not completed':
        result = 'Draw'

    print('#{} {}'.format(tc + 1, result))