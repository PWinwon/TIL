test_case = int(input())

for tc in range(test_case):
    N, M = map(int, input().split())
    flag = [input() for _ in range(N)]
    info = []
    result = 0
    for r in range(N):
        wbr = [M, M, M]
        for c in range(M):
            if flag[r][c] == 'W':
                wbr[0] -= 1
            elif flag[r][c] == 'B':
                wbr[1] -= 1
            else:
                wbr[2] -= 1
        info.append(wbr)
    for w in range(1, N-1):
        for b in range(w+1, N):
            sample = 0
            idx_r = 0
            idx_c = 0
            while idx_r < N:
                if idx_r == w or idx_r == b:
                    idx_c += 1
                sample += info[idx_r][idx_c]
                idx_r += 1
            if result == 0:
                result = sample
            elif result > sample:
                result = sample
    print('#{} {}'.format(tc+1, result))