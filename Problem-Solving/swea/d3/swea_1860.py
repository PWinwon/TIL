test_case = int(input())

for tc in range(test_case):
    N, M, K = map(int, input().split())
    time_lst = list(map(int, input().split()))
    people = [0] * 11112
    for i in range(N):
        people[time_lst[i]] += 1
    bread = 0
    cnt = 0
    idx = 0
    n = 0
    result = 'Possible'
    while n < N:
        if cnt == M:
            cnt = 0
            bread += K
        if people[idx] > 0:
            n += people[idx]
            if bread > 0:
                bread -= people[idx]
            else:
                result = 'Impossible'
                break
        idx += 1
        cnt += 1
    print('#{} {}'.format(tc+1, result))