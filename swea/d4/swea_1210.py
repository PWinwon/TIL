for t in range(1,11):
    T = int(input())
    ladder_list = []
    # 입력받은 데이터를 2차원 리스트로 저장
    for n in range(100):
        sample_list = list(map(int, input().split()))
        ladder_list.append(sample_list)
    start_point = 0
    end_point = 0
    # 2차원 리스트의 99번째 원소의 리스트에서 2를 찾아 도착점을 확인
    for i in range(100):
        if ladder_list[99][i] == 2:
            end_point = i
    idx_x = 99
    idx_y = end_point
    # idx_x 는 2차원 리스트의 첫번째 인덱스 값을 가리키며 이것이 0이되면
    # 즉 도착점을 역으로 거슬러 올라가 출발점을 찾으면 반복을 멈춤
    while idx_x:
        # ladder_list[idx_x][idx_y-1] 를 이용해 도착점을 거슬러 올라가면서 경로의 왼쪽의 값이 1이면
        # idx_y 를 좌측의 1을 따라 이동시키며 다시 위쪽방향에 1이 생길때까지 while 반복문을 통해 이동
        if (idx_y-1) > 0 and ladder_list[idx_x][idx_y-1] :
            while True:
                idx_y -= 1
                if ladder_list[idx_x-1][idx_y]:
                    idx_x -= 1
                    break
        # 오른쪽의 경우에 대해서도 똑같은 처리를 하여줌
        elif (idx_y+1) <= 99 and ladder_list[idx_x][idx_y+1]:
           while True:
                idx_y += 1
                if ladder_list[idx_x-1][idx_y]:
                    idx_x -= 1
                    break
        # 양쪽에 1이없다면 즉, 좌우 이동할 길이 없다면 그냥 idx_x -= 1 을 하면서 경로를 따라 직진
        else :
            idx_x -= 1
    # idx_x = 0 이 되었을 때, idx_y의 값은 출발점의 2번째 index 값이므로 start_point에 저장 후 출력
    start_point = idx_y

    print(f'#{t} {start_point}')
