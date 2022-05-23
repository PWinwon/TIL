def my_func(n, s):
    global N
    if n == N:
        print(' '.join(map(str, s)))
        return
    for i in range(N):
        if used[i] == 1:
            continue
        used[i] = 1
        s[n] = lst[i]
        my_func(n+1, s)
        s[n] = 0
        used[i] = 0
    return


N = int(input())
lst = [i for i in range(1, N+1)]
used = [0 for _ in range(N+1)]
ret = [0] * N
my_func(0, ret)