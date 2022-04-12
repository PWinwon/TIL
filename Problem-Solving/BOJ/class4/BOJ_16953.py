from collections import deque


A, B = map(int, input().split())

que = deque()
que.append([A, 1])
result = -1

while que:
    num, cnt = que.popleft()
    if num == B:
        result = cnt
        break
    elif num > B:
        continue

    num_1 = num * 2
    num_2 = num * 10 + 1
    que.append([num_1, cnt + 1])
    que.append([num_2, cnt + 1])

print(result)