import sys
from heapq import heappop, heappush

# sys.stdin = open('input.txt', 'r')

input = sys.stdin.readline
INF = float('inf')

N = int(input().strip())
M = int(input().strip())

MAP = [[] for _ in range(N+1)]
for m in range(M):
    a, b, c = map(int, input().split())
    MAP[a].append([b, c])

start, end = map(int, input().split())

h = []
parents = [[INF, -1] for _ in range(N+1)]

heappush(h, [0, start])
parents[start][1] = 0
parents[start][0] = 0

while h:
    cnt, x = heappop(h)
    if x == end:
        print(cnt)
        break
    for y, cost in MAP[x]:
        if parents[y][0] <= cost + cnt:
            continue
        parents[y][0] = cost + cnt
        parents[y][1] = x
        heappush(h, [cost+cnt, y])

idx = end
path = []
while True:
    path.append(idx)
    if idx == start:
        break
    idx = parents[idx][1]

path.reverse()
print(len(path))
print(' '.join(map(str, path)))

# # 메모리 초과 ㅠ

# import sys
# from heapq import heappop, heappush

# # sys.stdin = open('input.txt', 'r')

# input = sys.stdin.readline
# INF = float('inf')


# def print_path(e):
#     de = -1
#     while True:
#         if path[e] < 0:
#             result.append(e+1)
#             return
#         result.append(e+1)
#         e = path[e] - 1


# N = int(input().strip())
# M = int(input().strip())

# MAP = [[] for _ in range(N)]

# for m in range(M):
#     a, b, c = map(int, input().split())
#     MAP[a-1].append([b-1, c])

# start, end = map(int, input().split())

# dist = [INF for _ in range(N)]
# path = [-1 for _ in range(N)]

# h = []
# heappush(h, [0, start-1, 1])
# dist[start-1] = 0

# result = []

# while h:
#     c, x, cnt = heappop(h)
#     if x == end-1:
#         print(c)
#         print(cnt)
#         print_path(end-1)
#         break
#     for y, cost in MAP[x]:
#         new_cost = cost + c
#         if dist[y] < new_cost:
#             continue
#         dist[y] = new_cost
#         path[y] = x+1
#         heappush(h, [new_cost, y, cnt+1])

# result.reverse()
# print(' '.join(map(str, result)))