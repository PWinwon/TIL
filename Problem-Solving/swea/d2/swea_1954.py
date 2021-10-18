T = int(input())

for i in range(T):
    n = int(input())
    # 달팽이 출력될 2차원 리스트 0으로 초기화
    list_dalpang = [0] * n
    for j in range(n):
        line = []
        for k in range(n):
            line += [0]
        list_dalpang[j] = line
    max_val = n**2
    x_idx = 0
    y_idx = -1
    pl_mn = 1
    val = 1
    num = n
    # val은 달팽이에 입력될 숫자, max_val은 달팽이에 입력될 가장 큰 숫자
    # 달팽이를 따라 이동하면서 idx의 증감과 x와 y 어느 부분에 이동이 있는지를 확인하여 입력
    while(val <= max_val):
        for y in range(n):
            y_idx += pl_mn
            list_dalpang[x_idx][y_idx] += val
            val += 1
        for x in range(n-1):
            x_idx += pl_mn
            list_dalpang[x_idx][y_idx] = val
            val += 1
        # 달팽이의 특성상 증가와 감소를 반복하기 때문에 이를 조절해줄 변수 사용
        pl_mn *= (-1)
        n -= 1
    print(f'#{i+1}')
    for x in range(num):
        for y in range(num):
            print(list_dalpang[x][y], end = ' ')
        print('')