import sys
from collections import deque

input = sys.stdin.readline

A, B, N, M = map(int, input().split())

que = deque()
used = [0 for _ in range(100001)]
used[N] = 1

que.append([N, 0])

result = -1

while que:
    x, cnt = que.popleft()
    if x == M:
        result = cnt
        break

    for i in [x+1, x-1, x+A, x+B, x-A, x-B, x*A, x*B]:
        if i < 0 or i > 100000:
            continue
        if used[i]:
            continue
        que.append([i, cnt+1])
        used[i] = 1

print(result)