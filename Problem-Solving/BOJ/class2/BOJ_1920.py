N = int(input())

lst_n = list(map(int, input().split()))

lst_n.sort()

M = int(input())

lst_m = list(map(int, input().split()))

for idx in range(M):
    m = lst_m[idx]
    left = 0
    right = N - 1
    mid = N // 2
    chk = False
    while left <= right:
        mid = (left + right + 1) // 2
        if m < lst_n[mid]:
            right = mid - 1
            continue
        elif m > lst_n[mid]:
            left = mid + 1
            continue
        else:
            chk = True
            break

    if chk:
        print(1)
    else:
        print(0)