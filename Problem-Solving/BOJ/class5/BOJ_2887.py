import sys
from heapq import heappop, heappush

# sys.stdin = open('input.txt', 'r')
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


N = int(input().strip())
MAP = []

for n in range(N):
    a, b, c = map(int, input().split())
    MAP.append([a, b, c, n])

parents = [i for i in range(N)]

graph = []

MAP.sort(key=lambda x: x[0])
for i in range(N-1):
    # graph.append([abs(MAP[i][0] - MAP[i+1][0]), MAP[i][3], MAP[i+1][3]])
    heappush(graph, [abs(MAP[i][0] - MAP[i+1][0]), MAP[i][3], MAP[i+1][3]])

MAP.sort(key=lambda x: x[1])
for i in range(N-1):
    # graph.append([abs(MAP[i][1] - MAP[i + 1][1]), MAP[i][3], MAP[i + 1][3]])
    heappush(graph, [abs(MAP[i][1] - MAP[i + 1][1]), MAP[i][3], MAP[i + 1][3]])

MAP.sort(key=lambda x: x[2])
for i in range(N-1):
    # graph.append([abs(MAP[i][2] - MAP[i + 1][2]), MAP[i][3], MAP[i + 1][3]])
    heappush(graph, [abs(MAP[i][2] - MAP[i + 1][2]), MAP[i][3], MAP[i + 1][3]])

graph.sort()

# idx = 0
cnt = 1
result = 0

while cnt < N:
    # cost, a, b = graph[idx]
    cost, a, b = heappop(graph)
    # idx += 1
    if find(a) == find(b):
        continue
    union(a, b)
    result += cost
    cnt += 1

print(result)