def path_chk(node, cnt):
    global max_val
    for i in range(1, N+1):
        if adj[node][i] == 1 and visited[i] == 0:
            visited[i] = 1
            path_chk(i, cnt+1)
            visited[i] = 0
    else:
        if cnt > max_val:
            max_val = cnt
    return


test_case = int(input())

for tc in range(test_case):
    N, M = map(int, input().split())
    adj = [[ 0 for _ in range(N+1)] for _ in range(N+1)]
    visited = [0] * (N + 1)
    max_val = 0
    for m in range(M):
        idx1, idx2 = map(int, input().split())
        adj[idx1][idx2] = 1
        adj[idx2][idx1] = 1
    for idx in range(1, N+1):
        visited[idx] = 1
        path_chk(idx, 1)
        visited[idx] = 0
    print('#{} {}'.format(tc+1, max_val))