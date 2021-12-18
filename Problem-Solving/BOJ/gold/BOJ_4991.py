from collections import deque
# from itertools import permutations


dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# 입력받은 좌표에서 각 쓰레기들을 탐색, 최소거리 도출
def bfs(y, x):
    used = [[0 for _ in range(C)] for _ in range(R)]
    que = deque()
    que.append([y, x, 0])
    used[y][x] = 1

    while que:
        yy, xx, cnt = que.popleft()
        for i in range(4):
            y_idx = yy + dr[i]
            x_idx = xx + dc[i]
            if y_idx < 0 or y_idx >= R or x_idx < 0 or x_idx >= C:
                continue
            if used[y_idx][x_idx]:
                continue
            if MAP[y_idx][x_idx] == 'x':
                continue
            que.append([y_idx, x_idx, cnt+1])
            used[y_idx][x_idx] = cnt + 1

    return used


def adj_dfs(n, cnt, sum):
    global result, dirty_cnt, adj, used_temp
    if cnt == dirty_cnt-1:
        if sum < result:
            result = sum
        return
    if sum > result:
        return

    for i in range(dirty_cnt):
        if used_temp[i]:
            continue
        used_temp[i] = 1
        adj_dfs(i, cnt+1, sum+adj[n][i])
        used_temp[i] = 0
    return



while True:
    C, R = map(int, input().split())
    if C == 0 and R == 0:
        break

    # .: 깨끗한 칸
    # *: 더러운 칸
    # x: 가구
    # o: 로봇 청소기의 시작 위치
    dirty_points = []
    dirty_cnt = 0
    MAP = [list(input()) for _ in range(R)]
    for r in range(R):
        for c in range(C):
            if MAP[r][c] == 'o':
                robot = [r, c]
            elif MAP[r][c] == '*':
                dirty_points.append([r, c])
                dirty_cnt += 1

    visited = bfs(robot[0], robot[1])

    first_dirty = [0] * dirty_cnt


    is_posibble = True

    idx = 0
    for ry, cx in dirty_points:
        if visited[ry][cx]:
            first_dirty[idx] = visited[ry][cx]
            idx += 1
        else:
            is_posibble = False


    if is_posibble:
        adj = [[0 for _ in range(dirty_cnt)] for _ in range(dirty_cnt)]
        result = 9876543210
        for i in range(dirty_cnt-1):
            visited = bfs(dirty_points[i][0], dirty_points[i][1])
            for j in range(i+1, dirty_cnt):
                adj[i][j] = visited[dirty_points[j][0]][dirty_points[j][1]]
                adj[j][i] = visited[dirty_points[j][0]][dirty_points[j][1]]
        used_temp = [0] * dirty_cnt
        for idx in range(dirty_cnt):
            used_temp[idx] = 1
            adj_dfs(idx, 0, first_dirty[idx])
            used_temp[idx] = 0

        print(result)
    else:
        print(-1)