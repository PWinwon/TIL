def my_func(i, n):
    if i == n:
        print('{}'.format(' '.join(map(str,result))))
        return
    for idx in range(1, N+1):
        if visited[idx-1] == 1:
            continue
        visited[idx-1] = 1
        result.append(idx)
        my_func(i+1, n)
        result.pop()
        visited[idx-1] = 0
    return

N, M = map(int, input().split())
visited = [0] * N
result = []
my_func(0, M)