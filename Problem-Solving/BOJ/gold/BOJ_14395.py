import sys
from collections import deque

s, t = map(int, sys.stdin.readline().split())

if s == t:
    print(0)
else:
    q = deque()
    check = {s: 0}
    q.append((s, ''))

    op = ['*', '+', '/', '-']
    while q:
        now, path = q.popleft()

        if now == t:
            print(path)
            sys.exit(0)
        for idx, next in enumerate([now ** 2, 2 * now, 1, 0]):
            if next > t:
                continue

            if next not in check:
                check[next] = check[now] + 1
                q.append((next, path + op[idx]))

    print(-1)