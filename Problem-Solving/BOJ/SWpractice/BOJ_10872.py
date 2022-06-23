import sys
input = sys.stdin.readline

N = int(input().strip())

result = 1
num = 1
while num <= N:
    result *= num
    num += 1

print(result)