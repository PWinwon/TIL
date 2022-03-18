import sys
from collections import deque
INF = sys.maxsize


def my_func(n):
    global N
    used = [0] * N
    que = deque()
    que.append(n)

    ret = 0

    while que:
        x = que.popleft()
        for i in range(N):
            if adj[x][i] and used[i] == 0:
                used[i] = used[x] + 1
                ret += used[i]
                que.append(i)

    return ret



N, M = map(int, sys.stdin.readline().split())

adj = [[0 for _ in range(N)] for _ in range(N)]

for m in range(M):
    s, e = map(int, sys.stdin.readline().split())
    adj[s-1][e-1] = 1
    adj[e-1][s-1] = 1

result = 1
min_res = INF
for n in range(N):
    temp = my_func(n)
    if min_res > temp:
        result = n + 1
        min_res = temp
print(result)