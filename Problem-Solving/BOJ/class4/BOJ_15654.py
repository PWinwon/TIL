def my_func(n):
    global N, M
    if n == M:
        print(' '.join(map(str, result)))
        return

    for i in range(N):
        if used[i]:
            continue
        used[i] = 1
        result.append(lst[i])
        my_func(n+1)
        result.pop()
        used[i] = 0
    return


N, M = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
used = [0] * N
result = []
my_func(0)