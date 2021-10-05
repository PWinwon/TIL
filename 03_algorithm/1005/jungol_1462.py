from collections import deque

def find_money(rr, cc):
    used = [[0 for _ in range(C)] for _ in range(R)]
    que_func = deque()
    que_func.append([rr, cc, 0])
    used[rr][cc] = 1
    max_val = 0
    while que_func:
        temp = que_func.popleft()
        row = temp[0]
        col = temp[1]
        cnt = temp[2]
        if max_val < cnt:
            max_val = cnt
        for i in range(4):
            y = row + dr[i]
            x = col + dc[i]
            if y < 0 or y >= R or x < 0 or x >= C:
                continue
            if MAP[y][x] == 'W':
                continue
            if used[y][x] == 1:
                continue
            used[y][x] = 1
            que_func.append([y, x, cnt+1])
    return max_val


dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

R, C = map(int, input().split())
MAP = [list(input()) for _ in range(R)]
visited = [[0 for _ in range(C)] for _ in range(R)]
result = 0
que = deque()
for r in range(R):
    for c in range(C):
        if MAP[r][c] == 'L' and visited[r][c] == 0:
            visited[r][c] = 1
            ret = find_money(r, c)
            if ret > result:
                result = ret
print(result)

# de = -1
# while que:
#     temp = que.popleft()
#     y_idx = temp[0]
#     x_idx = temp[1]
#     if visited[y_idx][x_idx] > result:
#         result = visited[y_idx][x_idx]
#     for idx in range(4):
#         r_idx = y_idx + dr[idx]
#         c_idx = x_idx + dc[idx]
#         if r_idx < 0 or r_idx >= R or c_idx < 0 or c_idx >= C:
#             continue
#         if MAP[r_idx][c_idx] == 'W':
#             continue
#         if visited[r_idx][c_idx] >= 0:
#             continue
#         visited[r_idx][c_idx] = visited[y_idx][x_idx] + 1
#         que.append([r_idx, c_idx])

# print(result)