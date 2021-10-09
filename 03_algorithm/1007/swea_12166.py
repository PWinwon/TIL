def my_func(s, e):
    global cnt
    if s == e:
        return [lst[s]]
    mid = (s+e)//2
    left = my_func(s, mid)
    right = my_func(mid+1, e)
    l_idx = 0
    r_idx = 0
    l_len = len(left)
    r_len = len(right)
    temp = [0] * (l_len+r_len)
    idx = 0
    while l_idx < l_len and r_idx < r_len:
        if left[l_idx] > right[r_idx]:
            temp[idx] = right[r_idx]
            idx += 1
            r_idx += 1
            cnt += l_len - l_idx
        else:
            temp[idx] = left[l_idx]
            idx += 1
            l_idx += 1
    while l_idx < l_len:
        temp[idx] = left[l_idx]
        idx += 1
        l_idx += 1
    while r_idx < r_len:
        temp[idx] = right[r_idx]
        idx += 1
        r_idx += 1
    return temp


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))
    cnt = 0
    my_func(0, N-1)
    print('#{} {}'.format(tc, cnt))