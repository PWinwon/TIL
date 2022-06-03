import sys


def my_func(n, m, s):
    global N, M
    if n == M:
        print(' '.join(map(str, s)))
        return

    for i in range(m, N):
        if used[i] == 0:
            used[i] = 1
            s[n] = lst[i]
            my_func(n+1, i, s)
            s[n] = 0
            used[i] = 0
    return


N, M = map(int, input().split())
lst = list(map(int, input().split()))

lst.sort()

used = [0] * N
s = [0] * M
my_func(0, 0, s)