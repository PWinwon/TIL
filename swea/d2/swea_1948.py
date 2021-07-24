month_last_day = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

T = int(input())

for i in range(T):
    fir_m, fir_d, sec_m, sec_d = map(int, input().split())

    gap = 1

    while True:
        if fir_m == sec_m:
            if fir_d == sec_d:
                break
            else:
                gap += sec_d - fir_d
                fir_d = sec_d
        else:
            gap += month_last_day[fir_m-1]
            fir_m += 1

    print(f'#{i+1} {gap}')