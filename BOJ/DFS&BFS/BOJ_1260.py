import sys
from collections import deque


def dfs(level):
    result1.append(level)
    for idx in range(1, N+1):
        if used1[idx] == 1:
            continue
        if adj[level][idx] == 0:
            continue
        used1[idx] = 1
        dfs(idx)
    return


N, M, start_node = map(int, sys.stdin.readline().split())
lst_m = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]
used1 = [0] * (N+1)
used2 = [0] * (N+1)
adj = [[0 for _ in range(N+1)] for _ in range(N+1)]
for i in range(M):
    adj[lst_m[i][0]][lst_m[i][1]] = 1
    adj[lst_m[i][1]][lst_m[i][0]] = 1

used1[start_node] = 1
used2[start_node] = 1
result1 = []
result2 = []

dfs(start_node)

que = deque()
que.append(start_node)
while que:
    temp = que.popleft()
    result2.append(temp)
    for i in range(1, N+1):
        if used2[i] == 1:
            continue
        if adj[temp][i] == 1:
            used2[i] = 1
            que.append(i)

print(' '.join(map(str, result1)))
print(' '.join(map(str, result2)))
