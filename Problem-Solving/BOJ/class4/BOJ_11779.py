# 메모리 초과 ㅠ

import sys
from heapq import heappop, heappush

# sys.stdin = open('input.txt', 'r')

input = sys.stdin.readline
INF = float('inf')


def print_path(e):
    de = -1
    while True:
        if path[e] < 0:
            result.append(e+1)
            return
        result.append(e+1)
        e = path[e] - 1


N = int(input().strip())
M = int(input().strip())

MAP = [[] for _ in range(N)]

for m in range(M):
    a, b, c = map(int, input().split())
    MAP[a-1].append([b-1, c])

start, end = map(int, input().split())

dist = [INF for _ in range(N)]
path = [-1 for _ in range(N)]

h = []
heappush(h, [0, start-1, 1])
dist[start-1] = 0

result = []

while h:
    c, x, cnt = heappop(h)
    if x == end-1:
        print(c)
        print(cnt)
        print_path(end-1)
        break
    for y, cost in MAP[x]:
        new_cost = cost + c
        if dist[y] < new_cost:
            continue
        dist[y] = new_cost
        path[y] = x+1
        heappush(h, [new_cost, y, cnt+1])

result.reverse()
print(' '.join(map(str, result)))