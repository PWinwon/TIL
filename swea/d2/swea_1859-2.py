test_case = int(input())

for tc in range(test_case):
    n = int(input())
    lst_n = list(map(int, input().split()))

    max_val = 0
    total = 0
    for idx in range(n-1, -1, -1):
        if lst_n[idx] > max_val:
            max_val = lst_n[idx]
        else:
            total += max_val - lst_n[idx]
    print('#{} {}'.format(tc+1, total))