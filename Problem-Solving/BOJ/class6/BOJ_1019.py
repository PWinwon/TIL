import sys
# sys.stdin = open('input.txt', 'r')

input = sys.stdin.readline


def my_func(n, v):
    while n:
        result[n%10] += v
        n //= 10


N = int(input().strip())
result = [0 for _ in range(10)]
p = 1
while N:
    if N % 10 != 9:
        my_func(N, p)
        N -= 1
        continue
    if N == 0:
        break

    N //= 10
    res = (N + 1) * p
    for j in range(10):
        result[j] += res

    result[0] -= p
    p *= 10

print(' '.join(map(str,result)))

