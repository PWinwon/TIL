from collections import deque

# def dfs(level):
#     for i in range(N+1):
#         if lst_n[level][i] == 0 or used[i] == 1:
#             continue
#         used[i] = 1
#         dfs(i)
#     return

N, M = map(int, input().split())
lst_n = [[0 for _ in range(N+1)] for _ in range(N+1)]
used = [0 for _ in range(N+1)]

for m in range(M):
    u, v = map(int, input().split())
    lst_n[u][v] = 1
    lst_n[v][u] = 1

result = 0
for n in range(1, N+1):
    if used[n] == 0:
        que = deque()
        que.append(n)
        used[n] = 1
        while que:
            temp = que.popleft()
            for i in range(1, N+1):
                if lst_n[temp][i] == 1 and used[i] == 0:
                    que.append(i)
                    used[i] = 1
        result += 1

print(result)