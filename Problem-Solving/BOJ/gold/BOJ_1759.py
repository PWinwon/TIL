moum = ['a', 'e', 'i', 'o', 'u']


def my_func(lev, mcnt, jcnt, idx, pw):
    if lev == L:
        if mcnt >= 1 and jcnt >= 2:
            print(pw)
        return
    for i in range(idx, C):
        if used[i] == 1:
            continue
        if lst[i] in moum:
            used[i] = 1
            my_func(lev+1, mcnt+1, jcnt, i+1, pw+lst[i])
            used[i] = 0
        else:
            used[i] = 1
            my_func(lev+1, mcnt, jcnt+1, i+1, pw+lst[i])
            used[i] = 0
    return



L, C = map(int, input().split())
lst = list(input().split())
used = [0] * C
lst.sort()
my_func(0, 0, 0, 0, '')