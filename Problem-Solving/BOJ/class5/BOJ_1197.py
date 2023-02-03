import sys

input = sys.stdin.readline


def find(x):
    if x == parents[x]:
        return x
    parents[x] = find(parents[x])
    return parents[x]


def union(x, y):
    x = find(x)
    y = find(y)
    if x < y:
        parents[y] = x
    else:
        parents[x] = y
    return


V, E = map(int, input().split())

MAP = [list(map(int, input().split())) for _ in range(E) ]

MAP.sort(key=lambda x: x[2])

parents = [i for i in range(V+1)]

result = 0
cnt = 1


for a, b, c in MAP:
    if find(a) == find(b):
        continue
    union(a, b)
    cnt += 1
    result += c
    if cnt == V:
        break

print(result)