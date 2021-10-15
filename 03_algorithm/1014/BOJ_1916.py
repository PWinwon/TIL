import heapq


def dijkstra(s):
    minheap = []
    dist = [int(21e8) for _ in range(N + 1)]
    dist[0] = 0
    heapq.heappush(minheap, (0, s))

    while minheap:
        cost, now = heapq.heappop(minheap)  # 탐색
        if dist[now] < cost: continue  # 둘다 S~~~>now의 비용

        # s->now (cost) + edge의 가중치 (now->next)
        for w, next in adj[now]:
            if cost + w < dist[next]:
                dist[next] = cost + w  # 더 작은값으로 갱신
                heapq.heappush(minheap, (cost + w, next))

    return dist


N = int(input())
M = int(input())

adj = [
    [] for _ in range(N + 1)
]
for _ in range(M):
    a, b, w = map(int, input().split())
    adj[a].append((w, b))

S, G = map(int, input().split())
dist = dijkstra(S)
print(dist[G])  # S~~~>G 최단경로/최소비용