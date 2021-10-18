import sys

T = int(sys.stdin.readline())

for t in range(T):
    N, S = sys.stdin.readline().split()
    n = int(N)
    for s in S:
        print(s * n , end='')

    print('')