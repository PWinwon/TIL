import sys

N = int(sys.stdin.readline())
numbers = int(sys.stdin.readline())
total = 0

for n in range(N):
    total += numbers % 10
    numbers = numbers // 10

print(total)