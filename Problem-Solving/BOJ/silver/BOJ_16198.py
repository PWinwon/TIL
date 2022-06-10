import sys


def my_find_left(n):
    for j in range(n-1, -1, -1):
        if used[j] == 0:
            return j
    return -1


def my_find_right(n):
    global N
    for k in range(n+1, N+1):
        if used[k] == 0:
            return k
    return -1


def my_func(n, s):
    global N, result
    if n == N-2:
        if result < s:
            result = s
        return

    for i in range(1, N-1):
        if used[i]:
            continue
        used[i] = 1
        l, r = my_find_left(i), my_find_right(i)
        if r == -1 or l == -1:
            continue
        my_func(n+1, s + lst[r] * lst[l])
        used[i] = 0
    return


input = sys.stdin.readline

N = int(input().strip())
lst = list(map(int, input().split()))
result = -1
used = [0] * N
my_func(0, 0)
print(result)