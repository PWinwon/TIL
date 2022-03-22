import sys
from collections import deque

#       이때, 동시에 0인 값이 2개면 : ?
#       싸이클이 생긴다면? : impossible
# 4. 정상적인 경우 que 에 1개의 노드(x)가 삽입되고, 해당 노드(x)와 인접한 노드들의 in_degree 의 값을 1 감소
# 5. result 배열에 x 삽입
# 6. result 출력은 거꾸로 ? 하던지 뒤에서 부터 채우던지~


T = int(sys.stdin.readline().strip())

for tc in range(T):
    N = int(sys.stdin.readline().strip())
    rank = list(map(int, sys.stdin.readline().split()))

    # 1. 인접 행렬 순위표 이용해서 생성
    adj = [[0 for _ in range(N+1)] for _ in range(N+1)]

    for i in range(N):
        for j in range(i+1, N):
            adj[rank[i]][rank[j]] = 1

    M = int(sys.stdin.readline().strip())
    for m in range(M):
        a, b = map(int, sys.stdin.readline().split())
        if adj[a][b]:
            adj[a][b] = 0
            adj[b][a] = 1
        else:
            adj[b][a] = 0
            adj[a][b] = 1

    # 2. 본인 노드로 들어오는 간선의 수 : in_degree 생성
    in_degree = [0] * (N+1)

    for i in range(1, N+1):
        temp = 0
        for j in range(1, N+1):
            temp += adj[i][j]
        in_degree[i] += temp

    # 3. que 생성 후 in_degree의 값이 0인 노드 큐에 삽입
    que = deque()
    used = [0] * (N+1)
    for i in range(1, N+1):
        if in_degree[i] == 0:
            que.append(i)
            used[i] = 1

    result = []
    #    이때, 동시에 0인 값이 2개면 : ?
    #    싸이클이 생긴다면? : impossible
    while que:
        x = que.popleft()
        zero_degree_cnt = 0

        # 4. 정상적인 경우 que 에 1개의 노드(x)가 삽입되고, 해당 노드(x)와 인접한 노드들의 in_degree 의 값을 1 감소
        for i in range(1, N+1):
            if adj[i][x] and in_degree[i] > 0:
                in_degree[i] -= 1

        for i in range(1, N+1):
            if in_degree[i] == 0 and used[i] == 0:
                que.append(i)
                used[i] = 1

        if len(que) > 1:
            result = '?'
            break
        else:
            result.append(x)

    if len(result) == N:
        result = result[::-1]
        print(' '.join(map(str, result)))
    else:
        if result == '?':
            print(result)
        else:
            print("IMPOSSIBLE")



    # 5. result 배열에 x 삽입
    # 6. result 출력은 거꾸로 ? 하던지 뒤에서 부터 채우던지~
