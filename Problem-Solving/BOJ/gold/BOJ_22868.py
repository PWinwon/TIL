import sys
from collections import deque

# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N, M = map(int, input().split())

MAP = [[] for _ in range(N+1)]

for m in range(M):
    a, b = map(int, input().split())
    MAP[a].append(b)
    MAP[b].append(a)

S, E = map(int, input().split())

for n in range(1, N+1):
    MAP[n].sort()

que = deque()
used = [-1 for _ in range(N+1)]
que.append([S, 0])
used[S] = 0
ret_cnt = 0
while que:
    x, cnt = que.popleft()
    if x == E:
        ret_cnt = cnt
        break

    for y in MAP[x]:
        if used[y] >= 0:
            continue
        used[y] = x
        que.append([y, cnt+1])

visited = [0 for _ in range(N+1)]
idx = E
while idx != S:
    visited[idx] = 1
    idx = used[idx]

que = deque()
que.append([E, ret_cnt])

while que:
    x, cnt = que.popleft()
    if x == S:
        print(cnt)
    for y in MAP[x]:
        if visited[y]:
            continue
        visited[y] = 1
        que.append([y, cnt+1])