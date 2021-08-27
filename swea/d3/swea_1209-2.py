for tc in range(1, 11):
    T = int(input())
    MAP = [list(map(int, input().split())) for _ in range(100)]
    max_val = 0
    cross1 = 0
    cross2 = 0
    for r in range(100):
        garo = 0
        sero = 0
        for c in range(100):
            garo += MAP[r][c]
            sero += MAP[c][r]
            if r == c:
                cross1 += MAP[r][c]
            if r + c == 99:
                cross2 += MAP[r][c]
        if max_val < garo:
            max_val = garo
        if max_val < sero:
            max_val = sero
    if max_val < cross1:
        max_val = cross1
    if max_val < cross2:
        max_val = cross2

    print('#{} {}'.format(T, max_val))