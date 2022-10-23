import sys

input = sys.stdin.readline

ans = [1, 1, 2, 2, 2, 8]

lst = list(map(int, input().split()))

ret = [0] * 6

for i in range(6):
    ret[i] = ans[i] - lst[i]

print(' '.join(map(str, ret)))