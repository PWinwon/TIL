import sys
# sys.stdin = open('input.txt', 'r')

INF = float('inf')
input = sys.stdin.readline

N = int(input().strip())
lst = list(map(int, input().split()))

l = 0
r = N-1
result = INF
result_l = INF
result_r = INF

while l < r:
    res = lst[l] + lst[r]
    if abs(res) < abs(result):
        result_l, result_r = lst[l], lst[r]
        result = res

    if res > 0:
        r -= 1
    elif res < 0:
        l += 1
    else:
        break

print(result_l, result_r)