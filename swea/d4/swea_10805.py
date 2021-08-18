# 40개 중 28개
test_case = int(input())

for tc in range(test_case):
    N, Q = map(int, input().split())
    result = [1, 2] + [0] * (N-2)
    cnt = 1
    st_idx = 0
    for q in range(Q):
        idx1, idx2 = map(int, input().split())
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
