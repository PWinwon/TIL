import sys

input = sys.stdin.readline

N = int(input().strip())
lst = list(map(int, input().split()))
V = int(input().strip())

result = 0

for i in range(N):
    if lst[i] == V:
        result += 1
print(result)