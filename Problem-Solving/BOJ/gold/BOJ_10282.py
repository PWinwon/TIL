import sys
from heapq import heappop, heappush

# sys.stdin = open('input.txt', 'r')

input = sys.stdin.readline
INF = float('inf')

T = int(input().strip())

for tc in range(T):
    n, d, c = map(int, input().split())

    MAP = [[] for _ in range(n+1)]

    for _ in range(d):
        a, b, s = map(int, input().split())
        MAP[b].append([a, s])

    h = []
    used = [INF for _ in range(n+1)]
    used[c] = 0
    heappush(h, [0, c])

    while h:
        cnt, x = heappop(h)
        for y, cost in MAP[x]:
            if used[y] <= cost + cnt:
                continue
            heappush(h, [cnt+cost, y])
            used[y] = cost + cnt

    cnt = 0
    result = 0
    for i in range(1, n+1):
        if used[i] == INF:
            continue
        cnt += 1
        if result < used[i]:
            result = used[i]

    print(cnt, result)