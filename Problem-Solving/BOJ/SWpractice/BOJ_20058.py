from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


# 회전할 시작점 row, col 주고, c는 회전할 배열의 길이
def rotate_MAP(row, col, length):
    for r in range(length):
        for c in range(length):
            sample[row+c][col+length-1-r] = MAP[row+r][col+c]
    return


def my_chk(row, col):
    cnt = 0
    for i in range(4):
        r_idx = row + dr[i]
        c_idx = col + dc[i]
        if r_idx < 0 or r_idx >= 2**N or c_idx < 0 or c_idx >= 2**N:
            continue
        if MAP[r_idx][c_idx] <= 0:
            continue
        cnt += 1
    if cnt < 3:
        return True
    return False


N, Q = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(2**N)]
L_list = list(map(int, input().split()))
for q in range(Q):
    L = L_list[q]
    # 회전
    if L:
        sample = [[0 for _ in range(2**N)] for _ in range(2**N)]
        for r in range(0, 2**N, 2**L):
            for c in range(0, 2**N, 2**L):
                rotate_MAP(r, c, 2**L)
        # 회전 결과 적용
        for r in range(2**N):
            for c in range(2**N):
                MAP[r][c] = sample[r][c]
    # 얼음 줄이기 (완전탐색)
    sample = [[0 for _ in range(2**N)] for _ in range(2**N)]
    for r in range(2**N):
        for c in range(2**N):
            if my_chk(r, c):
                sample[r][c] = MAP[r][c] - 1
            else:
                sample[r][c] = MAP[r][c]

    for r in range(2**N):
        for c in range(2**N):
            MAP[r][c] = sample[r][c]

result1 = 0
result2 = 0
used = [[0 for _ in range(2**N)] for _ in range(2**N)]
for r in range(2**N):
    for c in range(2**N):
        if MAP[r][c] > 0 and used[r][c] == 0:
            cnt = 0
            que = deque()
            que.append([r, c])
            used[r][c] = 1
            while que:
                row, col = que.popleft()
                cnt += 1
                result1 += MAP[row][col]
                for i in range(4):
                    r_idx = row + dr[i]
                    c_idx = col + dc[i]
                    if r_idx < 0 or r_idx >= 2**N or c_idx < 0 or c_idx >= 2**N:
                        continue
                    if used[r_idx][c_idx] == 1:
                        continue
                    if MAP[r_idx][c_idx] <= 0:
                        continue
                    que.append([r_idx, c_idx])
                    used[r_idx][c_idx] = 1
            if cnt > result2:
                result2 = cnt

print(result1)
print(result2)