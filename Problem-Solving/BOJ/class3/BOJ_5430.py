import sys

from collections import deque


T = int(input())

for tc in range(T):
    temp = sys.stdin.readline().strip()
    N = int(input())
    lst = sys.stdin.readline().strip()[1:-1].split(',')
    if N:
        que = deque(lst)
    else:
        que = deque()

    flag = 1
    is_error = False
    for t in temp:
        if t == 'R':
            flag *= -1
        else:
            if que:
                if flag > 0:
                    que.popleft()
                else:
                    que.pop()
            else:
                is_error = True
                break

    if is_error:
        print('error')
    else:
        if flag > 0:
            print('[' + ','.join(list(que)) + ']')
        else:
            que.reverse()
            print('[' + ','.join(list(que)) + ']')