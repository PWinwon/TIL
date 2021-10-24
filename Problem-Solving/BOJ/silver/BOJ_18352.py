from collections import deque


N, M, K, X = map(int, input().split())

MAP = [[] for _ in range(N+1)]
result = -1
for m in range(M):
    x1, x2 = map(int, input().split())
    MAP[x1].append(x2)

used = [21e8] * (N+1)
que = deque()
que.append(X)
used[X] = 0


while que:
    temp = que.popleft()
    if used[temp] == K:
        print(temp)
        result = 1
    elif used[temp] > K:
        break
    for i in MAP[temp]:
        if used[temp] + 1 < used[i]:
            used[i] = used[temp] + 1
            que.append(i)

if result < 0:
    print(result)
