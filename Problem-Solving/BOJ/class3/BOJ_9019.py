import sys

from collections import deque


def func_D(n):
    ret = (n * 2) % 10000
    return ret


def func_S(n):
    ret = n - 1
    if ret < 0:
        return 9999
    return ret


def func_L(n):
    temp = num // 1000
    ret = (num - temp * 1000) * 10 + temp
    return ret

def func_R(n):
    temp = num % 10
    ret = num // 10 + temp * 1000
    return ret



T = int(input())

for tc in range(T):
    A, B = map(int, sys.stdin.readline().split())
    used = [0] * (10001)
    que = deque()
    que.append([A, ''])
    used[A] = 1

    while que:
        num, rec = que.popleft()
        if num == B:
            print(rec)
            break
        num_d = func_D(num)
        if used[num_d] == 0:
            used[num_d] = 1
            que.append([num_d, rec+'D'])
        num_s = func_S(num)
        if used[num_s] == 0:
            used[num_s] = 1
            que.append([num_s, rec+'S'])
        num_l = func_L(num)
        if used[num_l] == 0:
            used[num_l] = 1
            que.append([num_l, rec+'L'])
        num_r = func_R(num)
        if used[num_r] == 0:
            used[num_r] = 1
            que.append([num_r, rec+'R'])