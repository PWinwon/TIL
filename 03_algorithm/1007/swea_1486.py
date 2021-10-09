def my_func(level, total, max_val):
    global result
    if level == N:
        if total >= B and result > total - B:
            result = total - B
        return
    if max_val + total < B:
        return
    if total - B > result:
        return
    my_func(level+1, total+lst[level], max_val-lst[level])
    my_func(level+1, total, max_val-lst[level])
    return


T = int(input())

for tc in range(1, T+1):
    N, B = map(int, input().split())
    lst = list(map(int, input().split()))
    m_val = sum(lst)
    result = m_val - B
    my_func(0, 0, m_val)
    print('#{} {}'.format(tc, result))