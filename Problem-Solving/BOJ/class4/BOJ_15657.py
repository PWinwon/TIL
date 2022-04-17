def my_func(n, c):
    global N, M
    if n == M:
        print(' '.join(map(str, result)))
        return
    for i in range(c, N):
        result.append(lst[i])
        my_func(n+1, i)
        result.pop()
    return



N, M = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
result = []
my_func(0, 0)