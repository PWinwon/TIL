def my_func(level):
    global result, res
    if level == N:
        if result < res:
            result = res
        return
    if res < result:
        return
    for i in range(N):
        if used[i] != 0:
            continue
        if lst[level][i] == 0:
            continue
        used[i] = 1
        res *= (lst[level][i] / 100)
        my_func(level+1)
        res /= (lst[level][i] / 100)
        used[i] = 0
    return


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]
    used = [0] * N
    result = 0
    res = 1
    my_func(0)
    print('#{} {:6f}'.format(tc, result*100))