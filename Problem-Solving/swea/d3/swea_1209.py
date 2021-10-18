for t in range(10):
    T = int(input())
    case_sqare = []
    # 2차원 리스트 형태로 case_sqare 에 저장
    for loop_num in range(100):
        sample_list = list(map(int, input().split()))
        case_sqare.append(sample_list)
    # 각 행과 열의 합을 받아올 result와 각 대각선의 값을 받아올 변수 설정
    result = []
    cross_line1 = 0
    cross_line2 = 0
    for x in range(100):
        galo_val = 0
        selo_val = 0
        for y in range(100):
            #각각 가로와 세로의 값을 더해서 누적시킴
            galo_val += case_sqare[x][y]
            selo_val += case_sqare[y][x]
            #각각 오른쪽 대각선과 왼쪽 대각선의 값에 맞는 조건을 주어 값을 누적
            if (x == y):
                cross_line1 += case_sqare[x][y]
            if (x + y == 99):
                cross_line2 += case_sqare[x][y]
        # result 리스트에 추가하고 다시 반복
        result.append(galo_val)
        result.append(selo_val)
    # 대각선은 큰 반복당 한번씩 값이 누적되므로 모든 반복을 종료후 누적된 값을 append
    result.append(cross_line1)
    result.append(cross_line2)
    print(f'#{T} {max(result)}')

