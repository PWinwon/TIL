import sys
import heapq

input = sys.stdin.readline
inf = float("INF")

V, E = map(int, input().split())
K = int(input().strip())

MAP = [[] for _ in range(V)]
h = []
used = [inf] * (V)

heapq.heappush(h, (0, K-1))
used[K-1] = 0

for e in range(E):
    temp = list(map(int, input().split()))
    MAP[temp[0]-1].append([temp[1]-1, temp[2]])


while h:
    cnt, node = heapq.heappop(h)
    if used[node] < cnt:
        continue

    for x, y in MAP[node]:
        if used[x] > cnt + y:
            used[x] = cnt + y
            heapq.heappush(h, [cnt + y, x])

for i in range(V):
    if used[i] == inf:
        print("INF")
    else:
        print(used[i])
