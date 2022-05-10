from collections import deque

N, K = map(int, input().split())

que = deque()
path = str(N)
que.append([N, path])
used = [-1] * 150001
used[N] = 0

while que:
    x, x_path = que.popleft()
    if x == K:
        print(used[x])
        print(x_path)
        break
    for i in [x-1, x+1, x*2]:
        x_idx = i
        if x_idx < 0 or x_idx >= 150000:
            continue
        if used[x_idx] >= 0:
            continue
        que.append([x_idx, x_path + ' ' + str(x_idx)])
        used[x_idx] = used[x] + 1