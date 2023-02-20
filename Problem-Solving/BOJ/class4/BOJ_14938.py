import sys
from heapq import heappop, heappush

# sys.stdin = open('input.txt', 'r')

input = sys.stdin.readline
INF = float('inf')

N, M, K = map(int, input().split())
items = [-1] + list(map(int, input().split()))

MAP = [[] for _ in range(N+1)]

for k in range(K):
    a, b, c = map(int, input().split())
    MAP[a].append([b, c])
    MAP[b].append([a, c])

result = -1
# 시작 노드에 따라 달라지기 때문에
for i in range(1, N+1):
    h = []
    used = [INF for _ in range(N+1)]
    heappush(h, [0, i])
    used[i] = 0

    while h:
        cnt, x = heappop(h)
        for y, cost in MAP[x]:
            if cost + cnt > M:
                continue
            if used[y] < cost + cnt:
                continue
            heappush(h, [cnt+cost, y])
            used[y] = cost + cnt
    temp = 0
    for n in range(1, N+1):
        if used[n] <= M:
            temp += items[n]

    if result < temp:
        result = temp

print(result)

