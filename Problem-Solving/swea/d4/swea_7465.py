def my_union(a, b):
    global result
    ga = my_find(a)
    gb = my_find(b)
    if ga != gb:
        group[gb] = ga
        result -= 1
    return


def my_find(p):
    if group[p] == p:
        return p
    ret = my_find(group[p])
    group[p] = ret
    return ret


T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    group = [i for i in range(N+1)]
    result = N
    for m in range(M):
        p1, p2 = map(int, input().split())
        my_union(p1, p2)
    print('#{} {}'.format(tc, result))