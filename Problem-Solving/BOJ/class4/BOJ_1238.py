import sys
from heapq import heappop, heappush

# sys.stdin = open('input.txt', 'r')

input = sys.stdin.readline
INF = float('inf')

N, M, X = map(int, input().split())
MAP = [[] for _ in range(N+1)]

for m in range(M):
    a, b, c = map(int, input().split())
    MAP[a].append([b, c])

# X에서 각 마을에 도착하는 최단 거리
x_ret = [INF for _ in range(N+1)]
h = []
heappush(h, [0, X])
x_ret[X] = 0

while h:
    cnt, x = heappop(h)
    for y, cost in MAP[x]:
        if x_ret[y] < cost + cnt:
            continue
        heappush(h, [cost+cnt, y])
        x_ret[y] = cost+cnt

for i in range(1, N+1):
    h = []
    heappush(h, [0, i])
    used = [INF for _ in range(N+1)]
    temp = 0
    while h:
        cnt, x = heappop(h)
        for y, cost in MAP[x]:
            if used[y] < cost + cnt:
                continue
            heappush(h, [cost+cnt, y])
            used[y] = cost+cnt
    x_ret[i] += used[X]

result = -1
for i in range(1, N+1):
    if result < x_ret[i]:
        result = x_ret[i]
print(result)