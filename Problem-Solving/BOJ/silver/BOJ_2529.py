import sys


def my_func(n, s, bef, chk):
    global min_result, max_result, N
    if n == N+1:
        if int(s) < int(min_result):
            min_result = s
        if int(s) > int(max_result):
            max_result = s
        return
    if chk == '>':
        for i in range(0, bef):
            if used[i] == 0:
                used[i] = 1
                my_func(n+1, s + str(i), i, lst[n])
                used[i] = 0
    elif chk == '<':
        for i in range(bef+1, 10):
            if used[i] == 0:
                used[i] = 1
                my_func(n+1, s + str(i), i, lst[n])
                used[i] = 0
    else:
        for i in range(10):
            if used[i] == 0:
                used[i] = 1
                my_func(n+1, s + str(i), i, lst[n])
                used[i] = 0
    return


input = sys.stdin.readline

N = int(input().strip())
lst = list(input().split()) + ['.']
used = [0] * 10
min_result = 10 ** (N+1)
max_result = -1
my_func(0, '', -1, '')
print(max_result)
print(min_result)