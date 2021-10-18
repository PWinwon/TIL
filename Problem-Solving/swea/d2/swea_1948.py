# 각 달의 마지막 날을 담은 리스트 생성
month_last_day = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

T = int(input())

for i in range(T):
    # 연산을 할 두 날짜를 입력받음
    fir_m, fir_d, sec_m, sec_d = map(int, input().split())
    gap = 1
    # 두 날짜의 차이를 gap에 계속 누적시킴
    # 달과 일에 대해 각각 조건문을 통해 연산
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