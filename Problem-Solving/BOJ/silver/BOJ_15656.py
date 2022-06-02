import sys

input = sys.stdin.readline

def my_func(n, s):
    global N, M
    if n == M:
        print(' '.join(map(str, s)))
        return

    for i in range(N):
        s[n] = lst[i]
        my_func(n + 1, s)
        s[n] = 0
    return


N, M = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()

used = [0] * N
result = [0] * M

my_func(0, result)