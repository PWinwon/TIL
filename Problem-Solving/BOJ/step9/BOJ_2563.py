import sys

input = sys.stdin.readline

N = int(input().strip())

PAPER = [[0 for _ in range(100)] for _ in range(100)]

for n in range(N):
    a, b = map(int, input().split())

    for i in range(a, a+10):
        for j in range(b, b+10):
            PAPER[i][j] = 1
result = 0
for k in range(100):
    result += sum(PAPER[k])
print(result)
