# 실패
# 한번의 탐색으로 얼음을 카운트하고
# 백조가 만날수 있는지 탐색하는 방법을 고려해보자

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


from collections import deque

def melting_ice(r, c):
    que = deque()
    que.append([r, c])
    used[r][c] = 1
    while que:
        row, col = que.popleft()
        for i in range(4):
            r_idx = row + dr[i]
            c_idx = col + dc[i]
            if r_idx < 0 or r_idx >= R or c_idx < 0 or c_idx >= C:
                continue
            if used[r_idx][c_idx] > 0:
                continue
            if MAP[r_idx][c_idx] == 'X':
                used[r_idx][c_idx] = 1
                continue
            elif MAP[r_idx][c_idx] == 'L':
                used[r_idx][c_idx] = 2
                que.append([r_idx, c_idx])
            else:
                used[r_idx][c_idx] = 1
                que.append([r_idx, c_idx])
    return

R, C = map(int, input().split())

MAP = [list(input()) for _ in range(R)]


for r in range(R):
    for c in range(C):
        if MAP[r][c] == 'L':
            swan_r = r
            swan_c = c
            break
chk = False
result = 1
while True:
    used = [[0 for _ in range(C)] for _ in range(R)]
    # 얼음이 녹는다.
    de = -1
    for r in range(R):
        for c in range(C):
            if MAP[r][c] == '.' and used[r][c] == 0:
                melting_ice(r, c)
    # 백조 이동
    visited = [[0 for _ in range(C)] for _ in range(R)]
    swan_move = deque()
    swan_move.append([swan_r, swan_c])
    visited[swan_r][swan_c] = 1
    while swan_move:
        row, col = swan_move.popleft()
        if (row != swan_r or col != swan_c) and used[row][col] == 2:
            chk = True
            break
        for i in range(4):
            r_idx = row + dr[i]
            c_idx = col + dc[i]
            if r_idx < 0 or r_idx >= R or c_idx < 0 or c_idx >= C:
                continue
            if used[r_idx][c_idx] == 0:
                continue
            if visited[r_idx][c_idx] == 1:
                continue
            swan_move.append([r_idx, c_idx])
            visited[r_idx][c_idx] = 1

    if chk:
        break
    else:
        for r in range(R):
            for c in range(C):
                if used[r][c] == 1:
                    MAP[r][c] = '.'
                elif used[r][c] == 2:
                    MAP[r][c] = 'L'
                else:
                    MAP[r][c] = 'X'
    result += 1
print(result)
