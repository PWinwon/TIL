def merge_sort(s, e):
    global cnt
    mid = (s + e) // 2
    if len(lst[s:e]) < 2:
        return lst[s:e]
    left = merge_sort(s, mid)
    right = merge_sort(mid, e)
    if left[-1] > right[-1]:
        cnt += 1
    l_idx = 0
    r_idx = 0
    temp = []
    while l_idx < len(left) and r_idx < len(right):
        if left[l_idx] <= right[r_idx]:
            temp.append(left[l_idx])
            l_idx += 1
        else:
            temp.append(right[r_idx])
            r_idx += 1
    while l_idx < len(left):
        temp.append(left[l_idx])
        l_idx += 1
    while r_idx < len(right):
        temp.append(right[r_idx])
        r_idx += 1
    return temp


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))
    cnt = 0
    result = merge_sort(0, N)
    print('#{} {} {}'.format(tc, result[N//2], cnt))