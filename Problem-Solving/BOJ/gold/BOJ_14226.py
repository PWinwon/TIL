import sys
from collections import deque

input = sys.stdin.readline

N = int(input().strip())

que = deque()
que.append([1, 0])
used = [[-1 for _ in range(N+1)] for _ in range(N+1)]
used[1][0] = 0

while que:
    x, clip = que.popleft()

    if used[x][x] == -1:
        used[x][x] = used[x][clip] + 1
        que.append([x, x])

    if x + clip <= N and used[x+clip][clip] == -1:
        used[x+clip][clip] = used[x][clip] + 1
        que.append([x+clip, clip])

    if x-1 >= 0 and used[x-1][clip] == -1:
        used[x-1][clip] = used[x][clip] + 1
        que.append([x-1, clip])

result = -1
for i in range(N+1):
    if used[N][i] != -1:
        if result == -1 or result > used[N][i]:
            result = used[N][i]
print(result)