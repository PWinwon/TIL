import sys

input = sys.stdin.readline


def my_func(now, total, cnt):
    global result, N, n
    if cnt == N:
        if MAP[now][n] == 0:
            return
        if result > total + MAP[now][n]:
            result = total + MAP[now][n]
        return

    if result < total:
        return

    for i in range(N):
        if used[i] or MAP[now][i] == 0:
            continue
        used[i] = 1
        my_func(i, total + MAP[now][i], cnt+1)
        used[i] = 0
    return


N = int(input().strip())

MAP = [list(map(int, input().split())) for _ in range(N)]
used = [0] * N

result = 9876543210

for n in range(N):
    used[n] = 1
    my_func(n, 0, 1)
    used[n] = 0

print(result)