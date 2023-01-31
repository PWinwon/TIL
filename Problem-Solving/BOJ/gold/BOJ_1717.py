import sys
sys.setrecursionlimit(100000)

input = sys.stdin.readline


def find(t):
    if t == parents[t]:
        return t
    parents[t] = find(parents[t])
    return parents[t]


def union(x, y):
    x = find(x)
    y = find(y)

    if x < y:
        parents[y] = x
    else:
        parents[x] = y


N, M = map(int, input().split())
parents = [i for i in range(N+1)]

for m in range(M):
    a, b, c = map(int, input().split())

    if a:
        if find(b) == find(c):
            print('YES')
        else:
            print('NO')
    else:
        union(b, c)
