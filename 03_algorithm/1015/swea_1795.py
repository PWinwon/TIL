import heapq
T = int(input())


def dijkstra(s) :
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

for tc in range(1, T + 1) :
    N,M , X = map(int ,input().split())
    adj = [
        [] for _ in range(N + 1)
    ]
    for _ in range(M):
        a,b, w = map(int ,input().split())
        adj[a].append((w,b))

    # X-> K(1,2,3,4,...N)
    dist = dijkstra(X)


    max_dist = 0
    for i in range(1,N+1):
        if i == X : continue
        dist2 = dijkstra(i) # i -> 1,2,3,4,X,,,,N
        max_dist = max(max_dist, dist2[X] + dist[i]) # i->X + X-> i

    print("#{} {}".format(tc, max_dist))