import sys
sys.stdin = open('input.txt', 'r')

N = int(input().strip())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort(reverse=True)

total = 0
for n in range(N):
    total += A[n] * B[n]
print(total)