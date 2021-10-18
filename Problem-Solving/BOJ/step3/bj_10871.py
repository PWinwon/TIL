import sys

n, x = map(int, input().split())

list = list(map(int, sys.stdin.readline().split()))

for i in range(0,n):
    if(list[i] < x):
        print(list[i], end= ' ')
    