from collections import deque


N, Q = map(int, input().split())
adj = [[0 for _ in range(N+1)] for _ in range(N+1)]
for i in range(N-1):
    x1, x2, r = map(int, input().split())
    adj[x1][x2] = r
    adj[x2][x1] = r


for j in range(Q):
    k, r = map(int, input().split())
    que = deque()
    que.append([r, 1000000000])
    used = [0] * (N+1)
    used[0] = 1
    used[r] = 1
    result = 0
    while que:
        temp = que.popleft()
        if temp[1] >= k and temp[1] != 1000000000:
            result += 1
            continue
        for i in range(1, N+1):
            if used == 1:
                continue
            if adj[temp[0]][i] == 0:
                continue
            used[i] = 1
            res = min(temp[1], adj[temp[0]][i])
            que.append([i, res])
    print(result)
