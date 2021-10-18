def my_func(level, day, total):
    if level == N:
        result.append(total)
        return
    if lst_n[level][day] == 0:
        for d in range(day, N+1):
            if lst_n[level][d] > 0:
                my_func(level+1, d, total + lst_n[level][d])
            if d == N:
                my_func(level+1, day, total)
    else:
        my_func(level + 1, day, total)
    return


N = int(input())
lst_n = []
for i in range(1, N+1):
    temp = [0] * (N+1)
    T, P = map(int, input().split())
    for j in range(i, i+T-1):
        if j >= N+1:
            break
        temp[j] = -1
    if i+T-1 < N+1:
        temp[i+T-1] = P
    lst_n.append(temp)
result = [0]
for r in range(N):
    for c in range(N+1):
        if lst_n[r][c] > 0:
            my_func(r, c, lst_n[r][c])

print(max(result))