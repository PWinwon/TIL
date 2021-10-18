T = int(input())

for i in range(T):
    N = int(input())
    list_n = []
    # 입력값 2차원 리스트에 저장
    for n in range(N):
        sample_list = list(map(int, input().split()))
        list_n.append(sample_list)
    # 행과 열에 대해 길이를 담아올 리스트 생성
    list_hang = []
    list_y = []
    # 반복문을 통해 2차원 리스트 안의 값에 대해 0이 아니면 cnt += 1을 하다가 
    # 0을 만나거나 행이 끝나면 cnt를 리스트에 추가
    for x in range(N):
        cnt = 0
        for y in range(N):
            if list_n[x][y]:
                cnt += 1
            elif cnt: 
                list_hang.append(cnt)
                cnt = 0
            if y == N-1 and cnt:
                list_hang.append(cnt)
                cnt = 0
    # 리스트에 행에 대한 정보를 담고 있으므로 set 을 이용해서 중복값 제거
    # 행의 길이는 서로 모두 다르다고 했으므로 중복값 제거 가능
    list_h = list(set(list_hang))
    # 행의 개수(열의 길이)를 구해 이를 리스트로 묶어 저장
    for k in list_h:
        list_y.append([list_hang.count(k), k])
    result = [0] * len(list_y)
    # 앞서 구한 행과 열에 대한 길이의 리스트에 대해 정렬을 위한 반복
    for x in range(len(list_y)):
        idx = 0
        for y in range(len(list_y)):
            # 행과 열의 곱을 통해 넓이를 비교
            if list_y[x][0] * list_y[x][1] > list_y[y][0] * list_y[y][1]:
                idx += 1
            # 넓이가 같은 경우 행의 길이가 긴 것이 뒤에 출력
            if list_y[x][0] * list_y[x][1] == list_y[y][0] * list_y[y][1]:
                if list_y[x][0] > list_y[y][0]:
                    idx += 1
        result[idx] = list_y[x]
    print(f'#{i+1} {len(result)}', end = '')
    # 결과 출력
    for x in result:
        for y in x:
            print(f' {y}', end = '')
    print('')