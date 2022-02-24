import sys

T = int(input())

for tc in range(T):
    N = int(input())
    wears = dict()
    for n in range(N):
        a, b = sys.stdin.readline().split()
        if b in wears.keys():
            wears[b] += 1
        else:
            wears[b] = 1
    result = 1
    for key, val in wears.items():
        result *= (val+1)

    print(result-1)