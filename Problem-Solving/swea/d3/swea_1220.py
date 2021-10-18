for i in range(10):
    N = int(input())
    mag_list = []
    # 입력받은 테이블을 2차원 리스트로 저장
    for j in range(N):
        sample_list = list(map(int, input().split()))
        mag_list.append(sample_list)
    result = 0
    # 2차원 형태에서 세로줄 각각 안에서만 비교를 하면됨. 
    # 비교하는 세로줄의 양쪽에 있는 줄들이 영향을 주지 않음
    for y in range(N):
        # 세로줄을 따로 뽑아서 비교하기 위한 test_list 리스트 생성
        test_list = []
        for x in range(N):
            if mag_list[x][y] :
                test_list.append(mag_list[x][y])
        # 저장된 세로줄(test_list)에 대해 첫번째원소가 2이면(위로 이동 떨어짐) >> pop을 이용해 제거
        # 마찬가지로 마지막 원소가 1이면(아래로 떨어짐) >> pop을 이용해 제거
        # 무한히 반복 후 양 끝 값이 2와 1이 아니면 break
        while True:
            if test_list[0] == 2:
                test_list.pop(0)
            elif test_list[len(test_list)-1] == 1:
                test_list.pop()
            else:
                break
        test_len = len(test_list)
        idx = 0
        # 교착상태의 개수는 리스트에서 연속된 1과 2의 개수 이므로 while과 if를 이용해 result에 교착상태의 수 누적합을 구하여 출력
        while idx <= (test_len-2):
            if test_list[idx] == 1 and  test_list[idx+1] == 2:
                result += 1
                idx += 1
            idx += 1
    print(f'#{i+1} {result}')
