import sys
from collections import deque


N = int(input())

que = deque()
for n in range(N):
    temp = list(sys.stdin.readline().split())
    if temp[0] == 'push_front':
        que.appendleft(temp[1])
    elif temp[0] == 'push_back':
        que.append(temp[1])
    elif temp[0] == 'pop_front':
        if que:
            print(que.popleft())
        else:
            print(-1)
    elif temp[0] == 'pop_back':
        if que:
            print(que.pop())
        else:
            print(-1)
    elif temp[0] == 'size':
        print(len(que))
    elif temp[0] == 'empty':
        if que:
            print(0)
        else:
            print(1)
    elif temp[0] == 'front':
        if que:
            print(que[0])
        else:
            print(-1)
    elif temp[0] == 'back':
        if que:
            print(que[len(que)-1])
        else:
            print(-1)