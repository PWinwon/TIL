import sys

INF = float('inf')
input = sys.stdin.readline


def bellman_ford(s):
    global N
    distance[s] = 0
    for i in range(N):
        for j in range(M):
            start_node = edges[j][0]
            end_node = edges[j][1]
            time = edges[j][2]
            if distance[start_node] != INF and distance[end_node] > distance[start_node] + time:
                distance[end_node] = distance[start_node] + time
                if i == N - 1:
                    return True
    return False

N, M = map(int, input().split())
# print(N, M)

edges = []

distance = [INF] * (N+1)

for m in range(M):
    a, b, c = map(int, input().split())
    edges.append([a, b, c])

ret = bellman_ford(1)
if ret:
    print("-1")
else:
    for i in range(2, N+1):
        if distance[i] == INF:
            print("-1")
        else:
            print(distance[i])



