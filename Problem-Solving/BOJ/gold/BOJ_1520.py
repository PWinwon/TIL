import sys

sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline


def my_dfs(r, c):
    global R, C

    if r == R-1 and c == C-1:
        return 1

    if dp[r][c] != -1:
        return dp[r][c]

    dp[r][c] = 0
    for i in range(4):
        r_idx = r + dr[i]
        c_idx = c + dc[i]
        if r_idx < 0 or r_idx >= R or c_idx < 0 or c_idx >= C:
            continue
        if MAP[r][c] > MAP[r_idx][c_idx]:
            dp[r][c] += my_dfs(r_idx, c_idx)

    return dp[r][c]


dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

R, C = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(R)]

dp = [[-1 for _ in range(C)] for _ in range(R)]

print(my_dfs(0, 0))