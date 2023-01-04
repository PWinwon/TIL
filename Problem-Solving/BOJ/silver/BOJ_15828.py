import sys
from collections import deque

input = sys.stdin.readline

sizeOfBuf = int(input().strip())

que = deque()

while True:
    x = int(input().strip())
    if x == -1:
        break

    if x and len(que) < sizeOfBuf:
        que.append(x)
    if x == 0:
        que.popleft()

if que:
    print(' '.join(map(str, que)))
else:
    print('empty')