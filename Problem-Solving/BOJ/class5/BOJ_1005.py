import sys
from collections import deque

input = sys.stdin.readline

T = int(input().strip())

for tc in range(T):
    N, K = map(int, input().split())
    lst_D = list(map(int, input().split()))

    # in_degree는 진입차수!
    in_degree = [0] * N
    used = [0] * N
    order_lst = [[] for _ in range(N)]
    for k in range(K):
        a, b = map(int, input().split())
        order_lst[a-1].append(b-1)
        in_degree[b-1] += 1

    W = int(input().strip())
    que = deque()
    lst = []

    for i in range(N):
        if in_degree[i] == 0:
            que.append(i)

    dp = [0] * N
    for i in range(N):
        if in_degree[i]:
            continue
        dp[i] = lst_D[i]

    while que:
        x = que.popleft()
        lst.append(x)

        for i in order_lst[x]:
            in_degree[i] -= 1
            if in_degree[i] == 0:
                que.append(i)

    for i in lst:
        for j in order_lst[i]:
            dp[j] = max(dp[j], dp[i] + lst_D[j])

    print(dp[W-1])
