def my_func(level):
    if level > M:
        print(' '.join(map(str, lst[1:])))
        return
    for i in range(lst[level-1], N+1):
        if lst[level-1] > i:
            continue
        lst[level] = i
        my_func(level+1)
    return


N, M = map(int, input().split())
lst = [1] + [0] * M
my_func(1)
