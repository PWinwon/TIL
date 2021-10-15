import heapq

V, E = map(int ,input().split())

K = int(input()) # 시작 정점
adj = [
    [] for _ in range(V+1)
]
for _ in range(E) :
    a,b,w = map(int ,input().split())
    adj[a].append((w,b)) # a->b 얘만 존재


minheap = []
dist = [ int(21e8) for _ in range(V+1)] # K~~> 각 정점들의 최단 경로값
heapq.heappush(minheap, (0,K))

while minheap :
    cost,now = heapq.heappop(minheap)
    if dist[now] != int(21e8) : continue
    dist[now] = cost

    # K~~>now(cost)  + now->next(edge의 w)
    for w,next in adj[now] :
        heapq.heappush(minheap, (cost + w , next))

de = -1
for i in range(1, V+1):
    if dist[i] == int(21e8) :
        print("INF")
    else:
        print(dist[i])