import sys

def my_func(n, total):
    global N, K, result
    if n == N:
        if total >= 500:
            result += 1
        return

    if total < 500:
        return

    for i in range(N):
        if used[i] == 0:
            used[i] = 1
            my_func(n+1, total + lst[i] - K)
            used[i] = 0
    return


N, K = map(int, input().split())
lst = list(map(int, input().split()))
used = [0] * N
result = 0

my_func(0, 500)
print(result)