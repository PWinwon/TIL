## 성공코드

import sys

input = sys.stdin.readline

# 0 >> 우, 1 >> 우하, 2 >> 하

N = int(input().strip())
MAP = [list(map(int, input().split())) for _ in range(N)]

dp = [[[0 for _ in range(N)] for _ in range(N)] for _ in range(3)]

dp[0][0][1] = 1
for i in range(2, N):
    if MAP[0][i] == 0:
        dp[0][0][i] = 1
    else:
        break

for r in range(1, N):
    for c in range(1, N):
        if MAP[r][c] == 0 and MAP[r][c-1] == 0 and MAP[r-1][c] == 0:
            dp[1][r][c] = dp[0][r-1][c-1] + dp[1][r-1][c-1] + dp[2][r-1][c-1]

        if MAP[r][c] == 0:
            dp[0][r][c] = dp[0][r][c-1] + dp[1][r][c-1]
            dp[2][r][c] = dp[2][r-1][c] + dp[1][r-1][c]

print(dp[0][N-1][N-1] + dp[1][N-1][N-1] + dp[2][N-1][N-1])



# BFS를 이용한 풀이 시간초과가 나옴
# DP를 활용해 완전탐색을 해야할 것 같음 ㅠ

# import sys
# from collections import deque

# #    우하, 우, 하
# dr = [1, 0, 1]
# dc = [1, 1, 0]

# N = int(input().strip())

# MAP = [list(map(int, input().split())) for _ in range(N)]
# used = [[0 for _ in range(N)] for _ in range(N)]

# que = deque()
# # r, c, d: 방향
# # 방향이 -1, 0, 1로 주어지고, 0인 경우만 다 가고, 나머지는 본인과 0을 갈 수 있다.
# que.append([0, 1, 1])
# used[0][1] = 1

# while que:
#     y, x, d = que.popleft()
#     lst = [d]
#     if d:
#         lst.append(0)
#     else:
#         lst.append(1)
#         lst.append(-1)

#     for i in lst:
#         yr, xr = y+dr[i], x+dc[i]
#         if yr < 0 or yr >= N or xr < 0 or xr >= N:
#             continue
#         if MAP[yr][xr]:
#             continue
#         if i == 0:
#             yr1, xr1 = y+dr[1], x+dc[1]
#             yr2, xr2 = y+dr[2], x+dc[2]
#             # if yr1 < 0 or xr1 < 0 or yr2 < 0 or xr2 < 0 or yr1 >= N or yr2 >= N or xr1 >= N or xr2 >= N:
#             #     continue

#             if MAP[yr1][xr1] or MAP[yr2][xr2]:
#                 continue
#         used[yr][xr] += 1
#         que.append([yr, xr, i])

# print(used[N-1][N-1])

