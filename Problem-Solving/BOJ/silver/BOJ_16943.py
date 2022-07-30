import sys
input = sys.stdin.readline


def find_max_num(n, t):
    global A, B, result
    if t and int(t) > B:
        return
    if n == len(A):
        if result < int(t):
            result = int(t)
        return

    for i in range(len(A)):
        if used[i] == 0 and (A[i] != '0' or t != ''):
            used[i] = 1
            find_max_num(n+1, t + A[i])
            used[i] = 0
    return


A, B = input().split()
B = int(B)
result = -1
used = [0 for _ in range(len(A))]

find_max_num(0, '')
print(result)