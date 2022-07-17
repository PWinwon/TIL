import sys
from collections import deque

input = sys.stdin.readline


def bfs(start):
    Cnt = 1

    queue = deque([start])
    visited[start] = Cnt

    while queue:
        v = queue.popleft()

        for i in graph[v]:
            if visited[i] == 0:
                Cnt += 1
                queue.append(i)
                visited[i] = Cnt


N, M, R = map(int, input().split())

graph = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)

for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    graph[B].append(A)

for i in graph:
    i.sort()

bfs(R)

for i in range(1, N + 1):
    print(visited[i])