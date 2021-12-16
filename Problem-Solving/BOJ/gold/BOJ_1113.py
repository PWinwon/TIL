from collections import deque


def bfs(r, c, cnt):
    que = deque()
    que.append([r, c])
    used[r][c] = 1
    flag = False
    ret = 1
    while que:
        row, col = que.popleft()

        for idx in range(4):
            r_idx = row + dr[idx]
            c_idx = col + dc[idx]
            if r_idx < 0 or r_idx >= R or c_idx < 0 or c_idx >= C:
                flag = True
                continue
            if used[r_idx][c_idx]:
                continue
            if MAP[r_idx][c_idx] > cnt:
                continue
            used[r_idx][c_idx] = 1
            que.append([r_idx, c_idx])
            ret += 1

    if flag:
        return 0
    else:
        return ret



dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

R, C = map(int, input().split())

MAP = [list(map(int, list(input()))) for _ in range(R)]
result = 0

for i in range(1, 9):
    used = [[0 for _ in range(C)] for _ in range(R)]
    de = -1
    for r in range(R):
        for c in range(C):
            if MAP[r][c] <= i and used[r][c] == 0:
                res = bfs(r, c, i)
                result += res
print(result)