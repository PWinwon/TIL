test_case = int(input())

for tc in range(test_case):
    N = int(input())
    card_lst = list(input().split())
    result = []
    idx = 0
    cnt = 0
    while len(result) < N:
        result.append(card_lst[idx])
        idx = (idx + (N//2) + (N % 2)) % N
        cnt += 1
        if cnt % 2 == 0 and N % 2 == 0:
            idx += 1
    print('#{} {}'.format(tc+1, ' '.join(result)))
