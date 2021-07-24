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
            if list_N[x][y] == 1:
                galo += 1
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