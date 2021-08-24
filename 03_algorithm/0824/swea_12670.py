def miro_path(row, col):
    global result
    if miro[row][col] == 3:
        result = 1
        return
    if miro[row][col] == 1:
        return
    for i in range(4):
        if 0 <= row+dir_r[i] < N and 0 <= col+dir_c[i] < N:
            if visited[row+dir_r[i]][col+dir_c[i]] == 1:
                continue
            visited[row+dir_r[i]][col+dir_c[i]] = 1
            miro_path(row+dir_r[i], col+dir_c[i])
            visited[row+dir_r[i]][col+dir_c[i]] = 0
    return


#       상, 하, 좌, 우
dir_r = [-1, 1, 0, 0]
dir_c = [0, 0, -1, 1]

test_case = int(input().rstrip())

for tc in range(test_case):
    N = int(input().rstrip())
    miro = [list(map(int, input().rstrip())) for _ in range(N)]
    start_point = []
    visited = [[0 for _ in range(N)] for _ in range(N)]
    result = 0
    for r in range(N):
        for c in range(N):
            if miro[r][c] == 2:
                start_point.append(r)
                start_point.append(c)
                break
        if start_point:
            break

    visited[start_point[0]][start_point[1]] = 1
    miro_path(start_point[0], start_point[1])
    print('#{} {}'.format(tc+1, result))


#####################################################################
# 교수님 풀이 미로

# def find_start():
#     for y in range(N):
#         for x in range(N):
#             if MAP[y][x] == '2':
#                 return (y, x)
#
#     return (-1, -1)
#
#
# def dfs(y, x):
#     global check
#     if y < 0 or x < 0 or y >= N or x >= N: return
#     if visited[y][x] == 1: return
#     if MAP[y][x] == '1': return
#     visited[y][x] = 1
#
#     if MAP[y][x] == '3':
#         check = 1
#         return
#
#     dfs(y - 1, x)
#     dfs(y + 1, x)
#     dfs(y, x - 1)
#     dfs(y, x + 1)
#     return
#
#
# T = int(input())
# dy = [-1, 1, 0, 0]
# dx = [0, 0, -1, 1]
# for tc in range(1, T + 1):
#     N = int(input())
#     MAP = [
#         input() for _ in range(N)
#     ]
#     # visited
#     visited = [
#         [0 for _ in range(N)] for _ in range(N)
#     ]
#     # 시작점 찾기
#     sy, sx = find_start()
#     check = 0
#     dfs(sy, sx)
#     print("#{} {}".format(tc, check))