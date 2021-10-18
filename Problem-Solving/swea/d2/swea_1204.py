
T = int(input())

for i in range(T):
    num_case = int(input())
    case_list = list(map(int, input().split()))
    score_list = [0] * 101
    cnt = 0
    many_scr = 0
    a = 0
    for i in case_list:
        score_list[i] += 1
    for j in score_list:
        a += j
    for mn_s in score_list:
        if many_scr <= mn_s:
            many_scr = mn_s
            idx = cnt
        cnt += 1
    print(f'#{num_case} {idx}')

