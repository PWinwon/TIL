import sys

def my_func(n, s):
    global k
    if n == 6:
        print(' '.join(map(str, result)))
        return

    for i in range(s, k):
        result.append(lst[i])
        my_func(n+1, i+1)
        result.pop()
    return


input = sys.stdin.readline

while True:
    lst = list(map(int, input().split()))
    if lst[0] == 0:
        break
    k = lst[0]
    lst = lst[1:]
    result = []
    my_func(0, 0)
    print()