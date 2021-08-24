test_case = int(input())

for tc in range(test_case):
    N, L = map(int, input().split())
    # 입력받은 칼로리 만큼 섭취하기 위해 그 길이만큼 리스트 생성 및 초기화
    kcal_lst = [0] * (L+1)
    # 입력받는 재료마다 그 값을 역으로 추적하면서 리스트에 채운다.
    # 1개가 입력되면 값이 존재하지 않기 때문에 본인의 점수를 칼로리의 인덱스에 저장한다 
    # ex) 점수 : 150, 칼로리 300 --> kcal_lst[300] = 150
    # 이미 입력되어 있는 값이 존재한다면, 그 인덱스에 칼로리만큼 더 더해준다. 
    # 이때 리스트를 벗어나면 칼로리를 넘은것 이므로 이경우는 기록하지 않는다
    # 리스트의 범위내에 존재하면서 기존의 값과 겹친다면 둘중 더 큰 값을 그자리에 남기기 위해 max함수를 사용한다
    for _ in range(N):
        taste, k = map(int, input().split())
        for idx in range(L, 0, -1):
            if kcal_lst[idx] != 0 and (idx + k) <= L:
                kcal_lst[idx+k] = max(kcal_lst[idx+k], (kcal_lst[idx] + taste))
        kcal_lst[k] = max(kcal_lst[k], taste)
    max_taste = 0
    # 저장된 리스트에서 가장 큰 값을 도출한다.
    for t in range(L+1):
        if kcal_lst[t] > max_taste:
            max_taste = kcal_lst[t]
    print('#{} {}'.format(tc+1, max_taste))