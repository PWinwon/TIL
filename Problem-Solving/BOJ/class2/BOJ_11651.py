import sys

N = int(input())

lst = []

for n in range(N):
    x, y = map(int, sys.stdin.readline().split())
    lst.append((x, y))

lst.sort(key= lambda x: (x[1], x[0]))

for n in range(N):
    print(lst[n][0], lst[n][1])