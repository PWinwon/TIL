dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def my_func(row, col):
    for i in range(4):
        r_idx = row + dr[i]
        c_idx = col + dc[i]
        if r_idx < 0 or r_idx >= N or c_idx < 0 or c_idx >= N:
            continue
        if MAP[r_idx][c_idx] == 0:
            continue
        gap = (MAP[row][col] - MAP[r_idx][c_idx]) // 5
        if gap > 0:
            sample[r_idx][c_idx] += gap
            sample[row][col] -= gap
    return


N, K = map(int, input().split())

lst = list(map(int, input().split()))
MAP = [[0 for _ in range(N)] for _ in range(N)]

for n in range(N):
    MAP[N-1][n] = lst[n]

result = 1
while True:
    # 가장 적은 어항에 물고기 추가
    min_val = 10001
    for c in range(N):
        if MAP[N-1][c] < min_val:
            min_val = MAP[N-1][c]
    for c in range(N):
        if min_val == MAP[N-1][c]:
            MAP[N-1][c] += 1
    # 어항 쌓기
    cnt = 0
    idx = 0
    row_length = 1
    col_length = 1
    while True:
        if idx + row_length + col_length > N:
            break
        for r in range(N-1, N-row_length-1, -1):
            for c in range(idx, idx+col_length):
                MAP[N-1-col_length-idx+c][idx-1+col_length+N-r] = MAP[r][c]
                MAP[r][c] = 0
        if cnt % 2:
            col_length += 1
        else:
            row_length += 1
        idx += (cnt//2 + 1)
        cnt += 1

    # 어항 물고기 평준화
    sample = [[0 for _ in range(N)] for _ in range(N)]
    for r in range(N):
        for c in range(N):
            if MAP[r][c]:
                my_func(r, c)
            sample[r][c] += MAP[r][c]

    # 적용
    for r in range(N):
        for c in range(N):
            MAP[r][c] = sample[r][c]

    # 다시 일렬로 정렬
    idx = 0
    for c in range(N):
        for r in range(N-1, -1, -1):
            if MAP[r][c]:
                MAP[N-1][idx] = MAP[r][c]
                idx += 1
    # 찌꺼기 값들 초기화
    for r in range(N-1):
        for c in range(N):
            MAP[r][c] = 0

    # 두번째 어항정리
    # 반 접어 올리기
    end_point = N // 2
    c_idx_2nd = N // 2
    for c in range(end_point-1, -1, -1):
        MAP[N-2][c_idx_2nd] = MAP[N-1][c]
        MAP[N-1][c] = 0
        c_idx_2nd += 1
    de = -1
    # 한번 더 접어올리기
    # 올리기 전 r, c
    bef_r = N - 2
    aft_r = N - 3
    aft_c = N - N//4
    for r in range(aft_r, aft_r-2, -1):
        bef_c = N - N // 4 - 1
        for c in range(aft_c, N):
            MAP[r][c] = MAP[bef_r][bef_c]
            MAP[bef_r][bef_c] = 0
            bef_c -= 1
        bef_r += 1

    # 물고기 조절
    sample = [[0 for _ in range(N)] for _ in range(N)]
    for r in range(N):
        for c in range(N):
            if MAP[r][c]:
                my_func(r, c)
            sample[r][c] += MAP[r][c]

    # 적용
    for r in range(N):
        for c in range(N):
            MAP[r][c] = sample[r][c]

    # 다시 일렬로 정렬
    idx = 0
    for c in range(N):
        for r in range(N - 1, -1, -1):
            if MAP[r][c]:
                MAP[N - 1][idx] = MAP[r][c]
                idx += 1
    # 찌꺼기 값들 초기화
    for r in range(N - 1):
        for c in range(N):
            MAP[r][c] = 0

    # 물고기 큰값 작은 값 비교
    max_fish = -1
    min_fish = 10001
    for c in range(N):
        if max_fish < MAP[N-1][c]:
            max_fish = MAP[N-1][c]
        if min_fish > MAP[N-1][c]:
            min_fish = MAP[N-1][c]
    if max_fish - min_fish <= K:
        break
    else:
        result += 1
print(result)