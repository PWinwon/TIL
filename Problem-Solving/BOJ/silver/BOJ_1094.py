import sys
# sys.stdin = open('input.txt', 'r')

input = sys.stdin.readline


def bitCnt(num):
    if num == 0:
        return 0
    return num % 2 + bitCnt(num//2)


N = int(input().strip())
print(bitCnt(N))

