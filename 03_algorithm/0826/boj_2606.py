from collections import deque

num = int(input())
v = int(input())
adj = [[0 for _ in range(num+1)]for _ in range(num+1)]
for i in range(v):
    idx1, idx2 = map(int, input().split())
    adj[idx1][idx2] = 1
    adj[idx2][idx1] = 1
used = [0] * (num+1)
que = deque()
que.append(1)
used[1] = 1
cnt = 0
while que:
    temp = que.popleft()
    for i in range(1, num+1):
        if used[i] == 1:
            continue
        if adj[temp][i] == 0:
            continue
        que.append(i)
        used[i] = 1
        cnt += 1
print(cnt)
