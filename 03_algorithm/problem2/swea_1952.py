test_case = int(input())

for tc in range(test_case):
    D, M, tM, Y = map(int, input().split())
    lst = list(map(int, input().split()))
    cost = [0] * 12
    for idx in range(12):
        temp = min(lst[idx]*D, M)
        if idx == 0:
            cost[idx] = temp
        else:
            cost[idx] += cost[idx-1] + temp
        if idx >= 2:
            if idx == 2:
                cost[idx] = min(cost[idx], tM)
            else:
                cost[idx] = min(cost[idx], tM + cost[idx-3])
        if idx == 11:
            cost[idx] = min(cost[idx], Y)
    print('#{} {}'.format(tc+1, cost[11]))