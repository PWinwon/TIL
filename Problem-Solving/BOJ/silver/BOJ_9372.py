import sys
sys.stdin = open('input.txt', 'r')

input = sys.stdin.readline

T = int(input().strip())

for tc in range(T):
    N, M = map(int, input().split())
    for m in range(M):
        a, b = map(int, input().split())
    print(N-1)