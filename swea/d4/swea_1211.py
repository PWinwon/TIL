for i in range(10):
    T = int(input())
    ladder_list = []
    for lad in range(100):
        sample_list = list(map(int, input().split()))
        ladder_list.append(sample_list)
    # start_point를 선언하여, 시작점 1를 모두 찾아 그 index 값을 저장
    start_point = []
    for x in range(100):
        if ladder_list[0][x] == 1:
            start_point.append(x)
    
    idx_x = 0
    result = []
    # 각각의 start_point 의 index를 기준으로 반복문 실행
    for idx_y in start_point:
        idx_x = 0
        cnt = 0
        # 1210번과 같은 원리로 하되 cnt 변수를 통해 이동할때마다 이동 횟수를 누적시킴
        while idx_x < 99:
            if (idx_y-1 >= 0) and ladder_list[idx_x][idx_y-1]:
                while True:
                    idx_y -= 1
                    cnt += 1
                    if ladder_list[idx_x+1][idx_y]:
                        idx_x += 1
                        cnt += 1
                        break
            elif (idx_y+1 < 99) and ladder_list[idx_x][idx_y+1]:
                while True:
                    idx_y += 1
                    cnt += 1
                    if ladder_list[idx_x+1][idx_y]:
                        idx_x += 1
                        cnt += 1
                        break
            else:
                idx_x += 1
                cnt += 1
        # 누적된 cnt 반환
        result.append(cnt)
    # 가장 작은 cnt 값의 index를 반환하여 start_point에서 출발점 index 출력
    idx = result.index(min(result))
    print(f'#{i+1} {start_point[idx]}')