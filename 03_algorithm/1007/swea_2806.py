    # 좌하 우하
dr = [1, 1]
dc = [-1, 1]


def path_draw(row, col, n):
    for i in range(2):
        r = row
        c = col
        while 0 <= r+dr[i] < N and 0 <= c + dc[i] < N:
            r += dr[i]
            c += dc[i]
            MAP[r][c] += n
    return


def my_func(level):
    global result
    if level == N:
        result += 1
        return
    for i in range(N):
        if visited[i] != 0:
            continue
        if used_hap[level+i] != 0:
            continue
        if used_gap[level-i] != 0:
            continue
        # if MAP[level][i] != 0:
        #     continue
        visited[i] = 1
        used_hap[level + i] = 1
        used_gap[level - i] = 1
        # path_draw(level, i, 1)
        my_func(level+1)
        # path_draw(level, i, 0)
        used_hap[level + i] = 0
        used_gap[level - i] = 0
        visited[i] = 0
    return


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    MAP = [[0 for _ in range(N)] for _ in range(N)]
    visited = [0] * N
    used_hap = [0] * (2*N)
    used_gap = [0] * (2*N)
    result = 0
    my_func(0)
    print('#{} {}'.format(tc, result))


#########################################################
# 교수님 풀이

# def func(y):
#     global cnt
#     if y == N :
#         cnt += 1
#         return
#     for x in range(N):
#         if used[x] == 1 : continue
#         if used_hap[y+x] == 1: continue
#         if used_cha[y-x + N] == 1 : continue # 음수 방지하기 위해 + @
#         used[x] = 1
#         used_hap[y+x] = 1
#         used_cha[y-x+N] = 1
#         func(y + 1)
#         used[x] = 0
#         used_hap[y+x] = 0
#         used_cha[y-x+N] = 0
#
# T = int(input())
#
# for tc in range(1,T+1):
#     N = int(input())
#     used = [0] * N # x 좌표 사용 체크
#     used_hap = [0] * (2*N) # / 체크
#     used_cha = [0] * (2*N) # \ 체크
#     cnt = 0
#     func(0)
#     print("#{} {}".format(tc, cnt))