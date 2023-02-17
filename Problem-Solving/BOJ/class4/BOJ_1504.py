import sys
from heapq import heappop, heappush

# sys.stdin = open('input.txt', 'r')

input = sys.stdin.readline
INF = float('inf')


def my_func(s):
    h = []
    dist = [INF for _ in range(N + 1)]
    heappush(h, [0, s])
    dist[s] = 0

    while h:
        cost, x = heappop(h)
        for y, c in MAP[x]:
            if dist[y] < cost + c:
                continue
            dist[y] = cost + c
            heappush(h, [cost + c, y])
    return dist


N, E = map(int, input().split())

MAP = [[] for _ in range(N+1)]

for e in range(E):
    a, b, c = map(int, input().split())
    MAP[a].append([b, c])
    MAP[b].append([a, c])

v1, v2 = map(int, input().split())
start, end = 1, N

start_ret = my_func(start)
v1_ret = my_func(v1)
v2_ret = my_func(v2)
result = min(start_ret[v1] + v1_ret[v2] + v2_ret[end], start_ret[v2] + v2_ret[v1] + v1_ret[end])
if result == INF:
    print(-1)
else:
    print(result)
