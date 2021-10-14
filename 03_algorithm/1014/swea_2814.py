# 교수님 풀이

T = int(input())


def dfs(now, cnt) :
    global max_path
    max_path = max(max_path, cnt)

    # next 찾기 adj[now]
    for next in adj[now]:
        if visited[next] == 1 : continue # 경로상에 중복된 노드인가?
        visited[next] = 1 # 이후의 dfs(next) 금지
        dfs(next,cnt + 1)
        visited[next] = 0 # 원상복구



for tc in range(1, T + 1) :
    N,M = map(int ,input().split())
    adj = [
        [] for _ in range(N + 1) # 나랑 인접한 정점들을 저장
    ]
    de = - 1
    for _ in range(M) :
        x,y = map(int ,input().split())
        # x->y 간선 , y -> x간선
        adj[x].append(y)
        adj[y].append(x)

    max_path = 0
    visited = [0] * (N + 1)
    for i in range(1,N+1):
        visited[i] = 1 # 이후의 재귀호출 금지
        dfs(i,1)
        visited[i] = 0 # 원상복구
    print("#{} {}".format(tc, max_path))