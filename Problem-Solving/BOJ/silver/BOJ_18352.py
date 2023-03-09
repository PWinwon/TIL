import sys
from heapq import heappop, heappush

# sys.stdin = open('input.txt', 'r')

input = sys.stdin.readline
INF = float('inf')

N, M, K, X = map(int, input().split())

MAP = [[] for _ in range(N+1)]
used = [INF for _ in range(N+1)]

for m in range(M):
    a, b = map(int, input().split())
    MAP[a].append(b)

h = []
heappush(h, [0, X])
used[X] = 0

while h:
    cnt, x = heappop(h)
    for y in MAP[x]:
        if used[y] < cnt + 1:
            continue
        heappush(h, [cnt+1, y])
        used[y] = cnt + 1

result = []
for n in range(1, N+1):
    if used[n] == K:
        result.append(n)

if result:
    print(' '.join(map(str, result)))
else:
    print(-1)


# 오답!..ㅠ
# from collections import deque


# N, M, K, X = map(int, input().split())

# MAP = [[] for _ in range(N+1)]
# result = -1
# for m in range(M):
#     x1, x2 = map(int, input().split())
#     MAP[x1].append(x2)

# used = [21e8] * (N+1)
# que = deque()
# que.append(X)
# used[X] = 0


# while que:
#     temp = que.popleft()
#     if used[temp] == K:
#         print(temp)
#         result = 1
#     elif used[temp] > K:
#         break
#     for i in MAP[temp]:
#         if used[temp] + 1 < used[i]:
#             used[i] = used[temp] + 1
#             que.append(i)

# if result < 0:
#     print(result)
