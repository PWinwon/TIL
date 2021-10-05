# dr = [0, 1]
# dc = [1, 0]
#
# def my_func(row, col, total):
#     global min_val
#     if row == N-1 and col == N-1:
#         if min_val > total:
#             min_val = total
#         return
#     for i in range(2):
#         r = row + dr[i]
#         c = col + dc[i]
#         if r < 0 or r >= N or c < 0 or c >= N:
#             continue
#         my_func(r, c, total + MAP[r][c])
#     return
#
# T = int(input())
#
# for tc in range(T):
#     N = int(input())
#     MAP = [list(map(int, input().split())) for _ in range(N)]
#     min_val = 1000
#     my_func(0, 0, MAP[0][0])
#     print('#{} {}'.format(tc+1, min_val))

########################################################################
# 다이나믹 프로그래밍


# def my_func(row, col):
#     for i in range(2):
#         r = row + dr[i]
#         c = col + dc[i]
#         if r < 0 or r >= N or c < 0 or c >= N:
#             continue
#         if used[r][c] > used[row][col] + MAP[r][c]:
#             used[r][c] = used[row][col] + MAP[r][c]
#             my_func(r, c)
#     return
#
#
# dr = [0, 1]
# dc = [1, 0]
#
# T = int(input())
#
# for tc in range(T):
#     N = int(input())
#     MAP = [list(map(int, input().split())) for _ in range(N)]
#     used = [[1000 for _ in range(N)] for _ in range(N)]
#     used[0][0] = MAP[0][0]
#     my_func(0, 0)
#     print('#{} {}'.format(tc+1, used[N-1][N-1]))

########################################################################
# 교수님 풀이

def dfs(y,x):
    if y >= N or x >= N : return int(21e8) # 범위 벗어날때 정답에 영향 미치지 않은 값으로 리턴한다.
    if y == N-1 and x == N-1 :
        return MAP[y][x]

    a = dfs(y,x + 1)
    b = dfs(y+1, x)

    return min(a,b) + MAP[y][x]

T = int(input())
for tc in range(1, T + 1) :
    N = int(input())
    MAP = [
        list(map(int, input().split())) for _ in range(N)
    ]

    ret = dfs(0,0)
    print("#{} {}".format(tc, ret))