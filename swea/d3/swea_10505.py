test_case = int(input())

for tc in range(test_case):
    n = int(input())
    people = list(map(int, input().split()))
    total = 0
    for idx in range(n):
        total += people[idx]
    pp_avg = total / n
    cnt = 0
    for idx in range(n):
        if people[idx] <= pp_avg:
            cnt += 1
    
    print('#{} {}'.format(tc+1, cnt))