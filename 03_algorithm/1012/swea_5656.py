from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def my_gravity(board):
    for w in range(W):
        temp = H-1
        for h in range(H-1, -1, -1):
            if board[h][w]:
                if temp != h:
                    board[temp][w], board[h][w] = board[h][w], board[temp][w]
                temp -= 1
    return


def break_cnt(y_idx, x_idx, f_MAP):
    cnt = 1
    que = deque()
    que.append([y_idx, x_idx, f_MAP[y_idx][x_idx]])
    f_MAP[y_idx][x_idx] = 0
    while que:
        row, col, l = que.popleft()
        for i in range(4):
            r = row
            c = col
            for j in range(l-1):
                r += dr[i]
                c += dc[i]
                if r < 0 or r >= H or c < 0 or c >= W:
                    continue
                if f_MAP[r][c] == 0:
                    continue
                my_cnt = f_MAP[r][c]
                f_MAP[r][c] = 0
                cnt += 1
                que.append([r, c, my_cnt])
    return cnt


def find_block(n, blocks, c):
    global max_val, result
    if n == N:
        if max_val < c:
            max_val = c
        return
    if c == result:
        max_val = c
        return
    for w in range(W):
        in_blocks = [m[:] for m in blocks]
        for h in range(H):
            if in_blocks[h][w]:
                ret_c = break_cnt(h, w, in_blocks)
                my_gravity(in_blocks)
                break
        else:
            continue
        find_block(n + 1, in_blocks, c + ret_c)


T = int(input())

for tc in range(1, T+1):
    N, W, H = map(int, input().split())
    MAP = [list(map(int, input().split())) for _ in range(H)]
    result = 0
    max_val = 0
    for r_idx in range(H):
        for c_idx in range(W):
            if MAP[r_idx][c_idx]:
                result += 1
    de = -1
    find_block(0, MAP, 0)
    print('#{} {}'.format(tc, result - max_val))
