from collections import deque

move = [-1, 1, 0]

N, K = map(int, input().split())
used = [0 for _ in range(100001)]
used[N] = 1

que = deque()
que.append([N, 0])

while que:
    x, cnt = que.popleft()
    if x == K:
        print(cnt)
        break
    for i in range(3):
        if move[i]:
            nx = x + move[i]
        else:
            nx = 2 * x
        if nx < 0 or nx > 100000:
            continue
        if used[nx]:
            continue
        used[nx] = 1
        que.append([nx, cnt+1])