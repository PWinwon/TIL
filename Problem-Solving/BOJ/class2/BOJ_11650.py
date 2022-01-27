import sys

N = int(input())

lst = []

for n in range(N):
    x, y = map(int, sys.stdin.readline().split())
    lst.append((x, y))

lst = sorted(lst, key=lambda x: (x[0], x[1]))

for x, y in lst:
    print(x, y)