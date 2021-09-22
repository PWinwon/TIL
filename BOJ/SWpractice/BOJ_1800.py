def my_func(level, res):
    global result
    if level == N:
        res.sort(reverse=True)
        print(res)
        if result < res[P]:
            result = res[P]
        return
    if len(res) == N:
        return
    for i in range(1, N+1):
        if used[i] == 1:
            continue
        if MAP[level][i] == 0:
            continue
        used[i] += 1
        my_func(i, res + [MAP[level][i]])
        used[i] -= 0
    return


N, P, K = map(int, input().split())
MAP = [[0 for _ in range(N+1)] for _ in range(N+1)]
used = [0] * (N+1)
for p in range(P):
    x1, x2, c = map(int, input().split())
    MAP[x1][x2] = c
    MAP[x2][x1] = c
used[1] = 1
result = 0
my_func(1, [])
print(result)






