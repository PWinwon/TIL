import sys
from collections import deque

input = sys.stdin.readline

que = deque()

N = int(input().strip())

for n in range(N):
    lst = list(input().split())
    if lst[0] == 'push':
        que.append(lst[1])
    elif lst[0] == 'pop':
        if que:
            print(que.popleft())
        else:
            print(-1)
    elif lst[0] == 'size':
        print(len(que))
    elif lst[0] == 'empty':
        if que:
            print(0)
        else:
            print(1)
    elif lst[0] == 'front':
        if que:
            print(que[0])
        else:
            print(-1)
    elif lst[0] == 'back':
        if que:
            print(que[len(que)-1])
        else:
            print(-1)