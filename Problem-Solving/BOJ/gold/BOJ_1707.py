import sys
from collections import deque

input = sys.stdin.readline

T = int(input().strip())

for tc in range(T):
    V, E = map(int, input().split())
    MAP = [[] for _ in range(V+1)]
    used = [0] * (V+1)

    for i in range(E):
        a, b = map(int, input().split())
        MAP[a].append(b)
        MAP[b].append(a)
    que = deque()
    res = True

    for i in range(1, V+1):

        if not res:
            break

        flag = 1

        if used[i] == 0:
            que.append(i)
            used[i] = flag

            while que:

                if not res:
                    break

                x = que.popleft()
                for y in MAP[x]:
                    if used[y] == 0:
                        used[y] = used[x] * -1
                        que.append(y)
                    else:
                        if used[y] == used[x]:
                            res = False
    if res:
        print('YES')
    else:
        print('NO')