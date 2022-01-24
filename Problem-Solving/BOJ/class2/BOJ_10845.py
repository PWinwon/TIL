import sys
from collections import deque

N = int(input())

que = deque()
q_size = 0

for n in range(N):
    temp = list(sys.stdin.readline().split())
    if temp[0] == 'push':
        que.append(temp[1])
        q_size += 1
    elif temp[0] == 'pop':
        if que:
            print(que.popleft())
            q_size -= 1
        else:
            print(-1)
    elif temp[0] == 'size':
        print(q_size)
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
    else:
        if que:
            print(que[q_size-1])
        else:
            print(-1)