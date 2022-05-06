import sys

input = sys.stdin.readline


def my_func(l, r, num):
    if l > r:
        return False
    if l == r:
        if lst[r] == num:
            return True
        else:
            return False

    mid = (l + r) // 2
    if lst[mid] == num:
        return True
    elif lst[mid] > num:
        ret = my_func(l, mid, num)
    else:
        ret = my_func(mid+1, r, num)
    return ret


N = int(input().strip())
lst = list(map(int, input().split()))
lst.sort()

M = int(input().strip())
lst_m = list(map(int, input().split()))

result = [0] * M
for m in range(M):
    if my_func(0, N-1, lst_m[m]):
        result[m] = 1
    else:
        result[m] = 0

print(' '.join(map(str, result)))