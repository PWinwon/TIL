import sys
from collections import deque


MAP = [0 for _ in range(100)] + [-1]

N, M = map(int, input().split())

for n in range(N):
    s, e = map(int, sys.stdin.readline().split())
    MAP[s] = e

for m in range(M):
    s, e = map(int, sys.stdin.readline().split())
    MAP[s] = e

que = deque()
que.append([1, 0])
used = [0 for _ in range(101)]
used[1] = 1

while que:
    x, cnt = que.popleft()
    if MAP[x] < 0:
        print(cnt)
        break
    for i in range(1, 7):
        res = x + i
        if res > 100:
            continue
        if MAP[res]:
            res = MAP[res]
        if used[res]:
            continue
        que.append([res, cnt+1])
        used[res] = 1