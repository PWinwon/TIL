from collections import deque

INF = 10

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

T = int(input())


for tc in range(1, T+1):
    M, N, L = map(int, input().split())

    MAP = [list(map(int, input().split())) for _ in range(M)]

    st = [M-1, 0]
    ed = [0, N-1]

    que = deque()
    que.append([st[0], st[1], L, 0])
    used = [[INF for _ in range(N)] for _ in range(M)]
    used[st[0]][st[1]] = 0

    result = -1

    while que:
        r, c, cnt, res = que.popleft()
        if MAP[r][c] == 3:
            if result == -1:
                result = res
            elif result > res:
                result = res
        if cnt == 0:
            continue

        for i in range(4):
            r_idx = r + dr[i]
            c_idx = c + dc[i]
            if r_idx < 0 or r_idx >= M or c_idx < 0 or c_idx >= N:
                continue
            if used[r_idx][c_idx] <= res:
                continue

            if MAP[r_idx][c_idx] == 3:
                que.append([r_idx, c_idx, cnt-1, res])
                if used[r_idx][c_idx] > res:
                    used[r_idx][c_idx] = res
                continue

            if MAP[r_idx][c_idx] == 1:
                que.append([r_idx, c_idx, cnt-1, res])
                que.append([r_idx, c_idx, L, res+1])
                used[r_idx][c_idx] = res + 1
            else:
                que.append([r_idx, c_idx, cnt-1, res])
                used[r_idx][c_idx] = res


    print('#{} {}'.format(tc, result))