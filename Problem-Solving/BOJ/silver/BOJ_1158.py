from collections import deque

N, K = map(int, input().split())

lst = [i for i in range(1, N+1)]
que = deque(lst)
result = []
cnt = 0
while que:
    if cnt == K-1:
        result.append(que.popleft())
        cnt = 0
    else:
        que.append(que.popleft())
        cnt += 1
print('<' + ', '.join(map(str, result)) + '>')