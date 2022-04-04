def my_func(n, s, c):
    global result, N, M
    if n == M:
        print(' '.join(s))
        return

    for i in range(c+1, N+1):
        if used[i]:
            continue
        used[i] = 1
        my_func(n+1, s+str(i), i)
        used[i] = 0
    return


N, M = map(int, input().split())
used = [0] * (N+1)
my_func(0, '', 0)