from collections import deque


N, K = map(int, input().split())

lst = [x+1 for x in range(N)]
que = deque(lst)

cnt = 0
print('<', end='')

while que:
    temp = que.popleft()
    if cnt == K-1:
        if que:
            print(temp, end=', ')
        else:
            print(temp, end='>')
        cnt = 0
    else:
        cnt += 1
        que.append(temp)