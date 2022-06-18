import sys
from collections import deque

input = sys.stdin.readline

def my_dfs(n):
    ret = 0
    que = deque()
    que.append(n)
    used = [0] * (N+1)
    used[n] = 1
    while que:
        x = que.popleft()
        ret += 1
        for i in MAP[x]:
            if used[i] == 0:
                used[i] = 1
                que.append(i)
    return ret


N, M = map(int, input().split())

MAP = [[] for _ in range(N+1)]

for m in range(M):
    a, b = map(int, input().split())
    MAP[b].append(a)

max_result = -1
result = []

for i in range(1, N+1):
    if MAP[i]:
        temp = my_dfs(i)
        if max_result <= temp:
            if max_result < temp:
                result = []
            max_result = temp
            result.append(i)

print(' '.join(map(str, result)))