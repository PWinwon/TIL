INF = int(1e9)

n = int(input())
graph = [[INF for _ in range(n)] for _ in range(n)]
for i in range(n):
    a = list(map(int, input().split()))
    for j in range(n):
        if a[j]:
            graph[i][j] = 1

for k in range(n):
    for i in range(n):
        for j in range(n):
            graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])
for i in graph:
    s = ''
    for j in i:
        if j < INF:
            s += '1 '
        else:
            s += '0 '
    print(s.rstrip())