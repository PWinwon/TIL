import sys
# sys.stdin = open('input.txt', 'r')

input = sys.stdin.readline
INF = float('inf')

N = int(input().strip())
lst = list(map(int, input().split()))
lst.sort()

result = INF
result_lst = []
flag = False
for n in range(N-2):
    if flag:
        break
    l = n+1
    r = N-1
    start = lst[n]
    while l < r:
        res = start + lst[l] + lst[r]
        if abs(res) < result:
            result = abs(res)
            result_lst = [start, lst[l], lst[r]]
        if res < 0:
            l += 1
        elif res > 0:
            r -= 1
        else:
            flag = True
            break

print(result_lst[0], result_lst[1], result_lst[2])
