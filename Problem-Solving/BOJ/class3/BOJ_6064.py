import sys

def my_func(m, n, a, b):
    global max_val
    while a <= max_val:
        if (a-b) % n == 0:
            return a
        a += m
    return -1

def my_gcd(a, b):
    while b != 0:
        r = a % b
        a = b
        b = r

    return a

T = int(sys.stdin.readline().strip())

for tc in range(T):
    M, N, x, y = map(int, sys.stdin.readline().split())
    max_val = M * N / my_gcd(M, N)

    result = my_func(M, N, x, y)
    print(result)