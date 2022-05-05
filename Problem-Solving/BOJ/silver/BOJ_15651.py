def my_func(m, r):
    global N, M
    if m == M:
        print(' '.join(map(str, r)))
        return

    for n in range(1, N+1):
        r[m] = n
        my_func(m+1, r)
        r[m] = 0
    return

N, M = map(int, input().split())
result = [0] * M
my_func(0, result)