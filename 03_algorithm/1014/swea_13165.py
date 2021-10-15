
import heapq

INF = int(21e8)

T = int(input())

for tc in range(1, T+1):
    N, E = map(int, input().split())
    adj = [[] for _ in range(N+1)]
    used = [INF for _ in range(N+1)]
    for i in range(E):
        s, e, l = map(int, input().split())
        adj[s].append([l, e])
    h = []
    heapq.heappush(h, (0, 0))
    while h:
        cost, idx = heapq.heappop(h)
        if used[N] != INF:
            break
        if used[idx] != INF:
            continue
        used[idx] = cost
        for cost_n, idx_n in adj[idx]:
            heapq.heappush(h, [cost+cost_n, idx_n])
    print('#{} {}'.format(tc, used[N]))
