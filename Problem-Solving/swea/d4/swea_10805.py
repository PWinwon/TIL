# 40개 중 28개
test_case = int(input())

for tc in range(test_case):
    N, Q = map(int, input().split())
    result = [1, 2] + [0] * (N-2)
    cnt = 1
    st_idx = 0
    for q in range(Q):
        idx1, idx2 = map(int, input().split())
        if cnt == N:
            continue
        result[idx1-1], result[idx2-1] = result[idx2-1], result[idx1-1]
        if st_idx == (idx1 - 1):
            st_idx = idx2 - 1
        elif st_idx == (idx2 - 1):
            st_idx = idx1 - 1
        if st_idx - 1 >= 0 and result[st_idx-1] == 0:
            result[st_idx-1] = 2
            cnt += 1
        if st_idx + 1 < N and result[st_idx+1] == 0:
            result[st_idx+1] = 2
            cnt += 1
        
    print('#{} {}'.format(tc+1, cnt))






    # lst_q =[[0, 0]] + [list(map(int, input().split())) for _ in range(Q)]
    # st_idx = 1
    # result = [1] + [0] * N
    # cnt = 0
    # for idx in range(Q+1):
    #     if st_idx == lst_q[idx][0]:
    #         st_idx = lst_q[idx][1]
    #     elif st_idx == lst_q[idx][1]:
    #         st_idx = lst_q[idx][0]
    #     fake1 = st_idx - 1
    #     fake2 = st_idx + 1
    #     for f_idx in range(idx+1, Q+1):
    #         if fake1 == lst_q[f_idx][0]:
    #             fake1 = lst_q[f_idx][1]
    #         elif fake1 == lst_q[f_idx][1]:
    #             fake1 = lst_q[f_idx][0]
    #         if fake2 == lst_q[f_idx][0]:
    #             fake2 = lst_q[f_idx][1]
    #         elif fake2 == lst_q[f_idx][1]:
    #             fake2 = lst_q[f_idx][0]
    #     if result[fake1] == 0:
    #         result[fake1] = 1
    #         cnt += 1
    #     if fake2 < N+1 and result[fake2] == 0:
    #         result[fake2] = 1
    #         cnt += 1
    # print('#{} {}'.format(tc+1, cnt))

