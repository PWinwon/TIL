from collections import deque

for _ in range(10):
    T = int(input())
    que = deque()
    lst = list(map(int, input().split()))
    for i in lst:
        que.append(i)
    cnt = 0
    while True:
        cnt = (cnt % 5)+1
        temp = que.popleft()
        temp -= cnt
        if temp <= 0:
            temp = 0
            que.append(temp)
            break
        que.append(temp)

    result = ' '.join(map(str, que))
    print('#{} {}'.format(T, result))