import sys
input = sys.stdin.readline


def my_func(n, total, before_num):
    global N, result
    if n == N:
        if total > result:
            result = total
        return
    for i in range(N):
        if used[i]:
            continue
        used[i] = 1
        my_func(n+1, total + abs(before_num - lst[i]), lst[i])
        used[i] = 0
    return


N = int(input().strip())
lst = list(map(int, input().split()))
used = [0] * N
result = -1
for m in range(N):
    used[m] = 1
    my_func(1, 0, lst[m])
    used[m] = 0
print(result)