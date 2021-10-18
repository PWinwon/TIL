for tc in range(1, 11):
    N = int(input())
    table = [list(map(int, input().split())) for _ in range(100)]
    result = 0
    for c in range(100):
        chk = 0
        for r in range(100):
            if table[r][c] == 1:
                chk = 1
            if table[r][c] == 2 and chk == 1:
                result += 1
                chk = 0

    print('#{} {}'.format(tc, result))