import sys

def my_func(m, s):
    global N, M
    if m == M:
        temp = ' '.join(map(str, s))
        print(temp)
        return
    visit = 0
    for i in range(N):
        if used[i] == 0 and visit != lst[i]:
            s.append(lst[i])
            used[i] = 1
            visit = lst[i]
            my_func(m + 1, s)
            used[i] = 0
            s.pop()
    return

input = sys.stdin.readline

N, M = map(int, input().split())
lst = list(list(map(int, input().split())))
lst.sort()
used = [0] * N
my_func(0, [])