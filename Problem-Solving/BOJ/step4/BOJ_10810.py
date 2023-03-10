import sys

input = sys.stdin.readline

N, M = map(int, input().split())
lst = [0 for _ in range(N)]

for m in range(M):
    a, b, c = map(int, input().split())
    for i in range(a-1, b):
        lst[i] = c

print(' '.join(map(str, lst)))