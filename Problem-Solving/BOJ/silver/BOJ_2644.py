import sys
from collections import deque

input = sys.stdin.readline

N = int(input().strip())

MAP = [[] for _ in range(N)]

A, B = map(int, input().split())
M = int(input().strip())

for m in range(M):
    a, b = map(int, input().split())
    MAP[a-1].append(b-1)
    MAP[b-1].append(a-1)

que = deque()
que.append(A-1)
used = [-1] * (N)
used[A-1] = 0

result = -1

while que:
    x = que.popleft()
    if x == B-1:
        result = used[x]
        break
    for i in MAP[x]:
        if used[i] == -1:
            used[i] = used[x] + 1
            que.append(i)

print(result)
