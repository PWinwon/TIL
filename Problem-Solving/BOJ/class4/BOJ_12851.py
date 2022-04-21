from collections import deque


N, M = map(int, input().split())
que = deque()
used = [-1] * 200001
cnt = [0] * 200001

que.append(N)
used[N] = 0
cnt[N] = 1
while que:
    now = que.popleft()
    for i in range(3):
        if i == 0:
            nxt = now - 1
        elif i == 1:
            nxt = now + 1
        elif i == 2:
            nxt = now * 2
        if 0 <= nxt <= 200000:
            if used[nxt] == -1:
                used[nxt] = used[now] + 1
                cnt[nxt] = cnt[now]
                que.append(nxt)

            elif used[nxt] == used[now] + 1:
                cnt[nxt] += cnt[now]

print(used[M])
print(cnt[M])