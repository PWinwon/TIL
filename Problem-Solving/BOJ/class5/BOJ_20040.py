import sys
sys.setrecursionlimit(10000000)

input = sys.stdin.readline


def find(x):
    if x == parent[x]:
        return x
    parent[x] = find(parent[x])
    return parent[x]


def union(x, y):
    x = find(x)
    y = find(y)
    if x < y:
        parent[x] = y
    else:
        parent[y] = x
    return


N, M = map(int, input().split())

parent = [i for i in range(N)]

result = 0

for m in range(1, M+1):
    a, b = map(int, input().split())
    if find(a) == find(b):
        result = m
        break
    union(a, b)

print(result)