import sys
# sys.stdin = open('input.txt', 'r')

input = sys.stdin.readline

N, M = map(int, input().split())

lst = [i+1 for i in range(N)]

for m in range(M):
    a, b = map(int, input().split())
    while a < b:
        lst[a-1], lst[b-1] = lst[b-1], lst[a-1]
        a += 1
        b -= 1

print(' '.join(map(str, lst)))