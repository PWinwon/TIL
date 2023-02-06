import sys
from heapq import heappop, heappush

input = sys.stdin.readline


def find(x):
    if x == parents[x]:
        return x

    parents[x] = find(parents[x])
    return parents[x]


def union(x, y):
    x = find(x)
    y = find(y)

    if x < y:
        parents[y] = x
    else:
        parents[x] = y
    return


N, M = map(int, input().split())

parents = [i for i in range(N+1)]
h = []

# MAP = [list(map(int, input().split())) for _ in range(M)]
for m in range(M):
    a, b, c = map(int, input().split())
    heappush(h, [c, a, b])


result = 0
cnt = 1
for m in range(M):
    cost, a, b = heappop(h)
    if find(a) == find(b):
        continue
    union(a, b)
    result += cost
    cnt += 1
    if cnt == N-1:
        break

print(result)