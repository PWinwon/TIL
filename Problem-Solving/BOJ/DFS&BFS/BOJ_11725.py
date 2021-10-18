from collections import deque

N = int(input())
adj = [[] for _ in range(N+1)]
result = [0] * (N+1)
que = deque()
for i in range(1, N):
    x1, x2 = map(int, input().split())
    adj[x1].append(x2)
    adj[x2].append(x1)

que.append(1)
while que:
    temp = que.popleft()
    for t in adj[temp]:
        if result[t] != 0:
            continue
        result[t] = temp
        que.append(t)

for j in range(2, N+1):
    print(result[j])
