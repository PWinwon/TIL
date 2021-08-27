def kill_cnt(idx_r, idx_c, m):
    cnt = 0
    for r in range(idx_r, idx_r + m):
        for c in range(idx_c, idx_c + m):
            cnt += bugs[r][c]
    return cnt


test_case = int(input())

for tc in range(test_case):
    N, M = map(int, input().split())
    bugs = [list(map(int, input().split())) for _ in range(N)]
    max_kill = 0
    for row in range(N-M+1):
        for col in range(N-M+1):
            k_cnt = kill_cnt(row, col, M)
            if max_kill < k_cnt:
                max_kill = k_cnt
    print('#{} {}'.format(tc+1, max_kill))