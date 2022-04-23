from collections import deque

N, K = map(int, input().split())
used = [-1] * 100001
que = deque()

que.append(N)
used[N] = 0

while que:
    x = que.popleft()
    if x == K:
        print(used[x])
        break

    if 0 <= x-1 < 100001 and used[x-1] == -1:
        used[x-1] = used[x] + 1
        que.append(x-1)

    if 0 <= x*2 < 100001 and used[x*2] == -1:
        used[x*2] = used[x]
        que.appendleft(x*2)

    if 0 <= x+1 < 100001 and used[x+1] == -1:
        used[x+1] = used[x] + 1
        que.append(x+1)