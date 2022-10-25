import sys
input = sys.stdin.readline

total = int(input().strip())

N = int(input().strip())
temp = 0
for n in range(N):
    a, b = map(int, input().split())
    temp += a * b

if total == temp:
    print("Yes")
else:
    print("No")