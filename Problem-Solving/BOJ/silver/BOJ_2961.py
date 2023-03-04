import sys

# sys.stdin = open('input.txt', 'r')

input = sys.stdin.readline
INF = float('inf')

N = int(input().strip())
foods = [list(map(int, input().split())) for _ in range(N)]
sub_set = (1 << N) - 1
result = INF

while sub_set:
    lemon = 1
    spicy = 0
    for n in range(N):
        if sub_set & (1 << n):
            lemon *= foods[n][0]
            spicy += foods[n][1]
    temp = abs(lemon - spicy)
    if result > temp:
        result = temp
    sub_set = (sub_set - 1)

print(result)