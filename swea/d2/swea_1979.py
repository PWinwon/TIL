T = int(input())

for i in range(T):
    N, K = map(int, input().split())
    list_N = []
    for j in range(N):
        sample_ls = list(map(int, input().split()))
        list_N.append(sample_ls)
    # print(list_N)
    result = []
    total = 0
    galo = 0
    selo = 0
    for x in range(N):
        for y in range(N):
            # 1의 개수 만큼 가로와 세로의 변수에 각각 1씩증가
            if list_N[x][y] == 1:
                galo += 1
            # 0을 만났을때 그 변수의 값이 있다면 연속이 끊어진 것이므로
            # 그 순간 result에 추가후 변수 초기화
            else:
                if galo:
                    result.append(galo)
                    galo = 0
            if list_N[y][x]:
                selo += 1
            else:
                if selo:
                    result.append(selo)
                    selo = 0
        # 비교할 가로줄과 세로줄이 각각 끝나고
        # 그 값이 양수이면 result에 추가후 초기화
        if galo:
            result.append(galo)
        if selo:
            result.append(selo)
        galo = 0
        selo = 0
    for num in result:
        if num == K:
            total += 1
    print(f'#{i+1} {total}')